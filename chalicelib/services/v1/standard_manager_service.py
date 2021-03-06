from chalicelib.config import get_config
from chalicelib.database import get_connection
from chalicelib.nosql_database import get_connection as nosql_get_connection
from chalicelib.enums.messages import MessagesEnum
from chalicelib.exceptions import ApiException
from chalicelib.logging import get_logger
from chalicelib.nosql.repositories.v1.standard import StandardRepository as NoSQLStandardRepository
from chalicelib.repositories.v1.standard import StandardRepository
import uuid


class StandardManagerService:
    DEBUG = False
    ENTITY = None
    NOSQL_REPOSITORY = NoSQLStandardRepository
    REPOSITORY = StandardRepository
    VALIDATOR = None
    NOSQL = True
    TABLE_NAME = "standard"

    def __init__(self, logger=None, config=None, connection=None):
        # logger

        self.logger = logger if logger is not None else get_logger()
        # configurations
        self.config = config if config is not None else get_config()
        # database connection


        if self.NOSQL:
            self.connection = connection if connection is not None else nosql_get_connection()
            if self.DEBUG:
                self._repository = self.NOSQL_REPOSITORY(self.connection, self.config.DYNAMODB_TABLE_NAME, logger)
            else:
                self._repository = self.NOSQL_REPOSITORY(self.connection, self.config.DYNAMODB_TABLE_NAME)
        else:
            self.connection = connection if connection is not None else get_connection()
            if self.DEBUG:
                self._repository = self.REPOSITORY(self.connection, self.TABLE_NAME, logger)
            else:
                self._repository = self.REPOSITORY(self.connection, self.TABLE_NAME)

    def get(self, api_request, record_uuid):
        if not record_uuid:
            api_ex = ApiException(MessagesEnum.PARAM_REQUIRED_ERROR)
            api_ex.set_params('uuid')
            raise api_ex

        # valida a request, validando os campos
        request = self.validate_request(api_request)

        data = self._repository.get(record_uuid, request['fields'])

        if data is None:
            api_ex = ApiException(MessagesEnum.FIND_ERROR)
            api_ex.set_params(record_uuid)
            raise api_ex

        return data

    def list(self, api_request):

        request = self.validate_request(api_request)

        data = self._repository.list(where=request['where'], offset=request['offset'],
                                     limit=request['limit'], fields=request['fields'],
                                     sort_by=request['sort_by'], order_by=request['order_by'])
        return data

    def count(self, api_request):

        request = self.validate_request(api_request)

        data = self._repository.count(where=request['where'], sort_by=request['sort_by'], order_by=request['order_by'])

        count = 0
        try:
            count = data.get('total')
        except Exception as err:
            self.logger.error(err)

        return count

    def create(self, api_request):

        new_uuid = str(uuid.uuid4())
        request = self.validate_request(api_request)
        data = request['where']

        if data is None:
            api_ex = ApiException(MessagesEnum.CREATE_ERROR)
            api_ex.set_params(data)
            raise api_ex

        try:
            result = self._repository.create(new_uuid, data)

            if result is None:
                api_ex = ApiException(MessagesEnum.CREATE_ERROR)
                api_ex.set_params(data)
                raise api_ex

        except Exception as err:
            self.logger.error(err)
            if data is None:
                api_ex = ApiException(MessagesEnum.CREATE_ERROR)
                raise api_ex

        return data

    def delete(self, api_request, record_uuid):
        if not record_uuid:
            api_ex = ApiException(MessagesEnum.PARAM_REQUIRED_ERROR)
            api_ex.set_params('uuid')
            raise api_ex

        # valida a request, validando os campos
        request = self.validate_request(api_request)

        result = self._repository.delete(record_uuid)

        if result is not True:
            api_ex = ApiException(MessagesEnum.DELETE_ERROR)
            api_ex.set_params(uuid)
            raise api_ex

        return result

    def update(self, api_request, record_uuid):
        if not record_uuid:
            api_ex = ApiException(MessagesEnum.PARAM_REQUIRED_ERROR)
            api_ex.set_params('uuid')
            raise api_ex

        # valida a request, validando os campos
        request = self.validate_request(api_request)
        data = request['where']

        data = self._repository.update(record_uuid, data)

        if data is None:
            api_ex = ApiException(MessagesEnum.UPDATE_ERROR)
            api_ex.set_params(uuid)
            raise api_ex

        return data

    def upload(self):
        # TODO implementar m??todo para fazer upload para o S3 do arquivo da norma
        pass

    def validate_request(self, api_request):
        # TODO implementar quando necessario
        # self.logger.info('api_request', str(api_request))

        return api_request

import os
from time import sleep

from chalicelib.logging import get_logger
from sqlalchemy import create_engine

logger = get_logger()

_CONNECTION = False
_RETRY_COUNT = 0
_MAX_RETRY_ATTEMPTS = 3


def get_connection(connect=True, retry=False):
    global _CONNECTION, _RETRY_COUNT, _MAX_RETRY_ATTEMPTS
    if not _CONNECTION:
        connection = None
        params = {
            'host': os.environ['DB_HOST'],
            'user': os.environ['DB_USER'],
            'password': os.environ['DB_PASSWORD'],
            'db': os.environ['DB']
        }
        try:
            connection = create_engine('mysql://%s:%s@%s/%s'.format(
                params['user'], params['password'], params['host'],params['db']
            ))
            if connect:
                connection.begin()

            _CONNECTION = connection
            _RETRY_COUNT = 0
            logger.info('Connected')

        except Exception as err:
            if _RETRY_COUNT == _MAX_RETRY_ATTEMPTS:
                _RETRY_COUNT = 0
                logger.error(err)
                return connection
            else:
                logger.error(err)
                logger.info('Trying to reconnect... {}'.format(_RETRY_COUNT))

                sleep(0.1)
                # retry
                if not retry:
                    _RETRY_COUNT += 1
                    return get_connection(True)
    else:
        connection = _CONNECTION

    return connection

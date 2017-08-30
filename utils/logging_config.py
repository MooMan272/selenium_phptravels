import logging
import os

config = {
    'version': 1,
    'formatters': {
        'console': {
            'format' : '%(message)s',
        },
        'default': {
            'format' : '%(asctime)s %(levelname)-8s %(module)s.%(funcName)s -- %(message)s',
            'datefmt' : '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
            'level': logging.WARNING
        },
        'file_debug': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'level': logging.DEBUG,
            'filename': 'Logs/log_debug.log',
            'maxBytes': 5*1024*1024,
            'backupCount': 9,
            'mode': 'a'
        },
        'file_info': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'level': logging.INFO,
            'filename': 'Logs/log_info.log',
            'maxBytes': 5*1024*1024,
            'backupCount': 9,
            'mode': 'a'
        },
        'file_warning': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'level': logging.WARNING,
            'filename': 'Logs/log_warning.log',
            'maxBytes': 5*1024*1024,
            'backupCount': 9,
            'mode': 'a'
        }
    },
    'root': {
        'handlers': [
            'console',
            'file_debug',
            'file_info',
            'file_warning',
        ],
        'level': logging.DEBUG
    },
}

# Create log directories if necessary.
for key in config['handlers']:
    # Skip console handler.
    if 'filename' in config['handlers'][key].keys():
        dirname = os.path.dirname(config['handlers'][key]['filename'])
        if not os.path.exists(dirname):
            os.makedirs(dirname)

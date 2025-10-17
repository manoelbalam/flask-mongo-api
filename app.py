from flask import Flask, jsonify, request
from controllers.orderController import orderBP
from flasgger import Swagger
from logging.config import dictConfig
from flask.logging import default_handler


dictConfig({
    'version': 1,
    'formatters': {
        'console': {
            'format': '%(message)s'
        },
        'default': {
            'format': '[%(asctime)s] %(module)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'formatter': 'console',
        },
        'info': {
            'class' : 'logging.FileHandler',
            'formatter': 'default',
            'filename' : 'logs/info.log',
            'level'    : 'DEBUG'
        },
        'error': {
            'class' : 'logging.FileHandler',
            'formatter': 'default',
            'filename' : 'logs/error.log',
            'level'    : 'ERROR'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console']
    },
    "loggers": {
        "info_log": {
            "level": "INFO",
            "handlers": ["info"],
            "propagate": False,
        },
        "error_log": {
            "level": "ERROR",
            "handlers": ["error"],
            "propagate": False,
        }
    },
})

app = Flask(__name__)

app.logger.removeHandler(default_handler)

app.config['SWAGGER'] = {
    'title': 'flask-mongo-api',
    'description': 'API RESTful CRUD Orders',
    'version': 'v0.1',
    'uiversion': 2
}

app.config['FLASK_LOGGING_EXTRAS'] = {
    'BLUEPRINT': {
        'FORMAT_NAME': 'bp',
        'APP_BLUEPRINT': '<app>',
        'NO_REQUEST_BLUEPRINT': '<not a request>',
    },
    'RESOLVERS': {
        'categoy': '<unset>',
        'client': 'log_helper.get_client',
    },
}

swagger = Swagger(app)

app.register_blueprint(orderBP)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
from src import create_app
from src import routes ## DO NOT DELETE ##
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

if __name__ == '__main__':
    create_app().run(host='127.0.0.1', port=5000, debug=True, threaded=True)

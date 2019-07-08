import flask
import logging
import sys
import os
import datetime
import hashlib

from gumo.core import configure as core_configure

TARGET_AUDIENCE = '204100934405-b9gjp2hnbtq12r9s4i460mmrsjl1jvg4.apps.googleusercontent.com'

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)


if 'GOOGLE_CLOUD_PROJECT' not in os.environ:
    os.environ['GOOGLE_CLOUD_PROJECT'] = 'gumo-core-test'

core_configure()


app = flask.Flask(__name__)


@app.route('/')
def hello():
    return f'Hello, world. (gumo-dev-server)'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

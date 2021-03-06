import logging
import os

from flask import Flask
from helloworld import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint)

logging.getLogger('flask_clova').setLevel(logging.DEBUG)


if __name__ == '__main__':
    if 'CLOVA_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('CLOVA_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['CLOVA_VERIFY_REQUESTS'] = False
    app.run(debug=True)

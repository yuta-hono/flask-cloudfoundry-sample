from flask import Flask
from flask import render_template as render
import os

app = Flask(__name__)

# Port number is required to fetch from env variable
# http://docs.cloudfoundry.org/devguide/deploy-apps/environment-variable.html#PORT

cf_port = int(os.getenv("PORT"))


# Most simple example
@app.route('/')
def hello():
    return 'Hello World.'


# To see env variables
@app.route('/vars')
def showCFVariables():
    cf_var_dict = {}

    for k in os.environ:
        cf_var_dict[k] = os.getenv(k)

    return render('index.html', variables=cf_var_dict)


if __name__ == '__main__':
    # Diego cells do not provide VCAP_APP_HOST
    # It is required to set as "0.0.0.0"
    # http://docs.cloudfoundry.org/devguide/deploy-apps/environment-variable.html#VCAP-APP-HOST
    app.run(host='0.0.0.0', port=cf_port, debug=True)

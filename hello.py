from flask import Flask
from flask import render_template as render
from flask import request
import os

app = Flask(__name__)

# Port number is required to fetch from env variable
# http://docs.cloudfoundry.org/devguide/deploy-apps/environment-variable.html#PORT

cf_port = int(os.getenv("PORT"))

"""[summary]
    Most simple example web application.
[description]
    Most simple example web application for Flask on Cloud Foundry.
    You can access this with "http://<yourapp_url>/".
"""


@app.route('/')
def hello():
    return 'Hello World.'


"""[summary]
    Cloud Foundry app container environmental variables / HTTP request headers.
[description]
    Cloud Foundry app container environmental variables / HTTP request headers.
    You can access this with "http://<yourapp_url>/vars/".
"""


@app.route('/vars')
def showCFVariables():
    cf_var_dict = {}

    # Get all environment variables from the CF application container
    for k in os.environ:
        cf_var_dict[k] = os.getenv(k)

    # Get the HTTP request header
    headers = request.headers
    print(headers)

    return render('index.html', cf_variables=cf_var_dict, http_headers=headers)

if __name__ == '__main__':
    # Diego cells do not provide VCAP_APP_HOST
    # It is required to set as "0.0.0.0"
    # http://docs.cloudfoundry.org/devguide/deploy-apps/environment-variable.html#VCAP-APP-HOST
    app.run(host='0.0.0.0', port=cf_port, debug=True)

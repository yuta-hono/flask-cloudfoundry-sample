from flask import abort, request
from flask import Flask

@app.route('/ip')
def showIp():
    srcIp = request.access_route[0]

    if srcIp != '10.20.30.40':
        abort(403)
    return 'Hello World.'

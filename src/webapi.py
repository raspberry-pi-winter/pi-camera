"""
   Module providing a function printing python version.
"""
import flask
import camera

from datetime import datetime
from waitress import serve
from flask import jsonify, make_response

app = flask.Flask(__name__)

def start_webapi(port=8000, debug=False):
    '''
    Start the web API
    '''
    if debug:
        print("Start Web API in debug mode")
        app.run(host="0.0.0.0", port=port)
    else:
        print("Start Web API")
        serve(app, host="0.0.0.0", port=port)

@app.route("/")
@app.route("/api/v1")
def main_api():
    """Function printing python version."""
    return jsonify(
        id = "this is a test"
    )

@app.route("/camera/get_image")
@app.route("/api/v1/camera/get_image")
def camera_get_image():
    """Function printing python version."""
    image = camera.capture()
    headers = {"Content-Disposition": "attachment; filename=%s" % "{0}-{1}.jpg".format("pi", datetime.utcnow().strftime("%Y%m%d-%H%M%S-%f"))}
    return make_response((image, headers))


if __name__ == "__main__":
    start_webapi()

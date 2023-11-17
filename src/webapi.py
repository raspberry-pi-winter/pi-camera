"""
   Module providing a function printing python version.
"""
import os
import base64

from datetime import datetime
from waitress import serve
from flask import Flask,jsonify, make_response, render_template, send_from_directory

import camera

app = Flask(__name__)

def start_web_server(port=8000, debug=False):
    '''
    Start the web API
    '''
    if debug:
        print("Start Web API in debug mode")
        app.run(host="0.0.0.0", port=port)
    else:
        print("Start Web API")
        serve(app, host="0.0.0.0", port=port)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route("/")
@app.route("/index.html")
def main_index():
    image = camera.capture()
    img_src = "data:image/jpeg;base64,%s" % base64.b64encode(image).decode()

    return render_template('camera.html', head = "Camera Capture", image_source=img_src)

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
    start_web_server()

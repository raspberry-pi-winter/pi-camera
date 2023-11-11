
"""
   Module providing a function printing python version.
"""
import io
from picamera2 import Picamera2

cam=Picamera2()
#capture_config = self.cam.create_still_configuration(main={"size": (1640, 1232), }, buffer_count=2, encode = "main")
capture_config = cam.create_still_configuration(buffer_count=2)
cam.configure(capture_config)
cam.start()

#img =cam.capture_image()

def capture():
    img  = cam.capture_image()
    output = io.BytesIO()
    img.save(output, format='JPEG')
    return output.getvalue()
import time
from flask import Flask, url_for, render_template
from flask import request, Response
import cv2
from numpy import array
from servo import Servo

app = Flask(__name__, static_url_path = "", static_folder = "static" )

app.secret_key = 'X456yhj3k510oq'
servobase = Servo(18)
servoaltura = Servo(19)
servoinclinacao = Servo(17)

def gen():
    CAM = cv2.VideoCapture(0)
    while True:
        ret, image = CAM.read()
        frame = b''
        if image is not None:
            f = "./static/images/tmp/frame.jpeg"
            cv2.imwrite(f, image)
            frame = open(f, 'rb').read()
            #ret, frame = cv2.imencode('.png', image)
            #frame = array(frame).tostring()
        
        yield (b'--frame\r\n' +
               b'Contetn-Type:image/jpeg\r\n\r\n' +
               frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(), 
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/arm", methods=["GET"])
def move_arm():
    

    if "anglebase" in request.args:    
        anglebase =  request.args["anglebase"]
        try:
            servobase.move_angle(int(anglebase))
        except:
            servobase.stop()
   

    if "angup" in  request.args:
        angup =  request.args["angup"]
        try:
            servoaltura.move_angle(int(angup))
        except:
            servoaltura.stop()

    if "angfront" in request.args:
        angfront =  request.args["angfront"]
        try:
            servoinclinacao.move_angle(int(angfront))
        except:
            servoinclinacao.stop()
    
    
    

    
        
    return ""

@app.route("/")
def home():
    return render_template("home.html")



if __name__ == "__main__":
    
    app.run(debug=True, host="0.0.0.0", port=8080)
    




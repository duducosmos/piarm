import time
from flask import Flask, url_for, render_template
from flask import request



from servo import Servo 

app = Flask(__name__, static_url_path = "", static_folder = "static" )

app.secret_key = 'X456yhj3k510oq'
servobase = Servo(18)
servoaltura = Servo(19)
servoinclinacao = Servo(17)


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




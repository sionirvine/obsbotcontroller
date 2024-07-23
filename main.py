
# to communicate with OSC protocol
from pythonosc import udp_client

# get this values from the OBSBOT Center app, software settings, OSC
# set host to 127.0.0.1 on the OBSBOT Center settings.
DEFAULT_OSC_IP = "127.0.0.1"
DEFAULT_OSC_PORT = 16284

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def root():
    client = udp_client.SimpleUDPClient(DEFAULT_OSC_IP, DEFAULT_OSC_PORT)

    pitch = 0
    speed = 1
    pan = 0

    if request.method == 'POST':
        if request.form['command_move']:
            command_move = request.form['command_move']
            pitch = int(request.form['camera_pitch'])
            speed = int(request.form['camera_speed'])
            pan = int(request.form['camera_pan'])
            
            if command_move == 'left':
                pan = 129
            elif command_move == 'right':
                pan = -129

            client.send_message("/OBSBOT/WebCam/General/SetGimMotorDegree", [0,speed,pan,pitch])

    return render_template("main.html", data={    
        "speed": speed,
        "pan": pan,
        "pitch": pitch
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--ip", default="127.0.0.1", help="The IP of the OSC server.")
    # parser.add_argument("--port", type=int, default=16284, help="The port of the OSC server is listening on.")

    # args = parser.parse_args()

    
    # UDP Protocol is send-and-forget, we does not receive any responses.
    # client = udp_client.SimpleUDPClient(args.ip, args.port)

    # client.send_message("/OBSBOT/WebCam/General/Connected", [0])

    # client.send_message("/OBSBOT/WebCam/General/SetGimMotorDegree", [0,1,-129,90])
    # client.send_message("/OBSBOT/WebCam/General/SetGimMotorDegree", [0,1,129,90])
    
    # client.send_message("/OBSBOT/Webcam/General/ResetGimbal", [0, 0])
    # client.send_message("/OBSBOT/Webcam/General/SetGimbalLeft", [0, 4])
    # client.send_message("/OBSBOT/Webcam/General/SetGimbalUp", [0,0])
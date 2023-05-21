from flask import Flask, render_template, request
import socket
import smtplib 
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__, template_folder='C:\\Anul3_Semestrul2\\SM\\templates')
app.config['TEMPLATES_AUTO_RELOAD'] = True

def send_pin_states(red_state, green_state, blue_state):
    print(f"Received states: red={red_state}, green={green_state}, blue={blue_state}")
    server_address = ('98:DA:50:01:A3:FD', 1)
    sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    sock.connect(server_address)
    answers = f"red:{red_state}|green:{green_state}|blue:{blue_state}"
    print("Sending states:", answers)
    sock.send(answers.encode())
    sock.close()

     
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        red_state = request.form.get('red')
        green_state = request.form.get('green')
        blue_state = request.form.get('blue')
        send_pin_states(red_state, green_state, blue_state)
    return render_template('led.html')

if __name__ == '__main__':
    app.run(debug=True, port=5002)

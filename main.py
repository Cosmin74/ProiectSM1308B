from flask import Flask, render_template, request
import bluetooth

app = Flask(__name__, template_folder='C:\\Anul3_Semestrul2\\SM5\\templates')
app.config['TEMPLATES_AUTO_RELOAD'] = True

server_address = '98:DA:50:01:A3:FD'
port = 1  # Bluetooth port number
sock = None  # Bluetooth socket object

def establish_bluetooth_connection():
    global sock
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((server_address, port))

def send_pin_states(state):
    if sock is None:
        establish_bluetooth_connection()

    answers = f"{state}"
    print("Sending state:", answers)
    sock.send(answers.encode())

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        valoare = request.form.get('optiune')
        send_pin_states(valoare)
    return render_template('led.html')

if __name__ == '__main__':
    app.run(debug=True, port=5002)

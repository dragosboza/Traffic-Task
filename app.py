from flask import Flask
from flask import request
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'



@app.route('/', methods=['POST'])
def add_guide():
    

    type = request.json['type']
    address = request.json['detail']['destination']['address']
    port = request.json['detail']['destination']['port']
    protocol = request.json['detail']['protocol']['type']

    if protocol == 'udp':
        
        MESSAGE = "Hello! UDP Style"

        print("UDP target IP:", address)
        print("UDP target port:", port)
        print("message:", MESSAGE)

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        sock.sendto(bytes(MESSAGE, "utf-8"), (address, port))

    elif protocol == 'tcp':
        MESSAGE = "Hello! TCP Style"

        print("TCP target IP:", address)
        print("TCP target port:", port)
        print("message:", MESSAGE)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # UDP
        sock.connect((address, port))
        sock.sendto(bytes(MESSAGE, "utf-8"), (address, port))

    return 'Success'





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
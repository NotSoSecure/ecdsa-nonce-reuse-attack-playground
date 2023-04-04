from flask import Flask
import hashlib
import ecdsa
import base64
import os
from flask import request
from flask import send_from_directory

app = Flask(__name__, static_url_path='/static/')

sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)  # private key
private_key_int = sk.privkey.secret_multiplier
vk = sk.verifying_key  # public key

def generateNonce():
    return 1000;

def GenerateSignature(msg):
    hash_msg = hashlib.sha256(msg.encode('utf-8')).digest()  # hash the message
    sig = sk.sign_digest(hash_msg, sigencode=ecdsa.util.sigencode_der, k=generateNonce())
    return sig.hex()

def VerifySignature(msg, signature):
    hash_msg = hashlib.sha256(msg.encode('utf-8')).digest()
    return vk.verify_digest(bytes.fromhex(signature.strip()), hash_msg, sigdecode=ecdsa.util.sigdecode_der)

@app.route("/")
def index():
    print ("called")
    return app.send_static_file("index.html")

@app.route('/read_file')
def read_file():
    filename = request.args.get('filename')
    signature = request.args.get('signature')
    filepath = os.path.abspath("./files/" + filename)
    if VerifySignature(filename, signature):
        with open(filepath, 'r') as file:
            contents = file.read()
        return contents
    return "No file found"

@app.route('/list_files')
def list_files():
    folder_path = './files'
    file_names = os.listdir(folder_path)
    data = "["
    for file in file_names:
        data = data + "{\"file\":\"" + file + "\",\"sig\":\"" + GenerateSignature(file) + "\"},"
    data = data[:-1]
    data = data + "]"
    return data

if __name__ == '__main__':
    app.run(debug=True)
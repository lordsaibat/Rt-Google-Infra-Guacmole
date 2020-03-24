#!/bin/python3
import argparse, json, requests
from urllib.parse import urlencode

parser = argparse.ArgumentParser(description='Login to Guacmole and get the auth token')
parser.add_argument('--username', dest='username', action='store', help='username to guac')
parser.add_argument('--password', dest='password', action='store', help='pass to guac')
parser.add_argument('--host', dest='host', action='store',  help='host to guac')
parser.add_argument('--port', dest='port', action='store',  help='port to guac')

args = parser.parse_args()

Ihost=args.host
Iport=args.port
Iusername=args.username
Ipassword=args.password

def make_call (Ihost, Iport, Iusername, Ipassword):
    #'username=${var.guac-username}&password=${var.guac-password}' $'https://${var.guac-host}:${var.guac-port}/api/tokens
    host='https://' + str(Ihost) + ':' + str(Iport) + '/api/tokens'
    data = {"username": Iusername, "password": Ipassword}
    res = requests.post(host, data, verify=False)
    full_auth_code = res.text
    code=json.loads(full_auth_code)
    return code['authToken']
    #return code

code=make_call (Ihost, Iport, Iusername, Ipassword)
#printme=json.JSONEncoder().encode({"authToken": code})
#"{'authToken': " + "'" + str(code) + "'}"
#print(printme)
print(code)

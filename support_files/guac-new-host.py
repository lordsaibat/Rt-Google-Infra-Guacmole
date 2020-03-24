#!/bin/python3
import argparse, json, requests
from urllib.parse import urlencode

parser = argparse.ArgumentParser(description='Login to Guacmole and get the auth token')
parser.add_argument('--host', dest='host', action='store',  help='host to guac')
parser.add_argument('--port', dest='port', action='store',  help='port to guac')
parser.add_argument('--auth', dest='authtoken', action='store',  help='authtoken to guac')
parser.add_argument('--newhosttype', dest='newhosttype', action='store',  help='what type of connection')
parser.add_argument('--newhostport', dest='newhostport', action='store',  help='port number to new connection')
parser.add_argument('--newhostip', dest='newhostip', action='store',  help='ip address to new connection')
parser.add_argument('--newhostname', dest='newhostname', action='store',  help='name of the new connection')
parser.add_argument('--newhostusername', dest='newhostusername', action='store',  help='username of the new connection')
parser.add_argument('--newhostprivatekey', dest='newhostprivatekey', action='store',  help='private key to new connection')


args = parser.parse_args()

Ihost=args.host
Iport=args.port
IauthToken=args.authtoken
Inewhosttype=args.newhosttype
Inewhostport=args.newhostport
Inewhostip=args.newhostip
Inewhostname=args.newhostname
Inewhostusername=args.newhostusername
Inewhostprivatekey=args.newhostprivatekey

def make_call (Ihost, Iport, IauthToken, Inewhosttype, Inewhostport, Inewhostip, Inewhostname, Inewhostusername, Inewhostprivatekey):
    host="https://" + str(Ihost) + ":" + str(Iport) + "/api/session/data/postgresql/connections?token=" + str(IauthToken)
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    data={"parentIdentifier":"ROOT","name":str(Inewhostname),"protocol":"ssh","parameters":{"port":str(Inewhostport),"read-only":"","swap-red-blue":"","cursor":"","color-depth":"","clipboard-encoding":"","dest-port":"","recording-exclude-output":"","recording-exclude-mouse":"","recording-include-keys":"","create-recording-path":"","enable-sftp":"","sftp-port":"","sftp-server-alive-interval":"","enable-audio":"","font-size":"","server-alive-interval":"","backspace":"","terminal-type":"","create-typescript-path":"","hostname":str(Inewhostip),"username":str(Inewhostusername),"password":"","private-key":str(Inewhostprivatekey)},"attributes":{"max-connections":"","max-connections-per-user":"","weight":"","failover-only":"","guacd-port":"","guacd-encryption":""}}
    #print("-----DEBUG------")
    #print(host)
    #print(data)
    res = requests.post(host, data=json.dumps(data), headers=headers, verify=False)
    full_auth_code = res.text
    code=json.loads(full_auth_code)
    return code
output = make_call (Ihost, Iport, IauthToken, Inewhosttype, Inewhostport, Inewhostip, Inewhostname, Inewhostusername, Inewhostprivatekey)
print (output)
#!/bin/python3
import argparse, json, requests
from urllib.parse import urlencode

parser = argparse.ArgumentParser(description='Login to Guacmole and get the auth token')
parser.add_argument('--auth', dest='authtoken', action='store',  help='authtoken to guac')
parser.add_argument('--host', dest='host', action='store',  help='host to guac')
parser.add_argument('--port', dest='port', action='store',  help='port to guac')
parser.add_argument('--hosttodelete', dest='delhost', action='store',  help='port to guac')

args = parser.parse_args()

Ihost=args.host
Iport=args.port
IauthToken=args.authtoken
Ihosttodel=args.delhost

def find_id (Ihost, Iport, IauthToken, Ihosttodel):
    #'username=${var.guac-username}&password=${var.guac-password}' $'https://${var.guac-host}:${var.guac-port}/api/tokens
    host='https://' + str(Ihost) + ':' + str(Iport) + '/api/session/data/postgresql/connectionGroups/ROOT/tree?token=' + str(IauthToken)
    res = requests.get(host, verify=False)
    full_auth_code = res.text
    code=json.loads(full_auth_code)
    #which array has the name?
    try:
        for x in code['childConnections']:
            name=x['name']
            if (name == Ihosttodel):
                id=x['identifier']
                return id
                break
            else:
                continue
    except:
        print ("Could not make request!")

    

def del_id (id):
    host='https://' + str(Ihost) + ':' + str(Iport) + '/api/session/data/postgresql/connections/' + str(id) + '?token=' + str(IauthToken)
    res = requests.delete(host, verify=False)

id=find_id (Ihost, Iport, IauthToken, Ihosttodel)
del_id(id)

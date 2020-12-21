import http.client

def getIP():
    conn = http.client.HTTPConnection("ifconfig.me")
    conn.request("GET", "/ip")
    print(conn.getresponse().read())
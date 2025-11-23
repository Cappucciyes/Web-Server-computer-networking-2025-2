import json
import time 
import socket
import utils

def compareDict(a,b):
    if set(a.keys()) ^ set(b.keys()) != set():
        return False 

    for key in a.keys():
        if a[key] != b[key]:
            return False

    return True


def handleBoard(client_socket):
    header =  (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/event-stream\r\n"
        "Cache-Control: no-cache\r\n" 
        "Connection: keep-alive\r\n"
        "\r\n"
    )

    client_socket.sendall(header.encode())

    cache = json.loads(utils.getFileAsString("./db/fullList.json"))

    while True:
        updated = json.loads(utils.getFileAsString("./db/fullList.json"))
        if compareDict(cache, updated):
            time.sleep(1)
            continue

        frame = (
            f"event: update\n"
            f"data: {json.dumps(updated)}\n\n"
        )
        print(frame)

        try:
            client_socket.sendall(frame.encode())
        except:
            print("no client found")
            break

        cache = updated

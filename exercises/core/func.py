import socket


def send_udp_datagram(address, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect((address, port))
    print("UPD socket was connected")
    sock.send(b'ok')
    print("UPD package was send")
    sock.close()
    print("UPD socket was disconnected")
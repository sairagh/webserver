import argparse
import errno
import os
import socket
import ssl

SERVER_ADDRESS = 'localhost', 9000
REQUESTGET = b"""\
GET /new.html HTTP/1.1
Host: localhost:9000
"""
REQUESTPOST= b"""\
POST /login.html HTTP/1.1
Host: localhost:9000
Content-Type: application/x-www-form-urlencoded
Content-Length: 60

fileToUpload=&username=nikhil&password=nikhil&submit=success

"""
REQUESTPOST1= b"""\
POST /new.html HTTP/1.1
Host: localhost:9000
Cookie: username=nikhil
Content-Type: application/x-www-form-urlencoded
Content-Length: 38

fileToUpload=&name11=chickenbiryani&submit=Yummy

"""


def main(max_clients, max_conns):
    socks = []
    for client_num in range(max_clients):
        pid = os.fork()
        if pid == 0:
            print max_conns,max_clients
            for connection_num in range(max_conns):
                data=''
                sock = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
                sock.connect(SERVER_ADDRESS)
                sock.sendall(REQUESTGET)
                while True:
                    data_present = sock.recv(1024)
                    if not data_present:
                        break
                    data+=data_present
                print "REQUEST1\n"
                print data
                socks.append(sock)
                data=''
                sock1 = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
                sock1.connect(SERVER_ADDRESS)
                sock1.sendall(REQUESTPOST)
                while True:
                    data_present = sock1.recv(1024)
                    if not data_present:
                        break
                    data += data_present
                print "REQUEST2\n"
                print data
                data = ''
                socks.append(sock1)

                sock2 = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
                sock2.connect(SERVER_ADDRESS)
                sock2.sendall(REQUESTPOST1)
                while True:
                    data_present = sock2.recv(1024)
                    if not data_present:
                        break
                    data += data_present

                print "REQUEST3\n"
                print data

                socks.append(sock2)

                print(connection_num)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Test client for LSBAWS.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        '--max-conns',
        type=int,
        default=8,
        help='Maximum number of connections per client.'
    )
    parser.add_argument(
        '--max-clients',
        type=int,
        default=1,
        help='Maximum number of clients.'
    )
    args = parser.parse_args()
    main(args.max_clients, args.max_conns)
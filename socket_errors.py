import sys
import socket
import argparse

def main():
    # setup arguement parsing
    parser = argparse.ArgumentParser(description='Socket Error Examples')
    parser.add_argument(
        '--host', 
        action='store', 
        dest='host',
        required=False   
    )
    parser.add_argument(
        '--port', 
        action='store', 
        dest='port',
        type=int,
        required=False   
    )
    parser.add_argument(
        '--file', 
        action='store', 
        dest='file',
        required=False   
    )

    # give varibles to provided args
    given_args =parser.parse_args()
    host = given_args.host
    port = given_args.port
    file= given_args.file
    
    # create socket or exit with error
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as error:
        print('Error creating socket: {}'.format(error))
        sys.exit(1)

    # connect with host and port or exit with error
    try:
        sock.connect((host, port))
    except socket.gaierror as error:
        print(
            'Address related error connecting to server: {}'.format(error)
        )
        sys.exit(1)

    # send file or exit with error
    try:
        msg = 'GET {} HTTP/1.0\r\n\r\n'.format(file)
        sock.sendall(msg.encode('utf-8'))
    except socket.error as error:
        print('Error sending data: {}'.format(error))
        sys.exit(1)

    while True:
        # wait receive from remote host or exit woth error
        try:
            buffer = sock.recv(2048)
        except socket.error as error:
            print('Error receiving data: {}'.format(error))
            sys.exit(1)

        if not len(buffer):
            break
        # write received data
        sys.stdout.write(buffer.decode('utf-8'))

if __name__ == '__main__':
    main()

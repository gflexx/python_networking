import socket

def socket_mode():
    '''
        set blocking mode of server
        on local host, 
        sock.setblocking(0) to listen
        sock.setblocking(1) to block port
    '''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # set blocking mode and timeout
    sock.setblocking(1)
    sock.settimeout(0.5)

    # bind address then get address
    sock.bind(('127.0.0.1', 0))
    sock_addr = sock.getsockname()
    print('Server started on {}'.format(sock_addr))

    while 1:
        sock.listen(1)

socket_mode()
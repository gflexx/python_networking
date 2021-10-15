import socket

# get machine network info
def get_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print('Host Name: {}\nIP Address: {}'.format(host_name, ip_address))
    return host_name, ip_address

# host_name, ip_address = get_machine_info()


# get ip from host name
def get_remote_ip(remote_host):
    '''
        requires host name in 
        form of www.example.com
        otherwise throws error
    '''
    r_host = remote_host
    try:
        ip_address = socket.gethostbyname(r_host)
        print('Ip address of {} is {}'.format(r_host, ip_address))
        return ip_address
    except socket.error as eror_msg:
        print('{} occured in geting {}'.format(eror_msg, r_host))

# remote_ip = get_remote_ip('www.google.com')


# find name of service running on port
def find_port_service(ports, protocol):
    '''
        checks if tcp or udp protocol 
        used by the service on port
    '''
    prtcl = protocol
    allowed = ('tcp', 'udp')
    if prtcl not in allowed:
        print('Unsuported protocol: {} !'.format(prtcl))
        return None

    # multidimentianal list 
    # [[port(n)], [service(n)]]
    socket_pair = [[],[]]

    for port in ports:
        try:
            service =  socket.getservbyport(port, prtcl)
            print("Port: {} - Service: {}".format(port, service))
            socket_pair[0].append(port)
            socket_pair[1].append(service)
        except socket.error as sock_err:
            print("Error: {} in getting  port: {}".format(sock_err, port))
            return None
    return socket_pair

# services = find_port_service([80, 25], 'tcp')
# services = find_port_service([53, 69, 88], 'udp')
# print('\n{}'.format(services))

# get and set socket timeout
def socket_timeout():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Default timeout: {}'.format(sock.gettimeout()))

    # set timeout
    sock.settimeout(1000)
    print('Current timeout: {}'.format(sock.gettimeout()))

sock = socket_timeout()

import socket

# get machine ip address
def get_machine_ip():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print('Host Name: {}\nIP Address: {}'.format(host_name, ip_address))
    return host_name, ip_address

# host_name, ip_address = get_machine_ip()


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

# remote_ip = get_remote_ip('www.youtube.com')



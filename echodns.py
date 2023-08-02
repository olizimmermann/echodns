import argparse
import multiprocessing
import os
import pathlib
import socket
import sys
import threading
import time
from datetime import datetime, timedelta

from oztools import loguroz

# developed by github.com/olizimmermann
# initial inspiration from https://www.youtube.com/user/CreatiiveCode
# https://www.ietf.org/rfc/rfc1035.txt # dns protocol


# Use EchoDNS for analyzing dns traffic
# Run it via python3 echodns.py
# Not suited as default dns server, only for analyzing.
# Please check regulary on Github for latest updates

# configuration possible below

version = "0.0.2"
logo = r"""
  ___    _        ___  _  _ ___ 
 | __|__| |_  ___|   \| \| / __|
 | _|/ _| ' \/ _ \ |) | .` \__ \
 |___\__|_||_\___/___/|_|\_|___/
 developed by OZ          v{}
 github.com/olizimmermann/echodns""".format(version)


################defaults###############
dns_server = '1.1.1.1' # used for forwarding
max_threads = 100 # 100 is default
max_thread_age = 1 # seconds - 5 is default
l_port = 53 # local port to listen
l_ip = '0.0.0.0' # '0.0.0.0' listen for all local ips
max_log_size = 100000 # maximal size of log before replacement
#####################################

###############LOGGING###############
logger = loguroz.Loguroz(pathlib.Path(__file__).parent, max_size=max_log_size)
DIR = os.path.dirname(pathlib.Path(__file__))
####################################


def dns_response(data, addr):
    """Extracting requested domain out of dns packet

    Args:
        data (bytes): DNS packet
        addr (tupel(ip,port)): address information

    Returns:
        bytes: dns answer packet
    """
    ip = addr[0]
    state = 0
    expected_length = 0
    domain_str = ''
    domain_parts = []
    x = 0
    y = 0
    for byte in data[12:]:
        if state == 1:
            if byte != 0:
                domain_str += chr(byte)
            x += 1
            if x == expected_length:
                domain_parts.append(domain_str)
                domain_str = ''
                state = 0
                x = 0
            if byte == 0:
                domain_parts.append(domain_str)
                break

        else:
            state = 1
            expected_length = byte
        y += 1 # QNAME and QTYPE

    domain_merge = ".".join(domain_parts[:-1])
    logger.info("DNS -> {0}".format(domain_merge), ip)
  
    dns_forward = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dns_forward.connect((dns_server, 53))
    dns_forward.send(data)
    return dns_forward.recv(512)

def handler(data,addr,sock):
    """Handling DNS traffic

    Args:
        data (bytes): DNS packet
        addr (tupel(ip,port)): address information
        sock (socket): current socket which listens as dns

    Returns:
        int: 1 without exceptions
    """
    try:
        answer = dns_response(data, addr)
        sock.sendto(answer, addr)
    except:
        return 0
    return 1

def garbage_collector(maxtime:int=5):
    """Cleans up all the running processes in case the didn't terminated themself

    Args:
        maxtime (int, optional): max seconds of age of a process. Defaults to 5.
    """
    logger.info("Garbage collector started")
    while 1:
        terminated = []
        for ts in all_threads:
            dif = datetime.now() - ts
            if dif > timedelta(seconds=maxtime):
                try:
                    all_threads[ts].terminate()
                    terminated.append(ts)
                except Exception as e:
                    pass
        for ts in terminated:
            del all_threads[ts]
        time.sleep(1)


if __name__ == '__main__':
    print(logo)
    print()


    # use argparse for more options
    # setup config vars
    parser = argparse.ArgumentParser(description='EchoDNS - DNS traffic analyzer', prog='echodns.py')
    parser.add_argument('-d', '--dns', help='DNS server to forward requests to', default=dns_server)
    parser.add_argument('-t', '--threads', help='Max amount of threads', default=max_threads)
    parser.add_argument('-a', '--age', help='Max age of thread in seconds', default=max_thread_age)
    parser.add_argument('-p', '--port', help='Local port to listen', default=l_port)
    parser.add_argument('-i', '--ip', help='Local ip to listen', default=l_ip)
    parser.add_argument('-l', '--log-size', help='Max size of log in kb', default=max_log_size)
    args = parser.parse_args()

    dns_server = args.dns
    max_threads = int(args.threads)
    max_thread_age = int(args.age)
    l_port = int(args.port)
    l_ip = args.ip
    max_log_size = int(args.log_size)




    logger.info("Starting EchoDNS v{0}".format(version))
    logger.info("Forward requests to DNS {0}".format(dns_server))
    logger.info("Listen to IP: {0}".format(l_ip))
    logger.info("Listen to port: {0}".format(l_port))
    logger.info("Max amount of threads: {0}".format(max_threads))
    logger.info("Max age of thread: {0} seconds".format(max_thread_age))
    logger.info("Max logging size: {0} kb".format(max_log_size/1000))

    all_threads = {}

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((l_ip, l_port)) # listening on all available ip addresses  
        garbage = threading.Thread(target=garbage_collector, args=(max_thread_age,))
        garbage.daemon = True
        garbage.start()
        while 1:
            



            if len(all_threads) < max_threads:
                data, addr = sock.recvfrom(512)
                now = datetime.now()
                t = multiprocessing.Process(target=handler, args=(data, addr, sock,))
                t.start()
                all_threads[now] = t
            else:
                logger.warning("Too many active threads. Max is set to: {0}".format(max_threads))
                
    except (KeyboardInterrupt, SystemExit):
        sys.exit()

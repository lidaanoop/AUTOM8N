#!/usr/bin/env python3
import cgitb
import os
import socket
import subprocess


# cpaneluser = os.environ["USER"]

def close_cpanel_liveapisock():
    """We close the cpanel LiveAPI socket here as we dont need those"""
    cp_socket = os.environ["CPANEL_CONNECT_SOCKET"]
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect(cp_socket)
    sock.sendall('<cpanelxml shutdown="1" />')
    sock.close()

cgitb.enable()

close_cpanel_liveapisock()

print('Content-Type: text/html')
print('hello world')

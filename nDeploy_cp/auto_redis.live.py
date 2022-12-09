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
print('')
print('<div class="container">')
print('  <div class="row text-center">')
print('    <div class="col-12">')
print('      <form method="post" id="toggleForm">')
print('        <fieldset>')
print('          <legend>on/off status for machine 1</legend>')
print('          <div class="form-group">')
print('            <div class="custom-control custom-switch">')
print('              <input type="checkbox" class="custom-control-input" id="customSwitch1" name="machine_state">')
print('              <label class="custom-control-label" id="statusText" for="customSwitch1"></label>')
print('            </div>')
print('          </div>')
print('        </fieldset>')
print('      </form>')
print('      <p class="text-center" id="updatedAt">Last updated at: </p>')
print('    </div>')
print('  </div>')
print('</div>')

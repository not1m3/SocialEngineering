################################
# Alan Bovo, Simone Ceccarelli #
################################

from pwn import *
from datetime import datetime


l = listen(8080)

svr = l.wait_for_connection()

log = open('log.txt', 'w')

ora = datetime.now()

while(True):
    log.write(str(svr.recv().decode('utf-8')))

######################
# not1m3, NullPh0bia #
######################

from pwn import *   #uso la libreria

porta = str(input("Inserisci la porta: "))  #chiedo la porta da utilizzare
porta = str(porta).replace("\n", "")    #levo il carattere a capo dalla porta
porta = int(porta)  #converto la porta da stringa a intero

l = listen(porta)   #ascolto sulla porta richiesta

svr = l.wait_for_connection()   #aspetto una connessione

log = open('log.txt', 'w')  #apro il file log.txt

while(True):    #inizio il ciclo principale
    log.write(str(svr.recv().decode('utf-8')))  #scrivo sul file i caratteri intercettati

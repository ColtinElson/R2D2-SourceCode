from gpiozero import LED, Button
from time import sleep
from signal import pause

led = LED(17)
button = Button(2)

code = {'-.' : a, '-...' : b, '-.-.' : c, '-..' : d,
        '..-.' : e, '--.' : f, '--.' : g, '....' : h,
        '..' : i, '.---' : j, '-.-' : k, '.-..' : l,
        '--' : m, '-.' : n, '---' : o, '.--.' : p,
        '--.-' : q, '.-.' : r, '...' : s, '-' : t,
        '..-' : u, '...-' : v, '.--' : w, '-..-' : x,
        '-.--' : y, '--..' : z}

phrase = raw_input("What would you like to say?")
phrase.lower()
len = len(phrase)
for letter in phrase:
    if letter == 'a':
        

import pyshorteners
from urllib.request import urlopen

def link_shortener(link):
    shortenet = pyshorteners.Shortener() 
    short_link = shortener.tinyurl.short(link)

    #Mostrarlo
    print('\t[+] Real link: ' + link)
    print('\t[+] Shortener link: ' + short_link)

def link_opener(link):
    shortened_url = urlopen(link)
    real_link = shortened_url.geturl() # obtenemos el link real

    #Mostrarlo
    print('\t[+] Real link: ' + link)
    print('\t[+] Shortener link: ' + real_link)

if __name__ == '__main__':
    num = input("Seleccione una opcion ...\n"
                "1.- Opcion 1 para acortar enlace\n"
                "2.- Opcion 2 para extraer un enlace real de un enlace acortado\n")

    link = input("Engrese el link: ")

if num == 1:
    link_shortener(link)
else:
    link_opener(link)


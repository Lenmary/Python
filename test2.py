from urllib import request
from urllib.error import URLError
palabras_ofensivas = ['bobo', 'tonto', 'bastardo', 'inuti', 'mendigo']
def ver_contenido(url):
    try: 
        f = request.urlopen(url)
    except URLError:
        return('La url ' + url + ' no existe')
    else:
        contenido = f.read()
        return contenido
        
def verificar_web(url):
    try:
        f = request.urlopen(url)
    except URLError:
        return('La url ' + url + ' no existe')
    else: 
        contenido = f.read()
        pagina = contenido.split()
        palabras = []
        for l in palabras_ofensivas :
            for con in pagina:
                if l in con.decode():
                    palabras.append(l)
        return palabras

url = 'https://www.bbc.com/mundo/noticias-37246013'
print('\nBuscando palabras inadecuadas... \n')
print(verificar_web(url)) 

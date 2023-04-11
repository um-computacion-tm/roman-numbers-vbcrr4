def conta_palabras (frase):
    palabras={}
    palabras_lts= frase.lower().split()
    for palabra in palabras_lts:
        if palabra in palabras:
            palabras[palabra]+=1
        else:
            palabras[palabra]=1 
    resultado=palabras
    return resultado

if __name__=="__main__":
    pass   
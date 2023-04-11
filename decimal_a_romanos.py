
def decimal_to_roman(romano):
    lts_m=["","M"] #genera lista mil
    lts_c=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]#lista para centenas 
    lts_d=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]#lista para decimos
    lts_u=["","I","II","III","IV","V","VI","VII","VIII","IX"]#lista para unidades
    cero=lts_m [romano//1000]
    centena=lts_c[(romano%1000)//100]
    decena=lts_d[(romano%100)//10]
    unidad=lts_u[romano%10] 

    resultado=(cero + centena + decena + unidad)
    return resultado
if __name__ == "__main__":
    pass
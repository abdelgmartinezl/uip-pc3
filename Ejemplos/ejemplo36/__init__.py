if __name__ == '__main__':
    ruta = '/Users/potty/Documents/Workspace/uip-pc3/Ejemplos/ejemplo36/wololo.txt'
    archivo = open(ruta, 'r')
    # print( archivo.read() )
    # print( archivo.readline() + " es antes que " + archivo.readline() ) 
    # print( archivo.readline() ) 
    
    dias_de_la_semana = archivo.readlines()
    fin_de_semana = ["sabado", "domIngo"]
    for dia in dias_de_la_semana:
        if any(d.lower() in dia.lower() for d in fin_de_semana):
            print(dia)

    ruta2 = 'Ejemplos\\ejemplo36\\pereza.txt'
    archivo_pereza = open(ruta2, 'w')
    archivo_pereza.write("Tengo pereza\n")
    archivo_pereza.write("Espero que el prof termine temprano")

    archivo.close()
    archivo_pereza.close()
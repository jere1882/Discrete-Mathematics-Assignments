#! /usr/bin/python

# 1ra Practica Laboratorio
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos

import sys

#FUNCIONES GERARDO
def leeEntrada():
    count = 0
    for line in sys.stdin:
        count = count + 1
        print "Linea: [{0}]".format(line)
    print "leidas {0} lineas".format(count)
def leeEntrada2():
    count = 0
    try:
        while (True):
            line = raw_input()
            count = count + 1
            print "Linea: [{0}]".format(line)
    except (EOFError):
        pass

    print "leidas {0} lineas".format(count)
def leeArchivo(file):
    print "leyendo archivo: {0}".format(file)
    count = 0
    for line in open(file, "r"):
        count = count + 1
        print "Linea: [{0}]".format(line)
    print "leidas {0} lineas".format(count)
#REPRESENTACION DE UN GRAFO COMO LISTA
def leerGrafoStdin():
    nodos = []
    for x in range(int(raw_input().strip())):
        nodos.append(raw_input().strip())
    aristas = []
    try:
        while True:
            new = raw_input().strip().split()
            aristas.append( (new[0], new[1]) )
    except (EOFError):
        pass
    return (nodos, aristas)
def imprimeGrafoLista(grafo):
    print "Nodos:"
    for x in grafo[0]:
        print x
    print "Aristas:"
    for x in grafo[1]:
        print x 
def leerGrafoArchivo(file):


	nodos=[]
	aristas=[]
	count=0
	
	for line in open(file, "r"):
		if count==0:
			cant_nodos=int(line.strip())
		elif count>0 and count <=cant_nodos :
			nodos.append(line.strip())
		else :
			raw=line.strip()
			aristas.append((raw.split()[0],raw.split()[1]))
		count+=1
	return (nodos,aristas)
#REPRESENTACION DE UN GRAFO CON SU MATRIZ DE ADYACENCIA
def listaAAdyacencia(grafo):

    fila_nula=[0]*len(grafo[0])
    MA=[]

    for n in range(len(grafo[0])):
        MA.append(fila_nula[:])  #creo la matriz nula n x n

    for v in grafo[1]:
		io= grafo[0].index(v[0]) #busco el indice del origen y destino 
		ide= grafo[0].index(v[1])
		MA[io][ide]+=1

    return (grafo[0],MA)
def adyacenciaALista(grafoA):
    cant_nodos=len(grafoA[0])
    nodos=[]
    gCopy=grafoA[:]
    for x in range(cant_nodos):
        for y in range(cant_nodos):
			for z in range(gCopy[1][x][y]): #un error fue usar un while
#que restara de a uno hasta q eso fuera cero, pero modifica la matriz.
				nodos.append(  (gCopy[0][x], gCopy[0][y])  )
				
                            
    return (grafoA[0],nodos)  
def imprimeGrafoAdyacencia(grafoA):
    imprimeGrafoLista(adyacenciaALista(grafoA))
def adyacenciaALista2(grafo):  #VERSION GERARDO
	nodos=grafo[0] #para no modificar
	MA=grafo[1]

	lista = [[(nodos[i],nodos[j])*MA[i][j]]
			 for i in range (0,len(nodos))
			 for j in range (0,len(nodos))
			 if MA[i][j]>0]

	lista2 = [i for fila in lista for i in fila]

	return (nodos,lista2)
#REPRESENTACION DE UN GRAFO CON SU MATRIZ DE INCIDENCIA
def listaAIncidencia(grafoLista):
    fila_cero=len(grafoLista[1])*[0]
    MI=[]
    for x in grafoLista[0]:
        MI.append(fila_cero[:])

    for x in range(len(grafoLista[1])):
        if grafoLista[1][x][0]==grafoLista[1][x][1]: #si es un lazo
            MI[grafoLista[0].index(grafoLista[1][x][0])][x]=2
        else:
            MI[grafoLista[0].index(grafoLista[1][x][0])][x]=-1
            MI[grafoLista[0].index(grafoLista[1][x][1])][x]=1

    return(grafoLista[0],MI)
def incidenciaALista(grafoIncidencia):

	aristas=[]
	MI=grafoIncidencia[1]
	cant_nodos=len(grafoIncidencia[0])
	if MI== []:
		return grafoIncidencia
	cant_aristas=len(grafoIncidencia[1][0])
	for x in range(cant_aristas):
		for y in range(cant_nodos):
			if MI[y][x]==2:
				destino=origen=grafoIncidencia[0][y]
			if MI[y][x]==1:
				destino=grafoIncidencia[0][y]
			if MI[y][x]==-1:
				origen=grafoIncidencia[0][y]
		aristas.append((origen,destino))


	return (grafoIncidencia[0],aristas)    
def imprimeGrafoIncidencia(grafoIncidencia):
    imprimeGrafoLista(incidenciaALista(grafoIncidencia))


def main():
	g=leerGrafoStdin()
	print g
	g=listaAAdyacencia(g)
	print adyacenciaALista2(g)
	g=adyacenciaALista2(g)


if __name__ == "__main__":
    main()

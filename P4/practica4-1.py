#! /usr/bin/python

# 5ta Practica Laboratorio 
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos

import sys

#FUNCION DE PCA. 3
def leerGrafoPesoArchivo(file):

    nodos=[]
    aristas=[]
    count=0
    for line in open(file, "r"):
        if count==0:
            cant_nodos=int(line.strip())
        elif count>0 and count <=cant_nodos :
            nodos.append(line.strip())
        else :
            new=line.strip().split()
            if len(new)==2:
                aristas.append((new[0],new[1],None))
            if len(new)==3:
                aristas.append( (new[0], new[1], float(new[2])) )
        count+=1
    return (nodos,aristas)


#FUNCIONES AUXILIARES

def primer_nodo(dic1,dic2): #devuelve el primer nodo no fijo de dic1.
	for x,y in dic2.iteritems():
		if y==0:
			return x
	return -1


def enum_aristas(v1, E): #devuelve una lista con todos los arcos que salen de v1.
	arcos=[]
	for x in E:
		if x[0]==v1:
			arcos.append(x)
	return arcos


def diksjtra (G, v): # Supongo como argumento un grafo ponderado donde TODAS sus aristas tienen peso

	costos={}           # Para cada nodo, costos[nodo] es el minimo costo actual de v-n
	fijado={}           # Indica si el nodo esta fijado (1) o aun esta calculandose su costo minimo (0)


    #INICIALIZAMOS LOS DICCIONARIOS

	for x in G[0]:
		fijado[x]=0
		costos[x]=-1

    #FIJAMOS EL VERTICE INICIAL v

	costos[v]=0
	fijado[v]=1

	for arco in enum_aristas(v, G[1]):
		costos[arco[1]]=arco[2]



    #PARTE RECURSIVA

	while ( 0 in fijado.values() ): #mientras haya algun nodo no revisado
	 # Agregar condición para que termine si no es conexo
		

		temp_n=primer_nodo(costos,fijado)
		temp_c=costos[temp_n]

		for nodo,costo in costos.iteritems(): #ubico el proximo nodo a fijar
			if (fijado[nodo]==0 and costo!=-1 and costo<temp_c) :
				temp_c=costo
				temp_n=nodo

		fijado[temp_n]=1 #fijo el nodo


		for arco in enum_aristas(temp_n,G[1]):#actualizo los costos de los nodos adyacentes al que acabo de fijar
			if (fijado[arco[1]]==0 and (costos[arco[1]] > temp_c + arco[2] or costos[arco[1]]==-1)):
				costos[arco[1]] = temp_c + arco[2]


	return costos


def dijkstra2(G, v): #idem anterior pero devuelve, ademas, el camino mas corto

	costos={}           # Para cada nodo, costos[nodo] es el minimo costo actual de v-n
	fijado={}           # Indica si el nodo esta fijado (1) o aun esta calculandose su costo minimo (0)
	anterior={}         # Indica el nodo precedente en el camino mas corto

    #INICIALIZAMOS LOS DICCIONARIOS

	for x in G[0]:
		fijado[x]=0
		costos[x]=-1
		anterior[x]=0

    #FIJAMOS EL VERTICE INICIAL v

	costos[v]=0
	fijado[v]=1
	anterior[v]=' ' #no hay nodo precedente

	for arco in enum_aristas(v, G[1]):
		costos[arco[1]]=arco[2]
		anterior[arco[1]]=v



    #PARTE RECURSIVA

	while ( 0 in fijado.values() ): #mientras haya algun nodo no revisado

		

		temp_n=primer_nodo(costos,fijado)
		temp_c=costos[temp_n]

		for nodo,costo in costos.iteritems(): #ubico el proximo nodo a fijar
			if (fijado[nodo]==0 and costo!=-1 and costo<temp_c) :
				temp_c=costo
				temp_n=nodo

		fijado[temp_n]=1 #fijo el nodo


		for arco in enum_aristas(temp_n,G[1]):#actualizo los costos de los nodos adyacentes al que acabo de fijar
			if (fijado[arco[1]]==0 and (costos[arco[1]] > temp_c + arco[2] or costos[arco[1]]==-1)):
				costos[arco[1]] = temp_c + arco[2]
				anterior[arco[1]] = temp_n


	caminos_mas_cortos={}
	
	for vertice in G[0]:
		camino=" "
		precedente=vertice		
		while (precedente!=v):
			camino=precedente+camino
			precedente=anterior[precedente]
		camino=v+camino
		caminos_mas_cortos[vertice]=camino
	
	return caminos_mas_cortos



def main():
	G=leerGrafoPesoArchivo(sys.argv[1])

	print dijkstra2(G,'A')

if __name__ == "__main__":
    main()

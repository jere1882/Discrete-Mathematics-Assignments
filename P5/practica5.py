#! /usr/bin/python

# 4ta Practica Laboratorio 
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos


import sys
    
    
    


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
	
	
def set2(lista):
    S={}
    for pos, elem in enumerate(lista) :
       S[elem] = pos 
    return S


def find(elem, disjointSet):
    try:
        return disjointSet[elem]
    except KeyError:
        print "ERROR: elemento no encontrado"
        return
    

def union(id1, id2, disjointSet):
    if id1==id2:
        # print "funcion union: ya es la misma particion"
        return disjointSet
    else:
        # print "funcion union: debo combinar la particion de identificador {1} con la de identificador {0}".format(id1,id2)
        for nodo, ident in disjointSet.iteritems(): #ident es el identificador de la particion
            if ident==id2:
                # print "el elemento {0} tiene identificador {1} y lo cambiare a {2}".format(nodo,ident,id1)
                disjointSet[nodo]=id1
    return disjointSet
        


def kruskal(grafo):
    S=set2(grafo[0])
    aristas=[]
    
    if len(grafo[1])==0:
        return grafo
        
        
    # ORDENO EN aristas, LAS ARISTAS DE MENOR A MAYOR PESO

    aristas.append(grafo[1][0])
    # aristas=grafo[1][:]
    # key_fn = lambda a: a[1]
    # aristas.sort(key=key_fn)   
    for a in grafo[1]:
        for i in range(len(aristas)+1):
            try:
                if aristas[i][2]>a[2]:
                    aristas.insert(i,a)
                    break
            except IndexError:
                aristas.append(a)
                break


    
    #ahora en ARISTAS estan las aristas ordenadas de menor a mayor peso
    
    
    
    arbol=[]
    
    for arista in aristas:
        if S[arista[0]]!=S[arista[1]]: #para no crear ciclos
            e1= arista[0]
            e2= arista[1]
            S = union( find(e1,S) , find(e2,S) , S)
            arbol.append(arista)
   
    #ahora en arbol estan las aristas de un arbol recubridor minimal 
         
    return (grafo[0],arbol)
            
        
   
    '''
    Dado un grafo (en formato de listas con pesos), aplica el algoritmo de 
    Kruskal y retorna el MST correspondiente (o un bosque, en el caso de que 
    no sea conexo) lo devolvemos en el mismo formato.
    '''
    



def min_arista (nodos , conjunto_aristas): 
    aristas=[]
    
    for a in conjunto_aristas:
        if  ( ((a[0] in nodos) and not(a[1] in nodos))  or  ((a[1] in nodos) and not(a[0] in nodos)) ) :
            aristas.append(a)
    #print "llamada a min arista, el conjunto de todas las adyacentes minimo es:"
    print aristas
    if aristas==[]:
	return -1

    min_cost=aristas[0][2]
    min_arista=aristas[0]
    
    for arista in aristas:
        if min_cost>arista[2]:
            min_cost=arista[2]
            min_arista=arista        
    #print "elegimos como minima a:"
    print min_arista
    return min_arista
        
#Devuelve todas las aristas de conjunto_aristas que tienen exactamente un extremo en nodos


def prim(grafo):
    cant_nodos=len(grafo[0])
    

    # En a_arbol se guardaran las aristas del arbol.
    n_arbol=[grafo[0][0]] #elegimos un vertice inicial cualquiera
    a_arbol=[]
    
    while (len(n_arbol)!=cant_nodos):
        arista=min_arista(n_arbol,grafo[1]) 

	#elijo la arista de menor peso adyacente a exactamente un vertice de n_arbol	
	if arista==-1:
	    print "Error: Grafo no conexo"
	    break
        if arista[1] in n_arbol:
            n_arbol.append(arista[0])
        else:
            n_arbol.append(arista[1])
    	a_arbol.append(arista)
    
    
    return (n_arbol , a_arbol)
    
    
    # itero sobre el conjunto de aristas que son adyacentes a un solo nodo del arbol hasta ahora
        
    
    


def main():
    
    print prim(leerGrafoPesoArchivo(sys.argv[1]))
    
if __name__ == "__main__":
    main()

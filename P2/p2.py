#! /usr/bin/python

# 2da Practica Laboratorio 
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos

# Un disjointSet lo representaremos como un diccionario. 
# Ejemplo: {"A":1, "B":2, "C":1} (Nodos A y C pertenecen al conjunto 
# identificado con 1, B al identificado on 2)

def set2(lista):
    S={}
    i=0
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
        

def componentesConexas(grafoLista):
    S=set2(grafoLista[0])
    for arista in grafoLista[1]:
        e1= arista[0]
        e2= arista[1]
        # print "analizo el arista de extremos {0}, {1}".format(e1, e2)
        S = union( find(e1,S) , find(e2,S) , S)

    particion = []
    for x in set(S.values()):
        P=[]
        for nodo,ident_nodo in S.iteritems():
            if ident_nodo==x:
                P.append(nodo)
        
        particion.append(P)
        
        
    return particion
        



def main():
   
    G=  (['A','B','C','D','E','F'],[('A','B'),('B','C'),('D','E')])
    print componentesConexas(G)
    
    
if __name__ == "__main__":
    main()

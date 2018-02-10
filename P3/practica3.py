#! /usr/bin/python

# 3ra Practica Laboratorio 
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos


# Referencias:
# pygraphMl    : http://hadim.github.io/pygraphml/usage.html
# GraphML      : http://graphml.graphdrawing.org/
# XML          : http://www.w3schools.com/xml/
# Editores     : http://www.cs.bilkent.edu.tr/~ivis/layout/demo/lw1x.html
#                http://cytoscapeweb.cytoscape.org/demo
#                http://cytoscape.org/
# elementTree  : http://docs.python.org/2/library/xml.etree.elementtree.html 

import sys
from pygraphml import *

def leerGrafoPesoStdin():
    
    nodos = []
    for x in range(int(raw_input().strip())):
        nodos.append(raw_input().strip())
    aristas = []
    try:
        while True:
            new = raw_input().strip().split()
            if len(new)==2:
                aristas.append((new[0],new[1],None))
            if len(new)==3:
                aristas.append( (new[0], new[1], float(new[2])) )     
    except (EOFError):
        pass
    return (nodos, aristas)


def imprimeGrafoPesoLista(grafo):
    print "nodos:"
    for x in grafo[0]:
        print x
    print "aristas:"
    for x in grafo[1]:
        print "extremos arista {0} y {1}, peso {2}".format(x[0],x[1],x[2])
   

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
	


def leeGraphML(file):
    from pygraphml.GraphMLParser import GraphMLParser
    parser = GraphMLParser()
    g = parser.parse("a.graphml")
    dir(grafo) #examinamos el grafo
    nodos=grafo.nodes()
    


def leeGraphML2(file):
    '''
    OPCIONAL
    Lee un grafo en formato graphML, recorriendo el XML con la libreria 
    elementTree (xml.etree.ElementTree), y lo devuelve como lista con pesos
    '''
    pass





def main():
    print leerGraphMl(sys.argv[1])
if __name__ == "__main__":
    main()

#! /usr/bin/python
import argparse
import Gnuplot
import random
import time

x = 0
y = 1

grafo1 = ([1, 2, 3, 4, 5, 6, 7],   [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 1)])
grafo2 = ([1, 2, 3, 4, 5, 6, 7],   [(1, 3), (2, 3), (1, 7), (6, 5), (6, 7) ])
grafo3 = ([1, 2, 3, 4, 5, 6, 7],   [(1, 5), (2, 5), (3, 5), (6, 7), (3, 7), (4,7) ])
grafo4 = ([1, 2, 3, 4, 5, 6, 7],   [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)])  #grafo estrella
grafo5 = ([1, 2, 3, 4, 5, 6, 7],   [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),(2,3),(3,4),(4,5),(5,6),(6,7),(7,2)]) #grafo rueda 
grafo6 = ([1, 2, 3, 4, 5, 6, 7],   [(4, 5), (4, 6), (4, 7),(1,2)]) # 3 componentes


class LayoutGraph():
    def __init__(self, grafo, iters, refresh, Ca, Cr, verbose=False):
        self.grafo = grafo
        self.nodos = self.grafo[0] 
        self.aristas = self.grafo[1] 

        # Inicializo estado

        self.posiciones = {}
        self.fuerzas = {}

        # Guardo opciones
        self.iters = iters
        self.verbose = verbose
        self.refresh = refresh
        self.Cr = Cr
        self.Ca = Ca
        self.temp = 1


    def randomize(self):
        for nodo in self.nodos:
            a = random.randint(-125, 125)
            b = random.randint(-125, 125)
            self.posiciones[nodo] = [a,b]
		
    def fuerza_rep (self, n1, n2): # fuerza que actua sobre n1
        dif = F = [0,0]
        dif[x] = self.posiciones[n1][x]-self.posiciones[n2][x]
        dif[y] = self.posiciones[n1][y]-self.posiciones[n2][y]
        distancia = (dif[x]**2 + dif[y]**2  ) **0.5
        Fmod = self.Cr / distancia**0.8
        F[x] = dif[x] * Fmod / distancia
        F[y] = dif[y] * Fmod / distancia
        return F

    def fuerza_atr (self, arista):
        dif = F = [0,0]
        dif[x] = self.posiciones[arista[0]][x]-self.posiciones[arista[1]][x]
        dif[y] = self.posiciones[arista[0]][y]-self.posiciones[arista[1]][y]
        distancia = (dif[x]**2 + dif[y]**2  ) **0.5
        Fmod = self.Ca * (distancia**0.8)  # Ca = constante de atraccion
        if distancia==0: distancia=0.0001
        F[x] = -( dif[x] * Fmod / distancia )
        F[y] = -( dif[y] * Fmod / distancia )
        return F

    def step(self):
        ACUMx={}
        ACUMy={}
    # 1: Calcular repulsiones de nodos (actualiza fuerzas)
        for nodo in self.nodos:
            ACUMx[nodo] = 0
            ACUMy[nodo] = 0
    # Calculamos las fuerzas de repulsion
        for node1 in self.nodos:
            for node2 in self.nodos:
                if node1 == node2:    continue
                # Fuerza de node2 sobre node1
                F = self.fuerza_rep (node1, node2)
                ACUMx[node1] += F[x]
                ACUMy[node1] += F[y]

    # Calculamos las fuerzas de atraccion
        for arista in self.aristas:
            F = self.fuerza_atr(arista)  
            ACUMx[arista[0]] += F[x]
            ACUMx[arista[1]] -= F[x]
            ACUMy[arista[0]] += F[y]
            ACUMy[arista[1]] -= F[y]

    # 3: En base a fuerzas, actualizar posiciones, setear fuerzas a cero
        for nodo in self.nodos:
            modulo = (ACUMx[nodo]**2 + ACUMy[nodo]**2)**(1/2)
            dentro_de_la_pantalla = (-125 < self.posiciones[nodo][x]+ACUMx[nodo] < 125 and -125 < self.posiciones[nodo][y]+ACUMy[nodo] < 125)
            if not dentro_de_la_pantalla: continue
            self.posiciones[nodo][x] += ACUMx[nodo]
            self.posiciones[nodo][y] += ACUMy[nodo]         
       


    def dibujar(self):
        i = 1
        g = Gnuplot.Gnuplot()
        g('set title "Grafo"')
        g('set xrange [-300:300]; set yrange [-300:300]')
        for nodo in self.nodos:
            str = 'set object {0} circle center {1},{2} size 3,5 fc rgb "black"'.format(i,self.posiciones[nodo][x],self.posiciones[nodo][y])
            g(str)
            i += 1
        for arista in self.aristas:
            x_1 = self.posiciones[arista[0]][x]
            y_1 = self.posiciones[arista[0]][y]
            x_2 = self.posiciones[arista[1]][x]
            y_2 = self.posiciones[arista[1]][y]
            str ='set arrow nohead from {0},{1} to {2},{3}'.format( x_1, y_1, x_2, y_2)
            g(str)                          
        g('unset key')
        g('plot NaN')
        time.sleep(0.5)


    def layout(self):
        '''
        Aplica el algoritmo de Fruchtermann-Reingold para obtener (y mostrar)
        un layout
        '''

        # Inicializamos las posiciones
        self.randomize()

        # Si es necesario, lo mostramos por pantalla
        if (self.refresh > 0):
            self.dibujar()

        # Bucle principal
        for i in range(self.iters): 
            self.step()
            # Realizar un paso de la simulacion
            

            # Si es necesario, lo mostramos por pantalla
            if (self.refresh > 0 and i % self.refresh == 0): self.dibujar()

        # Ultimo dibujado al final
        self.dibujar()


def main():
    # Definimos los argumentos de lina de comando que aceptamos
    parser = argparse.ArgumentParser()

    # Verbosidad, opcional, False por defecto
    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        help='Muestra mas informacion')
    # Cantidad de iteraciones, opcional, 50 por defecto
    parser.add_argument('--iters', type=int,
                        help='Cantidad de iteraciones a efectuar',
                        default=50)
    parser.add_argument('--graph', type=str,
                        help='Direccion del grafo a utilizar',
                        default='')

    args = parser.parse_args()

    # Creamos nuestro objeto LayoutGraph
    if args.graph: 
        grafo = leerGrafoArchivo( args.graph )


    else: grafo = grafo5

    layout_gr = LayoutGraph(
        grafo,
        iters = 400,
        refresh = 20,
        Cr = 25,
        Ca = 0.1,
        verbose = args.verbose
        )

    # Ejecutamos el layout
    layout_gr.layout()

    return

def leerGrafoArchivo(file):
    nodos=[]
    aristas=[]
    count=0
    f = open(file, "r")
    for line in f:
        if count==0:
            cant_nodos=int(line.strip())
        elif count>0 and count <=cant_nodos :
            nodos.append(line.strip())
        else :
            raw=line.strip()
            aristas.append((raw.split()[0],raw.split()[1]))
        count+=1
    f.close()
    return (nodos,aristas)




if __name__ == '__main__':
    main()

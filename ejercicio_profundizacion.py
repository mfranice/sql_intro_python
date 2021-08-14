import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes
import sqlite3

def fetch():

    conn = sqlite3.connect('heart.db')
    c = conn.cursor()
    c.execute('SELECT pulso FROM sensor')
    data = c.fetchall()
    print(data)

    conn.close()

    return data

def show(data):

    fig = plt.figure()
    fig.suptitle('Ritmo cardíaco durante un partido de futbol', fontsize = 16)
    ax = fig.add_subplot()
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Pulsos')
    ax.plot(data)
    plt.show()

    return


def estadistica(data):

    valor_medio = np.mean(data)
    print('Valor medio', valor_medio)
    valor_min = np.min(data)
    print('Valor mínimo', valor_min)
    valor_máximo = np.max(data)
    print('Valor máximo', valor_máximo)
    desvio_stnd = np.std(data)
    print('Desvio estandar', desvio_stnd)
    
    return


def regiones(data):

    mean = np.mean(data)
    std = np.std(data)

    x1 = [x for x in range(len(data)) if data[x] <= (mean - std)]
    y1 = [data[x] for x in range(len(data)) if data[x] <= (mean - std)]

    x2 = [x for x in range(len(data)) if data[x] >= (mean + std)]
    y2 = [data[x] for x in range(len(data)) if data[x] >= (mean + std)]

    x3 = [x for x in range(len(data)) if (mean - std) <= data[x] <= (mean + std)]
    y3 = [data[x] for x in range(len(data)) if (mean - std) <= data[x] <= (mean + std)]

    fig = plt.figure()
    fig.suptitle('Regiones', fontsize = 18)

    ax = fig.add_subplot()
    ax.scatter(x1, y1, color = 'gray', label = 'Aburrido', marker = '.')
    ax.scatter(x2, y2, color = 'red', label = 'Exaltado', marker = '.')
    ax.scatter(x3, y3, color = 'green', label = 'Tranquilo', marker = '.')

    ax.legend()
    plt.show()

    return


if __name__ == '__main__':

    data = fetch()
    show(data)
    estadistica(data)
    regiones(data)



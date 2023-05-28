import csv

nombreArchivo = 'lista_estudiantes.csv'
listaDatos = []

def getId(indice):
    return listaDatos[indice][0]


def getNombre(indice):
    return listaDatos[indice][1]


def getApellido(indice):
    return listaDatos[indice][2]


def getEdad(indice):
    return listaDatos[indice][3]


def getNota1(indice):
    return listaDatos[indice][4]


def getPorcentajeNota1(indice):
    return listaDatos[indice][5]


def getNota2(indice):
    return listaDatos[indice][6]


def getPorcentajeNota2(indice):
    return listaDatos[indice][7]


def getNota3(indice):
    return listaDatos[indice][8]


def getPorcentajeNota3(indice):
    return listaDatos[indice][9]


def getNota4(indice):
    return listaDatos[indice][10]


def getPorcentajeNota4(indice):
    return listaDatos[indice][11]


def getNota5(indice):
    return listaDatos[indice][12]


def getPorcentajeNota5(indice):
    return listaDatos[indice][13]

def leerArchivo():
    with open(nombreArchivo, 'r', encoding='utf-8') as archivocsv:
        lector = csv.reader(archivocsv)
        next(lector)        # Salta la primera linea
        for fila in lector:
            listaDatos.append(fila)
        return listaDatos

def formatearNotas(lista):
    for n in range(len(lista)):
        lista[n][4] = lista[n][4].replace(',', '.')  # Nota 1
        lista[n][6] = lista[n][6].replace(',', '.')  # Nota 2
        lista[n][8] = lista[n][8].replace(',', '.')  # Nota 3
        lista[n][10] = lista[n][10].replace(',', '.')  # Nota 4
        lista[n][12] = lista[n][12].replace(',', '.')  # Nota 5


def imprimirLista(lista):
    for n in range(len(lista)):
        print(  "Lista de estudiantes: \n"+
            "Id: " + lista[n][0] +
            " |Nombres: " + lista[n][1] +
            " |Apellidos: " + lista[n][2] +
            " |Edad: " + lista[n][3] +
            " |Nota 1: " + lista[n][4] + " |% Nota 1: " + lista[n][5] +
            " |Nota 2: " + lista[n][6] + " |% Nota 2: " + lista[n][7] +
            " |Nota 3: " + lista[n][8] + " |% Nota 3: " + lista[n][9] +
            " |Nota 4" + lista[n][10] + " |% Nota 4: " + lista[n][11] +
            " |Nota 5: " + lista[n][12] + " |% Nota 5: " + lista[n][13])


def imprimirEstudiante(lista, Id):
    for n in range(len(lista)):
        if lista[n][0]==Id:
            return(
                "Id: " + getId(n) +
                " |Nombres: " + getNombre(n) +
                " |Apellidos: " + getApellido(n) +
                " |Edad: " + getEdad(n) +
                " |Nota 1: " + lista[n][4] + " |% Nota 1: " + lista[n][5] +
                " |Nota 2: " + lista[n][6] + " |% Nota 2: " + lista[n][7] +
                " |Nota 3: " + lista[n][8] + " |% Nota 3: " + lista[n][9] +
                " |Nota 4" + lista[n][10] + " |% Nota 4: " + lista[n][11] +
                " |Nota 5: " + lista[n][12] + " |% Nota 5: " + lista[n][13])
    return "No se encontro el estudiante con el id: "+Id+"\n\n\n"





def getPromedio(indice):
    promedio = float(getNota1(indice)) * float(getPorcentajeNota1(indice).rstrip('%'))/100 +\
               float(getNota2(indice)) * float(getPorcentajeNota2(indice).rstrip('%'))/100 +\
               float(getNota3(indice)) * float(getPorcentajeNota3(indice).rstrip('%'))/100 +\
               float(getNota4(indice)) * float(getPorcentajeNota4(indice).rstrip('%'))/100 +\
               float(getNota5(indice)) * float(getPorcentajeNota5(indice).rstrip('%'))/100
    return promedio

def promedioMaximo(listaDatos):
    promedioMax = 0
    id= 0
    for n in range(len(listaDatos)):
        if getPromedio(n) > promedioMax:
            promedioMax = getPromedio(n)
            id=getId(n)
    resultado= "El estudiante con el promedio mas alto es: \n" + imprimirEstudiante(listaDatos,id) + \
               "\nCon un promedio de: "+str(promedioMax)
    return resultado

if __name__ == '__main__':
    listaDatos = leerArchivo()
    formatearNotas(listaDatos)
    imprimirLista(listaDatos)
    print("\n\n\n")
    print("------------------------")
    print(promedioMaximo(listaDatos))


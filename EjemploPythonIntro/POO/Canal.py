from abc import ABC, abstractmethod

"""
La plataforma de streaming “PIRATAHN” desea llevar un control de los programas de televisión que emite
para lo cual requiere un listado de canales por ejemplo, canal Fox, canal Star, etc de los canales se
requiere su nombre, código, país de origen, y así mismo si se paga por suscripción o no y el monto que
se paga mensual por la suscripción,  de igual manera se desea llevar un control de productos terminados
dé cada canal que son las películas y las series de las cuales son dueños (solo van a existir estos dos
productos terminados), de cada serie se desea guardar el nombre de la serie, el año de publicación, el
ranking, costos y visualizaciones,  cada serie tiene un numero de temporadas y cada temporada está
conformada por un número de capítulos, nombre y duración del mismo(minutos) y el ranking del capítulo,
de las películas se desea saber el nombre de la película, el año de publicación, el ranking y,
genero(que pueden ser varios), actor principal(que pueden ser varios), costos y visualizaciones.
Tanto las películas como las series tienen una recaudación, esa recaudación es un cálculo,
para las series que tienen una temporada la recaudación es igual al 20% de los costos entre las visualizaciones,
si tiene mas de una temporada será igual al 50% de los costos entre las visualizaciones por el total de temporadas,
 en el caso de las películas es igual al 80% de los costos entre las visualizaciones.

Así mismo se realiza un calculo para saber cuanto se saca de utilidad por canal datos que se obtiene multiplicando
el costo por suscripción mensual por la cantidad de productos del canal
"""

class Canal:
    def __init__(self, nombre, codigo, porigen, susc, monto):
        self.nombre = nombre
        self.codigo = codigo
        self.porigen = porigen
        self.susc = susc
        self.monto = monto
        self.productosTerminados = []
        self.peliculas = []
        self.series = []

    def utilidad(self):
        pass

    def AddProductosTerminado(self, producto):
        self.productosTerminados.append(producto)

        if isinstance(producto, Pelicula):
            self.peliculas.append(producto)
        else:
            self.series.append(producto)


    def __str__(self):
        return f"Nombre: {self.nombre}"

    @staticmethod
    def MostrarProductosTerminados(productosTerminados):
        for producto in productosTerminados:
            print(producto)

class ProductoTerminado(ABC):
    def __init__(self, nombre, anno, ranking, costos, visualizaciones):
        self.nombre = nombre
        self.anno = anno
        self.ranking = ranking
        self.costos = costos
        self.visualizaciones = visualizaciones

    @abstractmethod
    def recuaudacion(self):
        pass


class Pelicula(ProductoTerminado):
    def __init__(self, nombre, anno, ranking, costos, visualizaciones, actor, generos):
        super().__init__(nombre, anno, ranking, costos, visualizaciones)
        self.actor = actor
        self.generos = generos

    def __str__(self):
        return f"Nombre: {self.nombre}, Actor: {self.actor}, Genero: {self.generos}"

    def recuaudacion(self):
        return 0.8 * self.costos / self.visualizaciones

class Serie(ProductoTerminado):
    def __init__(self, nombre, anno, ranking, costos, visualizaciones):
        super().__init__(nombre, anno, ranking, costos, visualizaciones)
        self.temporadas = []

    def __str__(self):
        return f"Nombre: {self.nombre}"

    def recuaudacion(self):
        if len(self.temporadas) == 1:
            return 0.2 * self.costos / self.visualizaciones
        else:
            return len(self.temporadas) * 0.5 * self.costos / self.visualizaciones

class Temporada:
    def __init__(self, numero, fecha):
        self.numero = numero
        self.fecha = fecha
        self.capitulos = []

    def __str__(self):
        return f"Numero: {self.numero}, Fecha: {self.fecha}"

class Capitulo:
    def __init__(self, nombre, duracion, ranking):
        self.nombre = nombre
        self.duracion = duracion
        self.ranking = ranking
        self.__accidentes = []

    def __str__(self):
        return f"Nombre: {self.nombre}, Duracion: {self.duracion}, Ranking: {self.ranking}"

    @property
    def propiedad(self):
        return 'esto es una propiedad'
    def add_accidente(self, accidente):
        self.__accidentes.append(accidente)

    def remove_accidente(self):
        self.__accidentes.pop()

    def showAccidentes(self):
        for accidente in self.__accidentes:
            print(accidente)


canal = Canal('Canal 5', 'c5', 'Honduras', True, 100.00)
print(canal)

pelicula = Pelicula('Avengers', 2015, 10, 100,
                    900000, 'Iron Man', 'Fantasia')

print(pelicula)

canal.AddProductosTerminado(pelicula)

print(canal.peliculas[0])
print(canal.productosTerminados[0])

serie = Serie('Juego de Tronos', 2012, 8,
              200, 899900)

print(serie)

canal.AddProductosTerminado(serie)

print(canal.peliculas[0])
print(canal.productosTerminados[1])
print(canal.series[0])

capitulo = Capitulo('Dragones', 10, 10)
capitulo2 = Capitulo('Dragones2', 20, 20)

temporada = Temporada('1', '2012-01-01')
temporada.capitulos.append(capitulo)
temporada.capitulos.append(capitulo2)

serie.temporadas.append(temporada)

print(serie.temporadas[0].capitulos[0].nombre)


Canal.MostrarProductosTerminados(canal.productosTerminados)

capitulo.add_accidente('no sabian que hiban a examen')
print(capitulo.showAccidentes())


print(capitulo.propiedad)
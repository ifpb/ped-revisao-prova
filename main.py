from arquivo import Arquivo
from fila import Fila

arquivo1 = Arquivo("foto1.jpg", 10000)
arquivo2 = Arquivo("foto2.jpg", 3000)
arquivo3 = Arquivo("foto3.jpg", 6000)
arquivo4 = Arquivo("foto4.jpg", 2000)
arquivo5 = Arquivo("foto5.jpg", 5000)


fila = Fila()
fila.inserir(arquivo1)
fila.inserir(arquivo2)
fila.inserir(arquivo3)
fila.inserir(arquivo4)
fila.inserir(arquivo5)
fila.remover()
fila.imprimir()
fila = fila.ordenar(fila)
print("Fila ordenada:")
fila.imprimir()
print("Buscando arquivo foto2.jpg:")
print(fila.buscar("foto4.jpg", fila))
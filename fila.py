from estrutura_linear import EstruturaLinear


class Fila(EstruturaLinear):
    def __init__(self):
        super().__init__()

    def inserir(self, valor):
        self.inserir_no_final(valor)

    def inserir_todos(self, lista):
        for i in lista:
            self.inserir(i.carga)

    def remover(self):
        return self.remover_do_inicio()

    def buscar(self, nome, arquivos, primeiro=0, ultimo=None):
        if not ultimo:
            ultimo = len(arquivos) - 1

        meio = (primeiro + ultimo) // 2

        if nome.lower() == arquivos[meio].carga.nome.lower():
            return arquivos[meio].carga.tamanho

        if meio == 0 or primeiro == ultimo:
            return -1

        if nome.lower() < arquivos[meio].carga.nome.lower():
            return self.buscar(nome, arquivos, primeiro, meio)
        else:
            return self.buscar(nome, arquivos, meio + 1, ultimo+1)

    def ordenar(self, lista):
        if len(lista) <= 1: return lista
        pivo = lista[0].carga.tamanho
        iguais = self.extrair_iguais(pivo, lista)
        menores = self.extrair_menores(pivo, lista)
        maiores = self.extrair_maiores(pivo, lista)

        resultado = Fila()
        resultado.inserir_todos(self.ordenar(menores))
        resultado.inserir_todos(iguais)
        resultado.inserir_todos(self.ordenar(maiores))

        return resultado

    def extrair_iguais(self, valor, lista):
        iguais = Fila()
        for i in range(len(lista)):
            if lista[i].carga.tamanho == valor:
                iguais.inserir(lista[i].carga)
        return iguais

    def extrair_menores(self, valor, lista):
        menores = Fila()
        for i in range(len(lista)):
            if lista[i].carga.tamanho < valor:
                menores.inserir(lista[i].carga)
        return menores

    def extrair_maiores(self, valor, lista):
        maiores = Fila()
        for i in range(len(lista)):
            if lista[i].carga.tamanho > valor:
                maiores.inserir(lista[i].carga)
        return maiores

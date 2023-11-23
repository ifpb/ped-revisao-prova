class Arquivo:
    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho

    def __str__(self):
        return f"Nome = {self.nome}, Tamanho = {self.tamanho}"

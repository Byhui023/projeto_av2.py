# Colégio Unasp-EC
#Turma: 2°A
#Disciplina: POO
#ALuno: Bianca Vitória Guimaro Dias
#25.05
class Livro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

class Usuario:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula

    def get_nome(self):
        return self.__nome

    def get_matricula(self):
        return self.__matricula


class Emprestimo:
    def __init__(self, usuario, livro):
        self.__usuario = usuario
        self.__livro = livro
        self.__status = "Ativo"

    def exibir_recibo(self):
        print("========== RECIBO DE EMPRÉSTIMO ==========")
        print(f"Usuário: {self.__usuario.get_nome()}")
        print(f"Matrícula: {self.__usuario.get_matricula()}")
        print("------------------------------------------")
        print(f"Livro: {self.__livro.get_titulo()}")
        print(f"Autor: {self.__livro.get_autor()}")
        print("------------------------------------------")
        print(f"Status do Empréstimo: {self.__status}")
        print("==========================================")


usuario1 = Usuario("Marina", "2026001")

livro1 = Livro("Casa Velha", "Machado de Assis")

emprestimo1 = Emprestimo(usuario1, livro1)

emprestimo1.exibir_recibo()
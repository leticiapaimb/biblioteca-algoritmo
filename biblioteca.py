
class Livro:
    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor



class Biblioteca:
    def __init__(self):
        # aqui usamos um dicionário para guardar os livros
        self.livros = {}

    # função para adicionar um livro
    def adicionar_livro(self, livro):
        # o id será a chave
        self.livros[livro.id] = livro

    # função para buscar um livro pelo id
    def buscar_livro(self, id):
        # retorna o livro se existir
        if id in self.livros:
            return self.livros[id]
        else:
            return None


#testando
biblioteca = Biblioteca()

# adicionando livros
biblioteca.adicionar_livro(Livro(1, "Dom Casmurro", "Machado de Assis"))
biblioteca.adicionar_livro(Livro(2, "1984", "George Orwell"))

# buscando um livro
livro = biblioteca.buscar_livro(1)

if livro:
    print("Livro encontrado:")
    print(livro.titulo, "-", livro.autor)
else:
    print("Livro não encontrado")
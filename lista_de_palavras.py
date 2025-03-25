import random

palavras = [
    "Abacaxi", "Aventura", "Aviao", "Amizade", "Barco", "Baleia", "Biblioteca", "Bicicleta",
    "Brinquedo", "Cachorro", "Cadeira", "Caminhao", "Caranguejo", "Carro", "Castelo",
    "Cavalo", "Chocolate", "Computador", "Deserto", "Dinossauro", "Elefante", "Escola",
    "Espelho", "Estrela", "Foguete", "Fotografia", "Futebol", "Geladeira", "Girassol",
    "Helicoptero", "Historia", "Hipopotamo", "Ilha", "Internet", "Inverno", "Jacare",
    "Jornal", "Labirinto", "Lanterna", "Leao", "Livro", "Lobo", "Marinheiro", "Montanha",
    "Musica", "Navio", "Oceano", "Orelha", "Palacio", "Papel", "Parque", "Passaporte",
    "Peixe", "Piano", "Piramide", "Planeta", "Planta", "Policia", "Ponte", "Professora",
    "Quadro", "Queijo", "Radio", "Relampago", "Relogio", "Rinoceronte", "Robo",
    "Sino", "Supermercado", "Tartaruga", "Telefone", "Tempestade", "Tesouro", "Tigre",
    "Trampolim", "Trator", "Trem", "Triangulo", "Tubarao", "Umbrella", "Universo",
    "Vampiro", "Veleiro", "Viagem", "Vulcao", "Xadrez", "Xicara", "Zebra", "Abelha",
    "Acucar", "Banana", "Cenoura", "Cerebro", "Churrasco", "Esmeralda", "Fada", "Fantasma",
    "Guitarra", "Harpa", "Jardim", "Mochila", "Navalha", "Neve", "Oculos", "Perola", "Relva"
]

def escolher_palavra():
    random.shuffle(palavras)
    return random.choice(palavras).upper()



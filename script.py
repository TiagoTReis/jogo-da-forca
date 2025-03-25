from Layout import mostrar_forca
from lista_de_palavras import escolher_palavra

palavra = escolher_palavra()
palavra = palavra.upper()
contador = len(palavra)
erros = 0
max_erros = 6
layout = ["_"] * contador

while "_" in layout and erros < max_erros:
    mostrar_forca(erros)
    print(" ".join(layout))
    insere = str(input("Digite uma letra: ")).upper()

    if insere in palavra:
        for i in range(contador):
            if palavra[i] == insere:
                layout[i] = insere
    else:
        erros +=1
        print("Letra nao encontrada")

if "_" not in layout:
    print("Parabéns! Você descobriu a palavra:", palavra)
else:
    mostrar_forca(erros)
    print("Fim de jogo! A palavra era:", palavra)
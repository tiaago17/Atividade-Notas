notas = []

for i in range(5):
    nome = str(input("Digite o seu nome: "))
    notaum = float(input("Digite sua nota na Avaliação 1: "))
    notadois = float(input("Digite sua nota na Avaliação 2: "))
    media = (notaum + notadois) / 2

    notas.append([nome, notaum, notadois, media])


print ("\n ---- RESULTADO FINAL ----")

for nota in notas:
    print(f"{nota[0]} - Nota 1: {nota[1]} | Nota 2: {nota[2]} | Média: {nota[3]:.2f}")

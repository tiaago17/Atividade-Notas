notas = []

for i in range(5):
    nome = str(input("Digite o seu nome: "))
    notaum = float(input("Digite sua nota na Avaliação 1: "))
    notadois = float(input("Digite sua nota na Avaliação 2: "))
    media = (notaum + notadois) / 2

    notas.append({
        "Nome": nome,
        "Nota 1": notaum,
        "Nota 2": notadois,
        "Média": media
    })


print ("\n ---- RESULTADO FINAL ----")

for nota in notas:
    print(f"{nota['Nome']} - Nota 1: {nota['Nota 1']} | Nota 2: {nota['Nota 2']} | Média: {nota['Média']:.2f}")
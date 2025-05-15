notas = []

for i in range(5):
    nome = str(input("Digite o seu nome: "))
    notaum = float(input("Digite sua nota na Avaliação 1: "))
    notadois = float(input("Digite sua nota na Avaliação 2: "))
    media = (notaum + notadois) / 2
    
    if media >= 6:
        situação = "Aprovado"

    else:
        situação = "Reprovado"

    notas.append([nome, notaum, notadois, media, situação])

    

print ("\n ---- RESULTADO FINAL ----")

for nota in notas:
    print(f"{nota[0]} - Nota 1: {nota[1]} | Nota 2: {nota[2]} | Média: {nota[3]:.2f} | Situação: {nota[4]}")
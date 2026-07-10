import re

padrao = r"^1\t(\d+)\t5\t\d+$"

filmes = []

with open("u.data", "r", encoding="utf-8") as arquivo:

    for linha in arquivo:

        linha = linha.strip()

        match = re.match(padrao, linha)

        if match:

            filme_id = match.group(1)

            filmes.append(filme_id)

with open(
    "filmes_user1_nota5.txt",
    "w",
    encoding="utf-8"
) as saida:

    for filme_id in filmes:

        saida.write(f"{filme_id}\n")

print(
    f"{len(filmes)} IDs salvos "
    f"em filmes_user1_nota5.txt"
)

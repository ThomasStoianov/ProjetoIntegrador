def validar_notas(notas):
    # Verifica se notas é uma lista ou está vazia, se for um dos casos, vai retornar False
    if not isinstance(notas, list) or len(notas) == 0:
        return False

    for nota in notas:
        # verifica se as notas são número e não strings ou booleanos, se for um dos casos retorna False
        if not isinstance(nota, (int, float)):
            return False
    
    return True

def calcular_media(notas):
    # soma as notas divido pela quantidade de notas, para calcular a media
    return sum(notas) / len(notas)

def processar_alunos(dados):
    alunos_validos = []
    recuperacao = []
    top_student = ("", 0)

    for nome, notas in dados:
        if not validar_notas(notas):
            print("Invalido: ", nome)
            continue

        media = calcular_media(notas)

        alunos_validos.append((nome, media))

        if (media < 7):
            recuperacao.append((nome, media))

        if (media > top_student[1]):
            top_student = (nome, media)

    return alunos_validos, recuperacao, top_student
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
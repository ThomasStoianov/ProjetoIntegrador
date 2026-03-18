from processamento import processar_alunos, gerar_relatorio

dados = [
    ("João", [8, 7, 9]), 
    ("Maria", [5, 6, 4]), 
    ("Pedro", [10, 9, 10]),  
    ("Ana", []),               
    ("Carlos", [7, "erro", 8]) 
]

alunos, recuperacao, top_student = processar_alunos(dados)

print("Alunos:", alunos)
print("Recuperação:", recuperacao)
print("Top Student:", top_student)

gerar_relatorio(alunos, recuperacao, top_student)

print("Relatório gerado!")
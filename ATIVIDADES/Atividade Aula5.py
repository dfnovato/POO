print("Programa de Calcular Media de Turma")
const_qtdprovas = 3 # Descobri que não existe constante em Python :(
qtd_provas = const_qtdprovas
qtd_alunos = int(input("Digite quantos alunos tem na turma: "))
soma_media_turma = 0
MediaMin = 7
# é possivel simplificar bastante o codigo abaixo porém optei por essa estrutura para exercitar a modularidade deste codigo futuramente.
for x in range(qtd_alunos, 0, -1): # utilizei a estrutura for conforme solicitado na questão abaixo optei pelo While somente para o exercitar na pratica
    nome = input(f"Nome do aluno: ")
    soma_nota = 0
    while qtd_provas>0:
        nota = float(input(f"Digite a nota do aluno {nome}: "))
        soma_nota += nota
        qtd_provas -=1
    else: #estou utilizando o else para reiniciar a variavel qtd_provas pois quando o laço while termina sem um break ele executa o else
        qtd_provas = const_qtdprovas
        
    media_aluno = soma_nota/const_qtdprovas
    soma_media_turma+=media_aluno
        
    if media_aluno >= MediaMin:
        Status = "Aprovado"
    else:
        Status = "Reprovado"
    print(f"Aluno: {nome}")
    print(f"Media: {media_aluno:.2f}")
    print(f"Status: {Status}\n")
    
media_turma = soma_media_turma / qtd_alunos
print(f"Media geral da turma: {media_turma:.2f}")
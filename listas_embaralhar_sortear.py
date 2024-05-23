import random
alunos=['João', 'Maria', 'Pedro', 'Ana', 'Lucas', 'Mariana']
print(f"lista:{alunos }")
#embaralhar a Lista
random.shuffle(alunos) 
print(f"lista embaralhada: {alunos}")
#escolhe um aluno aleatoriamente 
aluno_sorteado= random.choice (alunos)
print(f"aluno sorteado: {aluno_sorteado}")


import random
alunos=['João', 'Maria', 'Pedro', 'Ana', 'Lucas', 'Mariana']
print(f"lista:{alunos }")
#embaralhar a Lista
random.shuffle(alunos) 
print(f"lista embaralhada: {alunos}")
#Ordena a lista crescente 
alunos.sort()
print(f"lista crescente: {alunos}")
#ordena a lista decrescente 
alunos.sort(reverse=True)
print(f"lista decrescente:{alunos}")


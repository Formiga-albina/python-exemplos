print(f"Programa de empréstimo\n"
      f"Responda: (1-Sim ou 0-Não)")
nome_negativado=int(input('Possui nome negativado?: '))
if nome_negativado ==1:
    print('Não pode realizar empréstimo')
else:
    carteira_assinada=int(input('Possui carteira assinada?: '))
    if carteira_assinada ==0:
        print('Não pode realizar empréstimo')
    else:
        casa_propria=int(input('Você possui casa própria?: '))
        if casa_propria ==0:
            print('Não pode realizar empréstimo')
        else:
            print('Conceder o empréstimo')
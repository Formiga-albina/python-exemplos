def exibirMensagem(nome):
    print(f"Seja bem vindo {nome}")
    return f"usuario logodo: {nome}"

nome_usuario = input("digite o neme do usuario :")
msg = input("digite uma mensagem:")
usuario = exibirMensagem(nome_usuario, msg)
print(usuario)

print(50 * '-')

nome_usario = input('digite o nome de usuario:')
msg = input("digite uma mensagem :")
usuario = exibirMensagem(nome_usuario,msg)
print(usuario)
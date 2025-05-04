while True:
    usuario = input("Digite o nome de usuário (mínimo 5 caracteres): ")
    
    if len(usuario) < 5:
        print("O nome de usuário deve ter pelo menos 5 caracteres.")
        continue

    while True:
        senha = input("Digite a senha (mínimo 8 caracteres): ")
        if len(senha) < 8:
            print("A senha deve ter pelo menos 8 caracteres. Tente novamente.")
        else:
            print("Cadastro realizado com sucesso!")
            break
    break


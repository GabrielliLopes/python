usuario = input('Digite o seu usuario: ')
senha = input('Digite a sua senha: ')

login_valido = usuario == 'Admin' and senha == '123456'

print(f'login permitido: {login_valido}')
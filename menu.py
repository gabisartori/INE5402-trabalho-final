from user import User
from functions import *

def login(user_list):
    if len(user_list) == 0:
        # Não há necessidade de acessar o perfil admin se a rede não tem usuários
        print('Não há usuários cadastrados.')
        print('Para cadastrar um usuário, digite "2" no menu principal.')
        return
    
    admin_name = 'admin'
    admin_password = 'admin'
    admin_hash = sha256(admin_password)
    name = input('Insira o nome de usuário: ')
    password = input('Insira a senha: ')
    for user in user_list:
        if name == admin_name and sha256(password) == admin_hash:
            admin_menu()
            return
        elif user.name == name and user.password == password:
            print('Login realizado com sucesso!')
            user_menu()
            return
    
    print('Usuário ou senha inválidos!')



def menu():
    options = '''[1] Login
    [2] Cadastre-se
    [3] Sair
    '''

    while True:
        print('Seja bem-vinde ao redwitter!')
        print(options)
        option = input('Digite a opção desejada: ')
        if option == '1':
            login()
        elif option == '2':
            register_menu()
        elif option == '3':
            print('Programa encerrado.')
            break
        else:
            print('Opção inválida!')

def user_menu(user):
    pass

def admin_menu():
    options = '''
    [1] Deletar usuário
    [2] Deletar publicação
    [3] Listar usuários
    [4] Logout
    '''
    while True:
        print(options)
        option = input('Digite a opção desejada: ')
        if option == '1':
            delete_user()
        elif option == '2':
            delete_post()
        elif option == '3':
            list_users()
        elif option == '4':
            break
        else:
            print('Opção inválida!')

def register_menu(user_list):
    register_user(user_list)

def delete_user():
    pass

def delete_post():
    pass

def list_users():
    pass



menu()
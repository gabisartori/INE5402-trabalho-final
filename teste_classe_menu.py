from user import *
from functions import *

class Menu:
    menu_options = '''[1] Login
[2] Cadastre-se
[3] Sair
    '''

    admin_options = '''[1] Deletar usuário
[2] Deletar publicação
[3] Listar usuários
[4] Logout
    '''

    def __init__(self, user_list):
        self.user_list = user_list
    

    def run(self):
        while True:
            print('Seja bem-vinde ao redwitter!')
            print(self.menu_options)
            option = input('Digite a opção desejada: ')
            if option == '1':
                self.login_menu(self.user_list)
            elif option == '2':
                self.register_menu(self.user_list)
            elif option == '3':
                print('Programa encerrado.')
                break
            else:
                print('Opção inválida!')
    
    def login_menu(self, user_list):
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
                self.admin_menu(user_list)
                return
            elif user.name == name and user.password == password:
                print('Login realizado com sucesso!')
                self.user_menu(user)
                return
        
        print('Usuário ou senha inválidos!')
    

    def register_menu(self):
        name = input("Insira seu nome de usuário: ")
        private = input("Essa conta será privada? (s/n): ").strip()[0].lower() == 's'
        password = input("Insira sua senha: ")
        if password == input('Confira sua senha: '):
            user = User(name, len(self.user_list), private, password)
            self.user_list.append(user)
            print("User registered successfully!")
        else:
            print('Senhas não conferem! Tente novamente.')
            register_user(self.user_list)
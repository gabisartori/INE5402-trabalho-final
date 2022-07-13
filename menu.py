from user import *
from functions import *
import time

class Menu:
    menu_options = '''==============================
[1] Login
[2] Cadastre-se
[3] Sair
==============================
'''

    admin_options = '''==============================
[1] Deletar usuário
[2] Deletar publicação
[3] Listar usuários
[4] Logout
==============================
'''

    user_options = '''==============================
[1] Criar publicação
[2] Mostrar próxima página de publicações
[3] Acessar perfil
[4] Buscar perfil
[5] Abrir publicação
[6] Recarregar feed
[0] Logout
==============================
'''


    admin_name = 'admin'
    admin_password = 'admin'
    password_hash = sha256(admin_password)
    #admin_hash = ''

    def __init__(self, user_list):
        self.user_list = user_list
        self.creation_time = time.time()
        
    def get_post_list(self):
        temp = []
        for user in self.user_list:
            for post in user.posts:
                temp.append(post)
        
        temp.sort(key= lambda x: x.created_at, reverse=True)
        return temp

    def run(self):
        while True:
            print()
            print('Seja bem-vinde ao redwitter!')
            print(self.menu_options)
            option = input('Digite a opção desejada: ')
            if option == '1':
                # Inicia o menu de login
                self.login_menu()
            elif option == '2':
                # Inicia o menu de cadastro
                self.register_menu()
            elif option == '3':
                # Encerra o programa
                print('Programa encerrado.')
                break
            else:
                print('Opção inválida!')
    
    def login_menu(self):
        if len(self.user_list) == 0:
            # Não há necessidade de acessar o perfil admin se a rede não tem usuários
            print('Não há usuários cadastrados.')
            print('Para cadastrar um usuário, digite "2" no menu principal.')
            return
        
        
        name = input('Insira o nome de usuário: ')
        password = input('Insira a senha: ')
        for user in self.user_list:
            if name == self.admin_name and sha256(password) == self.password_hash:
                # Incia o menu de administrador
                self.admin_menu()
                return
            elif user.name == name and user.password == sha256(password):
                print()
                print('Login realizado com sucesso!')
                # Incia o menu do usuário logado
                self.user_menu(user)
                return
        
        print('Usuário ou senha inválidos!')
    

    def register_menu(self):
        # Coleta os dados do usuário
        name = input("Insira seu nome de usuário: ")
        private = input("Essa conta será privada? (s/n): ").strip()[0].lower() == 's'
        password = input("Insira sua senha: ")
        if password == input('Confira sua senha: '):
            # Cria o usuário e o adiciona na lista de usuários do programa
            user = User(name, len(self.user_list), private, sha256(password))
            self.user_list.append(user)
            print("Usuário cadastrado com sucesso!")
        else:
            print('Senhas não conferem! Tente novamente.')
            self.register_menu()
    
    def admin_menu(self):
        while True:
            print(self.admin_options)
            option = input('Digite a opção desejada: ')
            if option == '1':
                # Incia o menu de deletar usuário
                self.delete_user()
            elif option == '2':
                # Incia o menu de deletar publicação
                self.delete_post()
            elif option == '3':
                # Incia o menu de listar usuários
                self.list_users()
            elif option == '4':
                # Encerra o menu de administrador
                break
            else:
                print('Opção inválida!')
    
    def delete_user(self):
        # Coleta e confirma o nome do usuário a ser deletado
        name = input('Insira o nome de usuário que queres deletar: ')
        if not name == input('Confira o nome de usuário: '):
            print('Nomes não conferem! Tente novamente.')
            return        
        confirm = input('Tem certeza que deseja deletar o usuário? (s/n): ').strip()[0].lower() != 's'
        if confirm: return
        # Busca e remove o usuário da lista de usuários do programa
        for user in self.user_list:
            if user.name == name:
                self.user_list.remove(user)
                print('Usuário deletado com sucesso!')
                return

    def delete_post(self):
        posts = self.get_post_list()
        # Coleta e confirma o id da publicação a ser deletada
        id = input('Insira o id da publicação que queres deletar: ')
        if not id == input('Confira o id da publicação: '):
            print('Ids não conferem! Tente novamente.')
            return
        confirm = input('Tem certeza que deseja deletar a publicação? (s/n): ').strip()[0].lower() != 's'
        if confirm: return
        # Busca e remove a publicação da lista de publicações do usuário
        for post in posts:
            if post.id == id:
                post.owner.posts.remove(post)
                print('Publicação deletada com sucesso!')
                return

    def list_users(self):
        for user in self.user_list:
            print(user.name)

    def user_menu(self, user: User):
        count = 0
        while True:
            print(self.user_options)
            option = input('Digite a opção desejada: ')
            if option == '1':
                # Incia o menu de criar publicação
                user.create_and_add_post(self.creation_time)
            elif option == '2':
                # Incia o menu de mostrar próxima página de publicações
                user.build_feed(self.get_post_list(), count)
                count += 1
            elif option == '3':
                # Incia o menu de acessar perfil
                user.profile_menu()
            elif option == '4':
                # Incia o menu de buscar perfil
                self.search_profile(user)
            elif option == '5':
                # Recebe a publicação a ser aberta e a exibe
                publi = input('Insira o título da publicação a ser aberta: ')
                for post in user.posts:
                    if post.title == publi:
                        post.post_menu(self, user)
                        break
                if not any(post.title == publi for post in user.posts):
                    print('Publicação não encontrada!')
            elif option == '6':
                # Coloca o contador a zero, de modo a mostrar as publicações mais recentes
                count = 0
            
            elif option == '0':
                # Encerra o menu do usuário
                break
            else:
                print('Opção inválida!')

    def search_profile(self, user: User):
        # Coleta o nome do usuário a ser buscado
        name = input('Insira o nome de usuário que queres buscar: ')
        # Busca o usuário na lista de usuários do programa
        for other_user in self.user_list:
            if other_user.name == name and other_user != user and not other_user.private:
                # Incia o menu de perfil do usuário buscado
                other_user.profile_menu()
                return
        print('Usuário não encontrado!')
    

    def comment_menu(self):
        pass
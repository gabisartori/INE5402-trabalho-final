from user import *
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
        for user in self.get_user_list():
            for post in user.get_posts():
                temp.append(post)
        
        temp.sort(key= lambda x: x.created_at, reverse=True)
        return temp

    def run(self):
        '''Cria um menu com as opções para login, cadastro e encerrar programa'''
        def delete_user(user):
            self.get_user_list().remove(user)
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
            # Opção secreta para testes
            elif option == '0':
                user = User('Gabriel', 'gabriel.sartorirangel@gmail.com', False, sha256('gabriel'), delete_user)
                self.get_user_list().append(user)
                user = User('Sofia', 'sofia.sartori@gmail.com', False, sha256('sofia'), delete_user)
                self.get_user_list().append(user)
                user = User('Gabriel Rocha', 'rocha@gmail.com', True, sha256('rocha'), delete_user)
                self.get_user_list().append(user)            
            else:
                print('Opção inválida!')
    
    def login_menu(self):
        '''Pede por um nome de usuário e uma senha e faz o login caso o usuário exista'''
        if len(self.get_user_list()) == 0:
            # Não há necessidade de acessar o perfil admin se a rede não tem usuários
            print('Não há usuários cadastrados.')
            print('Para cadastrar um usuário, digite "2" no menu principal.')
            return
        
        
        name = input('Insira o nome de usuário: ')
        password = input('Insira a senha: ')
        for user in self.get_user_list():
            if name == self.admin_name and sha256(password) == self.password_hash:
                # Incia o menu de administrador
                self.admin_menu()
                return
            elif user.get_name() == name and user.get_password() == sha256(password):
                print()
                print('Login realizado com sucesso!')
                # Incia o menu do usuário logado
                self.user_menu(user)
                return
        
        print('Usuário ou senha inválidos!')
    

    def register_menu(self):
        '''Pede as informações e cria um novo usuário, armazenando-o numa lista de usuários'''
        # Coleta os dados do usuário
        def delete_user(user):
            self.get_user_list().remove(user)
        name = input("Insira seu nome de usuário: ")
        email = input("Insira um email válido: ")
        if any([user.get_email() == email for user in self.get_user_list()]):
            print('Email já cadastrado! Tente novamente.')
            return
        private = input("Essa conta será privada? (s/n): ").strip()[0].lower() == 's'
        password = input("Insira sua senha: ")
        if password == input('Confira sua senha: '):
            # Cria o usuário e o adiciona na lista de usuários do programa
            user = User(name, email, private, sha256(password), delete_user)
            self.get_user_list().append(user)
            print("Usuário cadastrado com sucesso!")
        else:
            print('Senhas não conferem! Tente novamente.')
            self.register_menu()
    
    def admin_menu(self):
        '''Menu do usuário admin'''
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
        '''Pede o email do usuário a ser deletado e o remove da lista de usuários'''
        # Coleta e confirma o nome do usuário a ser deletado
        email = input('Insira o email de usuário que queres deletar: ')
        if not email == input('Confira o nome de usuário: '):
            print('Emails não conferem! Tente novamente.')
            return        
        confirm = input('Tem certeza que deseja deletar o usuário? (s/n): ').strip()[0].lower() != 's'
        if confirm: return
        # Busca e remove o usuário da lista de usuários do programa
        for user in self.get_user_list():
            if user.get_email() == email:
                self.get_user_list().remove(user)
                print('Usuário deletado com sucesso!')
                return

    def delete_post(self):
        '''Pede o título da publicação a ser deletada e a remove da lista de publicações de seu dono'''
        posts = self.get_post_list()
        # Coleta e confirma o id da publicação a ser deletada
        title = input('Insira o título da publicação que queres deletar: ')
        if not title == input('Confira o título da publicação: '):
            print('Títulos não conferem! Tente novamente.')
            return
        confirm = input('Tem certeza que deseja deletar a publicação? (s/n): ').strip()[0].lower() != 's'
        if confirm: return
        # Busca e remove a publicação da lista de publicações do usuário
        for post in posts:
            if post.get_title() == title:
                post.get_owner().get_posts().remove(post)
                print('Publicação deletada com sucesso!')
                return

    def list_users(self):
        '''Mostra o nome de cada usuário na tela'''
        for user in self.get_user_list():
            print('='*30)
            print(user.get_name() + ' : ' + user.get_email())

    def user_menu(self, user: User):
        '''Menu do usuário logado, mostrando opções de criação, visualização e navegação de posts'''
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
                user.own_profile_menu()
            elif option == '4':
                # Incia o menu de buscar perfil
                self.search_profile(user)
            elif option == '5':
                # Recebe a publicação a ser aberta e a exibe
                publi = input('Insira o título da publicação a ser aberta: ')
                for post in self.get_post_list():
                    if post.get_title() == publi and (not post.get_private() or post.get_owner() == user):
                        post.post_menu(user)
                        break
                if not any(post.get_title() == publi for post in user.get_posts()):
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
        '''Busca o perfil de um usuário existente na lista de usuários'''

        # Coleta o nome do usuário a ser buscado
        name = input('Insira o nome de usuário que queres buscar: ')
        # Busca o usuário na lista de usuários do programa
        for other_user in self.get_user_list():
            if other_user.get_name() == name and other_user != user and not other_user.get_private():
                # Incia o menu de perfil do usuário buscado
                other_user.profile_menu()
                return
        print('Usuário não encontrado!')

    def set_user_list(self, user_list):
        '''Define a lista de usuários do programa'''
        self.user_list = user_list
    
    def get_user_list(self):
        '''Retorna a lista de usuários do programa'''
        return self.user_list
    
    # Data de criação não deve mudar, então não vou criar o setter
    def get_creation_time(self):
        '''Retorna o tempo de criação do programa'''
        return self.creation_time
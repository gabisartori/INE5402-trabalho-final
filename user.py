from posts.textpost import TextPost
from posts.imagepost import ImagePost
import hashlib
import time

def sha256(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()


class User:

    profile_options = '''==============================
[1] Carregar mais publicações
[2] Sair
'''

    own_profile_options = '''==============================
[1] Carregar mais publicações
[2] Alterar informações de cadastro
[3] Sair
==============================
'''

    create_options = '''==============================
[1] Criar publicação de texto
[2] Criar publicação de imagem
'''

    change_info_options = '''==============================
[1] Excluir conta
[2] Mudar nome de usuário
[3] Mudar senha
'''

    def __init__(self, name, email, private, password_hash, delete_self):
        self.name = name
        self.email = email
        self.posts = []
        self.private = private
        self.password = password_hash
        self.delete_account = delete_self

    def allow_post(self, menu_creation_time):
        '''Retorna False se a conta tiver publicado mais de X vezes num Y intervalo de tempo'''
        if not self.posts: return True
        posts_by_minute = {}
        for post in self.posts:
            time_diff = post.created_at - menu_creation_time 
            time_diff_minutes = time_diff // 60
            if str(time_diff_minutes) in posts_by_minute.keys(): posts_by_minute[str(time_diff_minutes)] += 1
            else: posts_by_minute[str(time_diff_minutes)] = 1
        
        current_minute = str((time.time() - menu_creation_time) // 60)
        if current_minute not in posts_by_minute.keys():
            return True
        if posts_by_minute[str(current_minute)] > 5:
            return False
        
        return True

    def create_and_add_post(self, menu_creation_time):
        '''Pergunta o tipo de publicação a ser criada e cria a publicação'''
        # Checa se o usuário ainda pode publicar no intervalo de tempo
        if self.allow_post(menu_creation_time):
            print(self.create_options)
            option = input('Digite a opção desejada: ')
            # Cria uma publicação de texto
            if option == '1':
                post = TextPost(self, input('Insira o título da publicação: '), input('Insira o texto da publicação: '))
            # Cria uma publicação de imagem
            elif option == '2':
                titulo = input('Insira o título da publicação: ')
                # A publicação de imagem consiste em criar um link para algum arquivo da pasta ascii_arts, que deve conter uma figura em formato txt
                link = input('Insira o link da imagem: ')
                try:
                    open(f'ascii_arts/{link}.txt', 'r')
                    post = ImagePost(self, titulo, link)
                except FileNotFoundError:
                    print('Arquivo não encontrado!')
                    return
            else:
                print('Opção inválida!')
                return
            self.posts.insert(0, post)
        else: print('Você já publicou demais por hoje, volte amanhã.')
        
    def build_feed(self, all_posts, count):
        '''Mostra as publicações do usuário'''
        all_posts = [post for post in all_posts if not post.owner.private or post.owner is self]
        if count *5 > len(all_posts):
            print('Não há mais publicações.')
            return
        try:
            for post in all_posts[count*5:count*5+5]:
                post.show_post()
        except:
            for post in all_posts[count*5:]:
                post.show_post()
    
    def build_my_feed(self, count):
        '''Mostra as publicações visíveis ao usuário'''
        if count*5 > len(self.posts):
            print('Não há mais publicações.')
            return
        try:
            for post in self.posts[count*5:count*5+5]:
                post.show_post()
        except:
            for post in self.posts[count*5:]:
                post.show_post()
    
    def own_profile_menu(self):
        '''Menu de perfil do usuário, permitindo que o usuário veja as próprias publicações e altere suas informações de cadastro'''
        print(self.name)
        print('='*30)
        count = 0
        while True:
            print(self.own_profile_options)
            option = input('Digite a opção desejada: ')
            if option == '1':
                self.build_my_feed(count)
                count += 1
            elif option == '2':
                self.change_info_menu(self)
            elif option == '3':
                print('Saindo do perfil.')
                break
            else:
                print('Opção inválida!')

    def profile_menu(self):
        print(self.name)
        print('='*30)
        count = 0
        while True:
            print(self.profile_options)
            option = input('Digite a opção desejada: ')
            if option == '1':
                self.build_my_feed(count)
                count += 1
            elif option == '2':
                print('Saindo do perfil.')
                break
            else:
                print('Opção inválida!')


    def change_info_menu(self):
        '''Menu de alteração de informações de cadastro'''
        print(self.change_info_options)
        option = input('Digite a opção desejada: ')
        if option == '1':
            self.delete_account(self)
        elif option == '2':
            self.change_name()
        elif option == '3':
            self.change_password()
        else:
            print('Opção inválida!')
    
    def change_name(self):
        '''Pergunta o novo nome do usuário e altera o nome'''
        new_name = input('Insira o novo nome: ')
        confirm = input('Confirma a alteração? (S/N) ').strip()[0].lower() == 's'
        if confirm: self.name = new_name
        else: print('Mudança cancelada.')

    def change_password(self):
        '''Altera a senha do usuário pedindo a senha nova e uma confirmação'''
        new_password = input('Insira o novo nome: ')
        confirm_password = input('Confirme a nova senha: ') == new_password
        confirm = input('Confirma a alteração? (S/N) ').strip()[0].lower() == 's'
        if confirm and confirm_password: self.password = sha256(new_password)
        else: print('Mudança cancelada.')

    def set_name(self, name):
        '''Define o nome do usuário'''
        self.name = name
        self.name = name

    def set_email(self, email):
        '''Define o email do usuário'''
        self.email = email
    
    def set_private(self, private):
        '''Define se o usuário é privado ou não'''
        self.private = private
    
    def set_password(self, password):
        '''Define a senha do usuário'''
        self.password = password
    
    def get_name(self):
        '''Retorna o nome do usuário'''
        return self.name
    
    def get_email(self):
        '''Retorna o email do usuário'''
        return self.email
    
    def get_private(self):
        '''Retorna se o usuário é privado ou não'''
        return self.private
    
    def get_password(self):
        '''Retorna a senha do usuário'''
        return self.password

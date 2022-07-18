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

    def __init__(self, name, email, private, password_hash):
        self.name = name
        self.email = email
        self.posts = []
        self.private = private
        self.password = password_hash

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


    def change_info_menu(self, user):
        '''Menu de alteração de informações de cadastro'''
        print(self.change_info_options)
        option = input('Digite a opção desejada: ')
        if option == '1':
            self.delete_account()
        elif option == '2':
            self.change_name()
        elif option == '3':
            self.change_password()
        else:
            print('Opção inválida!')
    

    def delete_account(self):
        pass

    def change_name(self):
        pass

    def change_password(self):
        pass
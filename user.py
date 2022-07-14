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
==============================
'''

    create_options = '''==============================
[1] Criar publicação de texto
[2] Criar publicação de imagem
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
        if self.allow_post(menu_creation_time):
            print(self.create_options)
            option = input('Digite a opção desejada: ')
            if option == '1':
                post = TextPost(self, input('Insira o título da publicação: '), input('Insira o texto da publicação: '))
            elif option == '2':
                post = ImagePost(self, input('Insira o título da publicação: '), input('Insira o link da imagem: '))
            else:
                print('Opção inválida!')
                return
            self.posts.insert(0, post)
        else: print('Você já publicou demais por hoje, volte amanhã.')
        
    def build_feed(self, all_posts, count):
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
        if count*5 > len(self.posts):
            print('Não há mais publicações.')
            return
        try:
            for post in self.posts[count*5:count*5+5]:
                post.show_post()
        except:
            for post in self.posts[count*5:]:
                post.show_post()
    
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
    
    def comment(self, post, comment):
        post.add_reply(TextPost(self, '', comment))

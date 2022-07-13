from posts.textpost import TextPost
from posts.imagepost import ImagePost
import hashlib

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
    def __init__(self, name, id, private, password_hash) -> None:
        self.name = name
        self.id = id,
        self.posts = []
        self.private = private
        self.password = password_hash

    def create_and_add_post(self) -> None:
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
        
    def build_feed(self, all_posts, count) -> None:
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
    
    
    def comment(self, post, comment):
        post.add_reply(TextPost(self, '', comment))
    
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

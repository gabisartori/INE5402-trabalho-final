from posts.textpost import TextPost
import hashlib

def sha256(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()


class User:

    profile_options = '''[1] Carregar mais publicações
[2] Sair'''
    def __init__(self, name, id, private, password_hash) -> None:
        self.name = name
        self.id = id,
        self.posts = []
        self.private = private
        self.password = password_hash

    def add_post(self, post) -> None:
        self.posts.append(post)
    
    def build_feed(self, all_posts) -> None:
        for post in all_posts:
            if not post.owner.private: print(post.content) 
    
    def build_my_feed(self, count):
        if count*5 > len(self.posts):
            print('Não há mais publicações.')
            return
        try:
            for post in self.posts[count*5:count*5+5]:
                print(post.content)
        except:
            for post in self.posts[count*5:]:
                print(post.content)
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
            
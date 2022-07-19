import time

class Post:
    
    post_options = '''==============================
[0] Sair
[1] Curtir
[2] Comentar
[3] Mostrar respostas
'''
    
    def __init__(self, owner):
        self.likes = 0
        self.owner = owner
        self.replies = []
        self.liked_by = []
        self.private = self.owner.private
        self.created_at = time.time()

    def add_like(self, user):
        '''Incrementa o número de curtidas do post e adiciona o usuário que curtiu na lista de quem curtiu o post'''
        # Checa se o usuário já curtiu a publicação
        if user not in self.liked_by:
            self.set_likes(self.get_like() + 1)
            self.get_liked_by().append(user)
            print('Curtiu!')
        else:
            print('Você já curtiu esta publicação!')

    def add_reply(self, reply):
        '''Adiciona uma resposta à lista de respostas do post'''
        self.get_replies().insert(0, reply)
    
    def post_menu(self, viewer):
        '''Menu de opções para o usuário interagir com a publicação'''
        self.show_post()
        while True:
            print(self.post_options)
            option = input('Digite a opção desejada: ')
            if option == '1':
                # Adiciona uma curtida à publicação
                self.add_like(viewer)
            elif option == '2':
                # Incia o menu de comentar
                self.comment_menu(viewer)
            elif option == '3':
                self.show_post_replies()
            elif option == '0':
                # Encerra o menu de publicação
                break

    def show_post_replies(self):
        '''Mostra as respostas da publicação'''
        for reply in self.get_replies():
            reply.show_post()

    def set_likes(self, like):
        '''Define o número de curtidas da publicação'''
        self.likes = like
    
    def set_owner(self, owner):
        '''Define o dono da publicação'''
        self.owner = owner
    
    def set_replies(self, replies):
        '''Define a lista de respostas da publicação'''
        self.replies = replies
    
    def set_likesd_by(self, liked_by):
        '''Define a lista de quem curtiu a publicação'''
        self.liked_by = liked_by
    
    def set_private(self, private):
        '''Define se a publicação é privada'''
        self.private = private
    
    def set_created_at(self, created_at):
        '''Define a data de criação da publicação'''
        self.created_at = created_at
    
    def get_like(self):
        '''Retorna o número de curtidas da publicação'''
        return self.likes
    
    def get_owner(self):
        '''Retorna o dono da publicação'''
        return self.owner
    
    def get_replies(self):
        '''Retorna a lista de respostas da publicação'''
        return self.replies
    
    def get_liked_by(self):
        '''Retorna a lista de quem curtiu a publicação'''
        return self.liked_by
    
    def get_private(self):
        '''Retorna se a publicação é privada'''
        return self.private
    
    def get_created_at(self):
        '''Retorna a data de criação da publicação'''
        return self.created_at
    
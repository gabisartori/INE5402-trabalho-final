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
        if user not in self.liked_by:
            self.likes += 1
            self.liked_by.append(user)
            print('Curtiu!')
        else:
            print('Você já curtiu esta publicação!')

    def add_reply(self, reply):
        self.replies.insert(0, reply)
    
    def post_menu(self, viewer):
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
        for reply in self.replies:
            reply.show_post()

import time

class Post:
    
    post_options = '''==============================
[1] Curtir
[2] Comentar
[3] Sair
'''
    
    def __init__(self, owner):
        self.likes = 0
        self.owner = owner
        self.replies = []
        self.liked_by = []
        self.private = self.owner.private
        self.created_at = time.time()

    def add_like(self, user_id):
        self.likes += 1
        self.liked_by.append(user_id)

    def add_reply(self, reply):
        self.replies.append(reply)
    
    def post_menu(self, menu, viewer):
        self.show_post()
        while True:
            print(self.post_options)
            option = input('Digite a opção desejada: ')
            if option == '1':
                # Adiciona uma curtida à publicação
                self.add_like(viewer.id)
                print('Curtida adicionada com sucesso!')
            elif option == '2':
                # Incia o menu de comentar
                self.comment_menu()
            elif option == '3':
                # Encerra o menu de publicação
                break

    def comment_menu(self):
        pass
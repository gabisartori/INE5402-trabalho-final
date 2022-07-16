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
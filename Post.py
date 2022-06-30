class Post:
    def __init__(self, owner) -> None:
        self.likes = 0
        self.owner = owner
        self.replies = []
    
    def like(self) -> None:
        self.likes += 1

    def add_reply(self, reply) -> None:
        self.replies.append(reply)
    

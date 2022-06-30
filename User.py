class User:
    def __init__(self, name, id, private) -> None:
        self.name = name
        self.id = id,
        self.posts = []
        self.private = private

    def add_post(self, post) -> None:
        self.posts.append(post)
    
    def build_feed(self, all_posts) -> None:
        for post in all_posts:
            pass
    
    def build_my_feed(self):
        for post in self.posts:
            print(post)
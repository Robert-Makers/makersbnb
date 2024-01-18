class Listing:
    def __init__(self, id, title, description, price, host_user_id):
        self.id = id
        self.title = title
        self.description = description
        self.price = price
        self.host_user_id = host_user_id

    def __repr__(self):
        return f"Listing({self.id}, '{self.title}', '{self.description}', {self.price}, {self.host_user_id})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
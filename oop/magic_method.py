

# Magic method = Dunder methods (Double underscore) __init__, __str__,__eq__,
        # They are automatically called by manny of pythons builtin operation 
        # They allow developers to define or customize the behaviour of objects

class Book :

    def __init__(self,title, author,pg_num):
        self.title = title
        self.author = author
        self.pg_num = pg_num



    def __str__(self):
        return f"{self.title} is written by : {self.author}"
    
    def __eq__(self, other):
        return self.pg_num == other.pg_num and self.pg_num == other.pg_num
             

# yestai we can check greater and lessthan also 
    def __lt__(self,other):
        return self.pg_num < other.pg_num

book1 = Book(title="Physcology of money", author= "MOrgan Housel",pg_num= 300)
book2 = Book(title="The hobbit", author= "j.r tolkin",pg_num= 340)
book3 = Book(title="Gamne of throne", author= "s.r martin",pg_num= 500)


print(f"{book1} \n {book2} \n {book3}")
print(book1 == book2)
print(book1< book2)
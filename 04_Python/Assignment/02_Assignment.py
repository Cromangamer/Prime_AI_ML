class Book :
    def __init__(self, title, author, list):
        self.title = title
        self.author = author
        self.list = list

    def new_review(self, new_review):
        self.list.append(new_review)
        print(f"new review added!")

    def count(self):
        print(f"total reviews {len(self.list)}")

    def show(self):
        print("+_+_+_+_+_+_+_+_BOOK+_+_+_+_+_+_+_+_")
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")
        print("reviews: ", end="\n")
        for review in self.list:
            print(review)

book1 = Book("CromanBraine" , "Dhruv Pankhaniya", ["nice book","great book i ever sicne!"])

book1.count()
book1.new_review("Amazing")
book1.show()
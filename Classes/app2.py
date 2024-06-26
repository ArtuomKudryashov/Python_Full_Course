class Comment:
    def __init__(self,text):
        self.text = text
        self.votes_qty = 0

    def upvote(self):
        self.votes_qty+=1

    def upvoteNum(self,qty):
        self.votes_qty+=qty


first_comment = Comment("First comment")
print(first_comment.votes_qty)
print(first_comment.text)
first_comment.upvote()
print(first_comment.votes_qty)
print(first_comment.__dict__)

my_comment = Comment("My_comment")
print(my_comment)
print(type(my_comment))
print(my_comment.__dict__)
print(dir(my_comment))
first_comment.upvoteNum(5)
print(first_comment.votes_qty)

first_comment.upvote()
print(first_comment.votes_qty)
print(first_comment.votes_qty)
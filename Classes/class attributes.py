class Comment:
    total_comments = 0

    def __init__(self,text):
        self.text = text
        self.votes_qty = 0
        Comment.total_comments+=1

first_comment = Comment("First comment")
print(Comment.total_comments)

second_comment= Comment("Second comment")
print(Comment.total_comments)

print(first_comment.total_comments)

print("<<<<<<<<<<<SECOND>>>>>>>>>>>>>>>")

# first_comment.total_comments=10

print(Comment.total_comments)
print(first_comment.total_comments)
print("<<<<<<<<<<Total>>>>>>>>>")
print(Comment.__dict__)
print(first_comment.__dict__)

print("<<<<<<<<<<Total-2>>>>>>>>>")
Comment.total_comments=100

print(Comment.total_comments)
print(first_comment.total_comments)


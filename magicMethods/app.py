class Comment:
    def __init__(self,text):
        self.text = text
        self.votes_qty = 0

    def upvote(self):
        self.votes_qty+=1

    def __add__(self, other):
        # return [f"{self.text}{other.text}", self.votes_qty + other.votes_qty]
        # return [f"{self.text}{other.text}", self.votes_qty + other.votes_qty]
        return {"test": f"{self.text} {other.text}",
                "total_votes_qty":self.votes_qty + other.votes_qty
        }

    def __eq__(self, other):
        if isinstance(other, Comment):
            return self.text == other.text and self.votes_qty == other.votes_qty
        return False


first_comment = Comment("First comment")
first_comment.upvote()
first_comment.upvote()
second_comment = Comment("Second comment")
second_comment.upvote()
second_comment.upvote()

print(first_comment + second_comment)
print(first_comment==second_comment)

another_first_comment = Comment("First comment")
another_first_comment.upvote()
another_first_comment.upvote()

print(first_comment==second_comment)
print(first_comment==another_first_comment)

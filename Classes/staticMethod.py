class Comment:
    def __init__(self, text):
        self.text = text


    def __str__(self):
        return self.text



    @staticmethod
    def merge_comments(first, second):
        return f"{first}{second}"

my_comment = Comment("My comment")
print(my_comment)
print(my_comment.text)


m_1 = Comment.merge_comments("Thanks!", "Excellent.")
print(m_1)

m_2 = my_comment.merge_comments("Great", "Ok")
print(m_2)

class Car:
    @staticmethod
    def info ( brand, model, color ):
        return f"This car is a {color} {brand}, and its model  is {model}"


car = Car()

my_car = car.info("Toyota", "Land Cruiser","Red")

print(my_car)

my_car2= Car.info("VW","Touareg", "Coffee")
print(my_car2)
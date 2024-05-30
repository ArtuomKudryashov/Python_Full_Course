user_data = ['Artuom',23]
user_data1 = ['Artuom',23,443]
def user_info(name, comments_qty):
    if not comments_qty:
        return f"{name} has no comment"

    return  f"{name} has {comments_qty} comments"

print(user_info(*user_data))
print(user_info(user_data[0],user_data[1]))

def user_info1(name, comments_qty,id):
    if not comments_qty:
        return f"{name} has no comment"

    return  f"{name} has {comments_qty} comments and {id} id"

print(user_info1(*user_data1))
print("<<<<<<<<<<<2>>>>>>>>>>>")
name,comments,id = user_data1
print(user_info1(name,comments,id))
print(user_info1(*user_data))

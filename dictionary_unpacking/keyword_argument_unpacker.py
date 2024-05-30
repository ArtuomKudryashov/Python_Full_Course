user_profile = {
    'name':'Artuom',
    'comments_qty':23,
}
def user_info(name, comments_qty = 0):
    if not comments_qty:
        return f"{name} has no comment"

    return  f"{name} has {comments_qty} comments"
print("<<<<<<<<<<1>>>>>>>>")
print(user_info(user_profile))

print("<<<<<<<<<<1.1>>>>>>>>")
print(user_info(**user_profile))

print("<<<<<<<<<<2>>>>>>>>")
print(user_info(user_profile['name'],user_profile['comments_qty']))

print("<<<<<<<<<<3>>>>>>>>")
print(user_info(name=user_profile['name'],comments_qty = user_profile['comments_qty']))

print("<<<<<<<<<<4>>>>>>>>")
name, coments_qty = user_profile
print(name)
print(coments_qty)
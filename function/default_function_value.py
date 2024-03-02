def mult_by_factor(value, multiplier =1):
    return value * multiplier


print(mult_by_factor(10,2))
print(mult_by_factor(56))


from datetime import date
def get_weekday():
    return date.today().strftime('%A')


def create_new_post(post, weekday = get_weekday()):
    post_copy = post.copy()
    post_copy['created_on_weekday'] = weekday
    print(post_copy)
    return  post_copy

initial_post = {
    'id': 243,
    'author': 'Artuom'
}

post_with_weekday = create_new_post(initial_post, "Monday")
print (post_with_weekday)
print()
print(initial_post)
print()


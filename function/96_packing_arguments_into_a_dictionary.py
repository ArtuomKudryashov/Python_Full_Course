def get_posts_info(**person):
    print(person)
    print(type(person))
    info = (
        f"{person['name']} wrote "
        f"{person['posts_qty']} posts"
    )
    return info


info = get_posts_info(name='Artuom', posts_qty=25)
print(info)


def get_post_info2(**person):
    info = f"{person['name']} wrote {person['posts_qty']} posts"
    return info


info = get_post_info2(name='Artuom', posts_qty=25)
print(info)




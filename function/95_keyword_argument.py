def get_post_info(name, posts_qty):
    info = f"{name} wrote {posts_qty} posts"
    return info


info = get_post_info(name="Artuom", posts_qty=25)
print(info)

info2 = get_post_info("Artuom", posts_qty=30)
print(info2)

info3 = get_post_info("Artuom", 30 )
print(info3)
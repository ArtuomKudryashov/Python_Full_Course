def image_info (img):
    if ('image_id' not in img) or('image_title' not in img):
        raise TypeError ("Keys image_id and image_title must be present")
    return f"Image {img['image_title']} has id {img['image_id']}"


a = image_info({'image_title': 'My cat', 'image_id':123})
print( a)

try:
    b = image_info({'image_title': 'My cat'})
except TypeError as e:
    print(e)

# c = image_info({ 'image_id':123})
# print(c)

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<SECOND TYPE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
def image_info(img):
    if 'image_id' not in img:
        raise TypeError("Key 'image_id' must be present")
    if 'image_title' not in img:
        raise TypeError("Key 'image_title' must be present")
    return f"Image {img['image_title']} has id {img['image_id']}"

# Вызов функции с корректными данными
a = image_info({'image_title': 'My cat', 'image_id': 123})
print(a)

# Вызов функции с отсутствующим ключом 'image_id'
try:
    b = image_info({'image_title': 'My cat'})
except TypeError as e:
    if "image_id" in str(e):
        print("Missing image_id:", e)
    else:
        raise

print("<<<<Second>>>>")

# Вызов функции с отсутствующим ключом 'image_title'
try:
    c = image_info({'image_id': 123})
except TypeError as e:
    if "image_title" in str(e):
        print("Missing image_title:", e)
    else:
        raise

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Third TYPE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
class MissingImageIDError(TypeError):
    pass

class MissingImageTitleError(TypeError):
    pass

def image_info(img):
    if 'image_id' not in img:
        raise MissingImageIDError("Key 'image_id' must be present")
    if 'image_title' not in img:
        raise MissingImageTitleError("Key 'image_title' must be present")
    return f"Image {img['image_title']} has id {img['image_id']}"

# Вызов функции с корректными данными
a = image_info({'image_title': 'My cat', 'image_id': 123})
print(a)

# Вызов функции с отсутствующим ключом 'image_id'
try:
    b = image_info({'image_title': 'My cat'})
except MissingImageIDError as e:
    print(e)
except MissingImageTitleError as e:
    print(e)

# Вызов функции с отсутствующим ключом 'image_title'
try:
    c = image_info({'image_id': 123})
except MissingImageIDError as e:
    print(e)
except MissingImageTitleError as e:
    print(e)

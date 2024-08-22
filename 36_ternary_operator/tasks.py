my_img =('1920','1980')
print(f"{my_img[0]}x{my_img[1]}")if len(my_img)==2 else print("Incorrect image formatting")

my_img4k = ( '3840' , '2160')
info=f"{my_img4k[0]}x{my_img4k[1]}"if len(my_img4k) == 2 else "Incorrect image formatting"
print(info)

my_img4k = ['3840','2160']
if len(my_img4k) == 2:
    print(f"{my_img4k[0]}x{my_img4k[1]}")
else:
    print("Incorrect image formatting")



string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+{}[]|:;<>,.?/авыаыв"

info_str = len(string)
message = f" String {string} is long " if  info_str >79 else "String is short"
print(message)

try:
    # print(10 / 0)
    print(10 / 5)

except ZeroDivisionError as e:
    print(type(e))
    print(dir(e))
    print(e)
    print("<<<<<<<<<<>>>>>>>>>>>")
    print(e.__str__())

except TypeError as e:
    print(type(e))
    print(e)
else:
    print("There was no error")
finally:
    print("Continue...")
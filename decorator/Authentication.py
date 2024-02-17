def is_user_authenticated():
    return  False


def check_user_auth(fn):
    def wrapper(*args, **kwargs):
        if is_user_authenticated():
            print ("User is authenticated!")
            return fn(*args, **kwargs)
        else:
            raise Exception("User is NOT authenticated")

    return wrapper

@check_user_auth
def do_sesitive_job():
    print("Result  of some sensitive tasks")

try:
    do_sesitive_job()
except Exception as e:
    print(e)
user,user_password = "byf","123"
def auth(auth_type):
    print("auth_type:",auth_type)
    def out_wrapper(func):
        def wrapper(*args,**kwargs):
            if auth_type=="local":
                name = input("请输入账号").strip()
                password = input("请输入密码").strip()
                if name == user and password == user_password:
                    print("\033[32;1m欢迎进入\033[0m")
                    re = func()
                    print(" have return")
                    return re
                else:
                    exit("\033[31;1m账号或密码错误\033[0m")
            elif auth_type=="ldap":
                print("do nothing")
        return wrapper
    return out_wrapper

def index():
    print("welcome to index page")
@auth(auth_type="local")
def home():
    print("welcome to home page")
    return "from home"
@auth(auth_type="ldap")
def bbs():
    print("welcome to bbs page")

index()
#home()
bbs("s")
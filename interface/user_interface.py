from db import db_handler


def register_interface(user, pwd):
    if db_handler.select(user):
        return False, "用户已存在"

    user_dic = {
        "name": user,
        "password": pwd,
        "balance": 15000,
        "flow": [],
        "shopping_cart": {}
    }

    db_handler.save(user_dic)

    return True, "用户：%s 注册成功" % user


def login_interface(user, pwd):
    user_dic = db_handler.select(user)
    if not user_dic:
        return False, "用户不存在，请重新登录"

    if pwd == user_dic["password"]:
        return True, "登录成功"
    else:
        return False, "密码错误"


def check_balance_interface(user):
    user_dic = db_handler.select(user)
    return user_dic["balance"]

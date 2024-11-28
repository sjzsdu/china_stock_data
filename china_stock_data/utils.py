def friendly_number(number, decimal_places=2):
    """
    将一个数值转换为比较友好的格式，用亿和万为单位，并支持指定小数点位数。

    :param number: 需要转换的数值
    :param decimal_places: 小数点位数，默认为2
    :return: 转换后的字符串
    """
    if number is None:
        return "无效的数字"

    try:
        num = float(number)
    except (ValueError, TypeError):
        return "无效的数字"

    if num >= 1e8:  # 大于等于 1 亿
        return f"{num / 1e8:.{decimal_places}f} 亿"
    elif num >= 1e4:  # 大于等于 1 万
        return f"{num / 1e4:.{decimal_places}f} 万"
    else:
        return f"{num:.{decimal_places}f}"

def get_first_line(text):
    # 使用 splitlines() 分割字符串，然后使用列表解析去除每行首尾空格并过滤掉空行
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    # 返回第一行，如果没有有效行则返回空字符串
    return lines[0] if lines else ''


import hashlib
def generate_stable_string(input_string):
    # 使用SHA-256哈希函数
    hash_object = hashlib.sha256(input_string.encode())
    stable_string = hash_object.hexdigest()[:8]
    return stable_string

import datetime

def is_within_days(date_str, days=30):
    """
    判断给定的日期字符串是否在当前日期的前后指定天数之内。

    :param date_str: 日期字符串，格式为 'YYYY-MM-DD'
    :param days: 指定的天数，默认为30
    :return: 如果在指定天数之内返回True, 否则返回False
    """

    try:
        # 将日期字符串转换为datetime.date对象
        target_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        print("日期格式错误，请使用 'YYYY-MM-DD' 格式")
        return False

    if days < 0:
        return False

    # 获取当前日期
    today = datetime.date.today()

    # 计算两个日期之间的天数差
    date_diff = (target_date - today).days

    # 判断是否在指定天数之内
    return abs(date_diff) <= days
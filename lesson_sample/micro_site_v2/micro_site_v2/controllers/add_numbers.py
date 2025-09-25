# controllers/add_numbers.py

from utils import render_template, parse_post
from app_logic import set_first_value, set_second_value, get_addition # 現在のimportのまま修正


def add_numbers(environ):
    method = environ["REQUEST_METHOD"]
    
    if method == "POST":
        data = parse_post(environ)
        first_value = data.get("first_value", [0])[0]
        second_value = data.get("second_value", [0])[0]

        # 致命的なエラーの解消: POST時のみ値をセット
        set_first_value(first_value)
        set_second_value(second_value)
        
    addition = get_addition()

    return render_template("boundaries/add_numbers_data.html", addition=addition)
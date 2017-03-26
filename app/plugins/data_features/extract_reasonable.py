from flask import flash

def test_one():
    return flash("The first one works!", "success")

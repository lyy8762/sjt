"""
 Created by 七月 on 2018/1/26.
 微信公众号：林间有风
"""
from app.models.gift import Gift
from app.view_models.book import BookViewModel
from . import web
from flask import render_template
from flask_login import login_required, current_user


__author__ = '七月'


@web.route('/')
def index():
    recent_gifts = Gift.recent()
    books = [BookViewModel(gift.book) for gift in recent_gifts]
    return render_template('index.html', recent=books)


@web.route('/personal')
@login_required
def personal_center():
    return render_template('personal.html', user=current_user.summary)

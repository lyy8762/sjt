"""
 Created by 七月 on 2018/1/26.
 微信公众号：林间有风
"""

from app import create_app

__author__ = '七月'

app = create_app()

if __name__ == '__main__':
    app.run(host=app.config['HOST'], debug=app.config['DEBUG'], port=81, threaded=True)
    #单进程、单线程
    # processes = 1
    # 10 个请求

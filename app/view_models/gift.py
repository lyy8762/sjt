"""
 Created by 七月 on 2018/1/26.
 微信公众号：林间有风
"""
from .book import BookViewModel
from collections import namedtuple

# MyGift = namedtuple('MyGift', ['id', 'book', 'wishes_count'])


class MyGifts:
    def __init__(self, gifts_of_mine, wish_count_list):
        self.gifts = []

        self.__gifts_of_mine = gifts_of_mine
        self.__wish_count_list = wish_count_list

        self.gifts = self.__parse()

    def __parse(self):
        temp_gifts = []
        for gift in self.__gifts_of_mine:
            my_gift = self.__matching(gift)
            temp_gifts.append(my_gift)
        return temp_gifts

    def __matching(self, gift):
        count = 0
        for wish_count in self.__wish_count_list:
            if gift.isbn == wish_count['isbn']:
                count = wish_count['count']
        r = {
            'wishes_count': count,
            'book': BookViewModel(gift.book),
            'id': gift.id
        }
        return r

























# class MyGifts:
#     def __init__(self, gifts, wish_count_list):
#         self.gifts = []
#         self.__gifts = gifts
#         self.__wish_count_list = wish_count_list
#
#         self.gifts = self.__parse()
#
#     def __parse(self):
#         my_gifts = []
#         for gift in self.__gifts:
#             r = self.__matching(gift)
#             my_gifts.append(r)
#         return my_gifts
#
#     def __matching(self, gift):
#         count = 0
#         for wish_count in self.__wish_count_list:
#             if gift.isbn == wish_count.isbn:
#                 count = wish_count.count
#         r = {
#             'wishes_count': count,
#             'book': BookViewModel(gift.book),
#             'id': gift.id
#         }
#         return r
#
#     def __parse_old(self, gifts, wishes_count):
#         my_gifts = []
#         for gift in gifts:
#             count = 0
#             for wish_count in wishes_count:
#                 if gift.isbn == wish_count[1]:
#                     count = wish_count[0]
#             else:
#                 r = {
#                     'wishes_count': count,
#                     'book': BookViewModel(gift.book.first),
#                     'id': gift.id
#                 }
#                 my_gifts.append(r)
#         self.my_gifts = my_gifts

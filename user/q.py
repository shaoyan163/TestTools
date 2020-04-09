# encoding: utf-8

"""
@author: shaoyanyan
@file: q.py
@time: 2020/4/9 23:35
@ide: pycharm

"""


class Hotel(object):
    """房间基本信息"""

    def __init__(self):
        # 房间初始化
        # self.room_no=room_no
        self.room_status = 0
        # 房间信息
        self.room_dict = {}
        # 房间列表
        self.room_info = []



    def add_room(self, room_no):
        self.room_no = room_no
        # 新建房间
        self.room_dict = {}
        if self.room_no in self.room_dict:
            return
        else:
            self.room_dict["roomNo"] = self.room_no
            self.room_dict["roomSta"] = self.room_status
            self.room_info.append(self.room_dict)
            print("房间[%s]新增成功" % room_no)


if __name__ == "__main__":
    hotel_info1 = Hotel()
    hotel_info1.add_room(501)
    print(hotel_info1.room_info)
    hotel_info1.add_room(502)
    print(hotel_info1.room_info)
    hotel_info1.add_room(503)
    print(hotel_info1.room_info)


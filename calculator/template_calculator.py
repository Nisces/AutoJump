import math

import cv2

from .calculator import Calculator


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


# 使用模板匹配的距离计算器
def get_dst_loc(img):
    return Point(0, 0)


class TemplateCalculator(Calculator):
    TEMPLATE_IMAGE = 'chess.png'

    def get_distance(self, img: cv2.Mat) -> float:
        chess_point = self.get_chess_loc(img)

        # draw chess point on the image
        cv2.rectangle(img, (int(chess_point.x), int(chess_point.y)),
                      (int(chess_point.x) + 5, int(chess_point.y) + 5),
                      (255, 0, 0), cv2.FILLED)
        print('chess_point', chess_point)
        dst_point = get_dst_loc(img)
        return chess_point.distance_to(dst_point)

    def get_chess_loc(self, img):
        templ = cv2.imread(self.TEMPLATE_IMAGE)
        res = cv2.matchTemplate(img, templ, cv2.TM_CCOEFF_NORMED)
        _, _, _, max_loc = cv2.minMaxLoc(res)
        return Point(max_loc[0] + templ.shape[1] / 2, max_loc[1] + templ.shape[0])

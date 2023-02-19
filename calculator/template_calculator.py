import math

import cv2
import numpy as np

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
class TemplateCalculator(Calculator):
    TEMPLATE_IMAGE = 'chess.png'

    def __init__(self):
        self.chess_loc = (0, 0)
        self.chess_size = (0, 0)

    def get_distance(self, img: cv2.Mat) -> float:
        # draw chess point on the image
        chess_point = self.get_chess_loc(img)
        print('chess_point  = ', chess_point)
        cv2.circle(img, (int(chess_point.x), int(chess_point.y)), 2, (0, 255, 0), -1)

        # get destination location and draw
        dst_center = self.get_dst_loc(img)
        print('center  = ', dst_center)
        cv2.circle(img, (int(dst_center.x), int(dst_center.y)), 5, (255, 0, 0), -1)

        return round(chess_point.distance_to(dst_center))

    def get_chess_loc(self, img) -> Point:
        templ = cv2.imread(self.TEMPLATE_IMAGE)
        self.chess_size = templ.shape[:2]  # [0] is height while [1] is width
        print('templ.shape = ', templ.shape)
        print('img.shape = ', img.shape)
        res = cv2.matchTemplate(img, templ, cv2.TM_CCOEFF_NORMED)
        _, _, _, max_loc = cv2.minMaxLoc(res)
        self.chess_loc = max_loc
        return Point(max_loc[0] + self.chess_size[1] / 2, max_loc[1] + self.chess_size[0])

    def get_dst_loc(self, img) -> Point:
        edge = cv2.Canny(img, 2, 10)
        for y in range(self.chess_loc[1], self.chess_loc[1] + self.chess_size[0]):
            for x in range(self.chess_loc[0], self.chess_loc[0] + self.chess_size[1]):
                edge[y][x] = 0
        # edge[self.chess_loc[1]:self.chess_loc[1] + self.chess_size[0]][
        # self.chess_loc[0]:self.chess_loc[0] + self.chess_size[1]] = 0
        crop_height = int(edge.shape[0] / 4)
        edge = edge[crop_height:int(edge.shape[0] / 2)]
        cv2.imshow('edge', edge)

        top_y = np.min(np.nonzero(np.max(edge, axis=1)))
        right_x = np.max(np.nonzero(np.max(edge, axis=0)))
        top_x = np.min(np.nonzero(edge[top_y]))
        right_y = np.min(np.nonzero(edge[:, right_x]))
        top = Point(top_x, top_y)
        right = Point(right_x, right_y)
        center = Point(top_x, right_y + crop_height)
        return center

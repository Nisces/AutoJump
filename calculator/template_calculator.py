import cv2

from .calculator import Calculator


# 使用模板匹配的距离计算器
class TemplateCalculator(Calculator):
    TEMPLATE_IMAGE = 'chess.png'

    def get_distance(self, img: cv2.Mat) -> float:
        templ = cv2.imread(self.TEMPLATE_IMAGE)
        cv2.imshow("template", templ)
        cv2.waitKey(0)
        return 100

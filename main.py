import cv2

from calculator.template_calculator import TemplateCalculator
from toucher.adb_toucher import ADBToucher
from watcher.adb_watcher import ADBWatcher


def main():
    while True:
        watcher = ADBWatcher()
        toucher = ADBToucher()
        calculator = TemplateCalculator()

        img = watcher.get_image()
        distance = calculator.get_distance(img)
        img_resize = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
        cv2.imshow('ready?', img_resize)
        print('next destination distance = ', distance)

        toucher.touch(distance)
        if cv2.waitKey(2500) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


if __name__ == '__main__':
    main()

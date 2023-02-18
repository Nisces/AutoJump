import cv2

from watcher.adb_watcher import ADBWatcher


def main():
    watcher = ADBWatcher()
    img = watcher.get_image()
    print(img.shape)
    cv2.imshow('screen', img)
    cv2.waitKey(0)
    pass


if __name__ == '__main__':
    main()

from toucher.adb_toucher import ADBToucher


def main():
    # watcher = ADBWatcher()
    # img = watcher.get_image()
    # watcher.get_object(img)
    # print(img.shape)
    # cv2.imshow('screen', img)
    # cv2.waitKey(0)
    toucher = ADBToucher()
    toucher.touch(100)


if __name__ == '__main__':
    main()

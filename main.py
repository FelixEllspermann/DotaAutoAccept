from PIL import ImageGrab
import time
import os


def capture_and_delete_screenshot(interval=5):
    while True:

        filename = f'screenshot_{time.strftime("%Y%m%d-%H%M%S")}.png'

        screenshot = ImageGrab.grab()
        screenshot.save(filename)
        print(f'Screenshot saved as {filename}')

        time.sleep(interval)

        os.remove(filename)
        print(f'Screenshot {filename} deleted')



if __name__ == '__main__':
    capture_and_delete_screenshot(interval=5)
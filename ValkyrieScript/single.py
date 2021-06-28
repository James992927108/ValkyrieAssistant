import pyautogui
import time
import threading
import signal
import sys
class thread_sample(threading.Thread):
    def __init__(self, picture):
        threading.Thread.__init__(self)
        self.picture = picture
        self.kill_received = False

    def run(self):
        while not self.kill_received:
            print("{} is active".format(self.picture))
            point = pyautogui.locateCenterOnScreen(
                self.picture, confidence=0.7, grayscale=True)
            if point is None:
                print(" -> Not found")
            else:
                x, y = point
                print(" -> found x: {}, y: {}".format(x, y))
                pyautogui.click(x, y)
            time.sleep(3)


def has_live_threads(threads):
    return True in [t.is_alive() for t in threads]

def main():

    pictures = ['images/restart.png',
                'images/again.png'
                ]
                # 'images/dragon_update.png']
    threads = []
    for picture in pictures:
        thread = thread_sample(picture)
        threads.append(thread)
        thread.start()
        time.sleep(1)

    while has_live_threads(threads):
        try:
            # synchronization timeout of threads kill
            [t.join(1) for t in threads
             if t is not None and t.is_alive()]
        except KeyboardInterrupt:
            # Ctrl-C handling and send kill to threads
            print("Sending kill to threads...")
            for t in threads:
                t.kill_received = True

    print("Exited")

if __name__ == "__main__":
    main()

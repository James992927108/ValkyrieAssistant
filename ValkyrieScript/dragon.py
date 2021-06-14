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
            point = pyautogui.locateCenterOnScreen(
                self.picture, confidence=0.7, grayscale=True)
            if point is None:
                print("{} -> Not found".format(self.picture))
            else:
                x, y = point
                pyautogui.click(x, y)
            print(self.picture, "is active")
            time.sleep(5)


def has_live_threads(threads):
    return True in [t.is_alive() for t in threads]


def main():

    pictures = ['images/fight.png',
                'images/join_fight_1.png',
                'images/join_fight_2.png',
                'images/join.png',
                'images/start_fight.png',
                'images/ok.png',
                'images/wait.png'
                'images/next.png']
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
from pynput.keyboard import Key, Listener
import time

T = 200
DOT = 1*T
DASH = 3*T
GAP = 1*T
SPACE = 7*T
TOLERANCE = 0.5*T


class PseudoMorse:
    def __init__(self,):
        self.letter = ""
        self.word = ""
        self.message = ""
        self.t1 = 0
        self.t2 = 0
        self.pd = 0

    def on_key_release(self, key):  # what to do on key-release
        if key == Key.space:
            self.t2 = time.time()
            # rounding the long decimal float
            time_taken = round(self.t2 - self.t1, 2) * 1000
            print("The key", key, " is pressed for", time_taken, 'ms')
            if time_taken >= DOT and time_taken < DOT + TOLERANCE:
                self.letter += "."
            elif time_taken >= DASH and time_taken < DASH + TOLERANCE:
                self.letter += "-"
            # @ TODO

        return False  # stop detecting more key-releases

    def on_key_press(self, key):  # what to do on key-press
        print("in on_key_press")
        if key == Key.space:
            if self.pd is not 0:
                self.pd = time.time() - self.t2
                if self.pd >= SPACE and self.pd < SPACE + TOLERANCE:
                    self.word += self.letter
                    self.message += self.word
                    self.message += "|"
                    self.word = ""
                elif self.pd >= GAP and self.pd < GAP + TOLERANCE:
                    self.letter += " "
                    self.word += self.letter
                self.letter = ""
                self.t1 = time.time()  # reading time in sec
        # print("t1 initialized")
        return False  # stop detecting more key-presses

    # setting code for listening key-press

    def run(self,):
        while True:
            try:
               
                with Listener(on_press=self.on_key_press) as press_listener:
                    press_listener.join()
     
                # setting code for listening key-release
                with Listener(on_release=self.on_key_release) as release_listener:
                    release_listener.join()
                print(self.message)
            except KeyboardInterrupt:
                exit()

if __name__ == "__main__":
    pm = PseudoMorse()
    pm.run()

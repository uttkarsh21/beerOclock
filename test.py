import schedule
import time
import simpleaudio as sa

for x in range(3):
        print("beerOclock %d" % (x))
        play_obj = Oclock.play()
        play_obj.wait_done()
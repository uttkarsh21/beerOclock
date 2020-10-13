import schedule
import time
import simpleaudio as sa

#crontab enter 33 18 * * * /home/uttkarsh/cron_beerOclock.py

Oclock = sa.WaveObject.from_wave_file("BeerOclock.wav")

for x in range(3):
        print("beerOclock %d" % (x))
        play_obj = Oclock.play()
        play_obj.wait_done()
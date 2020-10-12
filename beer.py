import schedule
import time
import simpleaudio as sa

def job():
    Oclock = sa.WaveObject.from_wave_file("BeerOclock.wav")

    for x in range(3):
            print("beerOclock %d" % (x))
            play_obj = Oclock.play()
            play_obj.wait_done()

schedule.every().day.at("18:33").do(job)

Oclock = sa.WaveObject.from_wave_file("BeerOclock.wav")

for x in range(3):
        print("beerOclock %d" % (x))
        play_obj = Oclock.play()
        play_obj.wait_done()
        
while 1:
    schedule.run_pending()
    time.sleep(1)
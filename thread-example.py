import threading, time, os, sys
print(sys.path)
import similarmusic
import downloadmusic
# def worker(name):
#   '''THREAD WORKER FUNCTION'''
#   print("WORKER : START - COUNT ", threading.active_count())
#   time.sleep(2)
#   print("WORKER : STOP - COUNT ", threading.active_count())
#   return

# threads = []
# for i in range(5):
#   t = threading.Thread(target = worker, args=(i, ))
#   threads.append(t)
#   t.start()
print(help(similarmusic))
print(help(downloadmusic))
my_list = similarmusic.similar_search('Armin van Buuren', 'feels so good')
print(my_list[:20])
for i in my_list[:2]:
  downloadmusic.download_music(i)
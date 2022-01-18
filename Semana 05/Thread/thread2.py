import time
import threading

start = time.perf_counter()


def wait_for_sec(seconds):
    print(f'Sleeping {seconds} sec...')
    time.sleep(seconds)
    print('Done sleeping.')

threads = []

for _ in range(10):
    t = threading.Thread(target=wait_for_sec, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds')

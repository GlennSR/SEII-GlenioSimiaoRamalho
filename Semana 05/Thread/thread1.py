import time
import threading

start = time.perf_counter()


def wait_for_sec():
    print('Sleeping 1 sec...')
    time.sleep(1)
    print('Done sleeping.')


t1 = threading.Thread(target=wait_for_sec)
t2 = threading.Thread(target=wait_for_sec)

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds')

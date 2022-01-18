import time
import multiprocessing

start = time.perf_counter()


def wait_for_sec():
    print('Sleeping 1 sec...')
    time.sleep(1)
    print('Done sleeping.')


p1 = multiprocessing.Process(target=wait_for_sec)
p2 = multiprocessing.Process(target=wait_for_sec)

p1.start()
p2.start()

p1.join()
p2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds')

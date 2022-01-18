import time
import multiprocessing

start = time.perf_counter()


def wait_for_sec(seconds):
    print(f'Sleeping {seconds} sec...')
    time.sleep(seconds)
    print('Done sleeping.')


processes = []

for _ in range(10):
    p = multiprocessing.Process(target=wait_for_sec, args=[1.5])
    p.start()
    processes.append(p)

for process in processes:
    process.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds')

import time
import concurrent.futures

start = time.perf_counter()


def wait_for_sec(seconds):
    print(f'Sleeping {seconds} sec...')
    time.sleep(seconds)
    return f'Done sleeping for {seconds} sec'


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = [executor.submit(wait_for_sec, sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds')

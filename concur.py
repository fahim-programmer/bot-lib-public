import concurrent.futures
from random import randint
from time import sleep

def process_item(item):
    times = randint(0, 4)
    sleep(times)
    return item.replace('Item', f"Item Sleeped {times}")

my_list = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']

def threadPool(values, targetFunction, maxWorkers=None):
    if maxWorkers == None:
        with concurrent.futures.ThreadPoolExecutor(max_workers=maxWorkers) as executor:
            results = list(executor.map(targetFunction, values))
    else:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = list(executor.map(targetFunction, values))
    return results

results  = threadPool(my_list, process_item)
print(results)
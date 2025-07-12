from concurrent.futures import ThreadPoolExecutor
import time
def print_num(number):
    time.sleep(1)
    return f"Number : {number}"
numbers = [1,2,3,4,5]
with ThreadPoolExecutor(max_workers=3) as executer:
    results = executer.map(print_num, numbers)
for result in results:
    print(result)

import requests
import json
import concurrent.futures
import time

API_LIST = []
for i in range(1, 101):
    API_LIST.append(f"https://dummyjson.com/products/{i}")

lists_for_processes = []
for i in range(0, len(API_LIST), 20):
    lists_for_processes.append(API_LIST[i:i + 20])


def saving_information(url):
    response = requests.get(url)
    return response.json()


def thread_function(api_list):
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor1:
        results1 = list(executor1.map(saving_information, api_list))

    return results1


if __name__ == "__main__":
    start_time = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        results = []
        for lists in lists_for_processes:
            results.extend(thread_function(lists))

with open("phones.json", "w") as file:
    json.dump(results, file, indent=4)

end_time = time.perf_counter()
print(f"Execution time: {end_time - start_time} seconds")

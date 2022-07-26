import heapq
from datetime import datetime
from collections import deque
from collections import defaultdict


def run_search(traffic_logs: str):
    daily_car_count = defaultdict(int)
    top_three = []
    heapq.heapify(top_three) # heap to keep track of the top three record
    least_time_window = deque([]) # queue to implement sliding window
    least_record_val = 10 ** 10
    least_record = None # to store the continuous 1.5 hour period with least cars
    cur_count = 0
    total_count = 0

    with open(traffic_logs) as file:
        for line in file:
            ts, count = line.split(' ')
            ts = datetime.strptime(ts, "%Y-%m-%dT%H:%M:%S")
            count = int(count)

            daily_car_count[ts.date()] += count
            total_count += count
            heapq.heappush(top_three, (count, ts.isoformat()))
            if len(top_three) > 3:
                heapq.heappop(top_three)

            least_time_window.append((count, ts.isoformat()))
            cur_count += count

            if len(least_time_window) > 3:
                prev_count, _ = least_time_window.popleft()
                cur_count -= prev_count
            if len(least_time_window) == 3 and cur_count < least_record_val:
                least_record_val = cur_count
                least_record = least_time_window.copy()

    return total_count, daily_car_count, top_three, least_record


def print_record(total_count, daily_car_count, top_three, least_time_window):
    output = ""
    output += "The number of cars seen in total: \n"
    output += str(total_count) + "\n"
    output += '\n'

    output += "Daily cars seen: \n"
    for kk, vv in daily_car_count.items():
        output += (kk.isoformat() + " " + str(vv))
        output += "\n"
    output += '\n'

    output += "Top 3 half hours with most cars: \n"
    tmp = []
    while top_three:
        cc, tt = heapq.heappop(top_three)
        tmp.append(f"{tt} {cc}")
    output += "\n".join(tmp[::-1])
    output += '\n\n'

    output += "1.5 hour preriod with least cars: \n"
    while least_time_window:
        cc, tt = least_time_window.popleft()
        output += f"{tt} {cc}\n"
    print(output)


if __name__ == "__main__":
    traffic_logs = "logs/traffic_log.txt"
    print_record(*run_search(traffic_logs))
from datetime import datetime, timedelta
from typing import Tuple, List
import random
import os


def generate_traffic_timestamps(start_date: datetime, end_date: datetime) -> Tuple[List[datetime], int]:
    """generate traffic logs"""

    assert end_date > start_date, "end_date needs to be later than start_date"
    delta = end_date - start_date # duration
    time_delta = 30 * 60 # half hour shift for each record
    record_count = int(delta.total_seconds() // time_delta)

    timestamps = [start_date + i * timedelta(seconds=time_delta) for i in range(record_count)]
    return timestamps, record_count


def generate_traffic_counts(record_count: int, maximum: int = 500) -> List[int]:
    """random integer for cars count"""
    return random.choices(list(range(2, maximum + 1)), k=record_count)


def generate_traffic_logs(save=False):
    start_date = datetime.strptime('2022-07-01T00:00:00', "%Y-%m-%dT%H:%M:%S")
    end_date = datetime.strptime('2022-07-21T00:00:00', "%Y-%m-%dT%H:%M:%S")
    timestamps, record_count = generate_traffic_timestamps(start_date=start_date, end_date=end_date)
    counts = generate_traffic_counts(record_count=record_count)
    timestamps = [i.isoformat() for i in timestamps]

    if save:
        save_dir = "logs"
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        log_path = os.path.join(save_dir, 'traffic_log.txt')
        with open(log_path, 'w') as tt:
            for record in zip(timestamps, counts):
                ts, cc = record
                # create dummpy maximum record for half hour car count
                if ts == '2022-07-04T05:00:00':
                    cc = 2000
                elif ts == '2022-07-12T09:00:00':
                    cc = 1000
                elif ts == '2022-07-14T16:00:00':
                    cc = 800
                elif ts == '2022-07-17T18:00:00':
                    cc = 0
                elif ts == '2022-07-17T18:30:00':
                    cc = 5
                elif ts == '2022-07-17T19:00:00':
                    cc = 0
                else:
                    pass
                tt.writelines(" ".join(map(str, (ts, cc))))
                tt.write('\n')
        print(f'{log_path} saved')


if __name__ == "__main__":
    generate_traffic_logs(save=True)
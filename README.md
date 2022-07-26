# Automatic traffic counter log analysis

This project is containing the function to generate traffic logs randomly with specified start date, end date. Record will be stored
into a txt file under the folder logs. No third party libraries required.

## How to run
```
# run unit testing
python -m unittest test_run_search.py

# run main
python main.py
```

## Project Structure
```
.
├── README.md
├── logs
│   └── traffic_log.txt
├── main.py
├── requirements.txt
├── run_search.py
├── test_run_search.py
└── traffic_log_generator.py
```

## Algorithms
- *main.py*\
  main function to demo the required functionality
- *traffic_log_generator.py* \
  simulator to generate the logs from automatic traffic counter - timestamp (each half an hour) and the cars seen during that half hour
- *run_search.py*\
  total cars counter, daily car seen counter, top three timestamp and least contiguous 1.5 hours time window search 
  - top - three: using heap
  - least continuous 1.5 hrs - using sliding window implemented with queue
- *test_run_search.py*\
  unit test case on run_search, scenarios where the top three or least contiguous 1.5 hrs not unique also considered
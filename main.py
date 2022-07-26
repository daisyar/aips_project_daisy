from test_run_search import Test
from run_search import run_search, print_record
from traffic_log_generator import generate_traffic_logs


if __name__ == '__main__':
    print('>>> generating traffic_logs ')
    generate_traffic_logs(save=True)
    print('\n')
    print('>>> run search and print record')
    print_record(*run_search('logs/traffic_log.txt'))


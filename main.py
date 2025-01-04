from src.processing import filter_by_state, sort_by_date

a = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    {'state': 'CANCELED', 'state': 'CANCELED', 'state': 'EXECUTED'},
    {'id': 615064591, 'state': 'CANCELED', 'state': 'CANCELED', 'state': 'EXECUTED'},
    {'id': 615064591, 'state': 'CANCELED', 'date': 'aaaa-10-14T08:21:33.419441'}
]
b = [
    {'state': 'CANCELED', 'state': 'CANCELED', 'state': 'EXECUTED'}
]

if __name__ == "__main__":
    print(filter_by_state([]))
    print(sort_by_date([]))
    print(filter_by_state(a))
    print(sort_by_date(a, False))
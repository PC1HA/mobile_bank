from src.processing import filter_by_state, sort_by_date


transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.312364"},
    {"id": 939719570, "state": "1", "date": "2018-06-30T02:08:58.725572"},
    {"id": 41428829, "state": "1", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "1", "date": "2018-06-30T02:08:58.625572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

if __name__ == "__main__":
    print(filter_by_state(transactions))
    print(sort_by_date(transactions))

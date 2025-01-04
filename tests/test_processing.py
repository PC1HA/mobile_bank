import pytest

from src.processing import filter_by_state, sort_by_date


def test_list_filter_by_state() -> None:
    with pytest.raises(ValueError) as exc_info:
        filter_by_state(123443)  # type: ignore
        filter_by_state("frrg")  # type: ignore
        filter_by_state(())  # type: ignore
        filter_by_state({})  # type: ignore
        filter_by_state([], 124)  # type: ignore
        filter_by_state(["rrrt"])  # type: ignore
        filter_by_state() # type: ignore
    assert str(exc_info.value) == "Неверный тип данных, ожидается List(список)"


def test_list_sort_by_date() -> None:
    with pytest.raises(ValueError) as exc_info:
        sort_by_date(123443)  # type: ignore
        sort_by_date("frrg")  # type: ignore
        sort_by_date(())  # type: ignore
        sort_by_date({})  # type: ignore

    assert str(exc_info.value) == "Неверный тип данных, ожидается List(список)"


def test_error_state() -> None:
    with pytest.raises(ValueError) as exc_info:
        filter_by_state([{}], 1213)  # type: ignore
        filter_by_state([], [])  # type: ignore
        filter_by_state([], {})  # type: ignore
        filter_by_state([], ())  # type: ignore

    assert str(exc_info.value) == "Неверный state"


@pytest.mark.parametrize(
    "a, b, c",
    [
        (
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
            "EXECUTED",
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
        ),
        (
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
            "executed",
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
        ),
        ([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}], "CANCELED", []),
        ([{"id": 41428829, "date": "2019-07-03T18:35:29.512364"}], "EXECUTED", []),
        ([{"state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}], "EXECUTED", []),
        ([{"id": 41428829, "state": "EXECUTED"}], "EXECUTED", []),
        ([], "EXECUTED", []),
    ],
)
def test_filter_by_state(a: list, b: str, c: list) -> None:
    assert filter_by_state(a, b) == c


@pytest.fixture()
def sort_date() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_date(sort_date: list) -> None:
    assert (
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"state": "CANCELED", "state": "CANCELED", "state": "EXECUTED"},  # noqa
                {"id": 615064591, "state": "CANCELED", "state": "CANCELED", "state": "EXECUTED"},  # noqa
                {"id": 615064591, "state": "CANCELED", "date": "aaaa-10-14T08:21:33.419441"},
            ]
        )
        == sort_date
    )

    assert (
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
        == sort_date
    )


@pytest.fixture()
def revers_sort_data() -> list:
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_revers_sort_data(revers_sort_data: list) -> None:
    assert (
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"state": "CANCELED", "state": "CANCELED", "state": "EXECUTED"},  # noqa
                {"id": 615064591, "state": "CANCELED", "state": "CANCELED", "state": "EXECUTED"},  # noqa
                {"id": 615064591, "state": "CANCELED", "date": "aaaa-10-14T08:21:33.419441"},
            ],
            False,
        )
        == revers_sort_data
    )

    assert (
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            False,
        )
        == revers_sort_data
    )


@pytest.fixture()
def zero_list_date() -> list:
    return []


def test_zero_list_date(zero_list_date: list) -> None:
    assert sort_by_date([]) == zero_list_date
    assert sort_by_date([{}]) == zero_list_date
    assert (
        sort_by_date(
            [
                {"state": "CANCELED", "state": "CANCELED", "state": "EXECUTED"},  # noqa
                {"id": 615064591, "state": "CANCELED", "state": "CANCELED", "state": "EXECUTED"},  # noqa
                {"id": 615064591, "state": "CANCELED", "date": "aaaa-10-14T08:21:33.419441"},
            ]
        )
        == zero_list_date
    )

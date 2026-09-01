import time
from typing import Callable, Any

PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8


def performance_logger (func: Callable[..., Any]) -> Callable[..., Any]:
    """
    This function decorator which count time processing main function, print this time and return result main function

    Args:
        func (Callable[..., Any]): main function

    Returns:
        func Callable[..., Any]: result of main function

    """

    def wrapper(*args, **kwargs) -> list[dict[str, str | float]]:
        start_process = time.perf_counter()
        result = func(*args, **kwargs)
        time_of_process = time.perf_counter() - start_process
        print(f"{PERFORMANCE_LOG_PREFIX} Function {func.__name__} finished in {time_of_process:.{TIME_DECIMALS}f} seconds")
        return result
    return wrapper

@performance_logger
def get_sorted_report(dictionary_list:list[dict[str, str | float]]) -> list[dict[str, str | float]]:
    """
    This function sorts list of dictionaries based on total sales

    Args:
        dictionary_list (list[dict[str, str | float]]): list of dictionaries

    Returns:
        sort_dictionary_list (list[dict[str, str | float]]): sorted list of dictionaries
    """

    return sorted(dictionary_list, key=lambda item: item['total_sales'], reverse=True)

sorted_report1 = get_sorted_report(
[
{"category": "Drama", "total_sales": 500.00}
]
)

print('Top Categories by Revenue')

for index, item in enumerate(sorted_report1, start=1):
    print(f"{index}. {item['category']}: {item['total_sales']}")

sorted_report2 = get_sorted_report(
[
{"category": "Action", "total_sales": 4311.85},
{"category": "Animation", "total_sales": 4656.30},
{"category": "Children", "total_sales": 3655.55}
]
)

print('Top Categories by Revenue')

for index, item in enumerate(sorted_report2, start=1):
    print(f"{index}. {item['category']}: {item['total_sales']}")

sorted_report3 = get_sorted_report(
[
{"category": "Classics", "total_sales": 1200.10},
{"category": "Comedy", "total_sales": 4000.00},
{"category": "Documentary", "total_sales": 4000.00}
]
)

print('Top Categories by Revenue')

for index, item in enumerate(sorted_report3, start=1):
    print(f"{index}. {item['category']}: {item['total_sales']}")


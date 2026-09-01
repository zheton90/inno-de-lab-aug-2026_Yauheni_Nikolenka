DEFAULT_RETURN_INDEX_BASE = 10.0

def calculate_overdue_fine(name: any, days_overdue: any, fine_rate: any) -> tuple[str | None, float, float] :
    """
       This function count total rate and index of return. Also handles ValueError, TypeError and ZeroDivisionError
       for invalid arguments.

       Args:
           name (str | any): name of the movie
           days_overdue (any): how many days overdue
           fine_rate (any): fine rate for day_overdue

       Returns:
           tuple[str | None, float, float]: return total fine rate and index of return. For Error return tuple[None, float, float]
       """
    try:
        numeric_days = float(days_overdue)
        total_fine = numeric_days * fine_rate
        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days
        return name, return_index, total_fine
    except ValueError:
        print(f"Error: ValueError. {name} could not convert string to float {days_overdue}")
        return None, 0.0 , 0.0
    except TypeError:
        print(f"Error: TypeError. Uncorrected type of date for {name} argument must be a string or a real number, not '{type(days_overdue)}'")
        return None, 0.0 , 0.0
    except ZeroDivisionError:
        print(f"Error: ZeroDivisionError. Return without overdue. {name} float division by zero")
        return None, 0.0 , 0.0
    finally:
        print('--- Return transaction validation completed ---')

name, index, total_fine = calculate_overdue_fine('Interstellar', 2, 3.0)

if name:
    print(f'Movie: {name} | Total Fine: {total_fine} | Fine Rate: {index}')
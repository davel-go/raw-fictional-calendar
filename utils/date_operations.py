def days_to_add(current_day, days_addition):
    if days_addition is None or days_addition == 0:
        return [current_day, 0]
    # Total days in a month for the fictional calendar
    days_in_month = 115

    # Calculate the new day by adding or subtracting days
    new_day = current_day + days_addition

    # Determine the number of months to add or subtract
    months_to_change = 0

    while new_day > days_in_month:
        new_day -= days_in_month
        months_to_change += 1

    while new_day < 1:
        new_day += days_in_month
        months_to_change -= 1

    return [new_day, months_to_change]


def months_to_add(current_month, months_addition):
    if months_addition is None or months_addition == 0:
        return [current_month, 0]
    # Total months in a year for the fictional calendar
    months_in_year = 6

    # Calculate the new month by adding or subtracting months
    new_month = current_month + months_addition

    # Determine the number of years to add or subtract
    years_to_change = 0

    while new_month > months_in_year:
        new_month -= months_in_year
        years_to_change += 1

    while new_month < 1:
        new_month += months_in_year
        years_to_change -= 1

    result = [new_month, years_to_change]
    return result


def date_operation(date: list, date_op: list, before: bool = True):
    if isinstance(before, str):
        before = before.upper() == "TRUE"
    days, months, years = date_op
    if days is None:
        days = 0
    if months is None:
        months = 0
    if years is None:
        years = 0
    if before is True:
        days *= -1
        months *= -1
        years *= -1

    curr_day, months_addition = days_to_add(date[0], days)
    months_addition += months
    curr_month, years_addition = months_to_add(date[1], months_addition)
    years_addition += years
    curr_year = date[2] + years_addition
    return [curr_day, curr_month, curr_year]

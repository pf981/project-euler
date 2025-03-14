# FIXME: This gives 170, rather than 171
from datetime import date, timedelta

days_in = {month: 31 for month in range(1, 13)}
days_in[9] = 30 # September
days_in[4] = 30 # April
days_in[6] = 30 # May
days_in[11] = 30 # and November

def finished_month(cur_date):
    # February
    if cur_date["month"] == 2:
        # If it's a leap year
        if cur_date["year"] % 4 == 0 and cur_date["year"] % 400 != 0:
            days_in_feb = 29
        else:
            days_in_feb = 28
        return cur_date["day"] < days_in_feb

    return cur_date["day"] < days_in[cur_date["month"]]

def tomorrow(cur_date):
    cur_date["day"] += 1

    # Handle the end of the month
    if finished_month(cur_date):
        cur_date["month"] += 1
        cur_date["day"] = 1

    # If its the end of the year
    if cur_date["month"] > 12:
        cur_date["year"] += 1
        cur_date["month"] = 1




def main():
    cur_date = {"day" : 1, "month": 1, "year": 1900}
    start_date = {"day" : 1, "month": 1, "year": 1901}
    end_date = {"day" : 1, "month": 1, "year": 2000}

    # day_name == 0 => sunday
    day_name = 0

    while cur_date != start_date:
        tomorrow(cur_date)
        day_name = (day_name + 1) % 7

    answer = 0
    print(cur_date, day_name)
    while cur_date != end_date:
        if day_name == 0 and cur_date["day"] == 1:
            answer += 1
        tomorrow(cur_date)
        day_name = (day_name + 1) % 7

    print(cur_date)
    print(answer)

if __name__ == '__main__':
    main()

from datetime import date, timedelta

def main():
    start_date = date(1901, 1, 1)
    end_date = date(2000, 12, 31)
    while start_date.strftime("%A") != "Sunday":
        start_date += timedelta(days=1)
#    print(start_date.strftime("%A"))
    days_between = (end_date - start_date).days
    print(days_between)
    answer = int(days_between / 7)
    print(answer)


if __name__ == '__main__':
    main()

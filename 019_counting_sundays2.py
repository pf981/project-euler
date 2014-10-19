from datetime import date, timedelta

def main():
    start_date = date(1901, 1, 1)
    end_date = date(2000, 12, 31)

    # Start on the first sunday
    cur_date = start_date
    while cur_date.strftime("%A") != "Sunday":
        cur_date += timedelta(days=1)

    answer = 0
    while cur_date != end_date:
        cur_date += timedelta(days=1)
        if cur_date.strftime("%A") == "Sunday" and cur_date.month == 1:
            answer += 1

    print(answer)


if __name__ == '__main__':
    main()

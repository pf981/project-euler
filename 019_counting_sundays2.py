from datetime import date, timedelta

def main():
    start_date = date(1901, 1, 1)
    end_date = date(2000, 12, 31)

    # Start on the first sunday
    cur_date = start_date

    answer = 0
    while cur_date != end_date:
        if cur_date.strftime("%A") == "Sunday" and cur_date.day == 1:
            print(cur_date)
            answer += 1

        cur_date += timedelta(days=1)

    print(answer)


if __name__ == '__main__':
    main()

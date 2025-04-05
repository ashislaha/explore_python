from datetime import datetime
from datetime import date

def explore_date_time():
    today = datetime.today()
    print(today)
    print(f"year => {today.year}")
    print(f"month => {today.month}")
    print(f"day => {today.day}")
    print(f"ctime => {today.ctime()}")

    datetime1 = datetime(2030,1,1,6,10) # 1st January 2030, 6:10 am
    datetime2 = datetime(2031,1,1,14,10) # 1st January 2031, 2:10 pm
    print(f"datetime diff {datetime2-datetime1}")

def explore_future_dates():
    future_date_1 = date(2030,1,1)
    future_date_2 = date(2031,2,1)
    print(f"date difference = {future_date_2 - future_date_1}")
1
if __name__ == "__main__":
    explore_date_time()
    explore_future_dates()
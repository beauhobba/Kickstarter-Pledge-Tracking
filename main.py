from find_ks_data import find_ks_data
import time 
import csv
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

urls = [
    "https://www.kickstarter.com/projects/dwyerart/star-travelers-oracle?ref=discovery_category",
    "https://www.kickstarter.com/projects/hphan/balmasque?ref=discovery_category_newest",
    "https://www.kickstarter.com/projects/realmsofrivers/realms-of-rivers?ref=discovery_category_newest",
    "https://www.kickstarter.com/projects/mystic-canopy-spells/mystic-canopy-the-ultimate-druid-spell-deck?ref=discovery_category"
]
files = ["star-travelers-oracle.csv", "balmasque.csv", "realms-of-rivers.csv", "mystic-canopy-spells.csv"]


def main():
    for url, file in zip(urls, files):
        
        try:
            pledge_amount, backers, days_to_go = find_ks_data(url)
        except Exception as ex:
            print(f"Error Reading {url} - {ex}")

        # Create a Timestamp 
        timestamp = time.time()
        date_time = datetime.fromtimestamp(timestamp).strftime('%d/%m/%y %H:%M:%S')
        
        
        with open('./data/'+file, 'a', newline='') as file:
            writer = csv.writer(file)
            # Write data rows
            row_data = [date_time, pledge_amount, backers, days_to_go]  
            writer.writerow(row_data)

        time.sleep(1)
        
        
main()
# Run the job every hour
sched.add_job(main, 'interval', hours=2)
sched.start()
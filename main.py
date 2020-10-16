# import libraries
import calendar
import os
import csv
from datetime import date


# create empty list for months and then append month name in it
dir_names = []
for month_num in range(1, 13):
    dir_names.append(calendar.month_name[month_num])
print("successfully got all months ")

dir_path = os.getcwd()

# return all Wednesdays of a given year
year = 2020
obj = calendar.TextCalendar(calendar.SUNDAY)
wednesdays = []
days = []
rows_header = ['year', 'month', 'date']

try:
    # get wednesdays
    for month in range(1, 13):
        for i in obj.itermonthdays(year, month):
            if i != 0:
                day = date(year, month, i)
                days.append(day)
                if day.weekday() == 2:                  # if its WEDNESDAY
                    wednesdays.append(day)

# create directories
    for dir_name in dir_names:
        path = os.path.join(dir_path, dir_name)
        os.mkdir(path)
        print("directory '{}' created".format(dir_name))

        for wednesday in wednesdays:
            for day in days:
                month = wednesday.strftime('%B')        # get wednesday's month

                # create csv files
                if dir_name == month:             # if directory name (month) is matching to wednesday's month
                    with open(os.path.join(dir_path, dir_name, str(wednesday) + '.csv'), 'a') as csvfile:
                        # creating a csv writer object
                        csvwriter = csv.writer(csvfile)
                        if wednesday > day:
                            day = str(day).split('-')
                            day = [day[0], day[1], day[2]]
                            csvwriter.writerow(day)
                            print("created csv file '{}'".format(wednesday))


except Exception as error:
    print(error)

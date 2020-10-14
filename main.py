# import libraries
import calendar
import os
import csv
from datetime import date


# create empty list for months and then append month name in it
directory_names = []
for month_num in range(1, 13):
    directory_names.append(calendar.month_name[month_num])
print("successfully got all months ")

dir_path = os.getcwd()

# Returns all Wednesdays of a given year
year = 2020
obj = calendar.TextCalendar(calendar.SUNDAY)
wednesdays = []


try:
    # get wednesdays
    for month in range(1, 13):
        for i in obj.itermonthdays(year, month):
            if i != 0:
                day = date(year, month, i)
                if day.weekday() == 2:                  # if its WEDNESDAY
                    wednesdays.append(day)

# create directories
    for directory_name in directory_names:
        path = os.path.join(dir_path, directory_name)
        os.mkdir(path)
        print("directory '{}' created".format(directory_name))
        for wednesday in wednesdays:
            file_name = wednesday.strftime('%B')        # get wednesday's month

            # create csv files
            if directory_name == file_name:             # if directory name (month) is matching to wednesday's month
                with open(os.path.join(dir_path, directory_name, str(wednesday) + '.csv'), 'w') as csvfile:
                    # creating a csv writer object
                    csvwriter = csv.writer(csvfile)
            else:
                print("doesn't match")


except Exception as error:
    print(error)

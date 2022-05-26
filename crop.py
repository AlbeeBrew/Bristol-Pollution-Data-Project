"""
This program will crop and filter bristol-air-quality-data.csv and generate crop.csv
"""
import datetime

# Defining CONSTANTS
DATABASE_PATH = "bristol-air-quality-data.csv"
LOWER_BOUND = datetime.datetime(2010, 1, 1, 0, 0, 0, 0)

# Reading/Writing a file using `with` statement
# Hence no need to call .close() method in the end
with open(DATABASE_PATH) as database:
    with open('crop.csv', 'w') as croped_csv:
        croped_csv.write(database.readline())
        line = database.readline()
        count = 0
        # While there is a line in the file. Read next line
        while line:
            try:
                line_list = line.split(';')
                date_time = line_list[0]
                date_time = date_time.split('T')
                hour, minute, second, milsec = date_time[1].split(':')
                second = second.split('+')[0]
                year, month, day = date_time[0].split('-')
                datetime_obj = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))
                if LOWER_BOUND <= datetime_obj:
                    croped_csv.write(line)
            except IndexError:
                pass
            line = database.readline()

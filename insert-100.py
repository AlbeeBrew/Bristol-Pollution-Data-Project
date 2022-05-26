"""
This program will create a file called insert-100.sql
In this file will be the query for the first 100 data
insertions.
"""
from datetime import datetime


# Defining CONSTANTS
CSV_PATH ='clean.csv'
SQL_PATH = 'insert-100.sql'
INSERTION_QUERY = 'INSERT INTO pollution.readings (datetime, nox, no2, no, `pm 10`, `nvpm 10`, `vpm 10`, `nvpm 2.5`, `pm 2.5`, \
`vpm 2.5`, co, o3, so2, temperature, rh, airpressure, datestart, \
dateend, current, `instrument type`, `stationid-fk` ) VALUES\n'

# Location_ids is used in maintaing foreign-key relationship
location_ids = {}

# Reading/Writing a file using `with` statement
# Hence no need to call .close() method in the end
with open(SQL_PATH, 'w+') as sql_file:
    with open(CSV_PATH) as csv_file:
        csv_file.readline() # skipping first line i.e header
        insertions = []
        current_id = 1
        # Range(100) for reading only first 100 rows
        for i in range(100):
            line = csv_file.readline()
            words = line.split(';')
            
            filtered_words = words[:4] + words[5:17] + words[-4:] 
            refined_words_list = []
            for word in filtered_words:
                word = word.rstrip()
                if word == '':
                    word = None
                refined_words_list.append(word)

            # Convert datetimes into Python Datetime objects
            if refined_words_list[0]:
                date = str(refined_words_list[0]).split('T')[0].split('-')
                time = str(refined_words_list[0]).split('T')[1].split(':')
                date_time = datetime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]), int(time[2].split('+')[0]))
                refined_words_list[0] = date_time
            if refined_words_list[16]:
                date = str(refined_words_list[16]).split('T')[0].split('-')
                time = str(refined_words_list[16]).split('T')[1].split(':')
                date_time = datetime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]), int(time[2].split('+')[0]))
                refined_words_list[16] = date_time
            if refined_words_list[17]:
                date = str(refined_words_list[17]).split('T')[0].split('-')
                time = str(refined_words_list[17]).split('T')[1].split(':')
                date_time = datetime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]), int(time[2].split('+')[0]))
                refined_words_list[17] = date_time
            
            # Working with location_ids dictionary
            Id = location_ids.setdefault(words[17], current_id)
            if Id == current_id:
                current_id += 1

            refined_words_list.append(Id)
            insertions.append(refined_words_list)

    x = INSERTION_QUERY
    # Formatting query
    for first_list in insertions:
        x += ' ('
        for index, word in enumerate(first_list):
            if index in [0, 16, 17]:
                if word:
                    word = word.strftime("%Y-%m-%d %H:%M:%S")
            x += str(word)
            x += ', '
        x = x[:-2]
        x += '),\n'
    x = x[:-1]
    x = x.replace('None', 'NULL')
    sql_file.write(x)
    
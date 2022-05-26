"""
This program will populate data into the pollution database
in the following tables:
- Schema
- Station
- Readings
"""
import mariadb
import pandas as  pd
from datetime import datetime

# DEFINING CONSTANTS
DATABASE_SELECTING = 'USE pollution'
SELECTION_QUERY = 'SELECT * FROM readings'
INSERTION_QUERY = 'INSERT INTO readings (datetime, nox, no2, no, `pm 10`, `nvpm 10`, `vpm 10`, `nvpm 2.5`, `pm 2.5`, \
                `vpm 2.5`, co, o3, so2, temperature, rh, airpressure, datestart, \
                dateend, current, `instrument type`, `stationid-fk` ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \
                %s, %s, %s, %s, %s, %s, %s, %s, %s)'
INSERTING_IN_STATIONS_QUERY = 'INSERT INTO stations (location, geo_point_2d) VALUES (%s, %s)'
INSERTING_IN_SCHEMA_QUERY = 'INSERT INTO `schema` (measure, description, unit) VALUES (%s, %s, %s)'
CREATE_DATABASE = "CREATE SCHEMA IF NOT EXISTS pollution DEFAULT CHARACTER SET utf8"
CREATE_TABLE_STATIONS = """CREATE TABLE IF NOT EXISTS `stations` (
 `stationId` INT NOT NULL AUTO_INCREMENT,
  `location` VARCHAR(48) NULL,
  `geo_point_2d` VARCHAR(45) NULL,
  PRIMARY KEY (`stationId`))
ENGINE = InnoDB"""
CREATE_TABLE_READINGS = """
CREATE TABLE IF NOT EXISTS `readings` (
  `readingId` INT NOT NULL AUTO_INCREMENT,
  `datetime` DATETIME NULL,
  `nox` FLOAT NULL,
  `no2` FLOAT NULL,
  `no` FLOAT NULL,
  `pm 10` FLOAT NULL,
  `nvpm 10` FLOAT NULL,
  `vpm 10` FLOAT NULL,
  `nvpm 2.5` FLOAT NULL,
  `pm 2.5` FLOAT NULL,
  `vpm 2.5` FLOAT NULL,
  `co` FLOAT NULL,
  `o3` FLOAT NULL,
  `so2` FLOAT NULL,
  `temperature` REAL NULL,
  `rh` INT NULL,
  `airpressure` INT NULL,
  `datestart` DATETIME NULL,
  `dateend` DATETIME NULL,
  `current` TEXT(5) NULL,
  `instrument type` VARCHAR(32) NULL,
  `stationid-fk` INT NOT NULL,
  PRIMARY KEY (`readingId`)
  )
ENGINE = InnoDB"""
CREATE_TABLE_SCHEMA = """
CREATE TABLE IF NOT EXISTS `schema` (
  `measure` VARCHAR(32) NOT NULL,
  `description` VARCHAR(70) NULL,
  `unit` VARCHAR(24) NULL,
  PRIMARY KEY (`measure`))
ENGINE = InnoDB """
PATH = 'clean.csv'

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def insert_schema(cursor):
    """ Inserts data into schema"""
    cursor.execute("TRUNCATE TABLE `schema`")
    insertion = {
    'measure': 
        ["Date Time", "NOx", "NO2", "NO", "SiteID", "PM10",
        "NVPM10", "VPM10", "NVPM2.5", "PM2.5", "VPM2.5", "CO", "O3", "SO2",
        "Temperature", "RH", "Air Pressure", "Location", "geo_point_2d",
        "DateStart", "DateEnd", "Current", "Instrument Type"],

    'desc' : 
        ["Date and time of measurement", "Concentration of oxides of nitrogen",
        "Concentration of nitrogen dioxide", "Concentration of nitric oxide", "Site ID for the station",
        "Concentration of particulate matter <10 micron diameter",
        "Concentration of non-volatile particulate matter <10 micron diameter",
        "Concentration of volatile particulate matter <10 micron diameter",
        "Concentration of no-valatile particulate matter <2.5 micron diameter",
        "Concentration of particulate matter <2.5 micron diameter",
        "Concentration of volatile particulate matter <2.5 micorn diameter", 
        "Concentration of carbon monoxide", "Concentration of ozone", "Concentration of sulphur dioxide",
        "Air temperature", "Relative Humidity", "Air Pressure", "Text description of location",
        "Latitude and longitude", "The date monitoring started", "The date monitoring ended", 
        "Is the monitor currently operating", "Classification of the instrument"],

    'unit': 
        ["datetime","μg/m3","μg/m3","μg/m3", "integer", "μg/m3","μg/m3",
        "μg/m3","μg/m3","μg/m3", "μg/m3", "μg/m3","μg/m3","μg/m3", "°C",
        "%", "mbar", "text", "geo point", "datetime", "datetime", "text" ,"text"]
            }   

    measures = insertion['measure']
    descriptions = insertion['desc']
    units = insertion['unit']

    data = [[measure, description, unit] for measure, description, unit in zip(measures, descriptions, units)]
    cursor.executemany(INSERTING_IN_SCHEMA_QUERY, data)
    print('Successfully inserted schema')
 

def insert_stations(cursor, stations_dataframe, location_ids):
    """ Inserts data into stations table"""
    cursor.execute("TRUNCATE TABLE `stations`")
    for location in stations_dataframe.groupby('Location'):
        location_name = location[0]
        geo_point = location[1]['geo_point_2d'].iloc[0]

        values = [location_name, geo_point]
        cursor.execute(INSERTING_IN_STATIONS_QUERY, values)
        location_ids[location_name] = cursor.lastrowid
    print('Successfully inserted rows in stations table')

def insert_readings(cursor, location_ids):
    """ Inserts data into readings table"""
    cursor.execute("TRUNCATE TABLE `readings`")
    # Reading csv file using with statement
    # Hence no need to call .close() method in the end
    with open(PATH) as csv_file:
        csv_file.readline()
        data = csv_file.readlines()
        insertions = []

        for d in data:
            val = d.split(';')
            val2 = val[:4] + val[5:17] + val[-4:] 
            new_val = []
            for x in val2:
                # Replace every missing value with None
                if x == '':
                    x = None
                new_val.append(x)
            
            # Convert datetimes into Python Datetime objects
            if new_val[0]:
                date = str(new_val[0]).split('T')[0].split('-')
                time = str(new_val[0]).split('T')[1].split(':')
                date_time = datetime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]), int(time[2].split('+')[0]))
                new_val[0] = date_time
            if new_val[16]:
                date = str(new_val[16]).split('T')[0].split('-')
                time = str(new_val[16]).split('T')[1].split(':')
                date_time = datetime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]), int(time[2].split('+')[0]))
                new_val[16] = date_time
            if new_val[17]:
                date = str(new_val[17]).split('T')[0].split('-')
                time = str(new_val[17]).split('T')[1].split(':')
                date_time = datetime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]), int(time[2].split('+')[0]))
                new_val[17] = date_time
            new_val.append(location_ids[val[17]])
            insertions.append(new_val)
        # Inserts chunks of data into table of 1000 rows
        insertions = list(chunks(insertions, 1000))

        # Call executemany function for every 1000 rows
        for insertion in insertions:
            cursor.executemany(INSERTION_QUERY, insertion)
    print("Successfully inserted rows in readings table")


def main():
    # connecting to the localhost
    pollution_db2 = mariadb.connect(
        host="localhost",
        user="root",
        password="",
        port=3306
    )
    # Creating tables in datbase if not exists
    sql_cursor = pollution_db2.cursor()
    sql_cursor.execute("DROP SCHEMA IF EXISTS pollution")
    sql_cursor.execute(CREATE_DATABASE)
    sql_cursor.execute(DATABASE_SELECTING)
    sql_cursor.execute(CREATE_TABLE_SCHEMA)
    sql_cursor.execute(CREATE_TABLE_STATIONS)
    sql_cursor.execute(CREATE_TABLE_READINGS)
    dataframe = pd.read_csv(PATH, sep=';')
    locationIds = {}

    # The order matters
    insert_schema(sql_cursor)
    pollution_db2.commit()
    insert_stations(sql_cursor, dataframe, locationIds)
    pollution_db2.commit()
    insert_readings(sql_cursor, locationIds)
    pollution_db2.commit()

    pollution_db2.close()


# Call main function if script is executed rather than being imported
if __name__ == "__main__":
    main()

"""
This program will clean crop.csv and generate clean.csv
"""
import pandas as pd

# Defining CONSTANTS
DATABASE_PATH = "crop.csv"


REFERENCE = {
188: 'AURN Bristol Centre',
203: 'Brislington Depot',
206: 'Rupert Street',
209: 'IKEA M32',
213: 'Old Market',
215: 'Parson Street School',
228: 'Temple Meads Station',
270: 'Wells Road',
271: 'Trailer Portway P&R',
375: 'Newfoundland Road Police Station',
395: "Shiner's Garage",
452: 'AURN St Pauls',
447: 'Bath Road',
459: 'Cheltenham Road \ Station Road',
463: 'Fishponds Road',
481: 'CREATE Centre Roof',
500: 'Temple Way',
501: 'Colston Avenue'}

df = pd.read_csv(DATABASE_PATH, sep=';')
df2 = df.copy()

# Looping through each REFERENCE element and replacing every element found in 
# the Series "SiteID" using .replace(to_replace=k, value=y). Inplace will 
# make changes to the dataframe instead of returning new dataframe
for k, v in REFERENCE.items():
    df2['SiteID'].replace(to_replace=k, value=v, inplace=True)

new_df = df.drop(df[df2['SiteID'] != df2['Location']].index)

# Print dud records
dud_record = df[(df2['SiteID'] != df2['Location'])]
dud_record.index = dud_record.index + 2
for line_number, mismatch_field in zip(dud_record.index, dud_record['SiteID']):
    print(line_number, str(mismatch_field).rjust(10))

# to_csv() will write the dataframe into csv file
new_df.to_csv('clean.csv', index=False, sep=';')
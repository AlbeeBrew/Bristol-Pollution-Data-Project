 **_Data modeling_**

** Schema Collection **


```json
{
    measure: ...
    description: ...
    unit: ...
}
```

<Stations Collection >


```json
{	
    _id : ..
    location : ....
    geo_point_2d : ...

}
```
</font>


<Readings Collection >

```json
{
    _id : ..
    datetime : ...
    nox : ...
    no2 : ...
    no : ...,
    pm10 : ...
    nvpm10 : ...
    vpm10 : ...
    nvpm2.5 : ...
    pm2.5 : ...
    vom2.5 : ...
    co : ...
    o3 : ...
    so2 : ...
    temperature : ... 
    rh : ...
    airpressure : ...
    datestart : ...
    dateend : ...
    current : ...
    instrument-type : ...
    station_id : ..

}
```

-----

**_Implementation_**


As you know, writing and dumping big data into a database isn't very easy. It consumes a lot of time to implement a large database. So, I decided to implement the database using a **python API** known simply as **pymongo**. With the help of python and pymongo, I was able to dump all the data into the database with very ease.


 ## Implementation of schema Collection##


 The following function will insert **schema collection** into the database. It takes the collection as an argument and dump the data into it. **pymongo**'s *insert_many* method works exactly the same as **mongodb**'s *insertMany*.

```python
def insert_schema(collection): 
    schema = {
        'measure': 
            ["Date Time", "NOx",  
            .....
            "Current", "Instrument Type"],

        'desc' : 
            ["Date and time of measurement", 
            "Concentration of nitrogen dioxide", 
            ..... 
            "Is the monitor currently operating",
            "Classification of the instrument"],

        'unit': 
            ["datetime","μg/m3", 
            .....
            "text" ,"text"]
        }   

    measures = schema['measure']
    descriptions = schema['desc']
    units = schema['unit']
    schema_data = [{'measure': measure, 'description': description, 'unit': unit} for measure, description, unit in zip(measures, descriptions, units)]
    collection.insert_many(schema_data)
    print("Schema successfully inserted")
```

## Implementation of stations Collection ##

 The following function will insert **stations collection** into the database. In this collection, there will be only one document inserted because we will be dealing with only **_1 specific station_**. It takes the collection as an argument and dump the data into it. One thing to notice is that, *insert_stations* must be called before the *insert_readings* function because the collection *readings* depends on the collection *stations*.
 The field '_stationId' points to the '_id' field of collection *stations*.


```python  
def insert_stations(collection):
    df = pd.read_csv(CSV_PATH, sep=';')
    for Id, location in enumerate(df.groupby('Location')):
        location_name = location[0]
        geo_point = location[1]['geo_point_2d'].iloc[0]
        document = {'_id': Id+1, 'location': location_name, 'geo_point': geo_point}
        collection.delete_one({'_id': Id+1})
        record = collection.insert_one(document)
        locationIds[location_name] = record.inserted_id
        break
        # Break statement is used to insert only 1 specific station
    print("Stations successfully inserted")
```

## Implementation of readings Collection##

Finally, *insert_readings* works exactly the same as other functions mentioned before. One thing to consider is that datetime strings must be converted to datetime objects before insertion. As did here, 'ISODate' is the datetime object referenced in **mongodb**. Good thing about **pymongo** is it automatically takes care of conversion between datetime objects of **python** and **mongodb**.
Also, the values of pollutants are type cast to floats beforehand.
One extra step we need to take is that we have to filter data based on stations and insert data which has monitor (station) that we selected.

# **_Query_**

I queried the last part of Task 4 (i.e. query-c). In the following code, I am calling the aggregate function of **MongoDB** after selecting the proper collection which is in this case *readings*. Selection can be done in multiple ways but I preferred *db.getCollection* method. Now, the aggregate method itself takes an array. Using the '$' operators. I was able to group and get the mean of VPM2.5 and PM2.5 fields.

```
db.getCollection('readings').aggregate([ {'$match' : {DateTime: {'$gte':2010} , DateTime: {'$lte': 2019} } }, {'$group': {_id: '$stationId', 'Mean of PM' : {'$avg': '$PM2'}, 'Mean of VPM': {'$avg' : '$VPM2'}} }])
```

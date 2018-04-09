import psycopg2

connection = psycopg2.connect("dbname=where_the_truck user=dbperson")

cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS where_the_truck_vendors")
table_create_command = """CREATE TABLE where_the_truck_vendors (
  submission_date varchar(30),
  customer_name varchar(30),
  food_truck_name varchar(30),
  serving_date varchar(10),
  starting_time varchar(20),
  ending_time varchar(20),
  location_name varchar(30),
  street_address varchar(30),
  city varchar(30),
  state varchar(4),
  zipcode varchar(8),
  email varchar(30)
);"""

cursor.execute(table_create_command)
submission_date ='04/08/2018'
customer_name ='Charles LaPress'
food_truck_name ='Chuck Truck'
serving_date = '04/09/2018'
starting_time ='10:00 am'
ending_time ='02:00 pm'
location_name ='Next on Main'
street_address ='101 Main Street'
city ='Greenville'
state ='SC'
zipcode ='29601'
email ='charleslapress@gmail.com'

cursor.execute("INSERT INTO where_the_truck_vendors VALUES('04/08/2018', 'John Smith','Asada', '04/09/2018','11:00 am', '03:00 pm','Spot Coffee', '500 E. McBee', 'Greenville', 'SC', '29615', 'jsmith@gmail.com');")
cursor.execute("INSERT INTO where_the_truck_vendors VALUES('04/08/2018', 'Adam Kelly','Pig Pickens', '04/09/2018','10:00 am', '01:00 pm','The Place on Main', '112 Main Street', 'Greenville', 'SC', '29602', 'adamkelly@att.net');")
cursor.execute("INSERT INTO where_the_truck_vendors VALUES('04/09/2018', 'Larry James','Donut Shack', '04/09/2018','12:00 pm', '03:00 pm','Starbucks', '1318 Augusta', 'Greenville', 'SC', '29602', 'larry J2@gmail.com');")
cursor.execute("INSERT INTO where_the_truck_vendors VALUES('04/08/2018', 'Anne Dory','Sandwich Shoppe', '04/09/2018','11:30 am', '01:30 pm','Strange Brew', '82 Elm Street', 'Simpsonville', 'SC', '29617', 'msanne@gmail.com');")
cursor.execute("INSERT INTO where_the_truck_vendors VALUES('04/09/2018', 'Peter Cotton','BBQ and Stuff', '04/10/2018','11:00 am', '03:00 pm','The Place on Main', '112 Main Street', 'Greenville', 'SC', '29602', 'cotton@yahoo.com');")
cursor.execute("INSERT INTO where_the_truck_vendors VALUES('04/08/2018', 'Charles LaPress','Chuck Truck II', '04/09/2018','01:00 pm', '05:00 pm','Spot Coffee', '500 E. McBee', 'Greenville', 'SC', '29615', 'charleslapress@gmail.com');")
cursor.execute("INSERT INTO where_the_truck_vendors VALUES('04/08/2018', 'Gloria Whittman','Vegan Van', '04/11/2018','12:00 pm', '04:00 pm','Artsphere', '104 Main Street', 'Greenville', 'SC', '29601', 'gwwitman@gmail.com');")
cursor.execute("INSERT INTO where_the_truck_vendors VALUES('04/08/2018', 'John Smith','Asada', '04/11/2018','11:30 am', '02:30 pm','Cleveland Park', '80 Washington Street', 'Greenville', 'SC', '29603', 'jsmith@gmail.com');")
cursor.execute("INSERT INTO where_the_truck_vendors VALUES(%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s);",(submission_date,customer_name,food_truck_name,serving_date, starting_time, ending_time, location_name, street_address, city, state, zipcode, email))
connection.commit()

cursor.close()
connection.close()

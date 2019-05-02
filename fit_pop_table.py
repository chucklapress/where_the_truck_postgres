import psycopg2

connection = psycopg2.connect("dbname=fit_pop user=chucklapress")

cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS fit_pop_listing")
table_create_command = """CREATE TABLE fit_pop_listing (
  submissiondate varchar(30),
  vendorname varchar(100),
  eventdate varchar(10),
  startingtime varchar(20),
  endingtime varchar(20),
  locationname varchar(30),
  streetaddress varchar(40),
  city varchar(30),
  state varchar(20),
  zipcode varchar(7),
  description text
);"""

cursor.execute(table_create_command)
submissiondate ='05/02/2019'
vendorname ='Barre studio one'
eventdate = '05/03/2019'
startingtime ='10:00 am'
endingtime ='02:00 pm'
locationname ='Next on Main'
streetaddress ='101 Main Street'
city ='Greenville'
state ='SC'
zipcode ='29601'
description ='Lengthy routine that will focus on each core region'

cursor.execute("INSERT INTO fit_pop_listing VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",(submissiondate,vendorname,eventdate,startingtime,endingtime,locationname,streetaddress,city,state,zipcode,description))
connection.commit()

cursor.close()
connection.close()

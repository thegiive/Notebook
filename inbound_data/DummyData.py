# it is PySpark juypter code dump
df = spark.read.load("flight_data/Flight_B6833_(10a2028c).csv",
                     format="csv", sep=",", inferSchema="true", header="true")
df.count()
df = spark.read.load("flight_data/",
                     format="csv", sep=",", inferSchema="true", header="true")
df.count()
df.show()
from pyspark.sql.functions import split
new_df = df.select(df.UTC.alias("time"),df.Callsign.alias("flight_no"),split(df.Position, ',')[0].alias("lat"),split(df.Position, ',')[1].alias("lon"))
new_df.show()
new_df.write.mode('overwrite').save("flight.json",  format="json")


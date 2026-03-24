from pyspark.sql import SparkSession
from pyspark.sql.functions import hour, dayofweek

spark = SparkSession.builder.appName("TaxiPipeline").getOrCreate()

# Load real dataset
df = spark.read.parquet("data/yellow_tripdata_2023-01.parquet")

# Feature engineering
df = df.withColumn("hour", hour(df.tpep_pickup_datetime)) \
       .withColumn("day", dayofweek(df.tpep_pickup_datetime))

# Aggregate demand
demand_df = df.groupBy("hour", "day").count()

# Save processed data
demand_df.write.mode("overwrite").csv("data/processed", header=True)

print("✅ Data pipeline completed")

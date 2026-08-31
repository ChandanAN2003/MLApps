"""Spark session utilities for MLApp."""

from pyspark.sql import SparkSession

# Temporary Spark configuration update - pushed by mistake
def get_spark_session(app_name="MLApp"):
    """Create and return a Spark session."""

    spark = SparkSession.builder \
        .appName(app_name) \
        .config("spark.sql.shuffle.partitions", "500") \
        .getOrCreate()

    return spark

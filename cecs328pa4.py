from pyspark.sql import SparkSession
import os
import glob

def sort_csv(input_csv_filename, output_csv_filename, num_partitions):
    # Create SparkSession
    spark = SparkSession.builder \
        .master('local[*]') \
        .config("spark.driver.memory", "15g") \
        .appName('SortLargeCSVParallel') \
        .getOrCreate()
    
    try:
        # Read the CSV file into a DataFrame
        df = spark.read \
            .option("header", "true") \
            .option("inferSchema", "true") \
            .csv(input_csv_filename)
        
        sorted_df = df.repartition(num_partitions, "column_1")
        
        # Sort the DataFrame by column_1
        sorted_df = sorted_df.orderBy("column_1")
        
        temp_dir = "temp_output_dir"
        sorted_df.coalesce(1).write.option("header", True).csv(temp_dir, mode="overwrite")
        
        # Move the single output file to desired output filename
        part_file = glob.glob(os.path.join(temp_dir, "part-*.csv"))[0]
        os.rename(part_file, output_csv_filename)

    finally:
        # Stop the SparkSession
        print(f"CSV file sorted using {num_partitions} partitions and saved to {output_csv_filename}")
        spark.stop()
from pyspark import SparkContext
import os
os.environ["PYSPARK_PYTHON"] = "D:/Software/Python/Python/Python37/python.exe"
#D:\Software\Python\Python\Python37

# Create a SparkContext
sc = SparkContext("local[*]", "SB")

# Load text file
rdd1 = sc.textFile("C:/Users/ADMIN/Desktop/Big Data/abc.txt")
#####C:\Users\ADMIN\Desktop\Big Data
# Split each line into words
rdd2 = rdd1.flatMap(lambda x: x.split(" "))

# Map each word to (word, 1)
rdd3 = rdd2.map(lambda x: (x, 1))

# Reduce by key to count occurrences of each word
rdd4 = rdd3.reduceByKey(lambda x, y: x + y)

# Collect and print the results
for word, count in rdd4.collect():
    print(word, count)
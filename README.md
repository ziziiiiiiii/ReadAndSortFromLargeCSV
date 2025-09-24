This project was made for CECS 328 at CSULB. It is written in Python. It utilizes PySpark to read arbitrary numbers from a large .csv file (in this case 2 GB) and sort them by column 1 using a number of partitions determined by the user. For a test run, the user can choose 10 partitions. These partitions are recombined into a singular .csv file which is saved to the user's drive. For a file of size 2GB or less, this process occurs in less than 2 minutes.

The sorted .csv file is stored at the same path as the original .csv file.

The sample .csv file is too big to upload to github, so it can be found here: https://drive.google.com/file/d/1mY2VbmScKJP_bwOjlwxxkR4-4wWhFmSb/view?usp=sharing. This program can also be run with any .csv file featuring numbers ordered by columns with numbers in column 1.

To run the program, PySpark must be installed and launched from cmd or PowerShell before the program can be run. Installation instruction for PySpark can be found here: https://medium.com/@deepaksrawat1906/a-step-by-step-guide-to-installing-pyspark-on-windows-3589f0139a30. The official PySpark documentation can be found here: https://spark.apache.org/docs/latest/api/python/.

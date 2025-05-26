This project was made for CECS 328 at CSULB. It is written in Python. It utilizes PySpark to read arbitrary numbers from a large .csv file (in this case 2 GB) and sort them by column 1 using partitions. These partitions are recombined into a singular .csv file which is saved to the user's drive. This process occurs in less than 2 minutes.

The sorted .csv file is stored in the same path as the original .csv file.

The .csv file is too big to upload to github, so it can be found here: https://drive.google.com/file/d/1mY2VbmScKJP_bwOjlwxxkR4-4wWhFmSb/view?usp=sharing. This program can also be run using any .csv file with numbers ordered by columns with numbers in column 1.

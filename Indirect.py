import csv
import os

# Assign a variable for the file to load and the path.
file_to_save = os.path.join("analysis", "election_results.txt")

#Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:

    #Write some data to the file
    txt_file.write("Counties in the Election\n-----------------\nArapahoe\nDenver\nJefferson")
"""
.. moduleauthor:: Mathias Schuh <mathias.schuh@hotmail.com>
"""

from os import path
import csv

sum = 0
file_path = path.abspath(__file__) #path holen
dir_path = path.dirname(file_path) #directory holen
dir_path1 = dir_path + '/' + 'andr.vi.csv'


with open (dir_path1) as csvdatei:
    csv_reader_object = csv.reader(csvdatei)


    for row in csv_reader_object:
        sum += float(row[-3])

avg = sum / 294.65


print(f' File to analyze: The average closing price was {avg:.2f}.')

a = float(row[-3])
#b = a - avg
print(f'The most recent closing price ({a:.2f}) was above the average.')
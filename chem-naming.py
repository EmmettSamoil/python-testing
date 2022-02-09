#Project to help with naming chemistry stuff
import csv
file = open('PeriodicTable.csv')
type(file)
csvreader = csv.reader(file)

eleFirst = input('Enter your First Element: ')
eleSecond = input('Enter your Second Element: ')


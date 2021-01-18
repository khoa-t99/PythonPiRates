import json 
import csv 
  
import A_people as As
df = As.read_json (r'Path where the JSON file is saved\A_people.json')
df.to_csv (r'Path where the new CSV file will be stored\A_people.csv', index = None)

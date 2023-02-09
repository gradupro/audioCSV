import json
import glob
from datetime import datetime
import csv

# Place your JSON data in a directory named 'data/'
src = "data/"

date = datetime.now()
data = []

# Change the glob if you want to only look through files with specific names
files = glob.glob('data/*', recursive=True)

# Loop through files

for single_file in files:
    with open(single_file, 'r') as f:

        # Use 'try-except' to skip files that may be missing data
        try:
            json_file = json.load(f)
            data.append([
                json_file['audio']['fileSize'],
                json_file['audio']['duration'],
                json_file['annotations'][0]['audio_id'],
                json_file['annotations'][0]['area']['start'],
                json_file['annotations'][0]['area']['end'],
                json_file['annotations'][0]['categories']['category_01'],
                json_file['annotations'][0]['categories']['category_02'],
                json_file['annotations'][0]['categories']['category_03'],
                json_file['annotations'][0]['note'],
                json_file['annotations'][0]['audioType'],
                json_file['annotations'][0]['gender'],
                json_file['annotations'][0]['generation'],
                json_file['annotations'][0]['dialect'],
            ])
        except KeyError:
            print(f'Skipping {single_file}')

# Sort the data
data.sort()

# Add headers
data.insert(0, ['fileSize', 'duration', 'audio_id', 'area_start', 'area_end',
            'category_01', 'category_02', 'category_03', 'note', 'audioType', 'gender', 'generation', 'dialect'])

# Export to CSV.
# Add the date to the file name to avoid overwriting it each time.
csv_filename = '도움요청,실외.csv'
with open(csv_filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("Updated CSV")

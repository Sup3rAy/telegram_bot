import csv
import subprocess
import json


def get_ulr(name):
    url = f"https://hotleak.vip/{name}"
    cmd = ["gallery-dl", "--get-urls", "--filter", "extension in ('mp4')", url]

    result = subprocess.run(cmd, capture_output=True, text=True)

    output = result.stdout

    urls = output.strip().split("\n")

    video_urls = []
    for url in urls:
        if 'ytdl' in url:
            substring = url[5:]
            video_urls.append(substring)
    return video_urls


csv_file = "output.csv"


data = []


with open(csv_file, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row[0])

model_data = {}
num = 0
for model in data :
    num += 1
    print(f"model{num}")
    links = get_ulr(model)

    model_data[model] = links

with open("model_data.json", "w") as f:
    json.dump(model_data, f, indent=1)

import json
import shutil
import subprocess
import cv2
import requests
import glob
import pandas
import os
import telegraph
import csv


class Getlink():
    def __init__(self,url):
        self.url = url
        self.folder_name =url[20:]

    def get_url(self):
        dir_path = f"short_links"

        # Create the directory if it doesn't exist
        os.makedirs(dir_path, exist_ok=True)

        urls = []
        images_path = glob.glob(f"photos/watermark/{self.folder_name}/*.*")

        for path in images_path:

            url = self.file_upload(path)

            urls.append(url)

        df = pandas.DataFrame(urls)
        df.to_csv(f"short_links/{self.folder_name}.csv", index=False, header=False)
        delete = f"photos/watermark/{self.folder_name}"

        # Delete the directory and its contents
        try:
            shutil.rmtree(delete)
        except OSError as e:
            pass


    def file_upload(self,path_to_file):
        '''
        Sends a file to telegra.ph storage and returns its url
        Works ONLY with 'gif', 'jpeg', 'jpg', 'png', 'mp4'

        Parameters
        ---------------
        path_to_file -> str, path to a local file

        Return
        ---------------
        telegraph_url -> str, url of the file uploaded

        #
        https://telegra.ph/file/16016bafcf4eca0ce3e2b.jpg
        #>>>telegraph_file_upload('untitled.txt')
        error, txt-file can not be processed
        '''
        file_types = {'gif': 'image/gif', 'jpeg': 'image/jpeg', 'jpg': 'image/jpg', 'png': 'image/png',
                      'mp4': 'video/mp4'}
        file_ext = path_to_file.split('.')[-1]

        if file_ext in file_types:
            file_type = file_types[file_ext]
        else:
            return f'error, {file_ext}-file can not be proccessed'

        with open(path_to_file, 'rb') as f:
            url = 'https://telegra.ph/upload'
            response = requests.post(url, files={'file': ('file', f, file_type)})
        telegraph_url = json.loads(response.content)
        telegraph_url = telegraph_url[0]['src']
        telegraph_url = f'https://telegra.ph{telegraph_url}'

        return telegraph_url





    def logo(self):
        logo = cv2.imread("logo/prenses.png")

        h_logo, w_logo, _ = logo.shape

        images_path = glob.glob(f"photos/hotleak/{self.folder_name}/*.*")
        dir_path = f"photos/watermark/{self.folder_name}"
        # Create the directory if it doesn't exist
        os.makedirs(dir_path, exist_ok=True)
        for image in images_path:
            img = cv2.imread(image)
            h_img, w_img, _ = img.shape
            top_y = 0
            left_x = 0

            bottom_y = top_y + h_logo
            right_x = left_x + w_logo

            roi = img[top_y: bottom_y, left_x: right_x]
            result = cv2.addWeighted(roi, 1, logo, 1, 0)
            img[top_y: bottom_y, left_x: right_x] = result
            filename = os.path.basename(image)
            dir_path = f"photos/watermark/{self.folder_name}"

            # Create the directory if it doesn't exist
            os.makedirs(dir_path, exist_ok=True)
            cv2.imwrite(f"{dir_path}/{filename}", img)
        delete = f"photos/hotleak/{self.folder_name}"

        # Delete the directory and its contents
        try:
            shutil.rmtree(delete)
        except OSError as e:
            pass


    def download(self):
        dir_path = "photos/"

        # Create the directory if it doesn't exist
        os.makedirs(dir_path, exist_ok=True)

        image_range = "1-15"

        # Gallery-dl command to download images in the specified range
        cmd = ["gallery-dl", "--range", image_range, "--filter", "extension in ('jpg', 'png', 'gif')", "-d", dir_path,self.url]

        # Execute the command using subprocess
        subprocess.run(cmd)


    def telegraph_page(self):
        # open the CSV file in read mode
        with open(f'short_links/{self.folder_name}.csv', 'r') as file:
            # create a csv reader object
            csv_reader = csv.reader(file)

            # initialize an empty list to store the contents of the CSV file
            data = []

            # iterate over each row in the CSV file
            for row in csv_reader:
                # convert each row to a list and extend the data list with the resulting list
                data.extend(list(row))

            # print the contents of the list
        video = self.get_video()
        htmlv="Here is a few model's videos💖<p><a href=" ">💖</a></p>"
        num = 0
        for vid in video:
            num += 1
            h=f'<p><a href="{vid}">{num}.Video</a></p>'
            htmlv += h


        ACCESS_TOKEN = '41e2418735b90c9c51a34c44942b300bd051ae0fb13ec6ed4d3f05dac444'
        AUTHOR_NAME = 'With love 💖OnflyfansFree💖'
        AUTHOR_URL = 'https://t.me/OnlyfansFree_chanel'

        avatar_url = self.file_upload(f"avatar/{self.folder_name}.jpg")
        telegraph_api = telegraph.Telegraph(access_token=ACCESS_TOKEN)
        html_content = f'<p><a href="{AUTHOR_URL}">{AUTHOR_NAME}</a> <p><img src="{avatar_url}" /></p>' \
               f'<p><img src="{"need_url"}" /></p></p>'
        html_img = self.html(data)
        page = telegraph_api.create_page(
            title=f'{self.folder_name} ⭐️⭐️⭐️⭐️⭐️',
            html_content=html_content + htmlv + html_img
        )

        # Print the URL of the newly created page
        url = page['url']


        with open('models.json', 'r') as file:
            # Load the existing JSON data into a Python dictionary
            data = json.load(file)

        # Add new data to the dictionary
        data[self.folder_name] = url

        # Open the same file for writing
        with open('models.json', 'w') as file:
            # Write the updated dictionary back to the JSON file
            json.dump(data, file, indent=4, ensure_ascii=False)
        delete = f"short_links"

        # Delete the directory and its contents
        try:
            shutil.rmtree(delete)
        except OSError as e:
            pass




    def html(self,list):
        lis = []

        for link in list:
            lis.append(f'<p><img src="{link}" /></p>')
        html = ''.join(lis)

        return html

    def get_video(self):

        range = "1-5"
        cmd = ["gallery-dl", "--get-urls", "--range", range, "--filter", "extension in ('mp4')", self.url]

        result = subprocess.run(cmd, capture_output=True, text=True)

        output = result.stdout

        urls = output.strip().split("\n")

        video_urls = []
        for url in urls:
            if 'ytdl' in url:
                substring = url[5:]
                video_urls.append(substring)
        return video_urls





    def one_step(self):
        self.download()
        self.logo()
        self.get_url()
        self.telegraph_page()
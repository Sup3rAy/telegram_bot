import json
import random
import requests
from bs4 import BeautifulSoup

class Stuff():
    def __init__(self,):
        self.random = "is it important?"

    def random_link(self):
        with open("models.json") as file:
            new_dict = json.load(file)

        # get a list of keys from the dictionary
        keys = list(new_dict.keys())

        # shuffle the list of keys
        random.shuffle(keys)

        # get the first 5 keys from the shuffled list
        random_keys = keys[:5]

        # get the values from the dictionary using the random keys
        random_values = [new_dict[key] for key in random_keys]

        return random_values

    def hot_models(self):
        model_list=[]
        
        url = f'https://hotleak.vip/'
        response = requests.get(url=url).text
        soup = BeautifulSoup(response, "lxml")
        models = soup.find_all('span', class_="date")
        for i in range(7):
            model_list.append(models[i].text)
        return model_list



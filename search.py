import csv
import json
import random
class Search():
    def __init__(self,word):
        self.word = word




    def search(self):
        csv_file = "output.csv"

        # Create an empty list to store the data
        data = []
        can_be_list =[]
        # Open the CSV file in read mode and read the data
        with open(csv_file, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row[0])

        # Print the data as a list

        for name in data:
            if self.word in name:
                can_be_list.append(name)


        if len(can_be_list)==1:
            self.word = can_be_list[0]
        elif len(can_be_list) ==2:
            new_list = []
            if can_be_list[0] in can_be_list[1]:
                new_list.append(can_be_list[0])
                can_be_list = new_list
                self.word = can_be_list[0]
            elif can_be_list[1] in can_be_list[0]:
                new_list.append(can_be_list[1])
                can_be_list = new_list
                self.word = can_be_list[0]


        return can_be_list


    def look(self):
        with open("models.json") as file:
            new_dict = json.load(file)

        if self.word in new_dict:
            return True
        else:
            return False



    def send_link(self):
        search_name = self.word

        with open("models.json") as file:
            new_dict = json.load(file)

        if search_name in new_dict:
            return new_dict[search_name]






import json
from pathlib import Path

class Person:
    def __init__(self,username,link):
        self.username=username
        self.link=link
        
    def __str__(self):
        return f"{self.username} -> {self.link}\n" #default string
     

def add_to_list(data,list,mode):
    #goes through every person in the file and gets their name
    if mode=="following":
        for person in data:
            for item in person.get("string_list_data", []):
                username = item.get("value")
                link = item.get("href")
                list.append(Person(username,link)) #adds the person's username and link to the list
    else:
        for person in data:
            for item in person.get("string_list_data", []):
                username = item.get("value")
                list.append(username) #adds the person's username to the list

def get_paths():
    folder_path = Path(__file__).parent #finds where the script is located
    json_folder = folder_path / 'connections/followers_and_following' #where the files containing the information are located
    return json_folder


def loop_through_files(json_folder):
    list_followers,list_following=[],[]
    #loop through all .json files
    for file_path in json_folder.glob("*.json"):
        #checks if the file corresponds to the people who follow the user
        if file_path.name=="followers_1.json":
            #opens the file in read-mode
            with file_path.open('r', encoding='utf-8') as json_file:
                try:
                    data = json.load(json_file)  #loads the data from the json file
                    add_to_list(data,list_followers,"followers")
                    
                except json.JSONDecodeError as e:
                    print(f"Error decoding followers_1.json: {e}")
                    
        #checks if the file corresponds to the people who the user follows
        if file_path.name=="following.json":
            #opens the file in read-mode
            with file_path.open('r', encoding='utf-8') as json_file:
                try:
                    following = json.load(json_file)  #loads the data from the json file
                    data = following.get("relationships_following",[])
                    add_to_list(data,list_following,"following")
                    
                except json.JSONDecodeError as e:
                    print(f"Error decoding following.json: {e}")
                    
    return list_followers,list_following


def dont_follow_back(list_followers,list_following):
    count=0           
    #creates a txt file in  the directory named peopleWhoDontFollowYouBack 
    with open('peopleWhoDontFollowYouBack.txt', 'w') as file:
        for person in list_following:
            if person.username not in list_followers:
                count+=1
                file.write(f"{count}: {str(person)}")
                #each line on the file will look like this: 
                # {number}: {username} -> {link}
        


def main():
    json_folder = get_paths() #where the files containing the information are located
    list_followers,list_following=loop_through_files(json_folder) #creates the lists containg both the followers as well as the following
    dont_follow_back(list_followers,list_following)

main()
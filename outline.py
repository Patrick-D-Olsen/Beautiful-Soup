# import beautifulsoup and request here
from bs4 import BeautifulSoup
import requests
import json


def displayJobDetails():
    print("Display job details")


# function to get job list from url 'https://www.monster.com/jobs/search?q={role}&where={location}'
def getJobList(role, location):

    url = 'https://www.monster.com/jobs/search?q={role}&where={location}'
    
    #response = requests.request("GET", url, headers=headers, data=payload)
    response = requests.get(url)

    print(response.text)

    # save data in JSON file

def saveDataInJSON(jobDetails):
    # Complete the missing part of this function here
    print("Saving data to JSON")


# main function
def main():
    # Get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()
    print("Enter location you want to search")
    location = input()

    # Print verification to user
    print("\nYour role is \"" + role +
          "\" and your location is \"" + location + "\".\n")

    # run getJobList
    getJobList(role, location)


if __name__ == '__main__':
    main()

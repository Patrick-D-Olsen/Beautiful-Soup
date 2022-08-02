# import beautifulsoup and request here
import requests


def displayJobDetails():
    print("Display job details")


# function to get job list from url 'https://www.indeed.com/jobs?q={role}&l={location}'
def getJobList(role, location):
    url = 'https://www.indeed.com/jobs?q={role}&l={location}'
    # Complete the missing part of this function here
    #url = "https://www.indeed.com/jobs?q=Software Developer&l=Charlotte"

    payload = {}
    headers = {
        'Cookie': 'CTK=1g9f9gc0ui7n4800; __cf_bm=rLC4cc.qWtc8NLgrGHHR7OgNqOiVxfhXfjm49jzYs1k-1659444408-0-AWH3gYigIG1/P0ndHehaDIRo01mlEdsJKc0SrnM2L/qoiB04DHhbDzRCgyx3GER1n6h3wlJCURbLYlP2usBrLaM=; _cfuvid=1yfTSHo3at37gTupJBr49bzOzFign.QuguxsdlqGECo-1659444408369-0-604800000; CMP_VISITED=1; INDEED_CSRF_TOKEN=S6ZC096E49XyRHxaxbZbPVekX3lXidQ3; JSESSIONID=BEFE39AD91F360EA0CF4157838A4BE21; LV="LA=1659444408:CV=1659444408:TS=1659444408"; PREF="TM=1659444408469:L=Charlotte"; RQ="q=Software+Developer&l=Charlotte&ts=1659444408496"; UD="LA=1659444408:CV=1659444408:TS=1659444408:SG=92dc7ca71441a235b5684f1b04a1deda"; indeed_rcc=CTK; jaSerpCount=1; mdserp=1'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

    # save data in JSON file


def saveDataInJSON(jobDetails):
    # Complete the missing part of this function here
    print("Saving data to JSON")


# main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()
    # Complete the missing part of this function here
    print("Enter location you want to search")
    location = input()

    getJobList(role, location)


if __name__ == '__main__':
    main()

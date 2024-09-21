import requests
from bs4 import BeautifulSoup
print("This is a Web Scrapping Tools")
website_address = input("Paste the link of website")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(website_address,headers=headers) #fetching data from request
soup = BeautifulSoup(response.text,'html.parser')
choice = input("do you want to save Default Name \t Y/N")
if(choice == 'y' or 'Y'):
    file_name = soup.title.string.replace(" ","_")+'.html'
else:
    file_name = input("Enter new file Name")

with open(file_name,'w') as file:
    file.write(soup.prettify())
print(f"{file_name} saved , {website_address} of scrapped data") 
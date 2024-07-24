import requests 
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

def get_links(subject):
    subj_in_site = website.find(string=subject)
    module = subj_in_site.parent.parent.parent
    links = module.find_all("a")
    return links

def download(filename, link):
    url = f"https://www.education.gov.za{link['href']}"
    urlretrieve(url, f"{filename} {year}.pdf")
    print(f"Done Downloading {filename}")

LANGUAGES = ["Afrikaans", "English"] #TODO: 
OTHER = [ "Business Studies", "Computer Applicaitons Technology", "Geography", "Life Sciences", "Mathematical Literacy", "Mathematics", "Physical Science"] # TODO: "Accounting", 
FOLDER = r"C:\Users\rahil\OneDrive\Desktop\Coding\Python\Automation"

year = 2008 # TODO
website_url = "https://www.education.gov.za/NSCNovember2008ExamPapers.aspx" # TODO
result = requests.get(website_url, verify=False)
website = BeautifulSoup(result.text, "html.parser")

# !DOWNLOADING PAPERS
for subject in LANGUAGES:
    links = get_links(subject)
    for link in links:
        name = link.string
        if "FAL" in name and subject==LANGUAGES[0]:
            download(name, link)
        if "HL" in name and subject==LANGUAGES[1]:
            download(name, link)

for subject in OTHER:
    links = get_links(subject)
    for link in links:
        name = f"{link.string}" 
        if "English" in name or "english" in name:
            download(name, link)

print("DONE")
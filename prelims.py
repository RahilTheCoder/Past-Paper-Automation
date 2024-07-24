import requests 
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

def get_links(subject):
    subj_in_site = website.find(string=subject)
    module = subj_in_site.parent.parent.parent
    links = module.find_all("a")
    return links

def download(filename, link):
    url = fr"https://education.gauteng.gov.za{link['href']}"
    urlretrieve(url.replace(' ', "%20"), f"{filename} {year}.pdf")
    print(f"Done Downloading {filename}")

LANGUAGES = ["Afrikaans", "English"] #TODO: 
OTHER = [ "Business Studies", "Computer Applicaitons Technology", "Geography", "Life Sciences", "Mathematical Literacy", "Mathematics", "Physical Science"] # TODO: "Accounting", 
FOLDER = r"C:\Users\rahil\OneDrive\Desktop\Coding\Python\Automation"

year = 2023 # TODO
website_url = "https://education.gauteng.gov.za/pages/Exam-Papers.aspx?RootFolder=%2FExam%20Papers%2FGrade%2012%2F2023%2FGrade%2012%20NSC%20Preparatory%20Examination%20Question%20Papers&FolderCTID=0x0120006FDCC5CC7E09AA4C974C7BA11E801683&View=%7BC0BB08B9%2DC2E9%2D4E23%2DB332%2D081E682B78CF%7D" # TODO
result = requests.get(website_url, verify=False)
website = BeautifulSoup(result.text, "html.parser")

# !DOWNLOADING PAPERS
for subject in LANGUAGES:
    links = website.find_all("a")
    for link in links:
        name = f"{link.string}" 
        if subject in name:
            if "FAL" in name and subject==LANGUAGES[0]:
                download(name, link)
            if "HL" in name and subject==LANGUAGES[1]:
                download(name, link)

for subject in OTHER:
    links = website.find_all("a")
    for link in links:
        name = f"{link.string}" 
        if subject in name:
            if "English" in name or "english" in name:
                download(name, link)

print("DONE")
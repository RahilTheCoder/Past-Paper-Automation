# DOWNLOAD CAT DATA FILES AND LO

import requests 
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

def get_links(subject):
    subj_in_site = website.find(string=subject)
    module = subj_in_site.parent.parent.parent
    links = module.find_all("a")
    return links

def download(filename, link, year, month):
    type = get_type(link)
    if type is None:
        return None
    
    if "octet" in type:
        url = f"https://www.education.gov.za{link['href']}"
        urlretrieve(url, f"{filename} {month} {year}.exe")
    elif "zip" in type:
        url = f"https://www.education.gov.za{link['href']}"
        urlretrieve(url, f"{filename} {month} {year}.zip")
    else:
        url = f"https://www.education.gov.za{link['href']}"
        urlretrieve(url, f"{filename} {month} {year}.pdf")
    print(f"Done Downloading {filename}")

def get_type(link):
    try:
        url = f"https://www.education.gov.za{link['href']}"
        path, headers = urlretrieve(url)
        return headers.get_content_subtype()
    except:
        print(f"{year} {month} failed")
    

NAME_LINK = {'2023 May/June NSC/SC Exam Papers': 'https://www.education.gov.za/LinkClick.aspx?link=https%3a%2f%2fwww.education.gov.za%2fCurriculum%2fNationalSeniorCertificate(NSC)Examinations%2f2023MayJuneExamPapers.aspx&tabid=593&portalid=0&mid=1741', 
'2022 NSC November Examination Papers': 'https://www.education.gov.za/LinkClick.aspx?link=3294&tabid=593&portalid=0&mid=1741', 
'2022 May/June NSC/SC Exam Papers': 'https://www.education.gov.za/LinkClick.aspx?link=https%3a%2f%2fwww.education.gov.za%2fCurriculum%2fNationalSeniorCertificate(NSC)Examinations%2f2022MayJuneExamPapers.aspx+&tabid=593&portalid=0&mid=1741', 
'2021 NSC November Examination Papers': 'https://www.education.gov.za/LinkClick.aspx?link=https%3a%2f%2fwww.education.gov.za%2fCurriculum%2fNationalSeniorCertificate(NSC)Examinations%2f2021NSCExamPapers.aspx&tabid=593&portalid=0&mid=1741', 
'2021 NSC/SC May/June Examinations': 'https://www.education.gov.za/LinkClick.aspx?link=https%3a%2f%2fwww.education.gov.za%2fCurriculum%2fNationalSeniorCertificate(NSC)Examinations%2f2021MayJuneNSCExams.aspx&tabid=593&portalid=0&mid=1741', 
'2020 NSC and SC Exam Papers (November)': 'https://www.education.gov.za/LinkClick.aspx?link=https%3a%2f%2fwww.education.gov.za%2fCurriculum%2fNationalSeniorCertificate(NSC)Examinations%2f2020NSCExamPapers.aspx&tabid=593&portalid=0&mid=1741', 
'2019 NSC Examination Papers (November)': 'https://www.education.gov.za/LinkClick.aspx?link=2556&tabid=593&portalid=0&mid=1741', 
'2019 May/June Examination Papers': 'https://www.education.gov.za/LinkClick.aspx?link=https%3a%2f%2fwww.education.gov.za%2f2019JuneNSCExamPapers.aspx&tabid=593&portalid=0&mid=1741', 
'2018 November NSC Examination Papers': 'https://www.education.gov.za/LinkClick.aspx?link=2268&tabid=593&portalid=0&mid=1741', 
'2018 Grade 12 NSC Supplementary Exams (Feb/March)': 'https://www.education.gov.za/Curriculum/NationalSeniorCertificate(NSC)Examinations/2018SupplementaryExams.aspx',  
'2018 May/June NSC Exam Papers': 'https://www.education.gov.za/LinkClick.aspx?link=2182&tabid=593&portalid=0&mid=1741', 
'2017 November NSC Examination Papers': 'https://www.education.gov.za/Home/2017NSCNovemberpastpapers.aspx', 
'2017 May/June SC(a) Exam Papers': 'https://www.education.gov.za/Curriculum/SeniorCertificate/2017SCMay-JuneExampapers.aspx', 
'2017 Feb/March NSC Exam Papers': 'https://www.education.gov.za/LinkClick.aspx?link=1608&tabid=593&portalid=0&mid=1741', 
'2016 NSC Examinations (Oct/Nov)': 'https://www.education.gov.za/LinkClick.aspx?link=1508&tabid=593&portalid=0&mid=1741', 
'2016 ASC Exam Papers (May/June)': 'https://www.education.gov.za/LinkClick.aspx?link=1375&tabid=593&portalid=0&mid=1741', 
'2016 Feb/March NSC Examination Papers': 'https://www.education.gov.za/Curriculum/NationalSeniorCertificate(NSC)Examinations/PastExamPapers/2016FebMarchNSCExaminationPapers.aspx', 
'2015 November NSC Examination Papers': 'https://www.education.gov.za/Curriculum/NationalSeniorCertificate(NSC)Examinations/PastExamPapers/2015NovemberNSCExamPapers1.aspx', 
'2015 Feb/March NSC Examination Papers': 'https://www.education.gov.za/LinkClick.aspx?link=730&tabid=593&portalid=0&mid=1741', 
'2014 November NSC Examination Papers': 'https://www.education.gov.za/LinkClick.aspx?link=568&tabid=593&portalid=0&mid=1741', 
'2014 Feb/March NSC Examination Papers': 'https://www.education.gov.za/LinkClick.aspx?link=584&tabid=593&portalid=0&mid=1741', 
'2014 Grade 12 NSC Exemplars': 'https://www.education.gov.za/LinkClick.aspx?link=599&tabid=593&portalid=0&mid=1741', 
'2013 November NSC Examination Papers': 'https://www.education.gov.za/LinkClick.aspx?link=607&tabid=593&portalid=0&mid=1741', 
'2013 Feb/March NSC Examination Papers': 'https://www.education.gov.za/LinkClick.aspx?link=610&tabid=593&portalid=0&mid=1741', 
'2012 November NSC Examination Papers': 'https://www.education.gov.za/LinkClick.aspx?link=626&tabid=593&portalid=0&mid=1741', 
'2012 Feb/March NSC Examination Papers': 'https://www.education.gov.za/LinkClick.aspx?link=649&tabid=593&portalid=0&mid=1741', 
'2011 November NSC Examination Papers': 'https://www.education.gov.za/LinkClick.aspx?link=647&tabid=593&portalid=0&mid=1741', 
'2011 Feb/March NSC Examination Papers': 'https://www.education.gov.za/LinkClick.aspx?link=726&tabid=593&portalid=0&mid=1741', 
'2009 November NSC Examination Papers': 'https://www.education.gov.za/LinkClick.aspx?link=677&tabid=593&portalid=0&mid=1741', 
'2008 November NSC Examination Papers': 'https://www.education.gov.za/LinkClick.aspx?link=694&tabid=593&portalid=0&mid=1741'}

for site_name in NAME_LINK:
    other = []
    year = site_name[:4] 
    website_url = NAME_LINK.get(site_name)
    result = requests.get(website_url, verify=False)
    website = BeautifulSoup(result.text, "html.parser")
    
    h2 = website.find_all("h2")

    for headings in h2:
        span = headings.find('span').string
        if "Comp" in span or "Or" in span:
            other.append(span)

    if "Nov" in site_name:
        month = "Nov"
    if "May" in site_name:
        month = "May"
    if 'Feb' in site_name:
        month = "Feb"
    if "Exemplar" in site_name:
        month = "Exemplar"

    for subject in other:
        links = get_links(subject)
        for link in links:
            name = f"{subject} {link.string}" 
            if "Office" in name:
                download(name, link, year, month)
                break
            if ("English" in name or "english" in name) and "Life" in subject:
                download(name, link, year, month)

print("DONE")

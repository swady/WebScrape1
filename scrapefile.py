# import libraries

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Soup

# website url
my_url = 'https://www.tender247.com/keyword/Electric+Vehicle+Tenders#'

uClient = uReq(my_url)
page_html= uClient.read()
uClient.close()
page_soup = Soup(page_html, "html.parser")

containers = page_soup.findAll("tbody",{"id":"tendercontent"})

# destination file 
filename= "g:/......./EVTenders2.csv" 
f = open(filename,"w")
headers = "TenderId, Description, Location, Cost, Date\n"
f.write(headers)

for container in containers:
    for i in range(20):
        tender_ID=container.findAll("td",{"class":"tenderindextd"})
        ID=tender_ID[i].text.split()
        Tender_Desc=container.findAll("p",{"id":"pReqBrief"})
        Desc = Tender_Desc[i].text.strip()
        location=container.findAll("td",{"class":"col-xs-6 col-sm-4 col-md-6 col-lg-7 tenderListingLocation"})
        place = location[i].text.strip()
        price=container.findAll("td",{"class":"text04"})
        costprice= price[i].text.split()
        if(len(costprice)>3):
            pass
        else:
            costprice.append("not")
            costprice.append(" Available")
        date=container.findAll("span",{"style":" color:#ff9600;"})
        Date=date[i].text

        print("Tender Id" + ID[4])
        print("Description = " + Desc)
        print("Location " + place)
        print("Cost " + costprice[0]+costprice[1]+costprice[2])
        print("Date Published " + Date)

        f.write(ID[4].replace(",", " ") + "," + Desc.replace(",", " ") + "," + place.replace(",", ";") + "," + costprice[0]+costprice[1]+costprice[2] + "," + Date + "\n")




f.close()




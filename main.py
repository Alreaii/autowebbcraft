import pnwkit 
import requests
import streamlit as st
from bs4 import BeautifulSoup
import pandas

kit = pnwkit.QueryKit(st.secrets["apikey"]) #add ur own api key here

# 88039652 2022-09-18 16:58:02+00:00 Safekeeping  35000000 0 0 0 0 0 0 0 0 0 0 # example output

allianceId = 10498 #change alliance id here

baseurl = "https://webbcraft.co.uk/pw/pwpei2.php?data=&land=&nation="



allNationsInAllianceList = []
allNationsInAlliance = kit.query("nations", {"alliance_id": allianceId}, "id nation_name").get()
df = pandas.DataFrame(columns=["nationname", "pei", "mil"])

for nation in allNationsInAlliance.nations:
    allNationsInAllianceList.append(nation.id)



def nationInfo(nationId):
    url = baseurl + str(nationId)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    #tr[1] = info row, td[4] = pei, td[1] = nationname
    table = soup.find_all("table")[0]
    table_pei = table.find_all("tr")[1].find_all("td")[4].text
    table_nationname = table.find_all("tr")[1].find_all("td")[1].text
    table_mil = table.find_all("tr")[1].find_all("td")[11].text
    df.loc[len(df)] = [table_nationname, table_pei, table_mil]

for nation in allNationsInAllianceList:
    nationInfo(nation)

st.title("Audit sheet")
st.dataframe(df, width=1024, height=768)
#sum of all pei


st.text(f"Average PEI:", df["pei"].sum()/len(allNationsInAllianceList))
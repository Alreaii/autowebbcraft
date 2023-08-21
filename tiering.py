import pnwkit
import requests
import streamlit as st
from bs4 import BeautifulSoup
import pandas

kit = pnwkit.QueryKit("")

top50aa = kit.query("alliances", 
                    {
                        "first": 50,
                    }, "id name").get()
aalist = []
treaties = []

for alliance in top50aa.alliances:
    aalist.append(alliance.name)

#return list of treaties for every alliance

for alliance in top50aa.alliances:
    q = kit.query("alliances", {"id": alliance.id}, "treaties").get()
    

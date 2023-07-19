import pnwkit
import requests
import streamlit as st
from bs4 import BeautifulSoup
import pandas

kit = pnwkit.QueryKit("26fcc93af7dfda")

top50aa = kit.query("alliances", 
                    {
                        "first": 50,
                    }, "id name").get()
aalist = []
treaties = []

for alliance in top50aa.alliances:
    aalist.append(alliance.name)

print(aalist)
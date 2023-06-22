import math
import requests
from bs4 import BeautifulSoup
import json
import time
import random
import numpy as np

with requests.session() as session:
    response = session.get('https://www.connexservice.com/HolidayPlus_Preview/hotelmap')

    soup = BeautifulSoup(response.content, "html.parser")
    list = soup.find("div", {"id": "hotels-list"})
    hotels = list.find_all("a", {"class": "m-3"})

    for hotel in hotels:
        print(hotel)

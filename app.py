import streamlit as st

# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# import seaborn as sns
from datetime import datetime, date
import pickle


def get_age(date_val):
    today = 2022 + (11 / 12)
    try:
        date_val = date_val.split('-')
        bd = int(date_val[0]) + (int(date_val[1]) / 12)
    except:
        try:
            date_val = date_val.split('/')
            bd = int(date_val[0]) + (int(date_val[1]) / 12)
        except:
            return 28
    return today - bd


def height_inches(h):
    temp = list(map(str, h.split("'")))
    for i in range(len(temp)):
        temp[i] = int(temp[i])

    return temp[0] * 12 + temp[1]


st.title("NFL Player Speed Precition")

st.write("Predicting the Speed of Player for the Whole Week")

age = get_age(st.date_input('Date of Birth of the Player', value = None, min_value=date(1995, 1, 1)))

height = height_inches(st.text_input("Height of the player", value= "0'0"))

weight = st.number_input('Weight of the Player', value=100)


for i in range(7):
    st.title(f"Day {i+1}")

    x = [0]*7
    y = [0]*7
    dis = [0]*7
    o = [0]*7
    dire = [0]*7

    x[i] = st.number_input("X coordinate of the player", value=0.0, key=f"x{i}")
    y[i] = st.number_input("Y coordinate of the player", value=0.0, key=f"y{i}")

    dis[i] = st.number_input("dis of the player", value=0.0, key=f"dis{i}")

    o[i] = st.number_input("o of the player", value=0.0, key=f"o{i}")

    dire[i] = st.number_input("dir of the player", value=0.0, key=f"dire{i}")

arr = {"age": [age]*7, "height_new": [height]*7, "weight": [weight]*7, "x": x, "y": y, "dis": dis, "o": o, "dir": dire}

df = pd.DataFrame(arr)

if st.button("Predict"):
    with open('./models/NFL_Predicting_the speed_of_players_model.pkl', 'rb') as f:
        # load using pickle de-serializer
        d_tree = pickle.load(f)
        result = d_tree.predict(df)

    st.write(result)

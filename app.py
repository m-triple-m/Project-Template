import streamlit as st
import pandas as pd
from PIL import Image

st.title("Video Game Sales Analysis")
st.image('title_image.jpg')
st.header("A Not very long description...")
st.markdown("---")
sidebar = st.sidebar

sidebar.header("Choose your option")
choices = ["View Dataset", "Search Tweets", "Upload Image"]
selOpt = sidebar.selectbox("Choose What to do?", choices)


def viewDataset():
    with st.spinner("Loading Data..."):
        df = pd.read_csv('Pokemon.csv')
        st.dataframe(df)

def getTwitterInput():
    with st.spinner("Loading View... "):
        user_input = st.text_input("Enter Twitter Handle or a hashtag")
        btn = st.button("Search Tweets")

def saveImage():
    img_name = st.text_input("Enter name of Image")
    img_file = st.file_uploader("Upload Your Image")
    if img_file:
        img = Image.open(img_file)
        st.image(img)

    btn = st.button("Save Image")

    if btn:
        try:
            img.save("uploads/"+img_name+".png")
            st.success("Image Saved")
        except:
            st.error('Something went wrong')


if selOpt == choices[0]:
    viewDataset()
elif selOpt == choices[1]:
    getTwitterInput()
elif selOpt == choices[2]:
    saveImage()
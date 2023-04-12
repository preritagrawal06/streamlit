import os
import sys
import pandas as pd
import numpy as np 
import requests

from io import BytesIO
from glob import glob
from PIL import Image, ImageEnhance


import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected=option_menu(
        menu_title=None,
        options=["Home", "Images", "Videos"],
        icons=["house", "camera", "camera-video"],
        
        default_index=0,
        
        styles={
                "container": {"padding": "0!important", "background-color": "violet"},
                "icon": {"color": "red", "font-size": "20px"},
                "nav-link": {
                    "font-size": "15px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "black",
                },
                "nav-link-selected": {"background-color": "purple"},
            },
    )
if selected=="Home":
    # st.set_page_config(f"page_title="My Webpage",page_icon=":tada:",layout="wide"")

    # ---- HEADER SECTION ----
    st.title(f"Hi ! I am Manasa :wave:")
    st.subheader(f"Welcome to my web page. Here you can upload images and videoes according to your choice. You also can provide a caption in the textbox. Please try it yourself and have fun.")

if selected=="Images":
    upload_tab , image_tab = st.tabs([ "Upload", "Image"]) 
    with upload_tab:
        image= st.file_uploader("Upload image", type=["png","jpg"])
        if image is not None:
            st.image(image)


    with image_tab:
        picture = st.camera_input(f"Take a picture")
        if picture:
            st.image(picture)

    title = st.text_input('caption', ' ')
    st.write(' ', title)

if selected=="Videos":
    upload_tab, video_tab = st.tabs(["Upload", "video"]) 
    with upload_tab:
        video= st.file_uploader("Upload video", type="mp4")
        if video is not None:
            st.video(video)

    with video_tab:
        video = st.camera_input(f"Take a video")
        if video:
            st.video(video)        
    title = st.text_input('caption', ' ')
    st.write(' ', title)      
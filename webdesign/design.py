import helpfunctions.designfunctions as design_functions
import streamlit as st
import pandas as pd
import threading
import os
from datetime import datetime
import csv
import datetime as dt
import time
import scraper.facebook_scraper as facebookscrape


def scraper_option():
    facebook_page = st.text_input('enter facebook page url here', '')
    if st.sidebar.button('Click here to start scraper'):
        st.write("Started scraper")
        url = facebook_page
        facebookscrape.main_scraper(url)
        

def selection_sidebar_1(sidebar_1_selected_option):
    sidebar_1_options = {"Scrape": scraper_option}
    sidebar_1_options.get(sidebar_1_selected_option)()


def select_option():
    sidebar_1_selected_option = st.sidebar.selectbox('what would you like to do', ("Scrape", "Load csv files", "Set scraper scheduling", "Bevakningar"))
    selection_sidebar_1(sidebar_1_selected_option)

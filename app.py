import calendar  # Core Python Module
from datetime import datetime  # Core Python Module

import streamlit as st  # pip install streamlit
import plotly.graph_objects as go  # pip install plotly


# ----------------- SETTINGS -----------------
incomes = ["Salary", "Blog", "Other Income"]
expenses = ["Rent", "Utilities", "Groceries", "Car", "Other Expenses", "Saving"]
currency = "INR"
page_title = "Income and Expense Tracker"
page_icon = ":money_with_wings:"  # https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"
# --------------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

# --- DROP DOWN VALUES FOR SELECTING THE PERIOD ---
years = [datetime.today().year(), datetime.today().year - 1]
months = list(calendar.month_name[1:])

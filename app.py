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
years = [datetime.today().year, datetime.today().year - 1]
months = list(calendar.month_name[1:])


# --- INPUT & SAVE PERIODS ---
st.header(f"Data Entry in {currency}")
with st.form("entry_form", clear_on_submit=True):
    col_month, col_year = st.columns(2)
    col_month.selectbox("Select Month:", months, key="month")
    col_year.selectbox("Select Year:", years, key="year")

    "___"
    with st.expander("Income"):
        for income in incomes:
            st.number_input(f"{income}:", min_value=0, format="%i", step=10, key=income)
    with st.expander("Expenses"):
        for expense in expenses:
            st.number_input(f"{expense}:", min_value=0, format="%i", step=10, key=expense)
    with st.expander("Comment"):
        st.text_area("", placeholder="Enter a comment here ...")

    "___"
    submitted = st.form_submit_button("Save Data")
    if submitted:
        period = str(st.session_state["year"]) + "_" + str(st.session_state["month"])
        incomes = {income: st.session_state[income] for income in incomes}
        expenses = {expense: st.session_state[expense] for expense in expenses}
        # TODO: Insert values into database
        st.write(f"incomes: {incomes}")
        st.write(f"expenses: {expenses}")
        st.success("Data saved!")


# --- PLOT PERIODS ---
st.header("Data Visualization")
with st.form("saved_periods"):
    # TODO: Get periods from database
    period = st.selectbox("Select Period:", ["2022_January"])
    submitted = st.form_submit_button("Plot Period")
    if submitted:
        # TODO: Get data from database
        comment = "Some comment"
        incomes = {"Salary": 100, "Blog": 20, "Other Income": 50}
        expenses = {"Rent": 10, "Utilities": 10, "Groceries": 10, "Car": 20, "Other Expenses": 30, "Saving": 10}

        # Create metrics
        total_income = sum(incomes.values())
        total_expense = sum(expenses.values())
        remaining_budget = total_income - total_expense
        col_income, col_expense, col_budget = st.columns(3)
        col_income.metric("Total Income", f"{total_income} {currency}")
        col_expense.metric("Total Expense", f"{total_expense} {currency}")
        col_budget.metric("Remaining Budget", f"{remaining_budget} {currency}")
        st.text(f"Comment: {comment}")

        # Create sankey chart
        label = list(incomes.keys()) + ["Total Income"] + list(expenses.keys())
        source = list(range(len(incomes))) + [len(incomes)] * len(expenses)
        target = [len(incomes)] * len(incomes) + [label.index(expense) for expense in expenses]
        value = list(incomes.values()) + list(expenses.values())

        # Data to dict, dict to sankey
        link = dict(source=source, target=target, value=value)
        node = dict(label=label, pad=20, thickness=30, color="#E694FF")
        data = go.Sankey(link=link, node=node)

        # Plot it!
        fig = go.Figure(data)
        fig.update_layout(margin=dict(l=0, r=0, t=5, b=5))
        st.plotly_chart(fig, use_container_width=True)

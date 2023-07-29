import os

from deta import Deta  # pip install deta
from dotenv import load_dotenv  # pip install python-dotenv

# Load the environment variables
load_dotenv()
DETA_KEY = os.getenv("DETA_KEY")

# Initialize with a project key
deta = Deta(DETA_KEY)

# Connect to database
db = deta.Base("expense_tracker")


def insert_period(period, incomes, expenses, comment):
    """Return the report on a successful creation, otherwise raises an error"""
    return db.put(
        {"key": period, "incomes": incomes, "expenses": expenses, "comment": comment}
    )


def fetch_all_periods():
    """Returns a dict of all periods"""
    res = db.fetch()
    return res.items


def get_period(period):
    """If not found, the function will return None"""
    return db.get(period)


def get_all_periods():
    items = fetch_all_periods()
    periods = [item["key"] for item in items]
    return periods

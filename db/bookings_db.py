from pydantic import BaseModel
from datetime import date, timedelta

class BookingsInDB(BaseModel):
  boo_id: int = 0
  boo_cli_id: int
  boo_dateIN: date
  boo_dateOUT: date
  boo_roo_id: int
  boo_name_roo: str
  boo_rec_id: int
  boo_price_charged: int

database_bookings = [
  {
    "boo_id": 1,
    "boo_cli_id": 1,
    "boo_dateIN": "2020-12-01",
    "boo_dateOUT": "2020-12-19",
    "boo_roo_id": 1,
    "boo_name_roo": "A11",
    "boo_rec_id": 1,
    "boo_price_charged": 90000
  },
  {
    "boo_id": 2,
    "boo_cli_id": 1,
    "boo_dateIN": "2020-12-12",
    "boo_dateOUT": "2020-12-16",
    "boo_roo_id": 1,
    "boo_name_roo": "A12",
    "boo_rec_id": 1,
    "boo_price_charged": 90000
  },
  {
    "boo_id": 3,
    "boo_cli_id": 1,
    "boo_dateIN": "2020-12-12",
    "boo_dateOUT": "2020-12-18",
    "boo_roo_id": 1,
    "boo_name_roo": "A13",
    "boo_rec_id": 1,
    "boo_price_charged": 90000
  },
  {
    "boo_id": 4,
    "boo_cli_id": 1,
    "boo_dateIN": "2020-12-12",
    "boo_dateOUT": "2020-12-16",
    "boo_roo_id": 3,
    "boo_name_roo": "C12",
    "boo_rec_id": 1,
    "boo_price_charged": 90000
  },
  {
    "boo_id": 5,
    "boo_cli_id": 1,
    "boo_dateIN": "2020-12-12",
    "boo_dateOUT": "2020-12-18",
    "boo_roo_id": 2,
    "boo_name_roo": "B13",
    "boo_rec_id": 1,
    "boo_price_charged": 90000
  },
  {
    "boo_id": 6,
    "boo_cli_id": 1,
    "boo_dateIN": "2020-12-12",
    "boo_dateOUT": "2020-12-18",
    "boo_roo_id": 2,
    "boo_name_roo": "B13",
    "boo_rec_id": 1,
    "boo_price_charged": 90000
  }
]

generator = {"id": 2}

def save_bookings(booking_in_db: BookingsInDB):
  generator["id"] = generator["id"] + 1
  
  booking_in_db.boo_id = generator["id"]
  database_bookings.append(booking_in_db)
  
  return booking_in_db

def get_bookings_active(inDate: date, outDate: date):
  bookings_active = []

  while inDate <= outDate:
    bookings_today = []
    
    for booking in database_bookings:
      
      if date.fromisoformat(booking["boo_dateIN"]) <= inDate and date.fromisoformat(booking["boo_dateOUT"]) >= inDate:
        bookings_today.append(booking)
    
    bookings_active.append(bookings_today)
    inDate += timedelta(days = 1)

  return bookings_active

def get_table(price: int, maintenance_cost: int):
  dic_prices = {0: "", 10: "", 20: "", 30: "", 40: "", 50: "", 60: "", 70: "", 80: "", 90:""}

  profit_margin = (price - maintenance_cost) / price

  if profit_margin < 0:
    profit_margin = 0
  
  multiple = 1 - profit_margin
  
  for i in dic_prices:
    dic_prices[i] = multiple
    multiple += 0.1
  
  return dic_prices

def get_tens(value: int):
  if value >= 90:
    value = 90
  elif value >= 80:
    value = 80
  elif value >= 70:
    value = 70
  elif value >= 60:
    value = 60
  elif value >= 50:
        value = 50
  elif value >= 40:
    value = 40
  elif value >= 30:
    value = 30  
  elif value >= 20:
        value = 20
  elif value >= 10:
    value = 10
  else:
    value = 0
  return value
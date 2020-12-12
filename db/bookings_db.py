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
    "boo_dateOUT": "2020-12-10",
    "boo_roo_id": 1,
    "boo_name_roo": "A11",
    "boo_rec_id": 1,
    "boo_price_charged": 90000
  },
  {
    "boo_id": 2,
    "boo_cli_id": 2,
    "boo_dateIN": "2020-12-01",
    "boo_dateOUT": "2020-12-09",
    "boo_roo_id": 1,
    "boo_name_roo": "A12",
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

# def get_bookings_active():
#   bookings_active = []
#   today = date.today() - timedelta(days = 1)
  
#   for booking in database_bookings:
#     if date >= today:
#       bookings_active.append(booking)
  
#   return bookings_active

def get_bookings_active(inDate: date, outDate: date):
  bookings_active = []

  while inDate <= outDate:
    for booking in database_bookings:
      if booking["boo_dateIN"] <= inDate and booking["boo_dateIN"] >= inDate:
        bookings_active.append(booking)
    inDate += timedelta(days = 1)

  return bookings_active
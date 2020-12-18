from db.bookings_db import BookingsInDB, save_bookings, get_bookings_active, get_table, get_tens
from models.bookings_model import BookingsIn, BookingsOut
from db.rooms_db import RoomsInDB, save_room, get_room, get_all_rooms, get_total_rooms
from models.rooms_model import RoomsIn, RoomsOut
from db.hotel_db import HotelInDB, save_hotel, get_info_hotel
from models.hotel_model import HotelIn, HotelOut
from db.clients_db import ClientsInDB, get_client, save_client
from models.clients_model import ClientsIn, ClientsOut
from db.users_db import UsersInDB, save_user, get_user
from models.users_model import UsersIn, UsersOut

from math import ceil

from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

origins = [
  "http://localhost.tiangolo.com", 
  "https://localhost.tiangolo.com",
  "http://localhost", 
  "http://localhost:8080",
  "https://graphcostapp.herokuapp.com/"
]

api.add_middleware(
  CORSMiddleware, 
  allow_origins=origins,
  allow_credentials=True, 
  allow_methods=["*"], 
  allow_headers=["*"],
)

@api.post("/bookings/price/")
async def booking_price(booking_in: BookingsIn):
  #necesito una fecha de entrada y salida de una reserva nueva y tipo de habitacion elegida
  #generar tabla de multiplos
  #generar ocupacion
  #consultar el multiplo correspondiente segun la ocupacion
  #multiplicar el multiplo con el precio base
  # precio
  total_rooms = get_total_rooms()
  occupied_rooms_list = get_bookings_active(booking_in.boo_dateIN, booking_in.boo_dateOUT)

  occupancy_percentage_list = []
  for occupied_rooms in occupied_rooms_list:
    occupancy_percentage = (100 * len(occupied_rooms)) / total_rooms
    occupancy_percentage_list.append(occupancy_percentage)

  room_in_db = get_room(booking_in.boo_name_roo[0])
  if room_in_db == None:
      raise HTTPException(status_code = 404, detail = "El tipo de habitación no existe")
  
  multiplier_table = get_table(room_in_db.roo_price, room_in_db.roo_maintenance_cost)
  
  sale_price = 0
  for value in occupancy_percentage_list:
    ten = get_tens(value)
    multi = multiplier_table.get(ten)
    sale_price += multi * room_in_db.roo_price

  sale_price = ceil(sale_price)
  booking_in.boo_price_charged = sale_price

  # booking_out = BookingsOut(**booking_in.dict())
  # return booking_out
  return sale_price

# Guardar reservación, este enlace se usa cuando el recepcionista hace click 
# en hacer reserva después de llenar el formulario
@api.post("/bookings/new/")
async def make_reservation(booking_in: BookingsIn):
  booking_in_db = BookingsInDB(**booking_in.dict())
  booking_in_db = save_bookings(booking_in_db)
  booking_out = BookingsOut(**booking_in_db.dict())

  return booking_out

# Obtener reservas activas por fecha de entrada y salida
@api.get("/bookings/")
async def get_bookings(dateIn, dateOut):
  occupied_rooms_list = get_bookings_active(dateIn, dateOut)
  return occupied_rooms_list

# Obtener todos los rooms y su info
# Este se usará cuando el adm hace click en la opción de habitaciones y aparece el 
# listado de tipo de habitaciones
@api.get("/rooms/")
async def get_rooms():
  all_rooms = get_all_rooms()
  all_rooms_out = []
  for room in all_rooms.values():
    room_out = RoomsOut(**room.dict())
    all_rooms_out.append(room_out)
  return all_rooms_out

# Obtener los datos de un tipo de habitación
# Este se usará cuando el adm hace click en la opción de habitaciones que hay 
# en el menú y dice ver detalles
@api.get("/rooms/{roo_type}")
async def get_room_type(roo_type: str):
  room_in_db = get_room(roo_type)

  if room_in_db == None:
    raise HTTPException(status_code = 404, detail = "El tipo de habitación no existe")
  
  room_out = RoomsOut(**room_in_db.dict())
  return room_out

# Guardar un tipo nuevo de room, este lo hace el adm en la 
# opción de agregar otros tipos de habitación
@api.post("/rooms/new/")
async def make_room(room_in: RoomsIn):
  room_in_db = RoomsInDB(**room_in.dict())
  room_in_db = save_room(room_in_db)
  room_out = RoomsOut(**room_in_db.dict())
  return room_out

# Guardar un hotel, esto va en la parte inicial de la cuenta del admin cuando
# se le solicita que ingrese los datos del hotel
@api.post("/hotel/new/")
async def make_hotel(hotel_in: HotelIn):
  hotel_in_db = HotelInDB(**hotel_in.dict())
  hotel_in_db = save_hotel(hotel_in_db)
  hotel_out = HotelOut(**hotel_in_db.dict())
  return hotel_out

# Obtener info del hotel, POR AHORA ES ESTÁTICO
# Este es cuando después del api.post de arriba el adm quiere consultar los datos del 
# hotel, creo que está como opción en el menú
@api.get("/hotel/")
async def get_hotel():
  hotel_in_db = get_info_hotel()
  hotel_out = HotelOut(**hotel_in_db.dict())
  return hotel_out

# Obtener gerencia
# Por ahora lo puse como get pero también necesitamos el post
# @api.get("/gerencia/")
# async def get_gerencia():
#   total_rooms = get_total_rooms()
#   occupied_rooms = get_bookings_active()

#   occupancy_percentage = (100 * occupied_rooms) / total_rooms

# Crear el cliente, lo hace el recepcionista
@api.post("/clients/new/")
async def make_client(client_in: ClientsIn):
  client_in_db = ClientsInDB(**client_in.dict())
  client_in_db = save_client(client_in_db)
  client_out = ClientsOut(**client_in_db.dict())
  return client_out

# Obtener el cliente, lo hace el recepcionista
@api.get("/clients/{cli_docNumber}")
async def get_client_doc(cli_docNumber: str):
  client_in_db = get_client(cli_docNumber)

  if client_in_db == None:
    raise HTTPException(status_code = 404, detail = "El cliente no existe")
  
  client_out = ClientsOut(**client_in_db.dict())
  return client_out

# Para el login
@api.post("/user/auth/")
async def auth_user(user_in: UsersIn):
    user_in_db = get_user(user_in.use_email)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    if user_in_db.use_password != user_in.use_password:
        return {"Autenticado": False} # Revisar !!!!

    user_out = UsersOut(**user_in_db.dict())
    return user_out
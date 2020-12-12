from db.bookings_db import BookingsInDB, save_bookings, get_bookings_active
from models.bookings_model import BookingsIn, BookingsOut
from db.rooms_db import RoomsInDB, save_room, get_room, get_all_rooms
from models.rooms_model import RoomsIn, RoomsOut
from db.hotel_db import HotelInDB, save_hotel, get_info_hotel, get_total_rooms
from models.hotel_model import HotelIn, HotelOut
from db.clients_db import ClientsInDB, get_client, save_client
from models.clients_model import ClientsIn, ClientsOut
from db.users_db import UsersInDB, save_user, get_user
from models.users_model import UsersIn, UsersOut

from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()

# Guardar reservación, este enlace se usa cuando el recepcionista hace click 
# en hacer reserva después de llenar el formulario
@api.post("/bookings/new/")
async def make_reservation(booking_in: BookingsIn):
  #Falta lógica de precios
  booking_in_db = BookingsInDB(**booking_in.dict(),  boo_price_charged = 0)
  booking_in_db = save_bookings(booking_in_db)
  booking_out = BookingsOut(**booking_in_db.dict())

  return booking_out

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

# Guardar un tipo nuevo de room, este lo hace el adm en la 
# opción de agregar otros tipos de habitación
@api.post("/rooms/new")
async def make_room(room_in: RoomsIn):
  room_in_db = RoomsInDB(**room_in.dict())
  room_in_db = save_room(room_in_db)
  room_out = RoomsOut(**room_in_db.dict())
  return room_out

# Guardar un hotel, esto va en la parte inicial de la cuenta del admin cuando
# se le solicita que ingrese los datos del hotel
@api.post("/hotel/new")
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

# Obtener gerencia, este es el más complicado, es donde necesito tu lógica Leo
# Por ahora lo puse como get pero también necesitamos el post
@api.get("/gerencia/")
async def get_gerencia():
  total_rooms = get_total_rooms()
  occupied_rooms = get_bookings_active()

  occupancy_percentage = (100 * occupied_rooms) / total_rooms


# Creo que me falta el get y post para reportes pero eso se hace después de 
# salir de este sprint jejejeje

# Obtener el cliente, lo hace el recepcionista
@api.get("/clients/{cli_docNumber}")
async def get_client_doc():
  client_in_db = get_client(cli_docNumber)

  if client_in_db == None:
    raise HTTPException(status_code = 404, detail = "El cliente no existe")
  
  client_out = ClientsOut(**client_in_db.dict())
  return client_out

# Crear el cliente, lo hace el recepcionista
@api.post("/clients/new")
async def make_client():
  client_in_db = ClientsInDB(**client_in.dict())
  client_in_db = save_client(client_in_db)
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

    user_out = UsersOut(**user_in.dict())
    return user_out

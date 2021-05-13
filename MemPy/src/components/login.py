from src.windows import login
import PySimpleGUI as sg
from src.models.user_repository import UserRepository
import os

window= login.build()

while True:
  event,values= window.read()
  if event == '-SALIR-':
      break
  usu=values['-USERNAME-']  
  repository= UserRepository()
  objusuario=repository.existe_usuario(usu)
  if objusuario is False:
      print('el usuario no esta')
  else: 
      print('el usuario se encuentra')     
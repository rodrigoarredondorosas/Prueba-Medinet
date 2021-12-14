from django.core.management.base import BaseCommand, CommandError
from farmacias.models import Farmacia
import requests
import datetime
import re
from django.conf import settings
from django.core.mail import send_mail

class Command(BaseCommand):
    help = 'Prueba Medinet'

    def add_arguments(self, parser):
        parser.add_argument('mail', type=str)

    def handle(self, *args, **options):
        #Instructions
        print('Processing...')

        #Get Data
        r = requests.get('https://farmanet.minsal.cl/maps/index.php/ws/getLocalesTurnos')
        data = r.json()
        
        #Variables
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        local_list = []
        to_mail = []
        to_mail.append(options.get('mail', None))
        message = ""
        total = 0

        for value in data:
            #Cast
            local_id = int(value['local_id'])
            fecha = re.sub('-','/',value['fecha'])
            local_nombre = value['local_nombre'].strip()

            #Validate Local
            clean_local = Farmacia.objects.filter(
                local_id=local_id,
                fecha = today
            )

            if clean_local:
                print("You have already created this local")
            else:
                #Save
                farmacia = Farmacia.objects.create(
                    fecha = datetime.datetime.strptime(fecha, '%d/%m/%Y').strftime('%Y-%m-%d'),
                    local_id = local_id,
                    local_nombre = local_nombre,
                    comuna_nombre = value['comuna_nombre'],
                    fk_localidad = int(value['fk_localidad']),
                    localidad_nombre = value['localidad_nombre'],
                    local_direccion = value['local_direccion'],
                    funcionamiento_hora_apertura = value['funcionamiento_hora_apertura'][0:4],
                    funcionamiento_hora_cierre = value['funcionamiento_hora_cierre'][0:4],
                    local_telefono = value['local_telefono'],
                    local_lat = value['local_lat'],
                    local_lng = value['local_lng'],
                    funcionamiento_dia = value['funcionamiento_dia'],
                    fk_region = int(value['fk_region']),
                    fk_comuna = int(value['fk_comuna'])
                )

                print("Local created!")

            #Add local to list
            if(local_nombre not in local_list):
                local_list.append(local_nombre)

        #Create Message
        for local in local_list:
            locales = Farmacia.objects.filter(local_nombre = local, fecha = today)
            text = f"{local} => {len(locales)}"
            message += text+" \n"
            total+=len(locales)

        #Add total to message
        message += f"TOTAL=> {total} \n"

        #Display Message
        print(message)

        #Send Mail
        send_mail(
            "Command getLocalesTurnos Information", # subject
            message, # message
            settings.EMAIL_HOST_USER, # from
            to_mail, # to
            fail_silently=False # display errors
        )
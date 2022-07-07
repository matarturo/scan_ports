#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Script: portscanner.py 
# Creado por: Arturo Mata < arturo.mata@gmail.com >
# Versión: 1.0.0
# DESCARGO DE RESPONSABILIDAD
# Este programa está diseñado con fines de investigación para la busqueda de vulnerabilidades en la configuracion de equipos,
# y el autor no asumirá ninguna responsabilidad si se le da cualquier otro uso.

import socket
import subprocess
import sys
import time
import errno
from datetime import datetime

#  Limpieza automatica del contenido de pantalla
subprocess.call('clear', shell=True)

# Solicitar la función input ()
remoteServer    = input('Ingresar el host a ser escaneado: ')
remoteServerIP  = socket.gethostbyname(remoteServer)

# Imprimir el banner con información sobre qué host estamos a punto de escanear
print ("-" * 60)
print ("Por favor espere, escaneando el host remoto", remoteServerIP)
print ("-" * 60)

# Compruebar a qué hora comenzó el escaneo
t1 = datetime.now()

# Usando la función de rango para especificar puertos (aquí escaneará todos los puertos entre 1 y 5910)

# También se implementó un manejo de errores para detectar errores.

try:
    for port in range(1,5910):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("Puerto {}:  Estado => ABIERTO".format(port))
        sock.close()
except KeyboardInterrupt:
        print("\n Saliiendo del programa !!!!")
        sys.exit()
except socket.gaierror:
        print("\n Hostname no puede ser resuelto !!!!")
        sys.exit()
except socket.error:
        print("\ Host no responde !!!!")
        sys.exit()


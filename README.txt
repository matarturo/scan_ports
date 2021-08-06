# Script escrito en lenguaje Python para escaneo de puertos vulnerables en un host activo
Autor: Arturo Mata <arturo.mata@gmail.com>
Script: portscanner.py
Version: 1.0.0
Repositorio: https://github.com/matarturo/
Released under the GNU General Public License WITHOUT ANY WARRANTY.
See LICENSE.TXT for details.

# Script de mantenimiento de logs de dispositivos firewalls bajo plataforma GNU/Linux

Es importante el mantenimiento periódico de estos equipos ya que los archivos logs del entorno GNU/Linux DebianOS 
crecen rápidamente y se pueden llenar los discos duros generando problemas de almacenamiento de información.

# Requisitos 

Python => apt install python3
Pip Python => pip install python-nmap

# Descarga e instalación del script
Para correr este script se requiere ingresar al equipo con credenciales de usuario < root >

$ cd /var/log
$ sudo git clone https://github.com/matarturo/scan_ports.git
$ cd scan_subnet
$ sudo cp portscanner.py /var/log
$ cd /var/log

#Para editar el script
$ sudo nano portscanner.py  

# Ejecución del script
$ sudo python3 portscanner.py 

#Detener el proceso de busqueda.
Pulsar simultaneamente las teclas CRTL+C

#Una vez obtenido el reporte de los puertos abiertos en el host, se debe detener el programa 
$ exit

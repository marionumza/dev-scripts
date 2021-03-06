Infraestructura de instalación Odoo
===================================
by jeoSoftware
Estructura de directorios de la instalación
-------------------------------------------
Esta es la estructura de directorios de una instalación de Odoo creada 
por odooenv.py, se diseñó así porque permite poner todo en un disco y 
dejar el SO en otro volumen. 
Permite coexistir varias versiones de odoo y varios clientes en la misma 
máquina, compartiendo los servicios de postgres y aeroo.

      odoo
      ├─ postgresql
      ├──odoo-8.0
      │  ├──[clientname]
      │  │   ├──config
      │  │   │  └──openerp-server.conf
      │  │   ├──data_dir
      │  │   │  └──[filestore]
      │  │   └──log
      │  │      └──odoo.log
      │  └──sources
      └──odoo-9.0
         ├──[clientname]
         │   ├──config
         │   │  └──openerp-server.conf
         │   ├──data_dir
         │   │  └──[filestore]
         │   └──log
         │      └──odoo.log
         └──sources

Repositorio de utilidades
-------------------------
En este repo se encuentran todas las utilidades que se usan para el 
desarrollo, en este resumen se detallarán solo dos, sd y odooenv.py

    https://github.com/jobiols/dev-scripts.git

Está clonado en *~/dev-scripts* para actualizarlo hacer

    $ cd ~/dev_scripts
    $ ./install_scripts 

Esto hace un pull del repositorio y copia dos scripts a _/usr/bin_

_odooenv.py_ - para el mantenimiento de la infraestructura
_sd_         - short para sudo docker, y algunas cositas más.

Manifiesto de instalación
-------------------------
La definición de cómo se instala el sistema está en el archivo:

    ~/dev-scripts/classes/client_data.py 

en ese archivo buscamos "esmeralda" y encontramos esto:

       {'name': 'esmeralda', 'port': '8069', 'odoover': '8.0',
         'repos': [
             {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '8.0'},
             {'usr': 'jobiols', 'repo': 'aeroo_reports', 'branch': '8.0'},
             {'usr': 'jobiols', 'repo': 'adhoc-reporting-engine', 'branch': '8.0'},
             {'usr': 'jobiols', 'repo': 'adhoc-account-payment', 'branch': '8.0'},
             {'usr': 'jobiols', 'repo': 'adhoc-stock', 'branch': '8.0'},
             {'usr': 'jobiols', 'repo': 'web', 'branch': '8.0'},
             {'usr': 'jobiols', 'repo': 'server-tools', 'branch': '8.0'},
             {'usr': 'jobiols', 'repo': 'adhoc-account-financial-tools', 'branch': '8.0'},
             {'usr': 'jobiols', 'repo': 'adhoc-account-invoicing', 'branch': '8.0'},
         ],
         'images': [
             {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
             {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '8.0'},
             {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
             {'name': 'backup', 'usr': 'jobiols', 'img': 'backup'},
         ]
       },

- En 'repos' están todos los repositorios
- En 'images' estan todas las imágenes de docker
 
Operaciones de mantenimiento
----------------------------
**Ver todos los backups que hay**
Esto muestra todos los backups que hay de todos los clientes en este caso 
hay un solo cliente, si hubiese varios se puede agregar un -c CLIENTNAME

    $ odooenv.py --backup-list
    
    List of available backups for client esmeralda
    esmeralda_prod 10/02/2017 03:00 GMT  [201702100300] 22M
    esmeralda_prod 10/02/2017 15:00 GMT  [201702101500] 22M

Cada línea es un backup realizado, y cada backup se compone de dos archivos, 
un dump de la base de datos y un tar del filestore.
Para mover estos archivos a otro lugar hay que mover los dos y restarurarlos 
juntos. Los archivos están en /odoo/odoo-8.0/esmeralda/backup

**Hacer un backup**
Para hacer un backup manual, el script lanza una imagen docker con las 
herramientas de backup, se conecta a la instancia  odoo y mapea el directorio 
donde está la bd, el filestore y el postgress. Hace el backup, empaqueta el 
filestore y luego se destruye la imagen.

    $ odooenv.py --backup -d esmeralda_prod -c esmeralda

Notar que en el host no está instalado posgres, ni las herramientas de backup.

**Restaurar un backup** 
Para Restaurar un backup dado se listan los backups disponibles y se 
elige uno según su timestamp. Observando el ejemplo de listar backups, 
el timestamp es lo que está entre corchetes, se copia y se pega después 
de la opcion -t en el siguiente comando:

    $ odooenv.py --restore \	# restorear la bd
    -d esmeralda_prod \		    # nombre original de la bd
    -c esmeralda \			    # cliente
    -t 201702072249 \			# timestamp a restorear
    -w esmeralda_prod_restored	# nuevo nombre de la bd

Hay que pasarle el nombre original y un nuevo nombre, luego se usan las 
herramientas en linea de odoo para eliminar y renombrar con lo cual la 
filestore queda correctamente sincronizada con la base de datos.

**Detener Odoo**
Para detener la instancia de odoo

    $ odooenv.py -s -c esmeralda

**Iniciar Odoo**
Para iniciar odoo, el server iniciado de esta manera ser reiniciará
automáticamente luego de un rebooteo.

    $ odooenv.py -r -c esmeralda
    
**Reiniciar Odoo**
Detiene y arranca el servidor

    $ odooenv.py -s -r -c esmeralda
    
**Detener Postgress y Aeroo**
Detiene los contenedores de postrgress y aeroo, el comando los ejecuta 
juntos pero son dos contenedores separados

    $ odooenv.py -S -c esmeralda
    
**Iniciar Postgress y Aeroo**
    
    $ odooenv.py -R -c esmeralda
    
Donde estan mis cosas
---------------------

Recurso | Ubicacion
------- | ---------
Repositorios                | /odoo/odoo-8.0/sources
Archivo de configuracion    | /odoo/odoo-8.0/esmeralda/config/openerp-server.conf
Archivo de log              | /odoo/odoo-8.0/esmeralda/log/odoo.log
Filestore *                 | /odoo/odoo-8.0/esmeralda/data

(*) El filestore es un directorio donde odoo guarda ciertos archivos de datos
como ser imágenes y también las sesiones.

Sobre las bases de datos
------------------------
Las bases de datos siempre deben empezar con "NOMBRECLIENTE_" en este
caso nombres validos son esmeralda_prod, esmeralda_test, etc.
El sistema cuenta con una opcion dbfilter que oculta todas las bases
de dato que no tengan este prefijo para permitir multiples clientes.

Cómo agregar / quitar un repositorio
------------------------------------
Como primera medida se supone que uno tiene muy claro lo que quiere 
hacer y porqué quiere poner o sacar un repo. Se recomienda enfáticamente
que no se agreguen módulos en la base de producción a menos que se esté
seguro de lo que quermos hacer. Para pruebas usar bases de test.
**La desinstalación de los módulos no siempre deja las cosas como estaban.**

1. Modificar el manifiesto que hay en _~/dev-scripts/classes/client_data.py_ 
y agregarle o quitarle el o los repos necesarios.

2. Reinstalar con el nuevo manifiesto

    $ odooenv.py -i -c esmeralda

    Esto bajará los repos que falten, hará un pull a los que ya existan y no
    tocará los que sobren. Por último actualizará el openerp-server.conf 
    para que odoo vea los repos que queremos que vea. O sea los que pusimos 
    en el manifiesto.

3. Reiniciar odoo para que tome los cambios en el odooenv-server.conf

    $ odooenv.py -s -r -c esmeralda
    
4. Actualizar los XML de los modelos en la bd.

    $ odooenv.py -u -m all -d esmeralda_prod -c esmeralda
     
5. Por último entrar como administrador y en configuración hacer 
"Actualizar la lista de módulos", de esta forma leerá nuevamente la lista 
de módulos que le pusimos en el config y mostrará los módulos de los nuevos
repositorios para que puedan ser instalados.

Nota:
Conviene hacer además un pull para actualizar las imágenes, la de postgress
tiene parches frecuentemente es el punto siguiente. 

Cómo hacer pull para actualizar imágenes y repos
------------------------------------------------
Para actualizar las imágenes y repositorios hacer:

    $ odooenv.py -p -c esmeralda

Como instalar desde cero
------------------------
Para instalar nuevamente el sistema en un SO fresco:

**Requerimientos**
- git
- docker
- python2.7
    
**Instalación**

    $ cd 
    $ git clone https://github.com/jobiols/dev-scripts.git
    $ cd dev-scripts
    $ ./install-scripts
    $ odooenv.py -p -i -c esmeralda
    $ odooenv.py -R -r -c esmeralda
    
**Terminar la instalación**
- La master password es admin, cambiarla 
- Restaurar la base de datos desde la interfase web

**Instalar baclup automático**

    $ odooenv.py -j -d esmeralda_prod -c esmeralda
    
Verificar que la tarea quedo instalada con
 
    $ odooenv.py --cron-list

Tags y versiones de repositorios
--------------------------------

Es un hecho que los repositorios públicos están cambiando constantemente, 
eso es una característica del open source. Por lo tanto para mantener 
la estabilidad de las instalaciones, hay forks de cada repositorio que se 
usa en https://github.com/jobiols/
 Sin embargo estos también cambian y alguna instalación de cliente se
queda atrás. Para poder volver al estado de una instalación de cliente
se usan los comandos

    -T --tag-repos        Tag all repos used by a client with a tag consisting
                          of client name and a timestamp. Need -c option
    --checkout-tag CHECKOUT_TAG
                          checkouts a tag from all the repos belonging to a
                          client needs -c option. If some repo does not have the
                          tag, reports theerror and continues with next repo.The
                          tag was previously setted with -T option. To revert this
                          situation issue a --revert-checkout
    --revert-checkout     checkouts the normal branch (i.e. odoo version) for
                          all the repos belonging to the client. Needs -c
                          option. This revers the --checkout-tags to the normal
                          state. Warning: if there is any local change in a
                          repo, the checkout will fail.
 
**Comando -T**
Cuando terminamos una instalación de cliente y sabemos (con razonable
seguridad) que no se le van a agregar más repositorios, se hace un 

    odooenv.py -T -c NOMBRE-DE-CLIENTE

Este comando taggea todos los repos que están en https://github.com/jobiols/ 
y que son usados por este cliente, con un tag de la forma 
AAAA-MM-DD-HH-MM-SS-NOMBRE-DE-CLIENTE
para que en algun futuro se pueda reconstruir esta instalación a pesar 
de que los repositorios evolucionen con nuevos commits.

**Comando --checkout-tag CHECKOUT_TAG**

Usado para reconstruir una versión anterior de un conjunto de repositorios
Lo primero es ir a la instalación del cliente y en uno de los repositorios
hacer un _git tag_ para obtener el último tag, todos los repos van a 
mostrar el mismo ultimo tag.

Luego en desarrollo se crea una instalación de la siguiente forma

    odooenv.py -i -c NOMBRE-DE-CLIENTE --checkout-tag EL-TAG
     
_Atención_: esto no tiene en cuenta posibles modificaciones en la imagen

Esto clonea o actualiza los repos según sea necesario y como es habitual
con el comando -i y al terminar hace un checkout del tag.


**Comando --revert-checkout**

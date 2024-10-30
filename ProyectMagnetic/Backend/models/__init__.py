from .db import db  # Importa la instancia de SQLAlchemy

# Importa los modelos para asegurarte de que se registren con SQLAlchemy
from .ambiente.campus import Campus
from .ambiente.bloque import Bloque
from .ambiente.aula import Aula
from .personas.persona import Persona
from .personas.rol import Rol

from .personas.usuario import Usuario

from .accesos.historial import HistorialAcceso
from .permisos.permiso import PermisoAcceso

# Importa la función para crear la base de datos
from .database import create_database

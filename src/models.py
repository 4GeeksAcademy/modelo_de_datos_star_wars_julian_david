from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(120), nullable=False)
    apellido: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    fecha_de_subscripcion: Mapped[str] = mapped_column(DateTime) 
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    # favorites

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "fecha_de_subscripcion": self.fecha_de_subscripcion
        }
    
class Planeta(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(120), nullable=False)
    poblacion: Mapped[int] = mapped_column(Integer, nullable=False)
    clima: Mapped[str] = mapped_column(String(120), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "poblacion": self.poblacion,
            "clima": self.clima
        }

class Personaje(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(120), nullable=False)
    edad: Mapped[int] = mapped_column(Integer, nullable=False)
    raza: Mapped[str] = mapped_column(String(120), nullable=False)
    origen: Mapped[str] = mapped_column(String(120), nullable=False)
    color_de_ojos: Mapped[str] = mapped_column(String(120), nullable=False)

    def serialize(self):
        return{
            "id": self.id,
            "nombre": self.nombre,
            "edad": self.edad,
            "raza": self.raza,
            "origen": self.origen,
            "color_de_ojos": self.color_de_ojos
        }

class Favorito(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    usuario_id: Mapped[int] = mapped_column(db.ForeignKey("user.id"))
    usuario: Mapped["User"] = db.relationship(backref="favorites") #crea relación en la tabla User

    planeta_id: Mapped[int] = mapped_column(db.ForeignKey("planeta.id"))
    planeta: Mapped["Planeta"] = db.relationship(backref="favorites") #crea relación en la tabla Favorito

    personaje_id: Mapped[int] = mapped_column(db.ForeignKey("personaje.id"))
    personaje: Mapped["Personaje"] = db.relationship(backref="favorites") #crea relación en tabla Personaje

    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "planeta_id": self.planeta_id,
            "personaje": self.personaje
    }
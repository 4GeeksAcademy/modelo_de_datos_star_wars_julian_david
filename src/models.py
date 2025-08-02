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
            # do not serialize the password, its a security breach
        }
    
class Planeta(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(120), nullable=False)
    poblacion: Mapped[int] = mapped_column(Integer, nullable=False)
    clima: Mapped[str] = mapped_column(String(120), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Personaje(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(120), nullable=False)
    edad: Mapped[int] = mapped_column(Integer, nullable=False)
    raza: Mapped[str] = mapped_column(String(120), nullable=False)
    origen: Mapped[str] = mapped_column(String(120), nullable=False)
    color_de_ojos: Mapped[str] = mapped_column(String(120), nullable=False)

class Favorito(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    usuario_id: Mapped[int] = mapped_column(db.ForeignKey("user.id"))
    usuario: Mapped["User"] = db.relationship(backref="favorites") #crea relación en la tabla User

    planeta_id: Mapped[int] = mapped_column(db.ForeignKey("planeta.id"))
    planeta: Mapped["Planeta"] = db.relationship(backref="favorites") #crea relación en la tabla Favorito

    personaje: Mapped[int] = mapped_column(db.ForeignKey("personaje.id"))
    personaje: Mapped["Personaje"] = db.relationship(backref="favorites") #crea relación en tabla Personaje


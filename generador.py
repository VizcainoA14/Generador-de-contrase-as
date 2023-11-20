from pydantic import BaseModel
import random
import string

class Generador(BaseModel):
    frase: str
    longitud: int = 10


    def generar(self):
        palabras_frase = self.frase.split()
        palabras_usadas = [palabra[:3] for palabra in palabras_frase]  # Tomar los primeros 3 caracteres de cada palabra
    
        contraseña = ''.join(palabras_usadas)
    
        # Añadir caracteres aleatorios para alcanzar la longitud deseada
        while len(contraseña) < self.longitud:
            contraseña += random.choice(string.ascii_letters + string.digits + string.punctuation)

        # Retornar solo los primeros 'longitud' caracteres para cumplir con la longitud mínima
        return contraseña[:self.longitud]
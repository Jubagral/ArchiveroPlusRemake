import json
import os

def actualizar_personajes(data):
    for personaje in data:
        filename = f"personajes/{personaje['nombre'].lower().replace(' ', '_')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(personaje, f, ensure_ascii=False, indent=4)

def main():
    # Ejemplo de datos a actualizar
    personajes = [
        {
            "nombre": "Hanse Davion",
            "alianza": "Federated Commonwealth",
            "rol": "Príncipe",
            "biografia": "Hanse Davion es el príncipe de la Mancomunidad Federada..."
        },
        # Agrega más personajes aquí
    ]
    
    actualizar_personajes(personajes)

if __name__ == "__main__":
    main()

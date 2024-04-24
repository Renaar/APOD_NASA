import requests
import ctypes
import os

# Mettre sa clé API ici :
my_API_key = "JHwoDNIMkSwtD1GTr9a5CrN9CM4K2uVo88S3Tw9R"
# Définir le nouveau chemin de destination
destination_path = r"C:\Users\loic.garcia_ext\Desktop\nasa_images"

# Récupérer l'image du jour sur le site de la NASA
url = f"https://api.nasa.gov/planetary/apod?api_key={my_API_key}"
response = requests.get(url)
image_url = response.json()['url']

# Télécharger l'image
# Assurez-vous que le chemin existe
os.makedirs(destination_path, exist_ok=True)
image_response = requests.get(image_url)
image_path = os.path.join(destination_path, 'nasa_image.jpg')
with open(image_path, 'wb') as file:
    file.write(image_response.content)

# Configurer l'image en tant que fond d'écran
ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)

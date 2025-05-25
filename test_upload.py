import requests

# URL of your Flask API
url = "http://127.0.0.1:5000/upload"




# Corrected path for the image file
file = {"image": open("d:\\shrey_onedrive\\Desktop\\Satellite_Data\\water\\SeaLake_1.jpg", "rb")}

# Send POST request to Flask
response = requests.post(url, files=file)

# Print response
print(response.json())  # Should show success message

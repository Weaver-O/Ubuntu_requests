import requests #Importing the requests library to handle HTTP requests
import os  #Importing the os library to interact with the operating system
from urllib.parse import urlparse
print("Welcome to my image downloader!")
print("You can download images from the web using this script\n")

url = input("Enter the URL of the image to download: ") #Prompting the user to enter the URL of the image to download
try:
    os.makedirs("Fetched_Images", exist_ok=True) # Creates the directory if it doesn't exist
    #Fetching the image from the provided URL
    response = requests.get(url, timeout = 10)
    response.raise_for_status() #Checking if the request was successful

    # Check if the response is an image
    if 'image' not in response.headers.get('Content-Type', ''):
        print("The URL does not point to an image. Please provide a direct image URL.")
        exit(1)
    
    #Extracting the filename from the URL
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename: #If the filename is empty, assign a default name
        filename = "downloaded_image"
    
    #Linking the full path for saving the image
    filepath = os.path.join("Fetched_Images", filename)
    with open(filepath, 'wb') as file: #Opening the file in write-binary mode
        file.write(response.content) #Writing the content of the response to the file
    print(f"Image successfully downloaded and saved as {filepath}")
except requests.exceptions.RequestException as e: #Handling exceptions related to HTTP requests
    print(f"An error occurred while fetching the image. Please check your network connection: {e}")
except requests.exceptions.Timeout: #Handling timeout exceptions
    print("The request timed out. Please try again later.")

print(f"Successfully completed the download of {filename}")
print("Thank you for using the image downloader!")


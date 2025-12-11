print("Hello from repository!")

from dotenv import load_dotenv 
import os  

def print_author():
    #load_dotenv(dotenv_path='/C/Users/Peter/Yandex.Disk/2nd/first_project/.env')
    load_dotenv(dotenv_path='C:/Users/Peter/Yandex.Disk/2nd/first_project/.env')
    author = os.getenv('AUTHOR')
    print(f"Автор проекта: {author}")
    
print_author()
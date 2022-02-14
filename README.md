# VoiceLine
Application that records audio and returns the text transcription.

## Run locally

To run locally

- Clone this repo:
  ```
   git clone https://github.com/diogosoares22/VoiceLine.git
  ```
  
- Install the dependencies:
  ```
  pip install -r requirements.txt
  ```
  
- Make migrations and migrate the database:
  ```
   python manage.py makemigrations
   python manage.py migrate
  ```
- Finally, run the application:
  ```
   python manage.py runserver
  ```
  
  Visit http://localhost:8000/record in your browser

Note: The app requires internet connection for the transcription


# Corporate Assets Tracker System


## How to Run This Project

### To run this project, follow these steps:

#### 1. Clone the Git Repository:
Clone the project's Git repository using the following command:

```bash
  git clone https://github.com/shamimkhaled/corporate-assets-tracker-django-app.git
```
#### 2. Set Up a Virtual Environment:
 Open the cloned project in Visual Studio Code (VS Code). In the VS Code terminal (either Command Prompt or Git Bash), create a virtual environment inside the project root folder:
```bash
  python -m venv env
```
#### Activate the virtual environment:

#### In Command Prompt terminal:
```bash
  .\env\Scripts\activate
```

#### or

#### In Git Bash terminal (replace the path with your virtual environment path):
```bash
source "C:\Users\shamim\Desktop\AssetsApp\env\Scripts\activate"
```
#### 3.  Navigate to the Project Directory:
If you're not already in the project root directory, navigate to the Django project directory named "assets_tracker":

```bash
  cd assets_tracker
```

#### 4.  Install Project Dependencies:
Install all project dependencies by running the following command:

```bash
  pip install -r requirements.txt
```

#### 5. Database Migration:
Migrate the database to create necessary tables:

```bash
  python manage.py makemigrations
```
```bash
  python manage.py migrate
```

#### 6. Create a Superuser:
Create a superuser account to access the admin panel of the project:

```bash
  python manage.py createsuperuser
```
Follow the prompts to set a username, email, and password for the superuser.

#### 7. Run the Project:
Start the Django development server:

```bash
  python manage.py runserver
```

### API Documentation (Swagger)
To view the API documentation with Swagger, visit the following URL:
```bash
  http://127.0.0.1:8000/docs/
```

This URL provides a list of all available APIs and their documentation.

By following these steps, you'll have the project up and running, and you can explore the API documentation to interact with the endpoints.
## Color Reference

| Color             | Hex                                                                |
| ----------------- | ------------------------------------------------------------------ |
| Example Color | ![#0a192f](https://via.placeholder.com/10/0a192f?text=+) #0a192f |
| Example Color | ![#f8f8f8](https://via.placeholder.com/10/f8f8f8?text=+) #f8f8f8 |
| Example Color | ![#00b48a](https://via.placeholder.com/10/00b48a?text=+) #00b48a |
| Example Color | ![#00d1a0](https://via.placeholder.com/10/00b48a?text=+) #00d1a0 |


## Authors

- [@shamimkhaled](https://www.github.com/shamimkhaled)


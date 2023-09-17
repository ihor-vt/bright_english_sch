# Backend for an English school website

A brief project description and its purpose.

## Introduction

Your project is designed for content management on your website through an admin panel and providing necessary data through an API on the frontend side. This README.md will help you quickly set up the project and get started with it.

## Requirements

Make sure you have the following components installed on your computer:

- Python >= 3.9

## Installation

1. Clone the repository to your computer:

   ```bash
   git clone https://github.com/ihor-vt/bright_english_sch.git
   ```

2. Navigate to the project folder:

   ```bash
   cd english_school
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run migrations and create the database:

   ```bash
   python manage.py migrate
   ```

6. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

7. Open a web browser and go to `http://localhost:8000/admin/` to access the admin panel.

## Usage

Your project allows you to:

- Add, edit, and delete data through the admin panel.
- Interact with the API on the frontend side to retrieve necessary data.

For details on how to use and configure the project, refer to the documentation or follow the instructions in the admin panel.

## Suggestions for improvement:

I was proposing to a client to use celery with redis to send emails, but he didn't want to add those technologies.

## Dependencies

Here is a list of the main Python libraries and packages used in this project:

- `python = ^3.9`
- `django = 4.1`
- `django-environ = ^0.10.0`
- `pillow = ^10.0.0`
- `djangorestframework = ^3.14.0`
- `markdown = ^3.4.3`
- `psycopg2-binary = ^2.9.6`
- `django-jet-reboot = ^1.3.3`
- `six = ^1.16.0`
- `feedparser = ^6.0.10`
- `cloudinary = ^1.33.0`
- `django-cloudinary-storage = ^0.3.0`
- `gunicorn = ^20.1.0`
- `whitenoise = 6.3.0`
- `django-cors-headers = ^4.2.0`
- `asgiref = ^3.7.2`
- `django-parler = ^2.3`
- `django-tinymce = ^3.6.1`

You can install these dependencies using `pip install`.

## License

This project is distributed under the MIT license. See the `LICENSE` file for details.

## Author

- Author: Ihor
- Contact Information: ihorvoitiukk@gmail.com

## Thank You

If you have any questions or suggestions, please feel free to contact me. Thank you for using our product!
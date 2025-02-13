Play2Learn Platform
==================

This repository contains the source code for the Play2Learn platform, a full-stack web application built using Python and JavaScript with Django and Vue.js. This was the main project I completed while in the Full Stack Software Development program at Loyola Marymount University.

Table of Contents
-----------------

*   Introduction
*   Features
*   Technologies Used
*   Installation
*   Usage
*   Contributing
*   License
*   Contact

Introduction
------------

Play2Learn is an educational platform designed to provide interactive learning experiences through various games and activities. The website allows users to create accounts, play games, track their scores, check leaderboards, submit reviews, apply for faux-jobs for a faux-company called "Play2Learn", and more.

This website demonstrates a scalable, seamless integration between multiple frameworks and languages.

Features
--------

*   User authentication and profile management
*   Interactive games written in Vue.js
*   Game leaderboards
*   User reviews and ratings
*   Contact form for user inquiries
*   Job application form

Technologies Used
-----------------

*   **Backend:** Django, Django REST framework
*   **Frontend:** Vue.js, Bootstrap
*   **Database:** PostgreSQL, MySQL
*   **Other:** SendGrid for email notifications, AWS S3 for static and media file storage

Installation
------------

1.  Clone the repository:
    
        git clone https://github.com/ryanlevee/play2learn.git
        cd play2learn
        
    
2.  Create and activate a virtual environment:
    
        python -m venv venv
        source venv/bin/activate  # On Windows use `venv\Scripts\activate`
        
    
3.  Install the required dependencies:
    
        pip install -r requirements.txt
        
    
4.  Set up the database:
    
        python manage.py migrate
        
    
5.  Create a superuser:
    
        python manage.py createsuperuser
        
    
6.  Run the development server:
    
        python manage.py runserver
        
    

Usage
-----

*   Access the website at `http://127.0.0.1:8000/`
*   Register for an account or log in with an existing account
*   Click the "Play Games" button to choose a Vue.js game
*   If you are logged in, your scores will be uploaded to an SQL database and can be immediately viewed on the "My Game Tracking" page
*   Top scores will be included on the "Leaderboard" page
*   Submit reviews for games, which will show up in the carousel once approved
*   Use the contact form to send inquiries
*   Apply for jobs through the job application form

If you would like superuser access to see the SQL back end via Django Admin, let me know. The full source code for the entire website is also available in my GitHub portfolio.

Contributing
------------

Contributions are welcome! Please fork the repository and create a pull request with your changes.

License
-------

This project is licensed under the GPL-3.0 License. See the LICENSE file for more details.


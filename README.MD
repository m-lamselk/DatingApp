Task: 
Django Frontend separated environment

Instructions:
You will need a new Django project that is properly configured to run that code. You will also need to mock a lot of data including view context and templatetags to properly display it in the browser.

1.	Write a Django project that will handle this approach.
2.	Configure the template paths in the project's settings to include the path to the frontend templates.
3.	Configure the static files paths in the project's settings to include the path to the frontend static files.
4.	Create a test view to display an example template with mocked context.
5.	Show us an example of how you would mock templatetags. 
6.	Explain your approach in the README file and add examples of how you would work with our code. So we add you to our repository with the frontend code and what do you do step by step?
7.	Create public repository and submit your code (Gitlab/Github/Bitbucket)

My approach:

1- created a separate virtual environment for the project.
2- created a new django projet (dating_app).
3- created an app inside (frontend) and added it in the installed apps in the settings.py file.
4- created "templates" and "static" folders in the root directory and configured both in the settings.py file.
5- created a basic view called "main" that returns an html template "index.html" that extends "base.html", it also passes some mocked context with it to be displayed in the frontend (profiles).


In terms of how would I work with the existing code:

First, I would need an good understanding of the existing apps withing the projects and how they interact with each other, and then I would create a specific folder (inside templates) for each app where I would store related templates. Also, I would need to know the different existing models that we'll be working with since that's the data that's gonna be displayed for the user so in order to interact with it, I need to have a good understanding of it.
Another important thing is user permissions, so in order to know which user has access to which data, I need to know how's the backend setup for that. 
That's in a nutshell would be my approach. 

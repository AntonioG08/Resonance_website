# Resonance website 

Repository used to develop the website for a business in a city located
in Guanajuato, México. The business is Resonance, a business dedicated
to audio equipment used in social events such as parties, weddings, 
conferences, among many other types of events.

The project so far has been made with the following languajes/technologies:
- Python (Django Framework)
- SQL (for databases)
- HTML / CSS / JS 
The project is currently deployed using PythonAnyWhere which makes things
easier to deploy a python project based on the Django framework.

Deploy processing (for developers): 
- First | in PythonAnyWhere (PAW) check if there is anything modified using 
  'git status', if there are any modifications (which probably are), 
  eliminate them. We can modify the files from the PythonAnyWhere console, 
  but it's not recommended, the oficial version should be the one in GitHub 
  and we only pull it to PAW. 
- Second | After the status in the PAW console is the same as the GitHub
  repository (no file modified or any change reistered untracked etc etc), 
  we use 'Git pull' to pull the most current version from the repository.
- Third | Once this is done and we have the latest version of the repository
  in our PAW console, in our console we'll go to our aplication (using 
  'cd aplication') and we run the following instruction 'python manage.py 
  collectstatic' to migrate all the images, CSS, and JS files stored in our 
  static folders. 
- Fourth | After the Static files are migrated, go to the folder of the main
  app and search in the files the one named 'settings.py' file to make some 
  modifications. Turn the DEBUG variable to FALSE for security reasons. After 
  doing this, lets go to the file 'urls.py' and in the MEDIA URL at the bottom,
  change the conditional to 'if not settings.DEBUG' since DEBUG is now set to
  false.

Repository & Project developed by:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>Ing. Antonio Gómez Ruiz
@echo off
echo Creating directory structure and files for La Petite Academie Django project...

:: Create main project directories
mkdir lapetiteacademie
mkdir daycare
mkdir static
mkdir static\css
mkdir daycare\templates
mkdir daycare\templates\daycare
mkdir daycare\migrations
mkdir daycare\locale
mkdir daycare\locale\fr
mkdir daycare\locale\fr\LC_MESSAGES
mkdir daycare\locale\en
mkdir daycare\locale\en\LC_MESSAGES

:: Create files in lapetiteacademie/
echo. > manage.py
echo. > lapetiteacademie\__init__.py
echo. > lapetiteacademie\asgi.py
echo. > lapetiteacademie\settings.py
echo. > lapetiteacademie\urls.py
echo. > lapetiteacademie\wsgi.py
echo. > lapetiteacademie\constants.py

:: Create files in daycare/
echo. > daycare\__init__.py
echo. > daycare\admin.py
echo. > daycare\apps.py
echo. > daycare\views.py
echo. > daycare\urls.py
echo. > daycare\tests.py

:: Create files in daycare/migrations/
echo. > daycare\migrations\__init__.py

:: Create template files
echo. > daycare\templates\daycare\base.html
echo. > daycare\templates\daycare\index.html

:: Create localization files
echo. > daycare\locale\fr\LC_MESSAGES\django.po
echo. > daycare\locale\fr\LC_MESSAGES\django.mo
echo. > daycare\locale\en\LC_MESSAGES\django.po
echo. > daycare\locale\en\LC_MESSAGES\django.mo

:: Create static files
echo. > static\css\tailwind.css

:: Create root files
echo. > requirements.txt
echo. > .gitignore

echo Directory structure and files created successfully!
pause
# FamilyTech  <a id="top"/>

<img src=""> 

## Introduction

This website was created for Code Institute, May Hackathon - themed: A Family Hackathon.<br>

The main objective of this Haackathon was to build a site/app that could provide support for IT issues that different members of the family generally have and how we could help them with these issues.

That would be achieved through showing guides for the users to fix their IT issues.

Live site: [FamilyTech](https://familytech-3d93c509ed81.herokuapp.com/)

## Table of Contents
- []()
    - [Introduction](#introduction)
    - [Table of Contents](#table-of-contents)
    - [Overview](#overview)
- [Ux - User Experience](#ux---user-experience)
    - [Colour Scheme](#colour-scheme)
    - [Contrast Check](#contrast-check)
    - [Typography](#typography)
- [Project Planning](#project-planning)
    - [Strategy](#strategy)
    - [Agile Methodologies](#agile-methodologies)
    - [Users](#users)
    - [Wireframes](#wireframes)
    - [Imagery](#imagery)
    - [Features](#features)
- [Technologies Used](#technologies-used)
    - [Languages and Technologies](#languages-and-technologies)
    - [Libraries](#libraries)
    - [Tools and Programs](#tools-and-programs)
- [Deployment](#deployment)
    - [Connecting to GigHub](#connecting-to-github)
    - [Django Project Setup](#django-project-setup)
    - [Cloudinary API](#cloudinary-api)
    - [Heroku Deployment](#heroku-deployment)
    - [Clone Project](#clone-project)
    - [Fork Project](#fork-project)
    - [Tailwind](#tailwind-css-setup)
      - [Prerequisits](#prerequisites)
      - [Installation](#installation)
- [Bugs to fix](#bugs-to-fix)
- [AI Implementation and Orchestration](#ai-implementaion-and-orchestration)
    - [Code Generation](#code-generation)
    - [Debugging](#debugging)#429
    - [Code Optimization](#code-optimisation)
    - [Impact on Workflow](#impact-on-workflow)
- [Testing](#testing)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [Lighthouse Audit](#lighthouse-audit)
    - [Manual Testing](#manual-testing)
- [Future Features](#future-features)
- [Credits](#credits)
    - [Code References](#code-references)
    - [Media References](#media-references)
    - [Acknowledgments](#acknowledgements)
    - [Owner Details](#owner-details)


[Back to top](#top)

# Overview
FamilyTech is a simple site that provides information about how to do some tasks on mobiles devices and laptops or computers.<br>

It also has a chat-bot function in case the user doesn't finds the information he needs.<br>

It aims to be an interactive and responsive site in different devices.<br>

The site goal is to help the user overcome the strugle with different issues while trying to open an app, sending a message or adding a new contact.<br>

## UX - User Experience
For this site we opted to use smooth colours that could help the user to relax and be confident with the solution provided.<br>

Some of the features available
  - Access to posts with guides for different devices
  - Chat-bot for extra help, in case no help is available on the site

[Back to top](#top)

## Colour Scheme

#ffffff - White
#4b5563 - Bright Grey
#4299e1 - Tufts Blue
#2d3748 - Japanese Indigo
#4b5563 - Independence

 - [Color Palette](https://colorkit.co/color-palette-generator/ffffff-4b5563-4299e1-2d3748-cac8c8-e9e7e7-f4BAF2E9f3f3/)

Names checked with [color-name](https://www.color-name.com/hex/4b5563)

<img src="" style="width: 90%; height: 60%;"><br>

| Colour      | WCAG Ratio (against #121212) | WCAG Contrast          |
|-------------|-------------------------------|-------------------------|
| Purple      | Pass (7.1:1)                 | ✅ AAA                 |
| Indigo      | Pass (8.23:1)                | ✅✅ AAA               |
| Roseberry   | Pass (6.71:1)                | ✅✅ AAA               |
| Bright Blue | Pass (6.95:1)                | ✅✅ AAA               |

## Contrast Check
<img src=""><br>

## Typography
Fonts used for this website were:

  - [Roboto](https://fonts.google.com/specimen/Roboto)
  - [sans-serif](https://fonts.google.com/?query=sans+serif&categoryFilters=Sans+Serif:%2FSans%2F*)
  
  
[Back to top](#top)

# Project Planning

Initial idea for the chat was to create help guides for tasks done at home, not just with technology, but also with household appliances and where to find different things.<br>

After discussing this, the group got to the conclusion that the hackathon theme was more related to tech issues and problems that different members of the family from different ages can find while using their devices, and we should focus more on this area, and add the household appliances, if possible, once the electronic devices (eg: mobile phone, latpop) are well covered and we are happy with the site working and responsiveness.<br>

With this done, different areas of the site (back-end, front-end, colours, etc, where picked by different members of the team.<br>

On the first day the repository and project were created with all members added with admin rights.<br>

Heroku deployment done successfully on the third day.<br>

The team kept working on improving the site features and fixing errors.<br>

## Strategy

  - Simple and appealing layout and colors
  - User-friendly platform
  - Menus easy to locate and select
  - Consistent UX design throughout different platforms
  - Allow for future improvements and addition of new features

## Agile Methodologies
FamilyTech was the first hackathon for one of our members and a come back experience for the rest of the group.<br>

In the begining sounded a bit tricky to check which role different members could get, but with communication within the team we were able to get everyone to work in different areas of the website, and slowly start building the project.<br>

We did our best to have 2 huddles per day, with one after lunch and another later in the day to discuss the site progress and what needed to be changed, improved and what was done well.<br>

Good and frequent (as possible) communication helped to keep the project on track, with extra huddles, as needed to check inidividual issues and try to solve them.<br>

Issues and features can be seen on [GitHub Project Board](https://github.com/users/Carlos-n21/projects/19).<br>

[Back to top](#top)

### Users

Persona 1: Tech-Savvy Student

    Name: Alex Chen

    Age: 20

    Occupation: Computer Science Student

    Devices Used: Laptop (primary), Smartphone (for quick lookups)

    Tech Skill Level: Intermediate to Advanced

    Goals:

        Find quick solutions for coding bugs or software installation issues

        Access reliable technical instructions between classes or while commuting

    Pain Points:

        Frustrated with vague or outdated solutions on forums

        Needs mobile-friendly content for use on the go

    Behaviors:

        Searches Google or Reddit first, but prefers visual step-by-step guides

        Frequently bookmarks or saves useful guides to read later

Persona 2: Non-Tech-Savvy Professional

    Name: Linda Martinez

    Age: 42

    Occupation: Office Manager at a small business

    Devices Used: Work Laptop (primary), Smartphone (occasionally)

    Tech Skill Level: Beginner

    Goals:

        Fix common issues like printer setup, Wi-Fi problems, or email errors

        Follow simple, jargon-free instructions

    Pain Points:

        Intimidated by overly technical explanations

        Needs clear visuals or videos to follow along

    Behaviors:

        Relies on step-by-step guides or video tutorials

        Often searches “[problem] + how to fix” on Google

Persona 3: Freelance IT Support Technician

    Name: Rajiv Patel

    Age: 33

    Occupation: Freelance IT Support Specialist

    Devices Used: Smartphone (on-site visits), Laptop (at home/office)

    Tech Skill Level: Advanced

    Goals:

        Quickly access troubleshooting steps while assisting clients on-site

        Stay updated with latest fixes and tech tools

    Pain Points:

        Time-sensitive troubleshooting—needs concise and accurate content

        Frustrated by guides that aren’t mobile-optimized

    Behaviors:

        Skims guides for relevant commands or screenshots

        Prefers content with clear structure, quick reference sections, or downloadable PDFs


[Back to top](#top)

### Wireframes
Initial wireframes - desktop view:

<img src="">
<img src="">

Initial wireframes - mobile view:

<img src="">
<img src="">

The initial concept was based on:

  - [doc)

Afns.<br>

[Back to top](#top)

### Imagery
Image used on the homepage:

- [Elderly using technology](https://cdn.shopify.com/s/files/1/0656/3289/5229/files/Elderly_Using_Technology_Stock_Imagery_TapTec.png?v=1695582894)

[Back to top](#top)

## Features
Some of the features that can be seen on the website are:

An

[Back to top](#top)

## Technologies Used
### Languages and Technologies
  - HTML
  - CSS
  - JavaScript
  - Python
  - Git
  - Github
  - VS-Code
  - Django
  - Heroku

### Libraries
  - Django v3.2.19
  - Google Fonts

### Tools and Programs
  - Balsamiq wireframe
  - MSCopilot AI
  - VS-Code Copilot
  - ChatGPT

[Back to top](#top)

## Deployment

### Connecting to GitHub
To begin this project from scratch, you must first create a new GitHub repository using the Code Institute's Template. This template provides the relevant tools to get you started. To use this template:

  - Log in to GitHub or create a new account.<br>
  - Navigate to the above CI Full Template.<br>
  - Click 'Use this template' -> 'Create a new repository'.<br>
  - Choose a new repository name and click 'Create repository from template'.<br>
  - In your new repository space, click the purple CodeAnywhere (if this is your IDE of choice) button to generate a new workspace.<br>

[Back to top](#top)

### Django Project Setup<br>
Install Django and supporting libraries:<br>
  - pip3 install 'django<4' gunicorn<br>
  - pip3 install dj_database_url psycopg2<br>
  - pip3 install dj3-cloudinary-storage<br>

Once you have installed any relevant dependencies or libraries, such as the ones listed above, it is important to create a requirements.txt file and add all installed libraries to it with the pip3 freeze --local > requirements.txt command in the terminal.

Create a new Django project in the terminal django-admin startproject ems .

Create a new app eg. python3 mangage.py startapp events

Add this to list of INSTALLED_APPS in settings.py - 'booking',

Create a superuser for the project to allow Admin access and enter credentials: python3 manage.py createsuperuser

Migrate the changes with commands: python3 manage.py migrate

An env.py file must be created to store all protected data such as the 
DATABASE_URL and SECRET_KEY. These may be called upon in your project's settings.py file along with your Database configurations. The env.py file must be added to your gitignore file so that your important, protected information is not pushed to public viewing on GitHub. For adding to env.py:

  - import os
  - os.environ["DATABASE_URL"]="<copiedURLfrom postgresql://neondb_owner>"
  - os.environ["SECRET_KEY"]="my_super^secret@key"

For adding to settings.py:

  - import os
  - import dj_database_url
  - if os.path.exists("env.py"):
  - import env
  - SECRET_KEY = os.environ.get('SECRET_KEY') (actual key hidden within env.py)

Replace DATABASES with:

DATABASES = {<br>
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))<br>
  }

Set up the templates directory in settings.py:
  - Under BASE_DIR enter TEMPLATES_DIR = os.path.join(BASE_DIR, ‘templates’)
  - Update TEMPLATES = 'DIRS': [TEMPLATES_DIR] with:<br>
  os.path.join(BASE_DIR, 'templates'),<br>
  os.path.join(BASE_DIR, 'templates', 'allauth')<br>
  - Create the media, static and templates directories in top level of project file in IDE workspace.<br>
  
A Procfile must be created within the project repo for Heroku deployment with the following placed within it: web: gunicorn ems.wsgi

Make the necessary migrations again.

[Back to top](#top)

### Heroku deployment
To start the deployment process , please follow the below steps:

  - Log in to Heroku or create an account if you are a new user.

  - Once logged in, in the Heroku Dashboard, navigate to the 'New' button in the top, right corner, and select 'Create New App'.

  - Enter an app name and choose your region. Click 'Create App'.

  - In the Deploy tab, click on the 'Settings', reach the 'Config Vars' section and click on 'Reveal Config Vars'. Here you will enter KEY:VALUE pairs for the app to run successfully. The KEY:VALUE pairs that you will need are your:<br>
CLOUDINARY_URL: cloudinary://....<br>
DATABASE_URL:postgres://...<br>
DISABLE_COLLECTSTATIC of value '1' (N.B Remove this Config Var before deployment),<br>
PORT:8000<br>
SECRET_KEY and value<br>

  - Add the Heroku host name into ALLOWED_HOSTS in your projects settings.py file ->  ['800-nielmc-django-project-lxqprmm3qz.us2.codeanyapp.com', '.herokuapp.com', 'localhost', '127.0.0.1'].

  - Once you are sure that you have set up the required files including your requirements.txt and Procfile, you have ensured that DEBUG=False, save your project, add the files, commit for initial deployment and push the data to GitHub.

  - Go to the 'Deploy' tab and choose GitHub as the Deployment method.

  - Search for the repository name, select the branch that you would like to build from, and connect it via the 'Connect' button.

  - Choose from 'Automatic' or 'Manual' deployment options, I chose the 'Manual' deployment method. Click 'Deploy Branch'.

  - Once the waiting period for the app to build has finished, click the 'View' link to bring you to your newly deployed site. If you receive any errors, Heroku will display a reason in the app build log for you to investigate. DISABLE_COLLECTSTATIC may be removed from the Config Vars once you have saved and pushed an image within your project, as can PORT:8000.

[Back to top](#top)

### Clone project
A local clone of this repository can be made on GitHub. Please follow the below steps:

  - Navigate to GitHub and log in.
  - Kids Art Repository can be found at this location.
  - Above the repository file section, locate the 'Code' button.
  - Click on this button and choose your clone method from HTTPS, SSH or GitHub CLI, copy the URL to your clipboard by clicking the 'Copy' button.
  - Open your Git Bash Terminal.
  - Change the current working directory to the location you want the cloned directory to be made.
  - Type git clone and paste in the copied URL from step 4.
  - Press 'Enter' for the local clone to be created.
  - Using the pip3 install -r requirements.txt command, the dependencies and libraries needed for FreeFido will be installed.
  - Set up your env.py file and from the above steps for Cloudinary and NeonSQL, gather the Cloudinary API key and the Neon SQL url for additon to your code.
  - Ensure that your env.py file is placed in your .gitignore file and follow the remaining steps in the above Django Project Setup section before pushing your code to GitHub.

### Fork Project
A copy of the original repository can be made through GitHub. Please follow the below steps to fork this repository:

  - Navigate to GitHub and log in.
  - Once logged in, navigate to this repository using this link Eventia Repository.
  - Above the repository file section and to the top, right of the page is the 'Fork' button, click on this to make a fork of this repository.
  - You should now have access to a forked copy of this repository in your Github account.
  - Follow the above Django Project Steps if you wish to work on the project.


[Back to top](#top)

### Bugs to fix
- Cele
## AI Implementaion and Orchestration
### Code Generation
The G

### Debugging
Regu

### Code Optimisation
When.<br>

### Impact on Workflow
Ov

[Back to top](#top)

## Testing
Va

### HTML Validation
Used [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input) to test the HTML on all webpages and updated as needed. No errors found after fixing as can be seen on the examples bellow.
<details>
  <img src="">
</details>

[Back to top](#top)

### CSS Validation

Used [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input) to test CSS style and no errors found.

  <img src="">

### Lighthouse Audit

Used Chrome Dev Tools Lighthouse to audit the site for response time and accessibility, as you can see onm the examples bellow.<br>
<details>
  <img src="">
</details>

[Back to top](#top)

### Manual Testing
Website manually tested on the following devices/browsers for responsiveness:
  - Google Chrome
  - Mozilla Firefox
  - Opera
  - Vivaldi
  - Samsung Galaxy A40
  - Google Pixel 8
  - iPhone 16
  - iPad
  - Samsung Galaxy

[Back to top](#top)

## Future Features
- Us

## Credits
### Code References
We.
<br>

### Acknowledgements
Th

### Owner Details
This website was created by . Students of Code Institute.<br>

  - [)

[Back to top](#top)


## Online-Meditation-and-Mindfulness-Community
The website can be found at

https://calm-connections.azurewebsites.net

## Author
Dmytro Bilyk

dmbilyk3861@gmail.com

https://t.me/@lkjhg13


# Project Documentation


## Architecture
The website is developed using Python version 3.11 and is built upon the Django framework version 5.0.3

### List of DB models
UserProfile
Profile
Video

### List of Views
home
profile_view
edit_profile
get_list_video
get_video
get_streaming_video


### The main program files are located in the WEB directory 
### Static files such as photos, javascript scripts, and css styles are located in the static directory
### Other image files are located in the media directory
### HTML files are located in the templates directory

#### Additionally 
JavaScript, CSS, and HTML are employed to enhance the frontend functionality and presentation.

## Usage
To get all the features of the service, you need to have a Google account for simple authorization, one step 
and you will have access to everything our service offers.And every week there will be more and more opportunities.

### Can use locallhost
```bash
pip install requirements.txt
```

```bash
python manage.py migrate
```

```bash
python manage.py runserver 8000
```
And go to:

http://127.0.0.1:8000/


## Application Features
• User Registration: Users can create accounts using their Google credentials, ensuring a seamless onboarding experience.

• Profile Customization: Personalize your profile with information and preferences to tailor your meditation experience.

• Guided Meditation Sessions: Access a library of guided meditation sessions led by experienced instructors, catering to various needs and skill levels.So that each user can choose the meditation they want.

• Coming soon.

## Project Task Decomposition
### Week 1:
- Implement feature: User Registration with Google OAuth 2.0 ✔️
- Set up Azure environment for project deployment ✔️
- Initialize GitHub repository for version control ✔️
- Create README.md file with Getting Started documentation ✔️
- Set up Continuous Integration/Continuous Delivery pipeline ✔️

### Week 2:
- Implement feature: Profile Customization ✔️
- Design architecture diagram for the project ✔️
- Configure CI/CD pipeline for automated deployment on Azure ✔️
- Begin writing unit tests for user registration functionality ✔️
- Document project architecture in README.md ✔️

### Week 3:

- Develop infrastructure diagram outlining Azure components ✔️
- Enhance unit test coverage for user registration ✔️
- Create Postman collection for testing user registration endpoints ✔️
- Implement feature: Guided Meditation Sessions ✔️
- Update README.md with project tasks decomposition ✔️

## User Acceptance Testing

-The "User Profile" section does not display BIO after saving.✔️

-No option to add a profile photo.-

-The site footer needs to correct "freeback" instead of "freeback".✔️

-Forum have no option to reply to a user and create your own wall on a question you interested in.✔️

-No "back" button when leaving a page with meditation video from youtube.✔️

-The section with tasks is useless if it is not logically connected to the parts of the site, which would be a task.✔️

-Cute loading wheel✔️

### Week 4:

- Expand unit tests to cover profile customization functionality ✔️
-
- Implement feature: Community ✔️
-
- Integrate feedback system for user interaction ✔️
-
- Conduct testing on Google Chrome PC browsers for compatibility ✔️
-
- Review and update documentation in README.md ✔️

## Week 5:

#### - Optimize Azure deployment for performance and scalability ✔️

Rewritten deployment logic and fixed static files

#### - Conduct user acceptance testing to ensure seamless functionality ✔️

#### - Refactor code for improved readability and maintainability ✔️

#### - Update README.md with testing procedures and results ✔️

Successfully tested user editing and checking the driver on google chrome

#### - Implement feature: Progress Tracking ✔️

# Project scheme

![img.png](img.png)

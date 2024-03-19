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

### Can use locallhot
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
- Develop infrastructure diagram outlining Azure components 
- Enhance unit test coverage for user registration ✔️
- Create Postman collection for testing user registration endpoints ✔️
- Implement feature: Guided Meditation Sessions ✔️
- Update README.md with project tasks decomposition ✔️





![img.png](img.png)

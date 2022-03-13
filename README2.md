# The Veggie Guy Online Cookbook
## Introuduction
Welcome to my third project. This project is a simple online cookbook that allows users to manage their own recipes remotely. This will use languages such as Django, Python, HTML, CSS and JavaScript.

This project will show the use of CRUD functionality (Create, Read, Update, Delete). The user will be able create, read, update and delete their user profile and table booking.

A live website can be found here.

![index web](static/assets/images/readme_lead_image.jpg)

# Table of Contents

* 1. UX
    * 1.1. Strategy
        * Project Goals
            * User Goals:
            * User Expectations:
            * Trends of Modern Websites
            * Strategy Table
    * 1.2. Structure
    * 1.3. Skeleton
    * 1.4. Surface
* 2. Features
* 3. Technologies Used
* 4. Testing
* 5. Development Cycle
* 6. Deployment
* 7. End Product
* 8. Known Bugs
* 9. Credits




# 1.UX
#### [Go To Top](#table-of-contents "Go To Top")

As a big foodie, I have always enjoyed going out to different restaurants to try new cuisines. The simplest way is to book a table at a restaurant. The booking system is best when it's simple to use and asks for the necessary information.



The project will give the user an easy way to store, update, delete and edit stored recipe's. Either personal or external.

## 1.1 Strategy
#### [Go To Top](#table-of-contents "Go To Top")

### Project Goals
The main goal of this project is to allow the user to sign up, sign in/out, create/update a user profile and create/update/delete a personal recipes in one place.

The website should:
* Promote a brand of cooking untensils
* Allow the user to create a profile
* Within this profile the user should be able to create and save their own recipes and the assoicated information


### User Goals:

First Time Visitor Goals

* The user should be able to view a selection of tools
* The user should be able to register an account
* The user should be able to create and store recipes
* The user should be able to delete and edit recipes they have created
* The user should be able to browse community approved recipes
* The user should be able to log into their profile on any device and easily view their recipes

Returning Visitor Goals
* The user should be able to view a selection of tools
* The user should be able to log into their account
* The user should be able to create and store recipes
* The user should be able to delete and edit recipes they have created
* The user should be able to browse community approved recipes
* The user should be able to log into their profile on any device and easily view their recipes

### User Expectations:
The system should have a simple user interface, with the navigation to each section clear and concise.

* Each page is clear to read.
* The user interface is easy to navigate.
* The website is responsive on all devices.


## 1.2 Structure
#### [Go To Top](#table-of-contents "Go To Top")

It is really important to include responsive design in this project as many users are using different devices (mobile, tablet, laptop/PC). This gives the user the best experience on their device.

* Responsive on all device sizes
* Easy navigation through labelled buttons
* All elements will be consistent including font size, font family, colour scheme.

## 1.3 Skeleton
#### [Go To Top](#table-of-contents "Go To Top")

## Sitemap

![index web](static/assets/images/site_map.jpg)

## Wireframes

### Base Template
![index web](static/assets/images/Wireframes/base_template.jpg)
### Home Pages
![index web](static/assets/images/Wireframes/home_pages.jpg)
### Cooking Tools Pages
![index web](static/assets/images/Wireframes/cooking_tools.jpg)
### Community Recipes Pages
![index web](static/assets/images/Wireframes/community_recipes.jpg)
### My Recipe Pages
![index web](static/assets/images/Wireframes/my_recipes.jpg)
### Profile Pages - On Load
![index web](static/assets/images/Wireframes/profile_page_list_items.jpg)
### Profile Pages - List Item 1
![index web](static/assets/images/Wireframes/profile_page_form.jpg)
### Profile Pages - List Item 2
![index web](static/assets/images/Wireframes/profile_page_manage_recipes.jpg)
### Profile Pages - List Item 3
![index web](static/assets/images/Wireframes/profile_page_user_info.jpg)

## 1.4 Surface
#### [Go To Top](#table-of-contents "Go To Top")

### Font and colors:
Colors used can be found <a href="https://materializecss.com/color.html">here</a>.

Fonts used have been pulled through using materializecss.


# 2. Features
#### [Go To Top](#table-of-contents "Go To Top")

# 3. Technologies Used
#### [Go To Top](#table-of-contents "Go To Top")

* <a href="https://html.com/html5/">HTML 5</a>  
    * The project uses HyperText Markup Language
* <a href="https://en.wikipedia.org/wiki/CSS">CSS3</a>
    * The project uses Cascading Style Sheets 
* <a href="https://www.javascript.com/">JavaScript</a>
    * The project uses JavaScript
* <a href="https://www.python.org/">Python</a>
    * The project uses Python
* <a href="https://materializecss.com/">Materialize</a>
    * The project uses Materialize css structuring

* <a href="https://balsamiq.com/wireframes/">Balsamiq Wireframes</a>
    * Balsamiq was used to create the wireframes during the design process
* <a href="https://www.gitpod.io/">Gitpod</a>
    * The project uses Gitpod
* <a href="https://github.com/">GitHub</a>
    * GitHub was used to store the project's code after being pushed from Git
* <a href="https://www.heroku.com/">Heroku</a>
    * The project uses Heroku to host the website
* <a href="https://www.google.co.uk/chrome/">Chrome</a>
    * The project uses Chrome to debug and test the source code using HTML5
* <a href="https://beautifier.io/">Code beutifier</a>
    * Corrects Javascript/HTML/CSS code with correct spacing/lines etc.


# 4. Testing
#### [Go To Top](#table-of-contents "Go To Top")

# 5. Developement Cycle
#### [Go To Top](#table-of-contents "Go To Top")

* Install supporting python libraries
    * Install PyMongo and Flask.
    * Create the requirements.txt file. This includes the project's dependencies allowing us to run the project in Heroku

* Create new Heroku app
    * Sign into Heroku
    * Select New
    * Select create new app
    * Enter a relevant app name
    * Select appropriate region
    * Select the create app button

* Prepare the environment and app.py file
    * Create env.py file
    * Add DATABASE_URL with the URL from Heroku
    * Add SECRET_KEY with a randomly generated key
    * Add SECRET_KEY and generated key to the config vars in Heroku
    * Replace insecure key with the environment variable for the SECRET_KEY
    * Add Heroku database as the back end
    * Migrate changes to new database

# 6. Deployment
#### [Go To Top](#table-of-contents "Go To Top")

 I used the terminal to deploy my project locally. To do this I had to:

  1. Create a repository on GitHub.
  2. Clone the repository on your chosen source code editor (GitPod in my case) using the clone link.
  3. Open the terminal within GitPod
  4. Enter "python3 app.py" into the terminal.
  5. Go to local host address on my web browser.
  6. All locally saved changes will show up here.

For the final deployment to Heroku, I had to:

  1. Set debug = False in my app.py file.
  2. Commit and push all files to GitHub
  3. In Heroku, remove the DISABLE_COLLECTSTATIC config var.
  4. In the deploy tab, go to the manual deploy sections and click deploy branch.

# 7. End Product
#### [Go To Top](#table-of-contents "Go To Top")

# 8. Known Bugs
#### [Go To Top](#table-of-contents "Go To Top")

* Various issues with naming
Due to a course break and a lack of initial understanding of the course material a lot of the python naming was  incorrect and or incosistent that lead to bugs that needed to be fixed with CI's help. This caused most of the  problems I had
* Elements expanding outside of their container 
    * Links in the profile cards had to be shortened due but this made the card look tidier anyway
    * Headers stretching the page when changing size
* Forms not submitting correctly or at all
* Materialize elements not changing size
* Not being able to load the preview
    * After the course break I couldnt load the preview because heroku had set the link to suspended
* Losing the app.py file and other elements when opening a workspace
    * I had to work with CI to understand that workspaces exist and that I had to pin and reload each time - https://gitpod.io/workspaces
* Open floating outside of the card bug 
    * Moved to center of card instead
        




# 9. Credits
#### [Go To Top](#table-of-contents "Go To Top")

## Code
* <a href="https://www.lakeland.co.uk/" target="_blank">LakeLand for tool page cotent</a>

* <a href="https://materializecss.com/" target="_blank">Website structure and inspiration</a>

* <a href="https://stackoverflow.com/questions/30523370/javascript-expand-collapse-button" target="_blank">Toggle buttons</a>

* <a href="https://materializecss.com/collapsible.html" target="_blank">Collapsible Elements</a>

## Content

* <a href="https://www.bbcgoodfood.com/" target="_blank">Recipe Idea's - BBC Good Food</a>

* <a href="https://www.pexels.com/" target="_blank">For pictures - Artists can be found in /static/assets/images</a>



## Project Acknowledgements
* Code Institue Tutor Support - For directing me to the correct solutions for any bugs.

* My Mentor - For his constructive criticism and always pushing me to go further to develop my skills.

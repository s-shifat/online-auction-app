# Online Auction App

This is an online auction app system, built with python django framework.

The app is live at: https://shifats-auction-app.herokuapp.com/
<br>
Issues: The media files are not loading due to debug=False, adding a database server should resolve this problem

While running locally, from settings.py change to debug=True

Here are the steps followed through out the building process:

### Step-1

1. Initialized the project and added an app named [accounts](./accounts). Configured the [media](./media) folder for storing media files.

2. Designed the [database models](./accounts/models.py) named `AuctionProduct` and `Bidder` for managing data. `AuctionProduct` has many-to-one relationship with the `User` model and `Bidder` has many-to-one relationship with `AuctionProduct` model.

3. Added the necessary views to the project for different relative routes.

4. Implemented the user login-registration system.

5. Styled the pages with css and bootstrap.

### Step-2

1. Implemented a gallery view.
2. Added login restrictions to relevent pages.
3. Added a create button that gets the user to a form page to post a new auction item.
4. Added another functionality so that a user can place bids but not the post owner.

### Step-3

1. Added functionality so that the users can interect the auciton posts with in auction end date and time.
2. During this time users can update or delete there bids.

### Step-4
1. After an auction finishes the interactibility of the post will be disabled and the winner will be showd in the page.

### Step-5
1. Added the appropriate routing for admin dashboard.
2. The admin dashboard is not completed as required yet.

### Step-6
1. Added some custom styling with help of bootstrap 4 in different views. Though the forms are not styled yet.


### Challanges Faced

1. Learnt django framework. Took help from youtube and the beautiful djnago documentation. 
2. The very first challenge was user authentication system. I took help from youtube and django documentations to overcome this.
3. Designing the database: I had some knowledge about how relational databases work and sql. So after spending some time in the documentation I was able to design the database for this project.
4. Database operations: Learnt how to do basic crud and querry operations on django models.
5. Upload image to server and render the image: At first it was not functioning correctly as expected. So I researced how to make it work in the internet. Several stack overflow posts helped me out here. I learned how POST method works for images and files works a bit differently than that for text/strings.
6. Though I have basic knowledge about html5 stack, I never worked with bootstrap before. I found out that bootstrap has a very well documentation and gained a better knowledge on bootstrap.
7. I learnt how I can add custom styling to django model form objects by modifiying the attributes using python code.
8. Deploying to Heroku.

### Out Come
1. Learnt user authentication system 
2. URL routings
3. Bootstrap
4. django database models
5. django forms
6. user specific url routing
7. managing static and media files
8. deployment to heroku
9. function base views
10. django templates
11. djnago models crud operations
12. working with date and time

### Some References where I took help from
1. [Django Documentation](https://docs.djangoproject.com/en/4.0/)
2. [Tech With Tim](https://www.youtube.com/c/TechWithTim)
3. [Dennis Ivy](https://www.youtube.com/channel/UCTZRcDjjkVajGL6wd76UnGg)
4. [John Elder from codemy.com](https://www.youtube.com/channel/UCFB0dxMudkws1q8w5NJEAmw)
5. [Corey Schafer](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g)
6. Some Stack Overflow Searches:
    * https://stackoverflow.com/questions/60128838/django-datetimeinput-type-datetime-local-not-saving-to-database
    * https://stackoverflow.com/questions/4945802/how-can-i-disable-a-model-field-in-a-django-form
    * https://stackoverflow.com/questions/2673647/enforce-unique-upload-file-names-using-django

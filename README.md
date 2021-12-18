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


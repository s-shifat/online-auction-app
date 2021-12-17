# Online Auction App

This is an online auction app system, built with python django framework.

Here are the steps followed through out the building process:

### Step-1

1. Initialized the project and added an app named [accounts](./accounts). Configured the [media](./media) folder for storing media files.

2. Designed the [database models](./accounts/models.py) named `AuctionProduct` and `Bidder` for managing data. `AuctionProduct` has many-to-one relationship with the `User` model and `Bidder` has many-to-one relationship with `AuctionProduct` model.

3. Added the necessary views to the project for different relative routes.

4. Implemented the user login-registration system.

5. Styled the pages with css and bootstrap.


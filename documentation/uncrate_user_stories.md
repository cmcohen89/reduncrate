# User Stories

## Users

### Sign Up

* As an unregistered and unauthorized user, I want to be able to sign up for the website via a sign-up form.
  * When I'm on the `/signup` page:
    * I would like to be able to enter my email, username, and preferred password on a clearly laid out form.
    * I would like the website to log me in upon successful completion of the sign-up form.
      * So that I can seamlessly access the site's functionality
  * When I enter invalid data on the sign-up form:
    * I would like the website to inform me of the validations I failed to pass, and repopulate the form with my valid entries (except my password).
    * So that I can try again without needing to refill forms I entered valid data into.

### Log in

* As a registered and unauthorized user, I want to be able to log in to the website via a log-in form.
  * When I'm on the `/login` page:
    * I would like to be able to enter my email and password on a clearly laid out form.
    * I would like the website to log me in upon successful completion of the lob-up form.
      * So that I can seamlessly access the site's functionality
  * When I enter invalid data on the log-up form:
    * I would like the website to inform me of the validations I failed to pass, and repopulate the form with my valid entries (except my password).
      * So that I can try again without needing to refill forms I entered valid data into.

### Demo User

* As an unregistered and unauthorized user, I would like an easy to find and clear button on both the `/signup` and `/login` pages to allow me to visit the site as a guest without signing up or logging in.
  * When I'm on either the `/signup` or `/login` pages:
    * I can click on a Demo User button to log me in and allow me access as a normal user.
      * So that I can test the site's features and functionality without needing to stop and enter credentials.

### Log Out

* As a logged in user, I want to log out via an easy to find log out button on the navigation bar.
  * While on any page of the site:
    * I can log out of my account and be redirected to a page displaying recent FauxTweets.
      * So that I can easily log out to keep my information secure.

## Cart

### Add an item to a cart

* As a website visitor, I want to be able add an item to my cart.
    * I can add an item to my cart by clicking "Add to Cart" 
      * so I can keep track of the items I plan to purchase.

### Viewing cart

* As a logged in _or_ logged out user, I want to be able to view my cart
    * I can view the items I've added to my cart.
      * So that I can keep track of the items I plan to purchase.

### Updating cart

* As a logged in user _or_ logged out user, I want to be able to edit the contents of my cart.
    * I can click "Edit" to change the quantity of items I plan to purchase.
      * So that I can revise planned purchases as desired.

### Deleting items from cart

* As a logged in user _or_ logged out user, I want to be able to delete items from my cart.
    * I can click "Delete" to permanently delete an item in my cart.
      * So that when I realize I don't want to purchase something, it won't be included at checkout.

## Products

### List a product on the site

* As a logged in user, I want to be able to list a product for sale / promote a product
    * I can click "New listing" to list the desired product on the site.
        * So that I can reach site visitors who may purchase the product.

### View a product listing

* As a logged in user _or_ logged out user, I can view a product post
    * I can click on the product's image to view the individual product's splash page
        * So that I can educate myself further on the product's features and pricing

### Edit a product listing

* As a logged in user _and_ owner of the product listing, I can edit information about the listing
    * I can click "Edit details" to change the details of the listing
        * So that I can present the latest and greatest product details to site visitors

### Delete a product listing

* As a logged in user _and_ owner of the product listing, I can delete the listing permanently
    * I can click "Delete listing" to remove it permanently from the site
        * So that I can opt out of selling or promoting the product as wanted

## Product Images

### Add a product image to a listing

* As a logged in user _and_ owner of the product listing, I can add a product image to the listing
  * I can click "add a new image" to add one permanently to the listing
      * So that I ensure the product is represented accurately and is current

### Edit a product image on a listing
* As a logged in user _and_ owner of the product listing, I can update a product image on a listing

### View a product's images
* As a site visitor, I can view a product's images
  * I can view one or a set of images for any product on its details page
      * So that I can get a complete visual sense of the product offering 

### Delete a product image
* As a logged in user _and_ owner of the product listing, I can delete a product image for a given listing
  * I can click "delete image" to permanently remove it from the listing
    * So that I can remove an image that poorly represents the product's value

## Search

### Search for products on the site

* As a logged in user _or_ logged out user, I can search keywords by clicking into the search icon
    * So that I can curate viewed products to match my shopping intent.

## Favorites (AKA Stash)

### Add an item to favorites

* As a logged in user, I can add an item to my favorites by clicking the star icon next to a product
    * So I can come back later to remind myself of the most suitable products!

### Read favorites

* As a logged in user, I can view my list of favorites

### Delete favorites

* As a logged in user, I can remove a favorited item permanently from my list

## WIP: Accessibility modal (Bonus Feature)

* As a site visitor with an impairment or disabliity, I can click on a suitable accessibility option to improve my site experience


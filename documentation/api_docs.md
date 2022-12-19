## API Documentation

## USER AUTHENTICATION/AUTHORIZATION

### All endpoints that require authentication

All endpoints that require a current user to be logged in.

* Request: endpoints that require authentication
* Error Response: Require authentication
  * Status Code: 401
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Authentication required",
      "status_code": 401
    }
    ```

### All endpoints that require proper authorization

All endpoints that require authentication and the current user does not have the
correct role(s) or permission(s).

* Request: endpoints that require proper authorization
* Error Response: Require proper authorization
  * Status Code: 403
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Forbidden",
      "status_code": 403
    }
    ```

### Get the Current User

Returns the information about the current user that is logged in.

* Require Authentication: true
* Request
  * Method: GET
  * URL: /api/session
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "id": 1,
      "first_name": "John",
      "last_name": "Smith",
      "email": "john.smith@gmail.com",
      "username": "JohnSmith"
    }
    ```

### Log In a User

Logs in a current user with valid credentials and returns the current user's
information.

* Require Authentication: false
* Request
  * Method: POST
  * URL: /api/session
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "credential": "john.smith@gmail.com",
      "password": "secret password"
    }
    ```

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "id": 1,
      "first_name": "John",
      "last_name": "Smith",
      "email": "john.smith@gmail.com",
      "username": "JohnSmith",
      "token": ""
    }
    ```

* Error Response: Invalid credentials
  * Status Code: 401
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Invalid credentials",
      "status_code": 401
    }
    ```

* Error response: Body validation errors
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Validation error",
      "status_code": 400,
      "errors": {
        "credential": "Email or username is required",
        "password": "Password is required"
      }
    }
    ```

### Sign Up a User

Creates a new user, logs them in as the current user, and returns the current
user's information.

* Require Authentication: false
* Request
  * Method: POST
  * URL: /api/users
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "first_name": "John",
      "last_name": "Smith",
      "email": "john.smith@gmail.com",
      "username": "JohnSmith",
      "password": "secret password"
    }
    ```

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "id": 1,
      "first_name": "John",
      "last_name": "Smith",
      "email": "john.smith@gmail.com",
      "username": "JohnSmith",
      "token": ""
    }
    ```

* Error response: User already exists with the specified email
  * Status Code: 403
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "User already exists",
      "status_code": 403,
      "errors": {
        "email": "User with that email already exists"
      }
    }
    ```

* Error response: User already exists with the specified username
  * Status Code: 403
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "User already exists",
      "status_code": 403,
      "errors": {
        "username": "User with that username already exists"
      }
    }
    ```

* Error response: Body validation errors
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Validation error",
      "status_code": 400,
      "errors": {
        "email": "Invalid email",
        "username": "Username is required",
        "first_name": "First Name is required",
        "last_name": "Last Name is required"
      }
    }
    ```
    
## PRODUCTS

### Get all Products

Returns all the products.

* Require Authentication: false
* Request
  * Method: GET
  * URL: /api/products
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "Products": [
        {
          "id": 1,
          "title": "Whiskey-flavored Soap",
          "description": "Clean your bits with soap that smells (and tastes) like whiskey!",
          "detailed_description": "Let the sultry aroma of triple-distilled Irish whiskey cleanse you from the inside and out. Smelling like an alcoholic has never been so classy.",
          "category_id": 1,
          "price": 24.99,
          "preview_img_id": 1,
        }
      ]
    }
    ```
    
### Get all Products listed by the Current User

Returns all the products listed (created) by the current user.

* Require Authentication: true
* Request
  * Method: GET
  * URL: /api/products/current
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "Products": [
        {
          "id": 1,
          "title": "Whiskey-flavored Soap",
          "description": "Clean your bits with soap that smells (and tastes) like whiskey!",
          "detailed_description": "Let the sultry aroma of triple-distilled Irish whiskey cleanse you from the inside and out. Smelling like an alcoholic has never been so classy.",
          "category_id": 1,
          "price": 24.99,
          "preview_img_id": 1,
        }
      ]
    }
    ```

### Get details of a Product from an id

Returns the details of a product specified by its id.

* Require Authentication: false
* Request
  * Method: GET
  * URL: /api/products/:product_id
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "id": 1,
      "title": "Whiskey-flavored Soap",
      "description": "Clean your bits with soap that smells (and tastes) like whiskey!",
      "detailed_description": "Let the sultry aroma of triple-distilled Irish whiskey cleanse you from the inside and out. Smelling like an alcoholic has never been so classy.",
      "category_id": 1,
      "price": 24.99,
      "preview_img_id": 1,
      "Product_Images": [
        {
          "id": 1,
          "url": "image url",
        },
        {
          "id": 2,
          "url": "image url",
        }
      ],
    }
    ```

* Error response: Couldn't find a Product with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Product couldn't be found",
      "status_code": 404
    }
    ```
    
### Create a Product

Creates and returns a new product.

* Require Authentication: true
* Request
  * Method: POST
  * URL: /api/products
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "title": "Whiskey-flavored Soap",
      "description": "Clean your bits with soap that smells (and tastes) like whiskey!",
      "detailed_description": "Let the sultry aroma of triple-distilled Irish whiskey cleanse you from the inside and out. Smelling like an alcoholic has never been so classy.",
      "category_id": 1,
      "price": 24.99
    }
    ```

* Successful Response
  * Status Code: 201
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "title": "Whiskey-flavored Soap",
      "description": "Clean your bits with soap that smells (and tastes) like whiskey!",
      "detailed_description": "Let the sultry aroma of triple-distilled Irish whiskey cleanse you from the inside and out. Smelling like an alcoholic has never been so classy.",
      "category_id": 1,
      "price": 24.99
    }
    ```

* Error Response: Body validation error
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Validation Error",
      "status_code": 400,
      "errors": {
        "title": "Title is required",
        "description": "Description is required",
        "detailed_description": "Detailed description is required",
        "category_id": "Category ID is required",
        "price": "Price is required"
      }
    }
    ```

### Add an Image to a Product based on the Product's id

Create and return a new image for a product specified by id.

* Require Authentication: true
* Require proper authorization: Product must belong to the current user
* Request
  * Method: POST
  * URL: /api/products/:product_id/images
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "url": "image url",
    }
    ```

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "id": 1,
      "url": "image url",
    }
    ```

* Error response: Couldn't find a Product with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Product couldn't be found",
      "status_code": 404
    }
    ```
    
### Edit a Product

Updates and returns an existing product.

* Require Authentication: true
* Require proper authorization: Product must belong to the current user
* Request
  * Method: PUT
  * URL: /api/products/:product_id
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "title": "Whiskey-flavored Soap",
      "description": "Clean your bits with soap that smells (and tastes) like whiskey!",
      "detailed_description": "Let the sultry aroma of triple-distilled Irish whiskey cleanse you from the inside and out. Smelling like an alcoholic has never been so classy.",
      "category_id": 1,
      "price": 24.99
    }
    ```

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "title": "Whiskey-flavored Soap",
      "description": "Clean your bits with soap that smells (and tastes) like whiskey!",
      "detailed_description": "Let the sultry aroma of triple-distilled Irish whiskey cleanse you from the inside and out. Smelling like an alcoholic has never been so classy.",
      "category_id": 1,
      "price": 24.99
    }
    ```

* Error Response: Body validation error
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Validation Error",
      "status_code": 400,
      "errors": {
        "title": "Title is required",
        "description": "Description is required",
        "detailed_description": "Detailed description is required",
        "category_id": "Category ID is required",
        "price": "Price is required"
      }
    }
    ```

* Error response: Couldn't find a Product with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Product couldn't be found",
      "status_code": 404
    }
    ```

### Delete a Product

Deletes an existing product.

* Require Authentication: true
* Require proper authorization: Product must belong to the current user
* Request
  * Method: DELETE
  * URL: /api/products/:product_id
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Successfully deleted",
      "status_code": 200
    }
    ```

* Error response: Couldn't find a Product with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Product couldn't be found",
      "status_code": 404
    }
    ```

## CARTS

### Get Cart by User id

Returns the user's cart specified by the User's id.

* Require Authentication: true
* Request
  * Method: GET
  * URL: /api/users/cart
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "Cart": [
        {
          "id": 1,
          "used_id": 1,
          "total": 92.43,
          "purchased": false,
          "Cart_Items": [
            {
              "id": 1,
              "cart_id": 1,
              "product_id": 5,
              "quantity": 1,
            },
            {
              "id": 2,
              "cart_id": 1,
              "product_id": 12,
              "quantity": 1,
            },
            {
              "id": 3,
              "cart_id": 1,
              "product_id": 17,
              "quantity": 1,
            }
          ]
        }
      ]
    }
    ```

### Add an Item to a Cart

Adds an item to a cart by the cart's id and returns the cart.

* Require Authentication: true
* Request
  * Method: POST
  * URL: /api/users/cart
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "product_id": 18,
      "quantity": 1
    }
    ```
    
* Successful Response
  * Status Code: 201
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "Cart": [
        {
          "id": 1,
          "usedId": 1,
          "total": 134.67,
          "purchased": false,
          "Cart_Items": [
            {
              "id": 1,
              "cart_id": 1,
              "product_id": 5,
              "quantity": 1,
            },
            {
              "id": 2,
              "cart_id": 1,
              "product_id": 12,
              "quantity": 1,
            },
            {
              "id": 3,
              "cart_id": 1,
              "product_id": 17,
              "quantity": 1,
            },
            {
              "id": 4,
              "cart_id": 1,
              "product_id": 18,
              "quantity": 1,
            }
          ]
        }
      ]
    }
    ```
    
* Error Response: Body validation error
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Validation Error",
      "status_code": 400,
      "errors": {
        "product_id": "Product id is required",
        "quantity": "Quantity is required",
      }
    }
    ```
    
### Edit a Cart Item

Updates and returns a cart item by the cart item's id.

* Require Authentication: true
* Require proper authorization: Cart must belong to the current user
* Request
  * Method: PUT
  * URL: /api/users/cart/:cart_item_id
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "quantity": 2,
    }
    ```

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "id": 1,
      "cart_id": 1,
      "product_id": 5,
      "quantity": 2
    }
    ```

* Error Response: Body validation error
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Validation Error",
      "status_code": 400,
      "errors": {
        "quantity": "Quantity is required",
      }
    }
    ```
    
* Error response: Couldn't find a Cart Item with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Cart Item couldn't be found",
      "status_code": 404
    }
    ```
    
### Edit a Cart's Purchased Status

Updates a cart's purchased status and returns the cart.

* Require Authentication: true
* Require proper authorization: Cart must belong to the current user
* Request
  * Method: PUT
  * URL: /api/users/cart
  * Body:

    ```json
    {
      "purchased": true,
      "purchase_date": "1969-06-19"
    }
    ```

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "Cart": [
        {
          "id": 1,
          "user_id": 1,
          "total": 134.67,
          "purchased": true,
          "Cart_Items": [
            {
              "id": 1,
              "cart_id": 1,
              "product_id": 5,
              "quantity": 1,
            },
            {
              "id": 2,
              "cart_id": 1,
              "product_id": 12,
              "quantity": 1,
            },
            {
              "id": 3,
              "cart_id": 1,
              "product_id": 17,
              "quantity": 1,
            },
            {
              "id": 4,
              "cart_id": 1,
              "product_id": 18,
              "quantity": 1,
            }
          ]
        }
      ]
    }
    ```

* Error Response: Body validation error
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Validation Error",
      "status_code": 400,
      "errors": {
        "purchased": "Purchased status is required",
      }
    }
    ```
    
### Remove a Cart Item

Deletes a cart item by the cart item's id.

* Require Authentication: true
* Require proper authorization: Cart must belong to the current user
* Request
  * Method: DELETE
  * URL: /api/users/cart/:cart_item_id
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Successfully deleted",
      "status_code": 200
    }
    ```

* Error response: Couldn't find a Cart Item with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Cart Item couldn't be found",
      "status_code": 404
    }
    ```

## Product Images

### Update Product Image URL

Updates the URL of a product image by its id.

* Require Authentication: true
* Require proper authorization: Image must belong to a product that belongs to the current user
* Request
  * Method: PUT
  * URL: /api/Product_Images/:product_image_id
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "url": "image url"
    }
    ```

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "id": 1,
      "product_id": 1,
      "url": "image url"
    }
    ```
    
* Error response: Body validation errors
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Validation error",
      "status_code": 400,
      "errors": {
        "url": "Image URL is required"
      }
    }
    ```

* Error response: Couldn't find a Product Image with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Product Image couldn't be found",
      "status_code": 404
    }
    ```

### Delete a Product Image

Delete an existing image for a Product.

* Require Authentication: true
* Require proper authorization: Image must belong to a product that belongs to the current user
* Request
  * Method: DELETE
  * URL: /api/Product_Images/:product_image_id
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Successfully deleted",
      "status_code": 200
    }
    ```

* Error response: Couldn't find a Product Image with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Product Image couldn't be found",
      "status_code": 404
    }
    ```

## Favorites

### Get Current User's Favorite Products

Returns the Current User's favorited Products.

* Require Authentication: true
* Request
  * Method: GET
  * URL: /api/favorites/current
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "Favorites": [
        {
          "id": 1,
          "title": "Whiskey-flavored Soap",
          "description": "Clean your bits with soap that smells (and tastes) like whiskey!",
          "detailed_description": "Let the sultry aroma of triple-distilled Irish whiskey cleanse you from the inside and out. Smelling like an alcoholic has never been so classy.",
          "category_id": 1,
          "price": 24.99,
          "preview_img_id": 1,
        },
        {
          "id": 2,
          "title": "Whiskey-flavored Shampoo",
          "description": "Clean your bits with soap that smells (and tastes) like whiskey!",
          "detailed_description": "Let the sultry aroma of triple-distilled Irish whiskey cleanse you from the inside and out. Smelling like an alcoholic has never been so classy.",
          "category_id": 1,
          "price": 29.99,
          "preview_img_id": 2,
        }
      ]
    }
    ```
    
### Add a Favorite to Current User's Favorite Products

Adds a product to the current user's favorites by the product's id.

* Require Authentication: true
* Request
  * Method: POST
  * URL: /api/favorites/current/:product_id
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "product_id": 3
    }
    ```

* Successful Response
  * Status Code: 201
  * Headers:
    * Content-Type: application/json
  * Body:

     ```json
    {
      "Favorites": [
        {
          "id": 1,
          "title": "Whiskey-flavored Soap",
          "description": "Clean your bits with soap that smells (and tastes) like whiskey!",
          "detailed_description": "Let the sultry aroma of triple-distilled Irish whiskey cleanse you from the inside and out. Smelling like an alcoholic has never been so classy.",
          "category_id": 1,
          "price": 24.99,
          "preview_img_id": 1,
        },
        {
          "id": 2,
          "title": "Whiskey-flavored Shampoo",
          "description": "Clean your bits with soap that smells (and tastes) like whiskey!",
          "detailed_description": "Let the sultry aroma of triple-distilled Irish whiskey cleanse you from the inside and out. Smelling like an alcoholic has never been so classy.",
          "category_id": 1,
          "price": 29.99,
          "preview_img_id": 2,
        },
        {
          "id": 3,
          "title": "Whiskey-flavored Conditioner",
          "description": "Clean your bits with soap that smells (and tastes) like whiskey!",
          "detailed_description": "Let the sultry aroma of triple-distilled Irish whiskey cleanse you from the inside and out. Smelling like an alcoholic has never been so classy.",
          "category_id": 1,
          "price": 29.99,
          "preview_img_id": 3,
        },
      ]
    }
    ```

* Error Response: Body validation error
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Validation Error",
      "status_code": 400,
      "errors": {
        "product_id": "Product ID is required."
      }
    }
    ```
    
### Remove a Favorite From Current User's Favorite Products

Deletes an existing product from the current user's favorites.

* Require Authentication: true
* Require proper authorization: Favorite must belong to the current user
* Request
  * Method: DELETE
  * URL: /api/favorites/current/:product_id
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Successfully removed",
      "status_code": 200
    }
    ```

* Error response: Couldn't find a Favorite with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Favorite couldn't be found",
      "status_code": 404
    }
    ```

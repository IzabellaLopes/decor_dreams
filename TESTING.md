# Decor Dreams | Testing

This document provides an overview of the testing strategies applied throughout the development of the Decor Dreams store. It includes various types of testing to ensure functionality, compatibility, usability, and responsiveness of the application.

[Back to README.md](README.md)

---

## CONTENTS

- [Decor Dreams | Testing](#decor-dreams--testing)
  - [CONTENTS](#contents)
  - [User Story Testing](#user-story-testing)
      - [EPIC - Viewing and Navigation](#epic---viewing-and-navigation)
      - [EPIC - User Authentication](#epic---user-authentication)
      - [EPIC - Shop Products](#epic---shop-products)
      - [EPIC - Administration and Store Management](#epic---administration-and-store-management)
      - [EPIC - Design \& Planning](#epic---design--planning)
      - [EPIC - Marketing and SEO](#epic---marketing-and-seo)
  - [Site Administration](#site-administration)
  - [Code Validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#javascript)
---

## User Story Testing

#### EPIC - Viewing and Navigation

| User Story                                                                                                                                                                     | Screenshot                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| *"As a Site User I want to be able to navigate intuitively around the site so that I can easily find the content I'm interested in."*                                       | ![Navigation](documentation/readme_images/features/header.png)          |
| *"As a Site User I want to be able to see a comprehensive list of products available so that I can choose what to explore further."*                                       | ![Shop Products](documentation/readme_images/features/shop_products.png)          |
| *"As a Shopper I want to be able to click on a product so that I can read the full product details."*                                       | ![Product Details](documentation/readme_images/features/product_details.png)          |
| *"As a Shopper I want to be able to view a specific category of products so that I can find what I like more easily and have a smoother time shopping."*                                       | ![Nav Products](documentation/readme_images/features/nav_categories.png)    ![Decoration Products](documentation/readme_images/features/decoration.png)      |
| *"As a Shopper I want to be able to search for products across the website so that I can easily find what I need."*                                       | ![Search](documentation/readme_images/features/search.png)      |
| *"As a Shopper I want to be able to arrange all products by price or title so that I can easily compare and view them."*                                       | ![Sort by](documentation/readme_images/features/sortby.png)      |
| *"As a Site User I want to be able to view a comprehensive list of interior design services provided so that I can understand the scope of each service and easily make an enquiry if I'm interested."*                                       | ![Interior Design](documentation/readme_images/features/interiordesign.png)      |
| *"As a Site User I want to be able to access the testimonials left by other customers so that I can gauge the quality of the Interior Design Services they received."*                                       | ![Testimonials](documentation/readme_images/features/testimonials.png)      |
| *"As a Site User I want to be able to browse through pictures of previous Decor Dreams interior design projects so that I can assess the quality of work and develop trust in the service provider."*                                       | ![Decor Dreams Projects](documentation/readme_images/features/project_gallery.png)      |

#### EPIC - User Authentication

| User Story                                                                                                                                                                     | Screenshot                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| *"As a Site User I want to be able to sign up so that I can have a personal account on Decor Dreams."*                                       | ![Sign up](documentation/readme_images/features/signup.png)          |
| *"As a Site User I want to be able to log in or log out of my account so that I can keep my account secure."*                                       | ![Sign in](documentation/readme_images/features/signin.png) ![Sign out](documentation/readme_images/features/signout.png)         |
| *"As a Site User I want to be able to check my login status so that I can know if I'm logged in or out."*                                       | ![User Logged in](documentation/readme_images/features/user_logged.png)         |
| *"As a Site User I want to be able to access my order history so that I can recall my past purchases."*                                       | ![Order history](documentation/readme_images/features/order_history.PNG)         |
| *"As a Site User I want to be able to save my personal details in my user profile so that I do not have to fill them out for future orders."*                                       | ![Save Personal Details](documentation/readme_images/features/save_personal_details.PNG)         |
| *"As a Site User I want to be able to recover my password if I forget it so that I can regain access to my account."*                                       | ![Password reset](documentation/readme_images/features/password_reset.PNG)         |

#### EPIC - Shop Products

| User Story                                                                                                                                                                     | Screenshot                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| *"As a Shopper I want to be able to add multiple products in varying quantities to my shopping bag so that I can purchase them all together when I'm ready."*                                       | ![Product Details](documentation/readme_images/features/product_details.png)          |
| *"As a Shopper I want to be able to see a running total of my shopping bag as I add items so that I can keep track of the total cost."*                                       | ![Bag success](documentation/readme_images/features/bag_success.png)         |
| *"As a Shopper I want to be able to view a summary of my shopping cart during checkout so that I can review the included products and the total cost before finalizing my purchase."*                                       | ![Shopping Bag](documentation/readme_images/features/shopping_bag.png)          |
| *"As a Shopper I want to be able to modify the quantity of individual products in my shopping bag so that I can easily make changes before finalizing my purchase."*                                       | ![Quantity](documentation/readme_images/features/quantity.PNG)          |
| *"As a Shopper I want to be able to securely enter my payment information easily so that I can ensure a quick and hassle-free purchase process for my selected products."*                                       | ![Payment](documentation/readme_images/features/payment.PNG)          |
| *"As a Shopper I want to be able to view the contents of my shopping bag at any time so that I can review what items are included and the total cost."*                                       | ![Shopping Bag](documentation/readme_images/features/shopping_bag.png)          |
| *"As a Shopper I want to be able to checkout as a guest so that I can make a purchase without having to sign up for an account."*                                       | ![Guest checkout](documentation/readme_images/features/guest_checkout.png)          |
| *"As a Shopper I want to be able to view an order confirmation after completing the checkout process so that I can ensure that my purchase was successful."*                                       | ![Thank you](documentation/readme_images/features/thankyou.png)          |
| *"As a Shopper I want to be able to receive an email confirmation of my order so that I can have a record of my purchase."*                                       | ![Order success](documentation/readme_images/features/order_success.PNG)         |

#### EPIC - Administration and Store Management

| User Story                                                                                                                                                                     | Screenshot                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| *"As a Store Owner I want to be able to add, edit, and delete products using a user-friendly interface so that I can ensure smooth management of the store's contents."*                                       | ![Add a Product](documentation/readme_images/features/products_add.png) ![Edit a Product](documentation/readme_images/features/products_edit.png) ![Delete a Product](documentation/readme_images/features/products_delete.png)         |
| *"As a Store Owner I want to be able to add, edit, and delete interior design services using a simple interface so that I can manage the site's content."*                                       | ![Add Interior Design](documentation/readme_images/features/interiordesign_add.png) ![Edit Interior Design](documentation/readme_images/features/interiordesign_edit.png) ![Delete Interior Design](documentation/readme_images/features/interiordesign_delete.png)         |
| *"As a Store Owner I want to be able to add, edit, and delete images and locations of previous Decor Dreams design projects so that I can effectively manage the site's content."*                                       | ![Add Decor Dreams Project](documentation/readme_images/features/project_add.PNG) ![Edit Decor Dreams Project](documentation/readme_images/features/project_edit.png) ![Delete Decor Dreams Project](documentation/readme_images/features/project_delete.PNG)         |
| *"As a Store Owner I want to be able to view and delete customer enquiries directly on the front-end so that I can manage them without having to access the admin panel."*                                       | ![Consultation Dashboard](documentation/readme_images/features/consultation_dashboard.png) ![Consultation Detail](documentation/readme_images/features/consultation_detail.png) ![Delete Consultation](documentation/readme_images/features/delete_consultation.PNG)         |

#### EPIC - Design & Planning

| User Story                                                                                                                                                                     | Screenshot                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| *"As a Site User I want to be able to submit an enquiry form so that I can contact the site owner."*                                       | ![Contact](documentation/readme_images/features/contact.png)         |
| *"As a Site User I want to be able to add, edit, or delete a testimonial related to a consultation I received so that I can provide my feedback."*                                       | ![Add Testimonials](documentation/readme_images/features/testimonials_add.png) ![Edit Testimonials](documentation/readme_images/features/testimonials_edit.png) ![Delete Testimonials](documentation/readme_images/features/testimonial_delete.PNG)         |

#### EPIC - Marketing and SEO

| User Story                                                                                                                                                                     | Screenshot                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| *"As a Site User I want to be able to sign up for the Decor Dreams' newsletter so that I can stay informed about new products and promotions."*                                       | ![Mailchimp](documentation/readme_images/features/mailchimp.png)         |
| *"As a Developer I want to be able to create a Facebook marketing promotional page to spotlight the Decor Dreams so that I can attract potential customers to the website."*                                       | ![Facebook Business page](documentation/readme_images/design/facebook.png)         |

[Back to Contents](#contents)

---

## Site Administration

- Admins possess complete access to Create, Read, Update, and Delete (CRUD) functionalities for all products, categories, interior design services, Decor Dreams projects, testimonials, and users within the admin panel.

![Admin](documentation/readme_images/features/admin.png)

[Back to Contents](#contents)

---

## Code Validation

### HTML

I've used [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page                           | Screenshot | Notes     |
|--------------------------------|------------|-----------|
| Home                           | ![screenshot](documentation/readme_images/testing/html_validation/home.png)  | Pass: No Errors |
| Products                       | ![screenshot](documentation/readme_images/testing/html_validation/products.png)  | Pass: No Errors |
| Product Details                | ![screenshot](documentation/readme_images/testing/html_validation/product_details.PNG)  | Pass: No Errors |
| Add Product                    | ![screenshot](documentation/readme_images/testing/html_validation/add_product.PNG)        | Pass: No Errors      |
| Edit Product                   | ![screenshot](documentation/readme_images/testing/html_validation/edit_product.PNG)        | Pass: No Errors      |
| Confirm Delete Product         | ![screenshot](documentation/readme_images/testing/html_validation/delete_product.PNG)        | Pass: No Errors |
| Bag                            | ![screenshot](documentation/readme_images/testing/html_validation/bag.PNG)  | Pass: No Errors |
| Checkout                       | ![screenshot](documentation/readme_images/testing/html_validation/checkout_success.PNG)  | Pass: No Errors |
| Profile                        | ![screenshot](documentation/readme_images/testing/html_validation/profile.PNG)        | Pass: No Errors |
| Search                         | ![screenshot](documentation/readme_images/testing/html_validation/search.PNG)        | Pass: No Errors |
| Interior Design Services       | ![screenshot](documentation/readme_images/testing/html_validation/interior_design.PNG)  | Pass: No Errors |
| Add Interior Design Service    | ![screenshot](documentation/readme_images/testing/html_validation/add_interior.PNG)        | Pass: No Errors      |
| Edit Interior Design Service   | ![screenshot](documentation/readme_images/testing/html_validation/edit_interior.PNG)        | Pass: No Errors      |
| Delete Interior Design Service | ![screenshot](documentation/readme_images/testing/html_validation/delete_interior.PNG)        | Pass: No Errors |
| Decor Dreams Projects          | ![screenshot](documentation/readme_images/testing/html_validation/decor_projects.PNG)  | Pass: No Errors |
| Add Interior Design Project    | ![screenshot](documentation/readme_images/testing/html_validation/add_decor.PNG)        | Pass: No Errors      |
| Edit Decor Dreams Projects     | ![screenshot](documentation/readme_images/testing/html_validation/edit_decor.PNG)  | Pass: No Errors |
| Delete Interior Design         | ![screenshot](documentation/readme_images/testing/html_validation/delete_decor.PNG)        | Pass: No Errors |
| Testimonials                   | ![screenshot](documentation/readme_images/testing/html_validation/testimonials.PNG)  | Pass: No Errors |
| Add Testimonial                | ![screenshot](documentation/readme_images/testing/html_validation/add_testimonial.PNG)        | Pass: No Errors |
| Edit Testimonial               | ![screenshot](documentation/readme_images/testing/html_validation/edit_testimonial.PNG)        | Pass: No Errors |
| Delete Testimonial             | ![screenshot](documentation/readme_images/testing/html_validation/delete_testimonial.PNG)        | Pass: No Errors |
| Contact                        | ![screenshot](documentation/readme_images/testing/html_validation/contact.PNG)  | Pass: No Errors |
| Consultation Dashboard         | ![screenshot](documentation/readme_images/testing/html_validation/consultation.PNG)        | Pass: No Errors |
| Consultation Detail            | ![screenshot](documentation/readme_images/testing/html_validation/consultation_detail.PNG)        | Pass: No Errors |
| Delete Consultation            | ![screenshot](documentation/readme_images/testing/html_validation/delete_consultation.PNG)        | Pass: No Errors |
| Sign In                        | ![screenshot](documentation/readme_images/testing/html_validation/signin.PNG)  | Pass: No Errors |
| Sign Up                        | ![screenshot](documentation/readme_images/testing/html_validation/signup.PNG)  | Pass: No Errors |
| Log Out                        | ![screenshot](documentation/readme_images/testing/html_validation/logout.PNG)        | Pass: No Errors |
| Password Reset                 | ![screenshot](documentation/readme_images/testing/html_validation/password_reset.PNG)  | Pass: No Errors |

### CSS

No errors were found when passing my CSS files through the official [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

| Page                           | Screenshot | Notes     |
|--------------------------------|------------|-----------|
| *base.css*                     | ![base_css](documentation/readme_images/testing/css_validation/css.PNG)  | Pass: No Errors |
| *checkout.css*                 | ![checkout_css](documentation/readme_images/testing/css_validation/checkout_css.PNG)  | Pass: No Errors |
| *profile.css*                  | ![profile_css](documentation/readme_images/testing/css_validation/profile_css.PNG)  | Pass: No Errors |

### JavaScript

All Javascript was passed through [JSHint](https://jshint.com/) with no issues.

| File                           | Screenshot | Notes     |
|--------------------------------|------------|-----------|
| *base*                     | ![base_js](documentation/readme_images/testing/js_validation/base.PNG)  | Pass: No Errors |
| *main nav*                     | ![main_nav](documentation/readme_images/testing/js_validation/main-nav.PNG)  | Pass: No Errors |
| *products*                     | ![products](documentation/readme_images/testing/js_validation/products.PNG)  | Pass: No Errors |
| *bag*                     | ![bag](documentation/readme_images/testing/js_validation/bag.PNG)  | Pass: No Errors |
| *stripe elements*                     | ![stripe](documentation/readme_images/testing/js_validation/stripe_elements.js_js.png)  | Pass: No Errors |
| *image selector*                     | ![add_image](documentation/readme_images/testing/js_validation/add_image.PNG)  | Pass: No Errors |
| *profile*                     | ![profile](documentation/readme_images/testing/js_validation/profile.PNG)  | Pass: No Errors |
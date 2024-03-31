# Decor Dreams

![Home Page]()

Welcome to [Decor Dreams](https://decor-dreams-ff212364915e.herokuapp.com/), your destination for all your home decor needs!

Discover our top-notch collection of furniture and decor items, from cozy sofas to elegant tables and chairs, along with outdoor essentials and beautiful decorations. Plus, take advantage of our expert team's insights by scheduling a consultation right here in Dublin, Ireland, and delve into the world of interior design with ease.

This is a fictional B2C e-commerce store created for educational purposes as part of the Portfolio of Code Institute.

## CONTENTS

- [Decor Dreams](#decor-dreams)
  - [CONTENTS](#contents)
  - [User Experience (UX)](#user-experience-ux)
    - [Target Audience](#target-audience)
    - [User Stories](#user-stories)
  - [Design](#design)
    - [Color Scheme](#color-scheme)
    - [Imagery](#imagery)
    - [Typography](#typography)
    - [Wireframes](#wireframes)
  - [Agile Methodology](#agile-methodology)
  - [Database Diagram](#database-diagram)
  - [Security Features and Defensive Design](#security-features-and-defensive-design)
    - [User Authentication](#user-authentication)
    - [Form Validation](#form-validation)
    - [Database Security](#database-security)
    - [Cross-Site Request Forgery (CSRF) Protection](#cross-site-request-forgery-csrf-protection)
    - [Custom Error Pages](#custom-error-pages)
  - [Features](#features)
    - [Favicon](#favicon)
    - [Header](#header)
    - [Mailchimp](#mailchimp)
    - [Footer](#footer)
    - [Home Page](#home-page)
    - [User Account Pages](#user-account-pages)
      - [Sign Up](#sign-up)
      - [Sign In](#sign-in)
      - [Sign Out](#sign-out)
    - [Profile](#profile)
    - [Shop Products](#shop-products)
    - [Product Details](#product-details)
    - [Products Management](#products-management)
      - [Add a Product](#add-a-product)
      - [Edit a Product](#edit-a-product)
      - [Delete a Product](#delete-a-product)
    - [Shopping Bag](#shopping-bag)
    - [Checkout](#checkout)
    - [Interior Design](#interior-design)
    - [Interior Design Management](#interior-design-management)
      - [Add a Interior Design Service](#add-a-interior-design-service)
      - [Edit a Interior Design Service](#edit-a-interior-design-service)
      - [Delete a Interior Design Service](#delete-a-interior-design-service)
      - [Decor Dreams Projects](#decor-dreams-projects)
    - [Decor Dreams Projects Management](#decor-dreams-projects-management)
      - [Add a Decor Dreams Project](#add-a-decor-dreams-project)
      - [Edit a Decor Dreams Project](#edit-a-decor-dreams-project)
      - [Delete a Decor Dreams Project](#delete-a-decor-dreams-project)

---

## User Experience (UX)

At Decor Dreams, we adhere to a philosophy of simplicity and user-friendliness in our e-commerce platform design. Recognizing that complex designs can deter potential customers, we've embraced a straightforward approach to ensure a seamless experience. Our primary objective is to create an inviting environment that facilitates easy exploration and purchase of home decor essentials.

**Welcome to Decor Dreams**
<br>
Upon landing on our platform, visitors are greeted with a captivating modern living room image, capturing the essence of decor, accompanied by our tagline: "DECOR YOUR DREAMS - Your destination for all your home decor needs." This visual introduction, coupled with a clear call-to-action button, promptly directs users to our product page or facilitates scheduling a consultation. This streamlined entry point ensures immediate access to our product range or interior design services, without unnecessary distractions.

**Navigational Simplicity**
<br>
Navigating through Decor Dreams is effortless. Users can seamlessly add items to their basket from product listings or detailed product pages. The shopping basket remains a constant fixture within the navigation menu, visible from every page, reinforcing transparency and trust by displaying a running total. This commitment to honesty and customer empowerment eliminates any hidden costs that might arise during checkout.

Our main navigation menu is intuitively designed, allowing users to effortlessly find and filter decor items by category with a simple click. This ease of access extends to the site's footer, where additional filtering options enhance discoverability and user autonomy.

**Connecting with Our Audience**
<br>
In addition to its user-friendly features, Decor Dreams caters to homeowners and interior design enthusiasts, fostering a deeper connection with our audience. Users can explore and purchase a variety of homeware products, discover different types of interior design services, and make inquiries. They can also browse images and testimonials of completed design projects or leave their own feedback.

**Crafting an Engaging Experience**
<br>
The Decor Dreams experience is carefully crafted to be seamless and engaging. With a focus on user-centric design, straightforward navigation, and playful elements, we aim to not only meet the needs of our customers but also provide a delightful journey from initial exploration to final purchase.

### Target Audience

Decor Dreams is designed to cater to the following target audience:

- Homeowners: Individuals looking to enhance their living spaces with stylish and functional furniture and decor items.

- Interior Design Enthusiasts: People passionate about interior design seeking inspiration, guidance, and access to expert consultation services.

- Online Shoppers: Individuals who prefer to shop for home decor items and services online, valuing user-friendly interfaces, transparent pricing, and efficient navigation. They seek a seamless and hassle-free shopping experience.

- Customers Seeking Interior Design Services: Those interested in professional interior design services, including consultations, design planning, and implementation. They may appreciate a platform that not only offers products but also connects them with reputable interior designers.

- Users Looking for Inspiration: Individuals who browse for design ideas, trends, and completed projects to inspire their own home decor endeavors. They value platforms that offer visual content, testimonials, and a community where they can engage and share their experiences.

### User Stories
<details>
<summary><strong>1. EPIC - Initial Set Up</strong></summary>

[EPIC - Initial Set Up](https://github.com/IzabellaLopes/decor_dreams/milestone/1)

- **USER STORY: Initial Django Set Up [#1](https://github.com/IzabellaLopes/decor_dreams/issues/1)** - As a Developer I want to be able to set up a new Django project so that I can create the project's structure
- **USER STORY: Initial Heroku Deployment [#2](https://github.com/IzabellaLopes/decor_dreams/issues/2)** - As a Developer I can perform an early deployment of the application to verify the functionality of the initial set up so that I can continue testing the application as it evolves during development
- **USER STORY: Connect Database and S3 Storage and Stripe [#3](https://github.com/IzabellaLopes/decor_dreams/issues/3)** - As a Developer I want to be able to connect database, static/media storage and stripe payments so that data is accessible on deployment and payments are configured early
</details>
</br>

<details>
<summary><strong>2. EPIC - User Experience (UX) Design Planning</strong></summary>

[EPIC - User Experience (UX) Design Planning](https://github.com/IzabellaLopes/decor_dreams/milestone/2)

- **USER STORY: Wireframes [#6](https://github.com/IzabellaLopes/decor_dreams/issues/6)** - As a Developer I can design wireframes so that I gain a clear understanding of the site's structure and theme
- **USER STORY: Color Theme [#7](https://github.com/IzabellaLopes/decor_dreams/issues/7)** - As a Developer I can refine the color theme for Decor Dreams so that I create an engaging and home decor enthusiasts atmosphere
- **USER STORY: Implement Responsive Layout [#8](https://github.com/IzabellaLopes/decor_dreams/issues/8)** - As a Developer I can optimize Decor Dreams's layout for responsiveness so that ensure a seamless and enjoyable browsing experience across diverse devices for users accessing the Decor Dreams website
- **USER STORY: Site Navigation [#9](https://github.com/IzabellaLopes/decor_dreams/issues/9)** - As a Developer I can enhance Decor Dreams's site navigation so that I provide an intuitive and user-friendly journey within the e-commerce website
- **USER STORY: UX/UI Theming and Styling Enhancement [#10](https://github.com/IzabellaLopes/decor_dreams/issues/10)** - As a Developer I want to be able to refine the UX/UI theming and styling of Decor Dreams so that I can enhance the overall aesthetic appeal and user experience for our customers
</details>
</br>

<details>
<summary><strong>3. EPIC - Viewing and Navigation</strong></summary>

[EPIC - Viewing and Navigation](https://github.com/IzabellaLopes/decor_dreams/milestone/3)

- **USER STORY: Intuitive Site Navigation [#12](https://github.com/IzabellaLopes/decor_dreams/issues/12)** - As a Site User I want to be able to navigate intuitively around the site so that I can easily find the content I'm interested in
- **USER STORY: Browse Products [#13](https://github.com/IzabellaLopes/decor_dreams/issues/13)** - As a Site User I want to be able to see a comprehensive list of products available so that I can choose what to explore further
- **USER STORY: Product Detail [#14](https://github.com/IzabellaLopes/decor_dreams/issues/14)** - As a Shopper I want to be able to click on a product so that I can read the full product details
- **USER STORY: Product Category [#15](https://github.com/IzabellaLopes/decor_dreams/issues/15)** - As a Shopper I want to be able to view a specific category of products so that I can find what I like more easily and have a smoother time shopping
- **USER STORY: Search for Products [#16](https://github.com/IzabellaLopes/decor_dreams/issues/16)** - As a Shopper I want to be able to search for products across the website so that I can easily find what I need
- **USER STORY: Sort Products [#17](https://github.com/IzabellaLopes/decor_dreams/issues/17)** - As a Shopper I want to be able to arrange all products by price or title so that I can easily compare and view them
- **USER STORY: Wishlist Functionality Implementation [#18](https://github.com/IzabellaLopes/decor_dreams/issues/18)** - As a Shopper I want to be able to create a wishlist of desired products so that I can save items for future purchase and easily track them across browsing sessions
- **USER STORY: Browse Interior Design Consultation Services [#19](https://github.com/IzabellaLopes/decor_dreams/issues/19)** - As a Site User I want to be able to view a comprehensive list of interior design services provided so that I can understand the scope of each service and easily make an enquiry if I'm interested
- **USER STORY: View Testimonials [#20](https://github.com/IzabellaLopes/decor_dreams/issues/20)** - As a Site User I want to be able to access the testimonials left by other customers so that I can gauge the quality of the Interior Design Services they received
- **USER STORY: View Decor Dreams Projects [#21](https://github.com/IzabellaLopes/decor_dreams/issues/21)** - As a Site User I want to be able to browse through pictures of previous Decor Dreams interior design projects so that I can assess the quality of work and develop trust in the service provider
</details>
</br>

<details>
<summary><strong>4. EPIC - User Authentication</strong></summary>

[EPIC - User Authentication](https://github.com/IzabellaLopes/decor_dreams/milestone/4)

- **USER STORY: Sign Up [#23](https://github.com/IzabellaLopes/decor_dreams/issues/23)** - As a Site User I want to be able to sign up so that I can have a personal account on Decor Dreams
- **USER STORY: User Log in & Log out [#24](https://github.com/IzabellaLopes/decor_dreams/issues/24)** - As a Site User I want to be able to log in or log out of my account so that I can keep my account secure
- **USER STORY: Login Status [#25](https://github.com/IzabellaLopes/decor_dreams/issues/25)** - As a Site User I want to be able to check my login status so that I can know if I'm logged in or out
- **USER STORY: View Order History [#26](https://github.com/IzabellaLopes/decor_dreams/issues/26)** - As a Site User I want to be able to access my order history so that I can recall my past purchases
- **USER STORY: Save Personal Details in User Profile [#27](https://github.com/IzabellaLopes/decor_dreams/issues/27)** - As a Site User I want to be able to save my personal details in my user profile so that I do not have to fill them out for future orders
- **USER STORY: Password Recovery [#28](https://github.com/IzabellaLopes/decor_dreams/issues/28)** - As a Site User I want to be able to recover my password if I forget it so that I can regain access to my account
</details>
</br>

<details>
<summary><strong>5. EPIC - Shop Products</strong></summary>

[EPIC - Shop Products](https://github.com/IzabellaLopes/decor_dreams/milestone/5)

- **USER STORY: Add Products to Shopping Bag [#30](https://github.com/IzabellaLopes/decor_dreams/issues/30)** - As a Shopper I want to be able to add multiple products in varying quantities to my shopping bag so that I can purchase them all together when I'm ready
- **USER STORY: Total Shopping Bag [#31](https://github.com/IzabellaLopes/decor_dreams/issues/31)** - As a Shopper I want to be able to see a running total of my shopping bag as I add items so that I can keep track of the total cost
- **USER STORY: Checkout Summary [#32](https://github.com/IzabellaLopes/decor_dreams/issues/32)** - As a Shopper I want to be able to view a summary of my shopping cart during checkout so that I can review the included products and the total cost before finalizing my purchase
- **USER STORY: Modify Product Quantity [#33](https://github.com/IzabellaLopes/decor_dreams/issues/33)** - As a Shopper I want to be able to modify the quantity of individual products in my shopping bag so that I can easily make changes before finalizing my purchase
- **USER STORY: Payment Information [#34](https://github.com/IzabellaLopes/decor_dreams/issues/34)** - As a Shopper I want to be able to securely enter my payment information easily so that I can ensure a quick and hassle-free purchase process for my selected products
- **USER STORY: View Shopping Bag [#35](https://github.com/IzabellaLopes/decor_dreams/issues/35)** - As a Shopper I want to be able to view the contents of my shopping bag at any time so that I can review what items are included and the total cost
- **USER STORY: Guest Checkout [#36](https://github.com/IzabellaLopes/decor_dreams/issues/36)** - As a Shopper I want to be able to checkout as a guest so that I can make a purchase without having to sign up for an account
- **USER STORY: View Order Confirmation after Checkout [#37](https://github.com/IzabellaLopes/decor_dreams/issues/37)** - As a Shopper I want to be able to view an order confirmation after completing the checkout process so that I can ensure that my purchase was successful
- **USER STORY: Email Confirmation [#38](https://github.com/IzabellaLopes/decor_dreams/issues/38)** - As a Shopper I want to be able to receive an email confirmation of my order so that I can have a record of my purchase
</details>
</br>

<details>
<summary><strong>6. EPIC - Administration and Store Management</strong></summary>

[EPIC - Administration and Store Management](https://github.com/IzabellaLopes/decor_dreams/milestone/6)

- **USER STORY: Product Management [#40](https://github.com/IzabellaLopes/decor_dreams/issues/40)** - As a Store Owner I want to be able to add, edit, and delete products using a user-friendly interface so that I can ensure smooth management of the store's contents
- **USER STORY: Design & Planning Services Management [#41](https://github.com/IzabellaLopes/decor_dreams/issues/41)** - As a Store Owner I want to be able to add, edit, and delete interior design services using a simple interface so that I can manage the site's content
- **USER STORY: Decor Dreams Projects Management [#42](https://github.com/IzabellaLopes/decor_dreams/issues/42)** - As a Store Owner I want to be able to add and delete images and locations of previous Decor Dreams design projects so that I can effectively manage the site's content
- **USER STORY: Enquiries Dashboard [#43](https://github.com/IzabellaLopes/decor_dreams/issues/43)** - As a Store Owner I want to be able to view and delete customer enquiries directly on the front-end so that I can manage them without having to access the admin panel
</details>
</br>

<details>
<summary><strong>7. EPIC - Design & Planning</strong></summary>

[EPIC - Design & Planning](https://github.com/IzabellaLopes/decor_dreams/milestone/7)

- **USER STORY: Design & Planning Consultation Enquiry [#45](https://github.com/IzabellaLopes/decor_dreams/issues/45)** - As a Site User I want to be able to submit an enquiry form so that I can contact the site owner
- **USER STORY: Manage Testimonials [#46](https://github.com/IzabellaLopes/decor_dreams/issues/46)** - As a Site User I want to be able to add, edit, or delete a testimonial related to a consultation I received so that I can provide my feedback
</details>
</br>

<details>
<summary><strong>8. EPIC - Marketing and SEO</strong></summary>

[EPIC - Marketing and SEO](https://github.com/IzabellaLopes/decor_dreams/milestone/8)

- **USER STORY: Newsletter [#48](https://github.com/IzabellaLopes/decor_dreams/issues/48)** - As a Site User I want to be able to sign up for the Decor Dreams' newsletter so that I can stay informed about new products and promotions
- **User Story: SEO [#49](https://github.com/IzabellaLopes/decor_dreams/issues/49)** - As a Developer I want to be able to configure SEO information about the website so that users can easily access content
- **USER STORY: Facebook marketing promotional page [#50](https://github.com/IzabellaLopes/decor_dreams/issues/50)** - As a Developer I want to be able to create a Facebook marketing promotional page to spotlight the Decor Dreams so that I can attract potential customers to the website
- **USER STORY: Robots.txt [#51](https://github.com/IzabellaLopes/decor_dreams/issues/51)** - As a Developer I want to be able to make a robots.txt file so that I can control which parts of my website search engines can see
- **USER STORY: SiteMap.xml [#52](https://github.com/IzabellaLopes/decor_dreams/issues/52)** - As a Developer I want to be able to make an SEO sitemap so that search engines can easily find and understand all the pages on my website
</details>
</br>

<details>
<summary><strong>9. EPIC - Documentation</strong></summary>

[EPIC - Documentation](https://github.com/IzabellaLopes/decor_dreams/milestone/9)

- **Documentation - README file [#54](https://github.com/IzabellaLopes/decor_dreams/issues/54)**
- **Code Documentation [#55](https://github.com/IzabellaLopes/decor_dreams/issues/55)**
</details>
</br>

[Back to Contents](#contents)

---

## Design

Decor Dreams's design is intentionally crafted to be simple and clean.

### Color Scheme

Decor Dreams' color palette showcases tones of green and gold, cultivating a contemporary and chic aesthetic that harmonizes seamlessly with the hero call-out image on the homepage.

In my CSS file, I employed variables to define colors and consistently applied them across the entire stylesheet. It enables easy color updates throughout the website by modifying the color once in the variable, maintaining consistency across the design.

Great care was taken to establish a good contrast between background colors and text at all times to ensure maximum user accessibility, confirmed through the [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/).

The color palette was generated using the [Coolors](https://coolors.co/) website.

![Coolors](documentation/readme_images/design/color_scheme.png)

### Imagery

The images utilized in Decor Dreams were generated by [Lexica Art](https://lexica.art/). Moreover, I created the logo using [Canva](https://www.canva.com/). Credits for the images can be found in the "Credits" section.

### Typography

In Decor Dreams, the following sans-serif fonts, obtained from Google Fonts, were carefully chosen to enhance the overall visual appeal:

- [Comfortaa](https://fonts.google.com/specimen/Comfortaa?preview.text=Decor%20Dreams&query=comfor) for Header:

![Comfortaa](documentation/readme_images/design/comfortaa.png)

- [Open Sans](https://fonts.google.com/specimen/Open+Sans?preview.text=Decor%20Dreams&query=open) for Content:

![Open Sans](documentation/readme_images/design/open_sans.png)

### Wireframes

I utilized Balsamiq to design the wireframes for the website.

<details>
 <summary>Home Page</summary>

![Home Page](documentation/wireframes/home.png)
</details>

<details>
 <summary>Shop Products</summary>

![Shop Products](documentation/wireframes/shop_products.png)
</details>

<details>
 <summary>Product Details</summary>

![Product Details](documentation/wireframes/product_details.png)
</details>

<details>
 <summary>Interior Design</summary>

![Interior Design](documentation/wireframes/interior_design.png)
</details>

<details>
 <summary>Decor Dreams Projects</summary>

![Decor Dreams Projects](documentation/wireframes/decor_dreams_projects.png)
</details>

<details>
 <summary>Testimonials</summary>

![Testimonials](documentation/wireframes/testimonials.png)
</details>

<details>
 <summary>Contact</summary>

![Contact](documentation/wireframes/contact.png)
</details>

<details>
 <summary>Shopping Bag</summary>

![Shopping Bag](documentation/wireframes/shopping_bag.png)
</details>

<details>
 <summary>Checkout</summary>

![Checkout](documentation/wireframes/checkout.png)
</details>

<details>
 <summary>Order Confirmation</summary>

![Order Confirmation](documentation/wireframes/order_confirmation.png)
</details>

<details>
 <summary>Consultation</summary>

![Consultation](documentation/wireframes/consultation.png)
</details>

<br>

[Back to Contents](#contents)

---

## Agile Methodology

GitHub Projects was utilized to facilitate the development process following an agile methodology. You can refer to the project board through this [link](https://github.com/users/IzabellaLopes/projects/3).

The 9 Epics mentioned earlier were documented as Milestones within the GitHub project. Each User Story was represented by a GitHub Issue, which was subsequently assigned to a milestone (Epic). Clear acceptance criteria were defined for each User Story to indicate when it is considered complete. Furthermore, these acceptance criteria were detailed into tasks, streamlining the execution of each User Story.

[Back to Contents](#contents)

---

## Database Diagram

The Decor Dreams project's data model adheres to Object-Oriented Programming principles and utilizes Django's Class-Based Generic Views.

User authentication is managed through Django AllAuth.

During development, SQLite was utilized as the relational database, while Postgres was employed for the Heroku-deployed version.

An entity relationship diagram was crafted using [Lucidchart](https://lucid.app/documents#/dashboard).

![Database Diagram](documentation/readme_images/database/db_diagram.png)

[Back to Contents](#contents)

---

## Security Features and Defensive Design

In the Decor Dreams project, robust user authentication and security features have been implemented to ensure a secure and reliable user experience.

### User Authentication

In Decor Dreams, I've implemented robust security measures for user authentication.

- LoginRequiredMixin: Employing Django's `LoginRequiredMixin`, any attempt by non-authenticated users to access secure pages results in an automatic redirection to the login page. This ensures that sensitive sections of the application are accessible only to authenticated users.

- UserPassesTestMixin: To finely control access based on specific permissions, I utilize Django's `UserPassesTestMixin`. For example, users can only edit/delete Testimonials for which they are the author or if the user is the superuser. If a user fails these tests, a clear HTTP 403 Forbidden error is displayed, maintaining a secure environment.

Where I have used function based views I have used Django's login_required and user_passes_test decorators to restrict access as required.

### Form Validation

I've implemented thorough form validation mechanisms to enhance data integrity.

- If incorrect or empty data is detected in a form submission, the form prevents submission, and a user-friendly warning appears. This approach ensures that users receive prompt feedback about the specific fields causing errors.

### Database Security

My approach to database security prioritizes confidentiality and protection against unauthorized access.

- The database URL and secret key are stored in a separate env.py file, preventing unintended database connections. 
- Stripe keys and wh secret are also stored in the env.py file. 

This practice was established before the initial push to Github, safeguarding sensitive information.

### Cross-Site Request Forgery (CSRF) Protection

Decor Dreams employs CSRF tokens on all forms throughout the site, providing an additional layer of defense against cross-site request forgery attacks.

### Custom Error Pages

Custom Error Pages were created to give the user more information on the error and to provide them with buttons to guide them back to the site.

- 400 Bad Request: The Decor Dreams is unable to process a request, providing a clear message to the user.
- 403 Forbidden: In cases of attempting to access forbidden content, the user is guided to log out and sign in to the correct account through a custom 403 Forbidden page.
- 404 Not Found: A custom 404 page assists users in navigating back to the site when the requested page doesn't exist.
- 500 Internal Server Error:  During server errors, users are informed through a custom 500 Internal Server Error, helping them understand the temporary unavailability of certain functionalities.

[Back to Contents](#contents)

---

## Features

### Favicon

The website features a favicon that is visible in the browser tab.

![Favicon](documentation/readme_images/features/favicon.png)

### Header

![Header](documentation/readme_images/features/header.png)

**Logo**

I created two custom logos using Canva:
  
- One in a horizontal format tailored for larger devices:
![Logo](documentation/readme_images/features/logo.png)

- And another in a rounded shape suitable for medium and small devices.
![Logo-sm](documentation/readme_images/features/logo_sm.png)

- The text is styled in dark green, while the circle surrounding it is light green, mirroring the main color scheme of the website. 
- Positioned in the center is a modern house with a flourishing plant, symbolizing the growth of dreams to decorate your house.
- The logo is situated in the top-left corner of the navigation bar and serves as a clickable link to the home page, enhancing user navigation.

**Navigation Bar**

- The navigation bar is consistently located at the top of each page, providing easy access to various sections.

**Search Bar**

![Search](documentation/readme_images/features/search.png)
- The search bar appears above the navigation bar.
- On smaller screens, this bar transforms into a search icon. Upon clicking the icon, the full search bar drops down.
- Any entered search term will be matched against the product's title or description, and the results will be displayed on the product's page.

**User Icon**

- The User icon in the navigation bar serves as a dropdown menu containing the "Register" and "Sign in" links.
  
![User Non logged in](documentation/readme_images/features/user_nonlogged.png)

  - Once a user logs in, their username will be displayed below the user icon.
The options to "Register" or "Sign in" will change to "Log out" after a user has logged in.
- After logging in, the "My Profile" option becomes accessible in the User dropdown.

![User Logged in](documentation/readme_images/features/user_logged.png)

- If the superuser has signed in, additional options such as 'Add a Product', 'Add an Interior Design Service', 'Add a Decor Dreams Project', and 'Check Consultations' become available in the User dropdown.
  
![Superuser Logged in](documentation/readme_images/features/superuser_logged.png)

- The navigation bar is fully responsive, collapsing into a hamburger menu when the screen size becomes too small.
- When hovering over the links, the font color changes to green and a golden bottom border appears.
- Additionally, when a link is active, it will feature a golden bottom border.

**Bag Icon**

![Bag](documentation/readme_images/features/bag.png)

- Situated on the right side of the navbar next to the User icon is the Bag icon.
- When a product is added to the bag, the initial price of €0.00 will adjust according to the items in the bag.
- As the user adds more products to their bag, a toast message appears in the top right corner of the screen, informing the user of the added item. It includes a quick view of the bag contents and the updated total cost.

![Bag Total](documentation/readme_images/features/bag_total.png)

- Clicking the bag icon navigates the user to the shopping bag page which displays a summary of what's been added.

**Banner**

![Banner](documentation/readme_images/features/banner.png)

- Below the navigation bar is an animated banner, where the sign "Free delivery on orders over €250!" grabs users' attention to encourage purchases. 
- The €250 threshold can be easily adjusted in the settings.py file by modifying the FREE_DELIVERY_THRESHOLD variable.

### Mailchimp

![Mailchimp](documentation/readme_images/features/mailchimp.png)

- There is a newsletter signup section powered by Mailchimp, allowing users to enter their email address to subscribe to newsletters and receive email updates about our new stock.

### Footer

![Footer](documentation/readme_images/features/footer.png)

- The footer is visible at the bottom of each page.
- It contains a link to the [Decor Dreams Facebook page](https://www.facebook.com/people/Decor-Dreams/61557145091799/). Clicking on external links will open the respective website in a new tab, preventing users from being redirected away from the site.
- The Quick Links section provides access to key parts of the site, including the ['Privacy Policy'](https://www.termsfeed.com/live/7bb0d942-6e1d-46d9-ac3c-1fe8a915cdb6).
- On the right-hand side of the footer, icons representing various payment methods are displayed to draw attention and encourage users to make purchases.

### Home Page

**Hero-callout section**

- The homepage showcases a prominent callout section with an animated slogan: "DECOR YOUR DREAMS: Your destination for all your home decor needs."
- Additionally, it includes two primary links for users: "Shop now," which directs users to browse products, and "Schedule a consultation," which redirects users to the Interior Design Service page.

![Hero](documentation/readme_images/features/hero.png)

**Who we are section**

The "Who we are" section offers a brief summary of the site's offerings, highlighting key features and incorporating relevant keywords within <strong></strong> tags to enhance the site's search ranking

![Who we are](documentation/readme_images/features/who_we_are.png)

### User Account Pages

- Django Allauth was installed and utilized to implement Sign Up, Log In, and Log Out functionalities. 
- Success messages inform users about successful login and logout actions, while error messages notify them of any unsuccessful attempts during these processes.
- When a user registers for an account, they need to verify their email address by clicking on the authentication link sent to the provided email address.
- If a user forgets their password, they can reset it by clicking on the 'Forgot Password' link on the login page.

#### Sign Up
![Sign up](documentation/readme_images/features/signup.png)

#### Sign In
![Sign in](documentation/readme_images/features/signin.png)

#### Sign Out
![Sign out](documentation/readme_images/features/signout.png)

### Profile

![Profile](documentation/readme_images/features/profile.png)

**Delivery Details Information**

- The delivery details section stores the user's delivery address and phone number, where the user can also update their information.
- This information is utilized to automatically populate the delivery address during the checkout process.

**Order History**

- The order history section exhibits a comprehensive list of all the user's placed orders.
- Within the table, users can view the order number, order date, and total amount.
- By clicking on the order number, users are directed to a summary page providing details of that specific order.

### Shop Products

![Shop Products](documentation/readme_images/features/shop_products.png)

- Upon selecting the 'Shop Products' link in the navigation bar, a dropdown menu will appear, presenting various categories such as 'Sofas,' 'Tables & Desks,' 'Chairs,' 'Outdoor Living,' and 'Decoration.'

![Nav Products](documentation/readme_images/features/nav_categories.png)

- The 'All Products' link will showcase a list of all products sourced from the database. 
- Upon clicking any category, the product list will be filtered to exclusively exhibit items belonging to the chosen category.
- The chosen category will then be prominently displayed as the heading of the page.

![Decoration Products](documentation/readme_images/features/decoration.png)

- Every product card features an image of the product, along with its product name, and price. 
- For superusers, additional edit and delete buttons are displayed at the bottom of each product card.
- The products page is designed to be fully responsive, dynamically adjusting the number of products displayed on each row according to the user's screen size.
- Additionally, a sorting box is available on the products page, allowing users to sort all products by price in ascending or descending order, as well as by title in alphabetical order.

![Sort by](documentation/readme_images/features/sortby.png)

### Product Details

![Product Details](documentation/readme_images/features/product_details.png)

- When a user clicks on an individual product card, they are directed to the complete product details page. The link is designed as a bootstrap stretched link, allowing users to click anywhere on the card to access the details.

- On the product detail page, users can view the product image, name, and price. If the user is a superuser, they will see edit and delete buttons beneath these details.

**Quantity Buttons:**
- Below the main product details, users will find quantity buttons used to add items to their bag.
- These buttons allow users to increase or decrease the quantity by clicking the plus and minus buttons respectively.
- The minus button is disabled when the quantity is set to 1, and the plus button is disabled when the quantity is set to 99.
- If a user manually enters a negative number or a number greater than 99 and clicks "Add to Bag," an error message will appear, prompting the user to input valid parameters.
- Clicking the 'Add to Bag' button adds the specified quantity of the product to the bag, while clicking 'Keep Shopping' returns the user to the store.

**Product Details Accordion:**
- Below these main details lies the product details accordion, an interactive box where users can select information such as:

- Description:
![Description](documentation/readme_images/features/description.png)

- Details and Dimensions:
![Details and dimensions](documentation/readme_images/features/details_dimensions.png)

- Delivery and Returns:
![Delivery and returns](documentation/readme_images/features/delivery_returns.png)

### Products Management

#### Add a Product

![Add a Product](documentation/readme_images/features/products_add.png)

- The "Add Product" page is accessible by clicking the corresponding button on the products page or within the user dropdown menu, under the "Add a Product" section. These options are exclusively visible to superusers.

- If a user attempts to access the add product page by altering the URL without superuser privileges, they will be redirected to the sign in page.

- To successfully submit the form, the user must complete all fields marked with an asterisk.
  
- If any of these mandatory fields are left blank or contain only whitespace upon submission, an error message will appear above the respective field, alerting the user to the issue.

![Error form](documentation/readme_images/features/error_form.PNG)

- The SKU field must be unique; if the entered SKU already exists, an error message will be displayed.

![Sku](documentation/readme_images/features/sku.PNG)

- If the price entered exceeds six digits, the form will fail, and an error message will appear beneath the price field.

- Users have the option to upload a photo for their product. If they opt not to, a default image will be displayed as the product image.

- Upon clicking the "Add Product" button at the bottom of the form, the product will be created, provided there are no errors present.

- A success message will be displayed, informing the user that the product has been successfully added.

![Add success](documentation/readme_images/features/add_success.PNG)

#### Edit a Product

![Edit a Product](documentation/readme_images/features/products_edit.png)

- The superuser has the option to edit a product either by clicking the edit button on the product card or on the product detail page.

- Upon opening the edit form, all fields are pre-populated with the original content.

- In the image field, a thumbnail of the existing image is displayed, along with a checkbox option to remove it. Checking this checkbox will replace the image with the default one.

- If a user attempts to edit a product by altering the URL without superuser privileges, they will be redirected to the sign in page.

- Upon successful update, the superuser will receive a notification confirming that the product has been successfully updated.

![Edit success](documentation/readme_images/features/edit_sucess.PNG)

#### Delete a Product

![Delete a Product](documentation/readme_images/features/products_delete.png)

- The superuser has the option to delete a product by clicking the delete button on either the product card or the product detail page.

- Upon clicking the delete button, the superuser is prompted to confirm their decision to delete the product or to cancel the action.

- Once the deletion process is successfully executed, the superuser will receive a notification confirming that the product has been deleted.

![Delete success](documentation/readme_images/features/delete_sucess.png)

### Shopping Bag

- After successfully adding a product, the shopper will receive a notification confirming the successful addition of the product to their bag.

![Bag success](documentation/readme_images/features/bag_success.png)

- Clicking either on the shopping bag icon in the navigation bar or on the "Go to secure checkout" button in the previous message redirects users to the shopping bag page.

![Shopping Bag](documentation/readme_images/features/shopping_bag.png)

- This page displays all the products that users have added to their cart, along with details such as unit price, quantity, and subtotal.

**Quantity Buttons:**

- The quantity input box on this page reflects the quantity of each product added to the bag.
- Users can adjust the quantity using the plus and minus buttons:
  
![Quantity](documentation/readme_images/features/quantity.PNG)

- The plus button increases the quantity.
- The minus button decreases the quantity.
- If the quantity is set to 1, the minus button is disabled.
- Similarly, if the quantity reaches 99, the plus button becomes disabled.

**Update and Delete Buttons:**

- Users have the option to update or delete items from their shopping bag using the corresponding buttons provided on the page.

![Update and delete](documentation/readme_images/features/update_delete.PNG)

- Clicking the 'Update' icon button saves any changes made to the quantity and updates the item's subtotal accordingly.
- Pressing the 'Bin' icon button removes the item entirely from the user's bag. 
- If the user inputs a negative number manually and clicks 'update', the respective item will be removed from the bag. 
- Similarly, if the user enters a number greater than 99 and clicks 'update', an error message will appear, prompting the user to input within the correct parameters.

![Error quantity](documentation/readme_images/features/error_quantity.png)

**Total Section:**

- At the bottom of the line items, a summary of costs is provided. 
- This summary includes the total cost of the items in the bag, the delivery cost, and the grand total to pay. 
- Below the grand total, users will find a message indicating how much more they need to spend to qualify for free delivery if they haven't yet met the threshold (€ 250).
- Additionally, two buttons are available below the grand total: users can either return to the products page by clicking 'Keep Shopping' or proceed to checkout by clicking 'Secure Checkout'.

![Bag total section](documentation/readme_images/features/bag_total_section.PNG)

### Checkout

![Checkout](documentation/readme_images/features/checkout.png)

**Users Details:**
- In this section, users can input their contact details, delivery address, and card number for making purchases.
- If the user is a guest, they will find a link to create an account or login.
![Guest](documentation/readme_images/features/guest.png)
- For signed-in users, a checkbox is available to save delivery information. 
- If delivery information is saved, it will be automatically filled in along with the email address.
- Error messages will prompt users to fill in required fields or match the requested format if any discrepancies are found.

**Order Summary:**
- The order summary provides a breakdown of all items to be purchased, including quantity, subtotal, and grand total. 
- The total number of items in the order is displayed alongside the summary title.
- Clicking on a product image within the summary redirects the user to the corresponding product detail page.

**Payment:**
- Payment processing is securely handled by Stripe. 
- Incorrect card numbers trigger an error message indicating an invalid card number. 
- A loading screen prevents users from navigating away while payment is being processed. 
- A warning message displays the impending charge on the user's card. 
- In case of submission errors or browser closure during processing, orders are still created in the database through the webhook. 
- Upon successful payment processing, the webhook verifies the existence of the order in the database and creates one if not found, using the payment information provided.

**Confirmation:**
- After the order is processed, the user is directed to the checkout success page, which provides a summary of the completed order. 
![Thank you](documentation/readme_images/features/thankyou.png)

- Additionally, a success message is displayed, and an email containing the order confirmation is sent to the user. 
![Order success](documentation/readme_images/features/order_success.PNG)
  
- At the bottom of the summary, a "Keep Shopping" button is available, allowing the user to return to the 'Shop products' page.

### Interior Design

![Interior Design](documentation/readme_images/features/interiordesign.png)

- The Interior Design page is accessible via the link in the navigation bar. 
- Upon arrival, users are greeted with a thorough list of services offered by Decor Dreams, including 'Full Interior Design Services', 'Color Consultation', 'Lighting Design', and 'Outdoor Living Design'. 
- Each service is accompanied by images, titles, and detailed descriptions. 
- An "Schedule a Consultation" button is positioned alongside each service, allowing users to easily navigate to the Contact form upon clicking. 
- For superusers, additional edit and delete buttons are displayed at the bottom of each interior design service. 

### Interior Design Management

#### Add a Interior Design Service

![Add Interior Design](documentation/readme_images/features/interiordesign_add.png)

- The "Add a Interior Design Service" page is accessible by clicking the corresponding button on the Interior Design page or within the user dropdown menu, under the "Add a Interior Design Service" section. These options are exclusively visible to superusers.

- If a user attempts to access the add interior design page by altering the URL without superuser privileges, they will be redirected to the sign in page.

- To successfully submit the form, the user must complete all fields marked with an asterisk.
  
- If any of these mandatory fields are left blank or contain only whitespace upon submission, an error message will appear above the respective field, alerting the user to the issue.

- Users have the option to upload a photo for their interior design service. If they opt not to, a default image will be displayed as the interior design image.

- Upon clicking the "Add Interior Design Service" button at the bottom of the form, the interior design service will be created, provided there are no errors present.

- A success message will be displayed, informing the user that the interior design service has been successfully added.

![Add Interior Design success](documentation/readme_images/features/add_interior_success.PNG)

#### Edit a Interior Design Service

![Edit Interior Design](documentation/readme_images/features/interiordesign_edit.png)

- The superuser has the option to edit a Interior Design Service by clicking the edit button located beneath the service description on the Interior Design Services Page. 
  
- Upon clicking, the form will appear with all fields pre-filled with the existing content. 

- Within the form, the image field will exhibit a thumbnail of the current image and provide a checkbox option to remove it. 
  
- Selecting this checkbox will replace the image with the default one. 
  
- If a non-superuser attempts to add a service by altering the URL, they will be redirected to a sign in. Upon successful update, the superuser will receive a notification confirming the service's update.

![Edit Interior Design success](documentation/readme_images/features/edit_interior_success.PNG)

#### Delete a Interior Design Service

![Delete Interior Design](documentation/readme_images/features/interiordesign_delete.png)

- The superuser has the option to delete a Interior Design Service by selecting the delete button situated below the service description on the Interior Design Services Page. 
- Upon clicking, the superuser will be prompted to confirm their choice to delete the service or to cancel the action. 
- Following successful deletion, the superuser will be presented with a notification confirming the service's removal.

![Delete Interior Design success](documentation/readme_images/features/delete_interior_success.PNG)

#### Decor Dreams Projects

![Decor Dreams Projects](documentation/readme_images/features/project_gallery.png)

- When users click on the "Decor Dreams Projects" tab in the navigation bar, they are directed to a page displaying images of projects by Decor Dreams, situated in various locations across Ireland.
- In desktop view, hovering over the image reveals the type of design service and location at the center of the image. 
- On mobile devices, this information appears below the image.
- Clicking on the image opens it in a new tab for further exploration.

### Decor Dreams Projects Management

#### Add a Decor Dreams Project

![Add Decor Dreams Project](documentation/readme_images/features/project_add.PNG)

- The "Add a Decor Dreams Project" page is accessible by clicking the corresponding button on the Decor Dreams Projects page or within the user dropdown menu, under the "Add a Decor Dreams Project" section. These options are exclusively visible to superusers.

- If a user attempts to access the add interior design page by altering the URL without superuser privileges, they will be redirected to the sign in page.

- To successfully submit the form, the user must complete all fields marked with an asterisk.
  
- If any of these mandatory fields are left blank or contain only whitespace upon submission, an error message will appear above the respective field, alerting the user to the issue.

- Upon clicking the "Add Decor Dreams Project" button at the bottom of the form, the project will be created, provided there are no errors present.

- A success message will be displayed, informing the user that the interior design service has been successfully added.

![Add Decor Dreams Project success](documentation/readme_images/features/project_add_success.PNG)

#### Edit a Decor Dreams Project

![Edit Decor Dreams Project](documentation/readme_images/features/project_edit.png)

- The superuser has the option to edit a Decor Dreams Project by clicking the edit button located beneath the project description on the Decor Dreams Projects Page. 
  
- Upon clicking, the form will appear with all fields pre-filled with the existing content. 

- Within the form, the image field will exhibit a thumbnail of the current image and provide a checkbox option to remove it. 
  
- Selecting this checkbox will replace the image with the default one. 
  
- If a non-superuser attempts to add a service by altering the URL, they will be redirected to a sign in. Upon successful update, the superuser will receive a notification confirming the service's update.

![Edit Decor Dreams Project success](documentation/readme_images/features/project_edit_success.PNG)

#### Delete a Decor Dreams Project

![Delete Decor Dreams Project](documentation/readme_images/features/project_delete.PNG)

- The superuser has the option to delete a Decor Dreams Project by selecting the delete button situated below the service description on the Decor Dreams Projects Page. 
- Upon clicking, the superuser will be prompted to confirm their choice to delete the project or to cancel the action. 
- Following successful deletion, the superuser will be presented with a notification confirming the projects's removal.

![Delete Decor Dreams Project success](documentation/readme_images/features/project_delete_success.png)
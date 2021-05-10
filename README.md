# The ELEX Fitness Website

ELEX Fitness is a website whose purpose is to sell various types of workout equipment. The site supports payment processing and anyone can make orders, 
but the site also supports signing up and allows logged in users to save their delivery details, upload fitness-related articles and to post product reviews.
Logged in users can also view their order history. Administrators can use an admin portal to to add or delete products, or to moderate reviews and articles.
The site is an e-commerce platform that incorporates community-building elements to reward returning visitors who decide to make an account.

** **

## UX

#### User stories
**As a first time visitor:**

* I can tell what the purpose of the site is right away.
* I can browse products.
* I can conveniently look up products I might be after.
* I can read articles.
* I can make a purchase.
* I can create an account.

**As a returning visitor:**

* I can log in.
* I can view my order history.
* I can review products I've ordered in the past.
* I can upload articles.

**As an administrator:**

* I can add & delete products
* I can delete users
* I can view orders
* I can moderate reviews and articles

** **

## Database Structure

Sqlite3 was initially used to store data for this project, with a migration to PostgreSQL being done during development.
The following apps have corresponding databases:

* Products
* Checkout
* Profiles
* Articles
* Reviews

This is what a Product model of the project looks like:

| Name | Type | Validation |
|---|---|---|
| category | ForeignKey | 'Category', null=True, blank=True, on_delete=models.SET_NULL |
| name | CharField | max_length=150 |
| sku | CharField | max_length=150, null=True, blank=True |
| description | TextField | max_length=800 |
| price | DecimalField | max_digits=6, decimal_places=2 |
| image_url | URLField | max_length=1024, null=True, blank=True |
| image | ImageField | null=True, blank=True |

This is what an Order model for the Checkout app looks like:

| Name | Type | Validation |
|---|---|---|
| order_number | CharField | max_length=32, null=False, editable=False |
| user_profile | ForeignKey | UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders' |
| full_name | CharField | max_length=60, null=False, blank=False |
| email | EmailField | max_length=60, null=False, blank=False |
| phone_number | CharField | max_length=32, null=False, blank=False |
| country | CountryField | blank_label='Country *', null=False, blank=False |
| post_code | CharField | max_length=32, null=True, blank=True |
| town_or_city | CharField | max_length=32, null=False, blank=False |
| street_address | CharField | max_length=100, null=False, blank=False |
| county | CharField | max_length=60, null=True, blank=True |
| date | DateTimeField | auto_now_add=True |
| delivery_cost | DecimalField | max_digits=6, decimal_places=2, null=False, default=0 |
| order_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0 |
| grand_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0 |
| original_bag | TextField | null=False, blank=False, default='' |
| stripe_pid | CharField | max_length=100, null=False, blank=False, default='' |

This is what a UserProfile model of profiles app of the project looks like:

| Name | Type | Validation |
|---|---|---|
| user | OneToOneField | User, on_delete=models.CASCADE |
| default_phone_number | CharField | max_length=32, null=True, blank=True |
| default_street_address | CharField | max_length=100, null=True, blank=True |
| default_post_code | CharField | max_length=32, null=True, blank=True |
| default_town_or_city | CharField | max_length=32, null=True, blank=True |
| default_county | CharField | max_length=60, null=True, blank=True |
| default_country | CountryField | blank_label='Country', null=True, blank=True |

This is what an Article model of the articles app of the project looks like:

| Name | Type | Validation |
|---|---|---|
| title | CharField | max_length=100, null=False, blank=False |
| article_body | CharField | max_length=4000, null=False, blank=False |
| description | CharField | max_length=100, null=False, blank=False |
| image | URLField | max_length=200, null=False, blank=False |
| author | ForeignKey |User, default=None, on_delete=models.CASCADE |
| date | DateTimeField | auto_now=True |

This is what a Review model of the reviews app of the project looks like:

| Name | Type | Validation |
|---|---|---|
| product | ForeignKey | Product, related_name='reviews', on_delete=models.CASCADE |
| reviewer | ForeignKey | User, default=None, on_delete=models.CASCADE |
| product_review | TextField | max_length=250, null=False, blank=False |
| image | URLField | max_length=200, null=False, blank=False |
| date | DateTimeField | auto_now=True |

** **

## Design

**Color Scheme**

The site has a simple color scheme utilizing red, white and blue. Blue is utilized for buttons, white for backgrounds and red on occasion to give contrast to the rest of the site.

**Typography**

The site utilizes Saira and Assistant fonts, with sans-serif as the fallback. Saira is utilized for the brand and headings as the more striking font, with Assistant being used for most 
purposes in the interest of clarity.

**Imagery**

The site contains a lot of product images, and a hero image on the home page and 404 and 500 error pages. The product images don't utilize a background color other than white to better suit the
white background of most pages. The color scheme was chosen due to the colors of the hero image being generally suitable for a fitness-related e-commerce site, based on my prior research to similar sites.

** **

## Wireframes

[Wireframes](https://github.com/ssruoh/CI_MS4/blob/master/static/wireframes/CI_MS4%20wireframes.pdf) were drafted in MS Paint.

** **

## Features

* Responsive on all screen sizes.
* All pages have a uniform navigation bar and footer.
* Signup and Login pages. 
* Profile pages, where stored delivery information and past orders may be viewed.
* Product category selection in navigation menu.
* Product search functionality with the search bar.
* Product pages showing info for each product, and a button to add a specified number of products to bag.
* Logged in users may submit, edit and delete their own articles for others to view.
* Logged in users may submit and delete their own product reviews.

**Features To Implement**

* A Product Management section allowing adding, deleting or editing products for superusers without the need to use the Django Admin panel.
* A star rating system to complement the user reviews.
* More sophisticated means of filtering products, and a button to skip back to the top of the page. This would be especially necessary with more products.
* Additional Profile page functionality - listings of previously submitted reviews and articles for each user.
* Overall more polished styling. Due to time limitations the front-end of the site is still rather bare and could overall use much more work to make it more appealing.

** **

## Languages used

* Python3
* HTML5
* CSS3
* JavaScript
* Jquery
* Jinja

## Frameworks, Libraries & programs

1. Git
* Used for development and version control.
2. Github
* The primary platform for hosting the project's code.
3. Django
* Used as the primary web framework of the project.
4. Django Allauth
* Used for its login and User registration functionality.
5. Heroku
* Used to deploy the website.
6. Gunicorn
* A necessity for Heroku deployment.
7. Psycopg2
* A necessity for using PostgreSQL.
8. Sqlite3
* Used as the initial database during development.
9. PostgreSQL
* The second data storage for the project, used for later stages of development and ultimately production.
10. Bootstrap
* Used for its various site styling tools.
11. Crispyforms
* Used for its form styling.
12. Crispy-bootstrap5
* A necessity for Crispy Forms styling to function with bootstrap5
13. AWS S3
* Used to store static files and images.
14. Stripe
* Used to implement payment processing.
15. FontAwesome
* Utilized for some of its icons for an improved UX.
16. Google Fonts
* The fonts used for the site are sourced from Google Fonts.

** **

## Testing

Ideally testing the project would involve some written tests or tools, but due to time limitations my testing was mostly limited to manual testing during development.

**Manual**

Base

* Tested that all navigation links and the bag on the navigation bar work and direct to the correct page, as do the social media links in the footer. 
The bag calculator displays current bag value as intended when products are added and deleted.

* Navigation bar shows the correct links to logged in users (My profile, Log out) and logged out users (Sign up, Log in).

* Social links in the footer redirect to correct sites.

Home page

* The hero image renders correctly and the button to the products page directs user to products.

Products page

* All products pages filter the correct product categories and the product image redirects to correct product detail as intended.
Adding and removing items in the Django Admin panel results in addition/removal of the product on the page.

Product detail pages

* Correct product detail page renders when accessing it from products. Image link opens image of product in another tab. Logged in users can post reviews, and have a button to delete their own as intended.
Superusers can remove any review.

Articles page

* Articles render correctly. Clicking on article description opens article detail page.

Article detail pages

* Article title, description, image and body load correctly. If viewed by the author, edit and delete buttons for the article are visible.

Profile page

* Updating the Default delivery details works when clicking Update. If orders have been made, they show on the right. Clicking on order number opens the order confirmation page for that order.

Bag page

* Added products show on the page. Changing product amount and clicking Update updates the bag total correctly. Delete button removes the product from bag entirely. Keep shopping button getbootstrap
back to products, and Checkout button goes to Checkout page.
* Empty bag renders a page with no products, and a button that goes back to products.

Checkout page

* Products and total show correctly. Edit bag button goes back to bag page. Filling Stripe test card detail for successful payment and clicking Checkout button goes to Checkout success page.
* Filling a test card that requires additional confirmation renders blue background and spinning icon.

Checkout success page

* Order details render correctly. Email confirmation is sent.

Login page

* Sign in button with correct details works. Incorrect details throw an error. 

Sign up page

* Filling the form with prerequisite details creates an account. Email verification is sent.

**Responsiveness**

* Responsiveness testing was done on the Google Chrome, Mozilla Firefox and Microsoft Edge browsers. The primary responsiveness testing tool was Chrome DevTools, 
and various other tablet and mobile device views were tested on it.

**Known Issues**

* The shopping bag and search bar should be fixed to the right side of the navbar.
* The cards on the products pages are not all the same size, as the image and product name length may currently alter their height.
* Pushing code will not render changes to static files on the Heroku site. [This Stack Overflow post](https://stackoverflow.com/questions/11266849/heroku-css-file-not-updating) notes 
that restarting with heroku restart fixes the issue.

** **

## Deployment

This section will walk through the steps necessary to deploy the project.

**Requirements**

* Github
* Gitpod
* Heroku
* Amazon Web Services
* Stripe
* Gmail

**Forking The Repository**

The copy of the Github repository can be forked to another account for viewing or editing without affecting the original one with the following steps:

1. Login to Github and locate the [repository](https://github.com/ssruoh/CI_MS4)
2. On top right, right under the Account menu and Notifications, click on the Fork button. This will create a copy of the repository to your Github account.

**Creating A Local Clone of the Github Repository**

1. Login to Github and locate the [repository](https://github.com/ssruoh/CI_MS4)
2. Click on the green Code button
3. Click on the clipboard icon under "Clone with HTTPS" to copy the link
4. Open Git Bash
5. Change the current working directory to the one where you want the clone to be created.
6. Type `git clone` and paste the URL you copied from the clipboard:

```
$ git clone https://github.com/ssruoh/CI_MS4
```

7. Press Enter to create a local clone.

```
$ git clone https://github.com/ssruoh/CI_MS4
> Cloning into `Spoon-Knife`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

**Working with a clone**

1. Install the necessary libraries to run the project in the Gitpod terminal:

```
$ pip3 install -r requirements.txt
```

2. Set up environment variables. The project will require a number of environment variables to protect sensitive information. Below is a full list of an example env.py
file for the project once it is fully deployed.

```
import os

os.environ['DEVELOPMENT'] = "1"
os.environ["SECRET_KEY"] = "YOUR_SECRET_KEY"
os.environ["STRIPE_PUBLIC_KEY"] = "YOUR_STRIPE_PUBLIC_KEY"
os.environ["STRIPE_SECRET_KEY"] = "YOUR_STRIPE_SECRET_KEY"
os.environ['STRIPE_WH_SECRET'] = "YOUR_STRIPE_WH_SECRET"
os.environ['AWS_ACCESS_KEY_ID'] = "YOUR_AWS_ACCESS_KEY_ID"
os.environ['AWS_SECRET_ACCESS_KEY'] = "YOUR_AWS_SECRET_KEY"
os.environ['EMAIL_HOST_PASS'] = "YOUR_EMAIL_HOST_PASS"
os.environ['EMAIL_HOST_USER'] = "YOUR_EMAIL_HOST"
os.environ['DATABASE_URL'] = "YOUR_DATABASE_URL"
os.environ['USE_AWS'] = "1"
```

3. Create superuser in the Gitpod terminal:

```
$ python3 manage.py createsuperuser
```

4. Make migrations in the terminal:

```
python3 manage.py makemigrations
python3 manage.py migrate
```

5. Load data in the terminal. Categories and Products should be done first:

```
$ python3 manage.py loaddata Categories
$ python3 manage.py loaddata Products
```

6. The project utilized sqlite3 for development prior to migration to Postgres. At this point, creating products, articles and the like would initially need to be done in the Django Admin panel.

**Setting up Heroku**

1. Create a Heroku account.
2. Create a new app, selecting the region closest to you.
3. Provision a new Postgres database in the Resources tab, this will be needed to migrate to Postgres database.
4. Istall necessary requirements (dj_database_url & psycopg2-binary for later Postgres migration) the Gitpod terminal:

```
$ pip3 install dj_database_url
$ pip3 install psycopg2-binary
$ pip3 install gunicorn
```

5. Freeze requirements:

```
$ pip3 freeze > requirements.txt
```

6. Configure your keys and variables in Config Vars under the Settings tab on the Heroku site thusly:
* AWS_ACCESS_KEY_ID = YOUR_AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY = YOUR_AWS_SECRET_ACCESS_KEY
* DATABASE_URL = YOUR_DATABASE_URL
* EMAIL_HOST_PASS = YOUR_EMAIL_HOST_PASS
* EMAIL_HOST_USER = YOUR_EMAIL_HOST_USER
* SECRET_KEY = YOUR_SECRET_KEY
* STRIPE_PUBLIC_KEY = YOUR_STRIPE_PUBLIC_KEY
* STRIPE_SECRET_KEY = YOUR_STRIPE_SECRET_KEY
* STRIPE_WH_SECRET = YOUR_STRIPE_WH_SECRET
* USE_AWS = True

7. Create a Procfile, and enter this in the file:

```
web: gunicorn elex_fitness.wsgi:application
```

8. Login to heroku in the terminal:

```
heroku login -i
```

9. Disable static files collection to avoid Heroku trying to collect static files during deployment:

```
$ heroku config:set DISABLE_COLLECTSTATIC=1 --app elex-fitness
```

10. Initialize heroku git remote:

```
$ heroku git:remote -a elex-fitness
```

11. Push to github, and master push to Heroku: 

```
$ git add .
$ git commit -m "Your commit message"
$ git push
$ git push heroku master
```

12. App is now deployed. Collection of static files can be re-enabled by removing the corresponding Config Vars entry on the website.

**Migrating to Postgres DB**

1. Create a json dump of the local database:

```
$ python3 manage.py dumpdata --exclude auth.permission --exclude contenttypes > database_name.json
```

1. Comment out the default DATABASES configuration in settings.py and add the code below. The Postgres DB URL 
referenced can be recovered from the Config Vars in Heroku Settings tab if you provisioned it as detailed in the Heroku setup section.

```
DATABASES = {
    'default': dj_database_url.parse('YOUR_POSTGRES_DATABASE_URL')
}
```

2. Create a superuser in the Postgres DB in the terminal.

```
$ python3 manage.py createsuperuser
```

3. Make migrations in the terminal:

```
python3 manage.py makemigrations
python3 manage.py migrate
```

4. Load the .json dump and fixtures into Postgres. Again, Categories & Products should be the first ones to be loaded (after the .json file):

```
$ python3 manage.py loaddata database_name.json
$ python3 manage.py loaddata Categories
$ python3 manage.py loaddata Products
```

5. Push to github, and master push to Heroku: 

```
$ git add .
$ git commit -m "Your commit message"
$ git push
$ git push heroku master
```

**AWS**

1. Media and static files are stored in an AWS S3 bucket and S3BotoStorage. An [AWS account](https://aws.amazon.com/) is required. Refer to their documentation for setup.
* [AWS S3 Documention](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
* [S3BotoStorage Documentation](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html)

**Stripe**

1. For the Stripe payment functionality to work, Stripe STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY and STRIPE_WH_SECRET need to be configured.
A [Stripe](https://stripe.com/) account is required. Documentation below.
* [Stripe key documentation](https://stripe.com/docs/keys)

**Gmail**
1. A Gmail SMTP server was used to handle signup emails, order confirmation emails and the like. A [Gmail account](https://www.gmail.com/) is required.
* [Gmail SMTP server documentation](https://support.google.com/a/answer/176600?hl=en#zippy=%2Cuse-the-gmail-smtp-server)

** **

## Testing User Requirements In UX Section

**First time visitors**

> I can tell what the purpose of the site is right away.
* The jumbotron, links and hero image make it clear what the site is about.
> I can browse products.
* Products can be viewed all at the same time or in categories, and each has an individual product page with more detailed information.
> I can conveniently look up products I might be after.
* The site has a functional search bar that allows for searching products.
> I can read articles.
* Anyone can view articles by navigating to the page.
> I can make a purchase.
* Anyone can make purchases, the site has a functional shopping bag, order logging and payment processing.
> I can create an account.
* Users can sign up from the link in the navigation bar.

**Returning visitors:**

> I can log in.
* There is a Login button on the navigation page, as well as on some pages where authentication is required to use features, such as the Articles page.
> I can view my order history.
* Logged in users can view their order history on the Profile page.
> I can review products I've ordered in the past.
* Logged in users can upload reviews for products.
> I can upload articles.
* Logged in users can upload articles.

** **

## Credits

**Code**

[Bootstrap](https://getbootstrap.com/) is utilized for its grid system, cards and other responsive elements.

The code for this project overall draws heavily from the Full Stack Frameworks with Django module of Code Institute for its models, forms and stripe functionality, 
particularly those of the Boutique Ado lessons. 

[This jsfiddle](https://jsfiddle.net/macloo/g39k3h3e/) was used to animate the product images on add product button hover.

While Widget Tweaks wasn't used, the widget method shown in this [Youtube tutorial](https://www.youtube.com/watch?v=VYs-u0g__1A) showcasing Widget Tweaks was used for styling some of the forms.

This [Django Central](https://djangocentral.com/building-a-blog-application-with-django/) guide for creating a blog app was used for some direction for writing the articles app.

[The method in this Youtube video](https://www.youtube.com/watch?v=pNVgLDKrK40) was initially used as the template for adding and deleting reviews, 
but was changed considerably as a result of feedback from [Tmuat](https://github.com/Tmuat), who had helpful suggestions for cleaning up the view.

[Matthew Yong's](https://github.com/MatthewYong/big_brains) solution to editing blogs in his project was adapted for edit_article view of this project.

Attaching user profile to articles as author was done based on the suggestions in these Stack Overflow posts, 
[#1](https://stackoverflow.com/questions/19799941/attaching-a-current-user-object-to-django-form) and [#2](https://stackoverflow.com/questions/8466768/using-request-user-with-django-modelform).

This [StackOverflow solution](https://stackoverflow.com/questions/53182024/move-image-to-right-of-card-in-bootstrap/53182241) was used to set article image to the right in the article cards.

This [StackOverFlow post](https://stackoverflow.com/questions/65238459/templatedoesnotexist-at-users-register-bootstrap5-uni-form-html) noted that there is a necessary, separate package for crispy_forms when using bootstrap5.

This [StackOverFlow post](https://stackoverflow.com/questions/40853952/bootstrap-footer-at-the-bottom-of-the-page) was used to place footer at the bottom of a page, whether content covers full viewport height or not.

**Content**

Product names, descriptions and images are from [Fitness Equipment Ireland](https://www.fitnessequipmentireland.ie), 
[McSport](https://www.mcsport.ie) and [Expert Leisure](https://www.expertleisure.ie/).

The sample articles are written by [Jodi Helmer](https://www.webmd.com/fitness-exercise/a-z/kettlebell-workout) and
 [K. Aleisha Fetters](https://www.everydayhealth.com/fitness/how-to-clean-your-home-gym-equipment/).

The structuring of the Database Structure and Deployment sections of this readme are presented in a manner similar to that of [Matthew Yong's project readme](https://github.com/MatthewYong/big_brains).

Any other site content is written by the developer. The readme file itself is similar in structure and some content to my previous readmes for earlier CI projects.

**Media**

The Hero image is from [Net World Sports](https://www.networldsports.ie/metis-dumbbell-rack-sets-3-tier.html).

Product images are from [Fitness Equipment Ireland](https://www.fitnessequipmentireland.ie), [McSport](https://www.mcsport.ie)
 and [Expert Leisure](https://www.expertleisure.ie/).

The image for K. Aleisha Fetter's article is from its 
[Net World Sports page](https://images.everydayhealth.com/images/how-to-clean-your-home-gym-equipment-1440x810.jpg?w=1110).

The image for Jodi Helmer's article was sourced from Google Images.

**Acknowledgments**

My mentor Gerald McBride for his helpful feedback and ideas, particularly as to what kinds of custom apps to include in the project.

The Slack Code Institute community for their support.

My friends for helping with testing site functionality.
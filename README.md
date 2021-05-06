# The ELEX Fitness Website

ELEX Fitness is a website that whose purpose is to sell various types of workout equipment. The site supports payment processing and anyone can make orders, 
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

* Profiles
* Products
* Checkout
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

All app models can be viewed in the models.py of the corresponding app file.

** **

## Design

**Color Scheme**

The site has a simple color scheme utilizing red, white and blue. Blue is utilized for buttons, white for backgrounds and red on occasion to offer contrast to the rest of the site.

**Typography**

The site utilizes Saira and Assistant fonts, with sans-serif as the fallback. Saira is utilized for the brand and headings as the more striking font, with Assistant being used for most 
purposes in the interest of clarity.

**Imagery**

The site contains a lot of product images, and a hero image on the home page and 404 and 500 error pages. The product images don't utilize a background color other than white to better suit the
white background of most pages. The color scheme was chosen due to the colors of the hero image being generally suitable for a fitness-related e-commerce site, based on my prior research to similar sites.

** **

## Wireframes

[Wireframes]() 
were drafted in MS Paint.

** **

## Features

* Responsive on all screen sizes.
* All pages have a uniform navigation bar and footer.
* Signup and Login pages. 
* Profile pages.
* Product category selection in navigation menu.
* Product search functionality with the search bar.
* Product pages showing info for each product.

**Features To Implement**

* A star rating system to complement the user reviews.
* Additional Profile page functionality - links to previous submitted reviews and articles for each user.
* Overall more polished styling. Due to time concerns the front-end of the site is still rather bare and could overall use work to make it more appealing.

** **

## Languages used

* Python3
* HTML5
* CSS3
* JavaScript
* Jquery
* Jinja


## Frameworks, Libraries & programs

1. FontAwesome
* 
2. Google Fonts
* 

** **

## Testing

**Tools**

[Results]()

[Results]()

[Results]()

**Manual**

Home page

* 

**Responsiveness**

* 

**Known Issues**

* 

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
heroku login
```

9. Disable static to avoid Heroku trying to collect static files during deployment:

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

Creating blog app: []https://djangocentral.com/building-a-blog-application-with-django/

[Tmuat](https://github.com/Tmuat) had helpful suggestions for cleaning up the view for posting reviews in the review app.

This [StackOverflow solution](https://stackoverflow.com/questions/53182024/move-image-to-right-of-card-in-bootstrap/53182241) was used to set article image to the right in the article cards.

This [StackOverFlow post](https://stackoverflow.com/questions/65238459/templatedoesnotexist-at-users-register-bootstrap5-uni-form-html) noted that there is a necessary, separate package for crispy_forms when using bootstrap5.

**Content**

Products are from https://www.fitnessequipmentireland.ie and https://www.mcsport.ie.

https://www.webmd.com/fitness-exercise/a-z/kettlebell-workout

https://www.everydayhealth.com/fitness/how-to-clean-your-home-gym-equipment/
https://images.everydayhealth.com/images/how-to-clean-your-home-gym-equipment-1440x810.jpg?w=1110

**Media**

Hero image from https://www.networldsports.ie/metis-dumbbell-rack-sets-3-tier.html

**Acknowledgments**

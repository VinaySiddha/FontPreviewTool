**Trevon Project**
================

**Overview**
-----------

This project is a Django-based application that utilizes MongoDB as its database. The project involves multiple apps, including `accounts` and `yasha`, which contain models, views, and templates for user authentication and profiling.

**Changes**
----------

### User Model Refactoring

The `User` model in `accounts/models.py` has been refactored to inherit from `AbstractBaseUser` and `PermissionsMixin`, allowing for more flexibility in customizing the user model. A new `UserManager` class has been added to handle user creation and superuser creation.

### MongoDB Connection Updates

The `con.py` file has been updated to use the `mongodb+srv` protocol and enable TLS connections for secure communication with the MongoDB database.

### Profile Model Addition

A new `Profile` model has been added to `yasha/models.py`, which has a one-to-one relationship with the `AUTH_USER_MODEL`.

**Installation**
--------------

To install the project, follow these steps:

1. Clone the repository: `git clone https://github.com/[username]/trevon.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Configure the `settings.py` file to point to your MongoDB database
4. Run the migrations: `python manage.py migrate`
5. Start the development server: `python manage.py runserver`

**Contributing**
--------------

If you'd like to contribute to the project, please fork the repository and submit a pull request with your changes.

**License**
---------

This project is licensed under the MIT License. See `LICENSE` for details.
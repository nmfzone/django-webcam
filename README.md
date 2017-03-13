<p align="center"><img src="https://www.djangoproject.com/s/img/logos/django-logo-positive.png" width="250px" alt="Django Boilerplate"></p>

# Django Boilerplate

Simple Django Boilerplate for building awesome web applications.

## Features

- Bootstrap 3, for styling the interfaces
- Laravel Mix, for bundling static assets through Webpack

## Requirements

- Python >= 3.5x
- Pip
- Mysql
- NodeJs (Optional)
- Yarn (Optional)
- Virtualenv (Optional)
- Pyenv (Optional)

## How to use

1. Download or clone this repository `git clone git@github.com:nmfzone/django-boilerplate.git`
2. Install the provided packages `pip install -r requirements/main.txt`
3. Duplicate `.env.example` to `.env`
4. Provide the appropriate value in the `.env`
5. Migrate the database schema `python manage.py migrate`
6. Create the administrator `python manage.py createsuperuser`
7. Start the server `python manage.py runserver`
8. Open `http://localhost:8000` in your browser
9. Let's rock!

## Additional

- If you want to make the app work with some **Deep Learning** tools, you may install it with this command `pip install -r requirements/deep-learning.txt`

## Contributing

Want to contribute? Awesome. Just send a pull request.

## Bugs

If you discover a bug within this Boilerplate, please send an e-mail to Nabil Muhammad Firdaus at 123.nabil.dev@gmail.com.

## License

This Boilerplate is open-sourced software licensed under the [MIT license](http://opensource.org/licenses/MIT).

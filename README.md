# map_swap_example
[Django](https://djangoproject.com), [Leaflet.js](https://leafletjs.com/) and [HTMX](https://htmx.org) work together to seamlessly upload georeferenced data.
## Requirements
This project is tested on Django 5.0.3 and Python 3.12.0. It does NOT rely on `GeoDjango` framework, but on [django-leaflet](https://django-leaflet.readthedocs.io/en/latest/index.html/) as map engine, [django-geojson](https://django-geojson.readthedocs.io/en/latest/) for storing geodata and [django-htmx](https://django-htmx.readthedocs.io/en/latest/) to manage interactions. I use [Bootstrap 5](https://getbootstrap.com/) for styling. `django-leaflet` requires the `GDAL` library to work, which is system specific.
## Installation
Prepare a virtual environment, clone this repository (`git clone https://github.com/andywar65/map_swap_example`) then install packages (`python -m pip install -r requirements.txt`). Prepare a `.env` file with at least `SECRET_KEY` environment variable, add `DATABASE_URL` if you are forced to use a specific database. Migrate database tables (`python manage.py migrate`), run `python manage.py generate_locations` to seed database and then run the server (`python manage.py runserver`).
## Usage
If all went well, you should see a diakog box in the left/top section of the screen (depends on device) and a world map with the locations previously generated. Click on a marker, the location name will pop up. Click on the link and the map will focus on the surroundings of chosen location. if you want to go back to world map, there is a link in the dialog box. Swapping the maps requires the transfert of minimal `HTML` fragments, without reloading the whole page.
## How it works
To be continued.

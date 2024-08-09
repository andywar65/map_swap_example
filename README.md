# map_swap_example
[Django](https://djangoproject.com), [Leaflet.js](https://leafletjs.com/) and [HTMX](https://htmx.org) work together to seamlessly upload georeferenced data.
## Requirements
This project is tested on Django 5.0.6 and Python 3.12.0. It does NOT rely on `GeoDjango` framework, but on [django-geojson](https://django-geojson.readthedocs.io/en/latest/) for storing geodata and [django-htmx](https://django-htmx.readthedocs.io/en/latest/) to manage interactions. I use [Bootstrap 5](https://getbootstrap.com/) for styling. A `SQLite` database is enough.
## Installation
Prepare a virtual environment, clone this repository (`git clone https://github.com/andywar65/map_swap_example`) then install packages (`python -m pip install -r requirements.txt`). Prepare a `.env` file with at least `SECRET_KEY` environment variable, add `DATABASE_URL` if you are forced to use a specific database. Migrate database tables (`python manage.py migrate`), run `python manage.py generate_locations` to seed database and then run the server (`python manage.py runserver`). In some cases a `OSError` exception is raised, so my personal fork of [django-geojson](https://github.com/andywar65/django-geojson/tree/oserror) is installed to fix this problem.
## Usage
If all went well, you should see a dialog box in the left/top section of the screen (depends on device) and a world map with the locations previously generated. Click on a marker, the location name will pop up. Click on the link and the map will focus on the surroundings of chosen location. if you want to go back to world map, there is a link in the dialog box. Swapping the maps requires the transfert of minimal `HTML` fragments, without reloading the whole page. If user is authenticated, whole set of CRUD views are available.
## How it works
### Model
The project has only one model: `Location`. The model has two text fields, `title` and `description`, and a `PointField` that stores geographic coordinates in `JSON` format and two `FloatField`s used in forms for coordinates. Apart from classic `__init__` - `save` overrides, the only significant method of the model is `popupContent(location)` that returns an `HTML` string that pops up when the location marker is clicked on the map. The string looks something like this: `<a onclick="openLocation({ location.url })">{ location.title }</a>`, and it will be used to swap content from within the map.
### Views
The project has a `ListView` for displaying all locations, a `DetailView` to display just one and all `CRUD` views. They are pretty standard `CBV`s, but they change behaviour depending on the request being triggered by `HTMX` or not. In the first case the templates will be partial, and some response headers will be dispatched.
### Templates
The project has several templates, somehow nested the one into the other. The `base.html` stands to it's name, laying the `<head>` and `<body>` tags of the document, downloading the `HTMX` and `Bootstrap` libraries. When the `ListView` is requested without `HTMX` headers (in example the first time you enter the page) the `location_list.html` is called, the `Leaflet` library is downloaded and the map is initialized. Another template (`htmx/location_list.html`) is included in the `<div id="dialog-box">`. This template carries a `GeoJSON template tag`, with all the data needed to populate the map. Other templates render the `CRUD` views. In analogy with previous ones, they are chosen depending on request (`HTMX` or not).
### JavaScript
A `base_list.js` is downloaded and initialized when the `ListView` is first called. The file sets up the map and looks for location data in the `GeoJSON`. An event listener is ready to be triggered to refresh data. Another function waits for events from the `onclick` attributes in the popups. This last function uses `htmx.ajax()` to send a `HTMX` request to the server, targeting the dialog box. The server responds with a template fragment that replaces the target and adds a new `GeoJSON`. The response comes along with a header (`HX-Trigger-After-Swap`) that activates the refresh event listener, so `base_list.js` deletes the markers on the map and reads new data in the `GeoJSON`. All this happens without reloading the whole page and/or reinitializing the map. Similar thing happens when you go back to the world map from the `DetailView`, but in this case the request is sent via `hx-get` attribute, targeting the dialog box. It is noteworth that this classic approach does not work in the popup, a simple `href` does the job, but unfortunately it reloads the whole page.
### Coordinate input
No special widgets are used to input geographic data: a simple `map.on('click')` event is triggered when clicking on the map, and the coordinates are input as values in the correspondent form `FloatField`s. As the form is saved, the values are passed to the `PointField`.
## Tests
Using unittests. Coverage 99%. Provide a DJANGO_SUPERUSER_PASSWORD in environment file.

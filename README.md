## Flask & Ferris 3 example for Google App Engine

This is an example project of using [Ferris3](https://github.com/jonparrott/ferris3) features inside of a simple Flask project.

This is based on the Google [Flask Skeleton](https://github.com/GoogleCloudPlatform/appengine-python-flask-skeleton).

## Description of functionality

This is more or less the App Engine Guestbook example written in Flask. The application use's Ferris' search utilites to automatically add entities to the search index and search over them.

## Run Locally
1. Install the [App Engine Python SDK](https://developers.google.com/appengine/downloads).
See the README file for directions. You'll need python 2.7 and [pip 1.4 or later](http://www.pip-installer.org/en/latest/installing.html) installed too.

2. Clone this repo with

   ```
   git clone https://github.com/jonparrott/flask-ferris-example.git
   ```
3. Install dependencies in the project's lib directory.

   ```
   cd flask-ferris-example
   pip install --pre -r requirements.txt -t lib
   ```
4. Run this project locally from the command line:

   ```
   dev_appserver.py .
   ```

Visit the application [http://localhost:8080](http://localhost:8080)

See [the development server documentation](https://developers.google.com/appengine/docs/python/tools/devserver)
for options when running dev_appserver.


## Basic steps to include Ferris in existing projects

1. Add endpoints to your app.yaml's libraries section. Even if you don't use endpoints, this is a prerequisite for ferris3.

   ```
   libraries:
   - name: endpoints
     version: 1.0
   ```

2. Add ferris to your requirements.txt
3. Install all requirements using pip. Be sure to use the ``--pre`` flag.

   ```
   pip install --pre -r requirements.txt -t lib
   ```

4. You can now import ``ferris3`` and use all features you'd like.

## Feedback
Star this repo if you found it useful. Use the github issue tracker to give
feedback on this repo.

## Licensing
See [LICENSE](LICENSE)

## Author
Jon Wayne Parrott, based on the skeleton by Logan Henriquez and Johan Euphrosine

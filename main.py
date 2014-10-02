"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

# Import Ferris so we get fun stuff.
import ferris3

# Import the app engine datastore api
from google.appengine.ext import ndb


class GuestbookPost(ferris3.ndb.Model):
    # Using ferris3.ndb.Model gives up behaviors.
    class Meta:
        # We'll use the searchable behavior to automatically index our models.
        behaviors = (ferris3.search.Searchable,)

    content = ndb.TextProperty()
    author = ndb.UserProperty(auto_current_user_add=True, indexed=False)
    created = ndb.DateTimeProperty(auto_now_add=True)


@app.route('/')
def guestbook_list():
    greetings = GuestbookPost.query().order(-GuestbookPost.created)
    return render_template("guestbook.html", greetings=greetings)


@app.route('/search')
def guestbook_search():
    query = request.args.get('query', '')
    search_results = ferris3.search.search('searchable:GuestbookPost', query)
    greetings = ferris3.search.to_entities(search_results).items
    return render_template('guestbook.html', greetings=greetings, query=query)


@app.route('/sign', methods=['POST'])
def guestbook_sign():
    content = request.form.get('content')
    post = GuestbookPost(content=content)
    post.put()
    return redirect('/')


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def page_not_found(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500

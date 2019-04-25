=====
Polls
=====

Polls is a simple Django app to conduct Web-based polls. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Install
-----------

dist/ has the tar file, you can install this package on ubuntu by 
pip install --user django-polls/dist/django-polls-0.1tar.gz

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

       INSTALLED_APPS = [
               ...
                       'polls',
                           ]

2. Include the polls URLconf in your project urls.py like this::

                            path('polls/', include('polls.urls')),

3. Run `python manage.py migrate` to create the polls models.


4. Start the development server and visit http://127.0.0.1:8000/admin/                  to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/ to participate in the poll.

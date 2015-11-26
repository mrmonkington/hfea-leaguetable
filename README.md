# UK HFEA regulated fertility centre league table

Scrapes the HFEA website and aggregates stats about the different providers of fertility treatment in the UK.

You should be very careful to interpet the data.  Many institutions achieve high success rates by:

  - Offering unnecessary treatment where cost is no object
  - Using a kitchen sink approach
  - Transfering several embryos resulting in more multiple births
  - Declining to treat patients with low chance of success

Get as much qualified advice as you can, and don't listen to people on internet forums!!!

## Installation

Set up.

```
virtualenv env --no-site-packages
env/bin/pip install -r requirements
```

Create settings (copy and edit example, though should work out of box).

```
cp fertilityleague/example_settings.py fertilityleague/settings.py
```

Run a scrape

```
env/bin/python manage.py scrape
```

(Will make a temp folder in `~/tmp/cache`.)


Run the web app to view league table.

```
env/bin/python manage.py runserver
```


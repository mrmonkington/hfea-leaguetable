# UK Fertility League

Scrapes the HFEA website and aggregates stats about the different providers of fertility treatment in the UK.

You should be very careful to interpet the data.  Many institutions achieve high success rates by:

  - Offering unnecessary treatment where cost is no object
  - Using a kitchen sink approach
  - Transfering several embryos resulting in more multiple births
  - Declining to treat patients with low chance of success

Get as much qualified advice as you can, and don't listen to people on internet forums!!!

## Installation

```
cp fertilityleague/example_settings.py fertilityleague/settings.py
```

Edit the setting

```
virtualenv env --no-site-packages
env/bin/pip install -r requirements
env/bin/python manage.py runserver
```

Will make a temp folder in `~/tmp/cache`.



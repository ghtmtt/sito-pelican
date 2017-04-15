Title: Pelican Setup
Date: 2017-04-14
Slug: pelican-setup
lang: en
tags: pelican, web

[TOC]

## Pelican Environment

Pelican is a great tool to create blog and websites. It is completely customizable and with additional plugin and a little bit of effort it is not difficult to build the final website.

I'm not a web developer at all, just hacking a little bit `html` and `css`, but not too much.

So I decided to share my experience and write a post on how I build this web site entirely written in pelican.


### Installation and first steps

I use Linux OS but this guide will be exactly the same for OSX and, maybe with some additional effort, with Windows machines.

#### virtualenv
Pelican is a `python` software so it is easy to use and to insall. I definitely recommend to use the great **virtualenv** software to create a virtual python environment and not mess up with other environmental variables.

Be sure to have `virtualenv` installed (if not, look [here]()), open a terminal and `cd` wherever you want to create your virtual environment, create and start it:


    $ virtualenv my-site
    New python executable in /home/matteo/my-site/bin/python
    Installing setuptools, pip, wheel...done.

    # cd into the folder
    $ cd my-site

    # finally start the virtual environment
    $ source bin/activate

now you can install `pelican` and all the other additional packages within this `virtualenv` and with `pip` without touching your system. I strongly suggest to install also the `markdown` package:

    $ pip install pelican markdown

you can install additional packages at any time, but for the moment it's enough.


#### pelican
Now that `pelican` is correctly installed, it is as simple as writing a line of code to have a working website.

`pelican` comes with a *facility*, `pelican-quickstart` that is really useful and allows to speed up the configuration setting. Before running pelican, create a folder that will store all the pelican stuff:

    # create and cd into the folder
    mkdir website
    cd website
    # start pelican
    $ pelican-quickstart

`pelican-quickstart` will ask you a bunch of stuff: don't worry, you can edit all the settings whenever you want:


    Welcome to pelican-quickstart v3.7.1.

    This script will help you create a new Pelican-based website.

    Please answer the following questions so this script can generate the files
    needed by Pelican.


    Where do you want to create your new web site? [.]
    What will be the title of this web site? my awsome website
    Who will be the author of this web site? me
    What will be the default language of this web site? [en]
    Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) n
    Do you want to enable article pagination? (Y/n) y
    How many articles per page do you want? [10]
    What is your time zone? [Europe/Paris] Europe/Rome
    Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) y
    Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) y
    Do you want to upload your website using FTP? (y/N) n
    Do you want to upload your website using SSH? (y/N) n
    Do you want to upload your website using Dropbox? (y/N) n
    Do you want to upload your website using S3? (y/N) n
    Do you want to upload your website using Rackspace Cloud Files? (y/N) n
    Do you want to upload your website using GitHub Pages? (y/N) y
    Is this your personal page (username.github.io)? (y/N) y
    Done. Your new project is available at /home/matteo/my-site/website

as you can notice all the options are pretty much self-explanatory. Be sure to say yes to both

**Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n)**

and

**Do you want an auto-reload & simpleHTTP script to assist with theme and site development?**.

These two options will create some files (`Makefile` and `develop-server.sh`) that will help you when running the site.

`pelican` creates a set of files and folder structure for you, that you will customize in the future:


    $ tree
    .
    ├── content
    ├── develop_server.sh
    ├── fabfile.py
    ├── Makefile
    ├── pelicanconf.py
    ├── publishconf.py

* `pelicanconf.py` is the files containing all the configuration options
* `develop_server.sh` is the bash script that you can run to build the website
* `Makefile` contains many different options
* `content` is the folder where you will store all your pages and posts

If you now simply run `make devserver`, the `Makefile` will call `develop_server.sh` for you and create the output folder with all the compiled html and css. Moreover, if you make some changes, the website is automatically refreshed:

    $ make devserver


open your browser and on `localhost:8000` you can see a complete website, with a custom template, header and footer:

![](/images/blog/pelican1.png)

and you will see the new `output` folder with all the generated html and css.


## The configuration file
The `pelicanconf.py` file is for sure the most important out here. You can declare variable in this file and call them wherever you want without writing the same code lines in different files.

Every time you build the website (with `Makefile`) pelican will read the information stored in this file and build the site accordingly to them.

In this file you can tell pelican to load other themes or plugins, add `JINJA` filters or custom python function.

To have a look at all the variables and options, see the [pelican docs](http://docs.getpelican.com/en/3.7.1/settings.html)


## Changing Template
It's great to have a custom template ready, but there are more complex theme out here.

For this website I've used the [pelican-bootstrap3 them](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3) that I modified in a second moment to fit my needs.

This theme is great because it supports really a lot of different plugins and you can customize it with a very little effort.

Changing templates is really super easy. Just go on [this webiste](https://github.com/getpelican/pelican-themes) and if you are familiar with `git` you cann clone the repository, else download it as zip.

Every folder is a theme; so you can see that you have a lot of themes available (once you have chosen you theme, you can keep just that folder).

Place the folder with all the sub(theme)folders within the `website`:

    $ ls
    content
    develop_server.sh
    fabfile.py
    Makefile
    pelicanconf.py
    pelicanconf.pyc
    pelican-themes
    publishconf.py

then open the `pelicanconf.py` file, add/edit the variable `THEME` so it will point to the right theme. Be aware to add the correct path and the correct name:

    # Theme
    THEME = "pelican-themes/pelican-bootstrap3"

by running `make devserver` you will see the changes:

![](/images/blog/pelican2.png)

Try the theme and see which one is better for you.

**Remember**, once you got you theme, the files in that folder are the ones to handle with to customize the theme itself!

## Additional plugins
Adding plugins is as easy as for loading default themes.

Again download as zip or clone the repository at [this link](https://github.com/getpelican/pelican-plugins) inside your `website` folder and open the `pelicanconf.py` file. You have to tell pelican the folder of the plugin and the name of the plugin you want to load by adding two new variables:

    PLUGIN_PATHS = ['pelican-plugins']
    PLUGINS = ['i18n_subsites', 'headerid', 'tipue_search']

Again, be sure to type the correct path and the correct name of the plugins.


## Localize your website
Adding additional languages to your website is possible with additional plugin and some patience.

### Localize the theme
Before to get deepen into the localization of pages and posts, it does not make any sense to have articles translated when your theme in mono language.

The theme `pelican-bootstrap3` supports the localization with `JINJA`. If you have a look in some html file of the template, you can see some strings surrounded by:

    {{ _('A string') }}

all the stuff is mandatory for `JINJA` to know which strings have to be localized. As the process in easy in the html files of the theme (just add `{{ _('here the string')}}`) it is not that easy with the localization commands.

First of all you will need an additional package, install it with `pip` in your virtual environment:

    $ pip install Flask-Babel

All the following information are an extension of the content you can see [here](https://github.com/getpelican/pelican-plugins/blob/master/i18n_subsites/localizing_using_jinja2.rst).

The workflow is simple:

1. add the *tag* to all the strings you want to translate in the html file (adding {{ _('here the string')}})
2. create a `babel.cfg` file for babel with some configuration: if you use the theme `pelican-bootstrap3` the file is already there
3. create a `pot` file that will store all the strings to localize. Enter in the theme directory and run the following command:

    cd pelican-themes/pelican-bootstrap3
    pybabel extract --mapping babel.cfg --output messages.pot ./

4. initialize your `po` files of the language you want to translate the strings with this command:

    pybabel init --input-file messages.pot --output-dir translations/ --locale lang --domain messages

where `lang` has to be replaced with the target language (`it`, `de`, etc.. **be sure to use [ISO codes](https://en.wikipedia.org/wiki/ISO_639-1))

5. translate the `po` generated file that you will find in `translations/lang/LC_MESSAGE/messages.po` where `lang` is the language code. You can find many tools to translate `po` files ([Poedit](https://poedit.net/), [Qt Linguist](http://doc.qt.io/qt-5/qtlinguist-index.html))

6. create the binary `mo` file that will be read during the website builing with:

pybabel compile --directory translations/ --domain messages


That's it! Your theme is now translate in as many languages you want.

If you have updated you theme you have to do just some of the steps.

7. regenerate a `pot` file as described in step 3.
8. merge together the new and the old strings in the same `po` file but maintaining the old translations with:

    pybabel update --input-file messages.pot --output-dir translations/ --domain messages

9. translate the strings as described in step 5.
10. compile the `mo` file as described in step 6.


### Localize pages and articles
A great plugin to localize pages and article is [i18n_subsites](https://github.com/getpelican/pelican-plugins/tree/master/i18n_subsites): it allows you to add as may languages as you want and it organizes them into a ordered structure.

You have to add some additional variable in `pelicanconf.py` file as suggested in the main page of the repository.

All that follows are the settings for my website:

    PLUGINS = ['i18n_subsites'] # to activate it

    # dictionary of languages
    I18N_SUBSITES = {
        'it': {
            'THEME_STATIC_DIR': 'pelican-bootstrap3',
        },
        'en': {
            'THEME_STATIC_DIR': 'pelican-bootstrap3',
        },
    }

For each language in the dictionary, the plugin will generate a copy of all the content in the output folder:

    ├── author
    ├── category
    ├── drafts
    ├── en
    │   ├── author
    │   ├── category
    │   ├── drafts
    │   ├── pages
    │   ├── pelican-bootstrap3
    │   │   ├── css
    │   │   │   ├── pygments
    │   │   │   └── shariff
    │   │   ├── fonts
    │   │   ├── js
    │   │   └── tipuesearch
    │   │       └── img
    │   └── tag
    ├── extras
    │   └── data_analysis
    ├── images
    │   ├── blog
    │   └── site
    ├── it
    │   ├── author
    │   ├── category
    │   ├── drafts
    │   ├── pages
    │   ├── pelican-bootstrap3
    │   │   ├── css
    │   │   │   ├── pygments
    │   │   │   └── shariff
    │   │   ├── fonts
    │   │   ├── js
    │   │   └── tipuesearch
    │   │       └── img
    │   └── tag
    ├── pages
    ├── tag
    └── theme
        ├── css
        │   ├── pygments
        │   └── shariff
        ├── fonts
        ├── js
        └── tipuesearch
            └── img


within the `en` and the `it` folder all the pages and articles are available.

Even if it is not mandatory, I personally added the DEFAULT_LANG to the dictionary because, for my website structure, I need different folders for each languages.

Next, probably you want to add some kind of *switching button* to change the language. I'll not go deep into it, just point to the [original source](https://github.com/getpelican/pelican-plugins/blob/master/i18n_subsites/implementing_language_buttons.rst) and an [additional resource](https://github.com/getpelican/pelican-plugins/issues/282).

The only lack I see is that it not so easy to keep the translations synchronized. In fact, when you change the content of a page, you have manually to change the same page for all the other languages, but without knowing which strings have changed.

I have not find a solution for that, awesome would be to have the plugin using the `pot`, `po` and `mo` files: that way the workflow would be super simple.

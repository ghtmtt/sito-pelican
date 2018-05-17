Title: Server random notes
Date: 2017-09-20
Slug: server-notes
lang: en
tags: linux, server

The following documents is just a container of some notes for the correct (maybe)
server maintaining.

* connect to the server via terminal. `root` is the user `@` and the server name
or the IP address `root@94.130.104.252`:

    $ ssh root@94.130.104.252

* add and switch user:

    #you must be connected as root!
    $ ssh root@94.130.104.252
    $ adduser user_name

    #change user_name
    $ su user_name

    #change password
    $ passwd user_name

  many other options listed [here](https://askubuntu.com/a/410274/190165)

* locale problems. In my case the server was delivered with 3 *locales* (English,
  German and Russian), but had some problem when running command due to a missing
  setting.

    $ locale
    LANG=en_US.UTF-8
    LANGUAGE=not set
    LC_CTYPE="en_US.UTF-8"
    LC_NUMERIC="en_US.UTF-8"
    LC_TIME="en_US.UTF-8"
    LC_COLLATE="en_US.UTF-8"
    LC_MONETARY="en_US.UTF-8"
    LC_MESSAGES="en_US.UTF-8"
    LC_PAPER="en_US.UTF-8"
    LC_NAME="en_US.UTF-8"
    LC_ADDRESS="en_US.UTF-8"
    LC_TELEPHONE="en_US.UTF-8"
    LC_MEASUREMENT="en_US.UTF-8"
    LC_IDENTIFICATION="en_US.UTF-8"
    LC_ALL=en_US.UTF-8

  The **LANGUAGE** variable is not set, so problems will be there. I solved by
  adding the environmental variable and to recompile the locales:

    #switch as root
    $ export LC_ALL="en_US.UTF-8"
    $dpkg-reconfigure locales

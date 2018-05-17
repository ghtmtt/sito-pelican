Title: Add a raster layer into a PostGIS database
Date: 2017-09-20
Slug: add-raster-postgis
lang: en
tags: gis, postgis

PostGIS is a very powerful, complete and reliable DBMS. Besides vector layers you
can also add **raster** layers into it and load them into QGIS.

PostGIS installation comes together with a tool named `raster2psql` that makes all
the effort for you. The commands are pretty simples:

1. create a `sql` file from a raster layer with:

    $ raster2pgsql raster > file.sql

2. load the `sql` file into your database:

    $ psql -d database -f file.sql


That's it!

Title: Aggiungere una vista in un geopackage
Date: 2018-05-15
Slug: view-geopackage
lang: it
tags: gis, geopackage

I geopackage supportano anche le vista. Per inserire una nuova vista bisogna però
aggiungere manualmente anche 2 righe in 2 colonne nascoste.

Creazione vista:

    CREATE VIEW vista AS
    SELECT * FROM citta_toscana

Prima registrazione nella tabella `gpkg_contents`:

    INSERT INTO gpkg_contents (table_name, identifier, data_type, srs_id)
    VALUES ( 'vista', 'vista', 'features', 3003)

Seconda registrazione dentro la tabella `gpkg_geometry_columns`:

    n po chet

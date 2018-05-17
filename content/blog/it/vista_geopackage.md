Title: Aggiungere una vista in un geopackage
Date: 201-05-15
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

    INSERT INTO gpkg_geometry_columns (table_name, column_name, geometry_type_name, srs_id, z, m)
    values ('vista', 'vista', 'GEOMETRY', 3003, 0, 0)

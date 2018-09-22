Title: RecoverGeometryColumn SpatiaLite
Date: 2017-04-15
Slug: recovergeomcolumn
lang: it
tags: gis, spatialite

Avendo una tabella in un db SpatiaLite,s e si vuole creare una tabella con
solamente alcune colonne:

```sql
CREATE TABLE peaks AS
SELECT id, geom as geom, ele, name
FROM all_peaks
```

la tabella non è ancora spaziale anche se contiene la colonna `geom` che è
riconosciuta come binario (BLOB). Per recuperare una colonna geometrica (se già
presente nella tabella):

```sql
SELECT RecoverGeometryColumn('peaks', 'geom', 4326, 'MULTIPOINT', 'XY')
```

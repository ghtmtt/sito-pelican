Title: Sincronizzare i file con Lucky Backup
Date: 2017-06-15
Slug: lucky-backup
lang: it
tags: backup, rsync

[Lucky Backup](http://luckybackup.sourceforge.net/) altro non è che un'interfaccia grafica al potentissimo programma [rsync](https://linux.die.net/man/1/rsync).

Ci moltissime opzioni disponibili: impostare un calendario delle sincronizzazioni (es. ogni mercoled' alle 12:00 sincronizzare una specifica), definire diversi **profili** ognuno con diversi *task* (diverse cartelle da sincronizzare) e soprattutto copiare la stringa finale di `rsync` e crearci uno script `bash`.

![](/images/blog/luckyBackup_01.png)

Volendo faer il backup di un'intera cartella di lavoro su un dispositivo esterno, basta creare un nuovo *Task* e a seconda delle opzioni che si vogliono attivare, Lucky Backup fornisce un'ampia gamma di opzioni avanzate, fra cui

* escludere determinati file
* includere determinati file
* connettersi anche a cartelle remote

Una delle impostazioni più importanti è quella di scegliere il **Tipo** di backup che si vuole fare. Luck offre 2 scelte:

1. **Sorgente del backup dentro la Destinazione**. Ottima opzione se si collega un hard disk esterno e si vuole copiare il contenuto di una o più cartelle. In questo viene creata una copia esatta  della **Sorgente** dentro la destinazione. Si può spuntare la casella *NON creare altre directory* per **non** creare un'altra cartella dentro la Destinazione:

    Sorgente -> `/home/matteo/Pictures`
    Destinazione -> `/media/usb/Images`

    In questo esempio la cartella `Pictures` verrà interamente copiata dentro `Images`. Con la casella non spuntanta verrebbe creata la cartella `Pictures` dentro la cartella `Images`. Inoltre, se nelle opzioni avanzate si spunta la casella *Cancella file sulla destinazione*, eliminando un file nella Sorgente questo verrà anche eliminato nella Destinazione.

    ![](/images/blog/luckyBackup_02.png)

2. **Sincronizzazione Sorgente e Destinazione**. Questa opzione permette di mantenere la copia **più recente** dei file in entrambe le cartelle Sorgente e Destinazione. Viene fatta una verifica temporale (**snapshot**) dei file e viene quindi copiata la versione più recente in entrambe le direzioni (da Sorgente a Destinazione ma anche viceversa). Ottima opzione se si lavora anche sulla Destinazione, non molto indicato se la Destinazione è pensata solamente come una copia della sorgente.

    Inoltre, se viene eliminato un file in una delle due cartelle, ma nell'altra cartella viene modificato in un momento successivo, dal momento che la modifica è più rencete rispetto all'eliminazione, il file verrà di nuovo copiato.

    ![](/images/blog/luckyBackup_03.png)

Infine, cliccando sul pulsante *Controlla* viene fatta una verifica delle cartelle e del comando ed è possibile copiare la stringa di `rsync` da includere direttamente in uno script bash. Si può creare il file `mio_backup.sh` e copiare la stringa:

`#!/bin/bash`

`rsync -h --progress --stats -r -tgo -p -l -D --update /home/matteo/Pictures/ /media/usb/Images`

ed aggiungere la modalità `esecuzione`:

```
chmod +x mio_backup.sh
```

e da un terminale eseguire semplicemente:

```
./mio_backup.sh
```

per fare il backup in *background*.

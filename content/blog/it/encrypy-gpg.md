Title: Crittografare un file con gpg
Date: 2017-04-15
Slug: encrypt-gpg
lang: it
tags: encrypt, gpg

Proteggere un file con una password è molto utile e a volte necessario.
[gpg](https://gnupg.org/) è un programma perfetto, semplice e molto sicuro per crittografare i file.

Per crittografare un file bisogna andare nella cartella dove si trova il file (esempio, `documento.odt`) e lanciare un semplice comando:

    cd Documents
    gpg -c documento.odt

`gpg` chiederà di inserire una password e di confermarla. Fatto questo, nella cartella sarà presente il file `documento.odt.gpg` che è a tutti gli effetti il file protetto e impossibile da aprire senza la password.

Per decrittare il file, sempre nella cartella dove si trova, bisogna dare il comando:

    gpg documento.odt.gpg

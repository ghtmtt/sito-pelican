Title: Encrypt file with gpg
Date: 2017-04-15
Slug: encrypt-gpg
lang: en
tags: encrypt, gpg


Protect important files with a password is very important and sometimes necessaary.
[gpg](https://gnupg.org/) is the perfect software: simple, very secure and strong.

To encrypt the file you have to change the directory where the file is located (e.g. document.odt) and run the following command:

    cd Documents
    gpg -c document.odt

`gpg` will ask you to add a password and to conferm it. Then, in the folder you will see the additional file `document.odt.gpg` that is the protected file and impossible to open without the password.

To decrypt the file, in the file folder, just run:

    gpg document.odt.gpg

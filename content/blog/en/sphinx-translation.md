Title: Create a translation environment with a sphinx project
Date: 2017-09-21
Slug: translation-sphinx
lang: en
tags: sphinx, i18n

Some instructions to add the translation environment for a sphinx project.

1. check your `Makefile` and look if there is the `gettext` rule. If not add this
2 parameters to the Makefile:

    I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) source

    gettext:
      $(SPHINXBUILD) -b gettext $(I18NSPHINXOPTS) $(BUILDDIR)/locale
      @echo
      @echo "Build finished. The message catalogs are in $(BUILDDIR)/locale."

In this way you are configuring the `I18NSPHINXOPTS` variable. Be sure that in
this line the `source` parameter is the directory where the `conf.py` file is located.
If you have the `conf.py` file in the same directory of the `Makefile` then just
add a `.`

Moreover, the building directory is set up to be `locale` within the building
directory (so the same directory where all the other building files are shipped).

2. now you are ready to run `gettext`:

    make gettext

this will add `.pot` files in the `locale` directory (e.g. `build/locale`)

3. you can now create the `.po` files from the just created `.pot` ones for your
language. So `.pot` files are the main *i18n* documents, while the `.po` files
are created **for each** language in specific directories:

    sphinx-intl update -p build/locale -l it

where `build/locale` is the directory of the `.pot` files, so the ones generated
by `gettext` and `it` is the language code of the future translated documents.

`.po` files are ready to be translated with `Qt Linguist` or any other software.

The last 2 steps have to be re-run any time the source `.rst` files change: the
last command will take care to **update** the files and not to trash the existing
translations.

4. before compiling the final documents, the `Makefile` needs a small change is
order to accept the language options.

It is useful to put the translations of different languages into separated
directories, like `build/html/en` and `build/html/it`.

In the `Makefile` add at the beginning some additional options:

    LANG = en
    SPHINXOPTS = -D language=$(LANG) -A language=$(LANG) $(SOURCEDIR)

so you are creating the `LANG` variable and you are defining the `SPHINXOPTS` for
further use.

Next you have to add a small check into the target makes:

    html:
    	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html/$(LANG)
    	@echo
    	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

    	@if [ $(LANG) != "en" ]; then \
    		$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html/$(LANG); \
    	else \
    		$(SPHINXBUILD) -n -W -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html/$(LANG); \
    	fi
    	@echo
    	@echo "HTML Build finished. The HTML pages for '$(LANG)' are in $(BUILDDIR)."

this will check the language source and will compile in the output directory the
corresponding languages (`build/html/en`).

You can then simply compile the final documents with:

    make html LANG=it

4. you can create an useful command in the `Makefile` that runs `gettext` and
`sphinx-intl` in order to create updated strings (if something is changed in the
original documents).

The command could be something like this:

    transupdate: gettext
    	$(SPHINXINTBUILD) update -p $(BUILDDIR)/locale -l $(LANG)
    	@echo
    	@echo "Build finished. po fies have been updated."

So typing:

    make transupdate LANG=it

will run first `gettext` (this means cleaning and recreating the `.pot` files)
and will also look for some updates in the source strings so to create new `.po`
file for the language specified.

So the workflow is the following:

1. create `.pot` files with `gettext`
2. create language specific `.po` files with `sphinx-intl`
3. translate the `.po` files with `Qt Linguist`
4. compile the final output with for example `make html LANG=it`

If some source document is changed:

4. run `make transupdate LANG=en` and `make transupdate LANG=it` to update the
documents.


### sphinx and transifex

Super useful is also combining sphinx and transifex. It is pretty straightforward

1. go on transifex and create another organization (if non yet) and a new project
  in this example we will call the project *my-project*

2. install the transifex client with pip (so very useful is having a virtualenv
  set up):

    pip install transifex-client

3. cd into your documents root and create the `tx-config` files with:

    cd my-document-root
    tx init

  have a look that the .tx folder exists and is inside the document-root directory.

4. now you have to update the transifex-resources file indicating where the `.pot`
  files are. In orther to do that, always within the document-root:

    sphinx-intl update-txconfig-resources --pot-dir build/locale \
    --transifex-project-name my-project

  where `build/locale` is the directory where all the `.pot` files are located
  and `my-project` is the name of the transifex remote project

5. if everything is fine you can now upload the translation files in transifex
  simply with:

    tx push -s

6. now in transifex you can translated the different strings and to get them into
  your local directory type:

    tx pull -l it

  so one pull for each language.

7. build your local files (e.g. `make html LANG=it`) and that's it.

refer also here http://www.sphinx-doc.org/en/stable/intl.html#contributing-to-sphinx-reference-translation

Title: Translate your QGIS plugin in many languages
Date: 2017-09-24
Slug: qgis-plugin-i18n
lang: en
tags: qgis, i18n

If you have used the Plugin Builder to create the template of your plugin, good
news! You already have a perfect suite on how to build both documentation and UI
in different languages with a small effort.

## UI translation

The `Makefile` shipped with the Plugin Builder should become your best friend.
In the first rows of the file you should see something like:

    #Add iso code for any locales you want to support here (space separated)
    # default is no locales
    # LOCALES = af
    LOCALES =
    # If locales are enabled, set the name of the lrelease binary on your system. If
    # you have trouble compiling the translations, you may have to specify the full path to
    # lrelease
    #LRELEASE = lrelease
    #LRELEASE = lrelease-qt4

    # translation
    SOURCES = \
    	__init__.py \
    	data_plotly.py data_plotly_dialog.py

    PLUGINNAME = DataPlotly

    PY_FILES = \
    	__init__.py \
    	data_plotly.py data_plotly_dialog.py

    UI_FILES = data_plotly_dialog_base.ui

so, some variables are defined and some other are waiting for you.

1. add as many languages in the **LOCALE** variable (space separated) as you want:

    LOCALES = it es de

2. uncomment the **LRELEASE** variable:

        #If locales are enabled, set the name of the lrelease binary on your system. If
        #you have trouble compiling the translations, you may have to specify the full path to
        #lrelease
        LRELEASE = lrelease

3. be sure that all the files that contains strings that have to be translated are
listed in the **PY_FILES** and **UI_FILES**. If you have extended the plugin with
other files or many other forms (UI) you have to add them here.

4. The translation workflow is pretty simple:

  * read all the source forms and py files with strings to be translated
  * create the corresponding `.ts` file **for each** language
  * translate the strings using an editor (Qt Linguist recommended)
  * compile the `.ts` file into `.qm` (the one QGIS can read)

To accomplish this, the `Makefile` come with 2 useful command: **transup** and
**transcompile**.
The first calls the script `updaste-strings.sh` script and takes care of creating
the `.ts` file while the second calls the `compile-strings.sh` script that creates
the `.qm` file from the translations within `.ts`

QGIS will upload and read the file `your_plugin_language.qm` in the i18n directory,
so if your plugin is called geocoding and you have translated it in Spanish, the
name of the final `.qm` file **must be** `geocoding_es.qm` else the default source
language is loaded.

In order to do this, you have to make small adjustments to both `update-strings.sh`
and `compile-strings.sh`.

The only *hack* I introduced is add the **PLUGINNAME** variable as `yourPlugin_`
so that the final file is correctly named (before this hack the translation files
were named only with the language code).

For the `update-strings.sh` script, add this variable at the beginning:

    PLUGINNAME="myplugin_"

and add this variable where needed:

    for LOCALE in ${LOCALES}
    do
      echo "i18n/"$PLUGINNAME${LOCALE}".ts"
      # Note we don't use pylupdate with qt .pro file approach as it is flakey
      # about what is made available.
      pylupdate4 -noobsolete ${PYTHON_FILES} -ts i18n/$PLUGINNAME${LOCALE}.ts
    done

while for `compile-strings.sh`:

    LRELEASE=$1
    LOCALES=$*
    PLUGINNAME="myplugin_"


    for LOCALE in ${LOCALES}
    do
        echo "Processing: $PLUGINNAME${LOCALE}.ts"
        # Note we don't use pylupdate with qt .pro file approach as it is flakey
        # about what is made available.
        $LRELEASE i18n/$PLUGINNAME${LOCALE}.ts
    done


**WARNING** you have to re-run the `update-string.sh` script every time you add
something in your plugin. You will not loose the old translation but if you don't
run this script you cannot translate the newer strings.

## Small note for DataPlotly
All the scripts are within the Makefile.

For the UI:

1. if something is changed just run: `make txpush`. This command will call automatically
the `transup` command that will look for newer strings and pushes them to tx
2. translate only in tx. Once done run `make transcompile`. This command will download
all translated strings from transifex, make the ts and compile the qm.

For the manual:

1. cd in the `help` directory
2. run ``make txpush``. This will take all the new and untranslated strings and push
them to tx
3. translate in tx then run `make html LANG=it` to automatically download the strings
  from transifex and build the html. **TO BE DONE FOR ALL LANGUAGES**
4. given the big space required for each language (_images folder), after having
  run `make html LANG=here the language` run `make replace`. This will run and
  an additional script that does all the work (moving and removing folder and
  replacing the paths of the images in each html).

**IF SOMETHING IS NOT WORKING FOR UI OR MANUAL REMOVE THE TS FILE (UI) AND THE
PO FILES (MANUAL) AND RE-PULL FROM TX (AND RECOMPILE)**

## Addendum for the MANUAL

1. to **upload** new strings because the source changed just run `tx push`. It
  calls automatically `gettext` that checks for strings updating

2. to **build** the html just run `make html`. This command calls:

  * txpullcomplete that pulls the translations from transifex
  * make clean to clean the build directory
  * localehtml that build the html for each language with the translated strings
  * the script that moves/replaces all the images and paths

**IMPORTANT** if new languages are added, the language code has to be added in
both Makefile and replace_script (in the LOCALES variable)

**SUPER IMPORTANT** if new rst files are added you **have to add them also in the
.tx/config file** and this file is hidden! Be careful!

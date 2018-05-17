Title: QGIS plugin unittesting
Date: 2017-04-14
Slug: qgis-plugin-unittesting
lang: en
tags: qgis, pyqgis, python

For the moment, just some instructions and reminders.

Useful links:

https://github.com/BRGM/gml_application_schema_toolbox/blob/master/tests/test_load_as_xml.py
https://gis.stackexchange.com/questions/152320/setting-pythonpath-for-compiled-qgis-version-on-linux
http://osgeo-org.1560.x6.nabble.com/Testing-plugins-against-QGIS3-with-Travis-td5287867.html
docker container of Alessandro
https://hub.docker.com/r/elpaso/qgis-testing-environment/
some instructions to combine docker and travis (kind of working but takes huge time to build the container)
https://github.com/boundlessgeo/qgis-testing-environment-docker#running-in-travis


It is mandatory to add **2 PATHS** to `PYTHONPATH`:

1. the python path of the qgis building ()
2. the python path of the plugin folder in order to import the plugin classes

The correct way to add them is:

    $ # default python of QGIS
    export PYTHONPATH="${PYTHONPATH}:/usr/local/share/qgis/python/plugins"
    # user installed plugins
    export PYTHONPATH="${PYTHONPATH}:${HOME}/.qgis2/python/plugins"

So in my case, for the `DataPlotly` plugin the upper snippet becomes:


    $ # default QGIS plugins
    export  PYTHONPATH="${PYTHONPATH}:/home/matteo/lavori/QGIS/build-qgis3/output/python/"
    # user installed plugins
    export PYTHONPATH="${PYTHONPATH}:/home/matteo/.local/share/QGIS/QGIS3/profiles/matteo/python/plugins/"

Then from the **same bash** tests can be run:

    $ python3.5 test/test_my_dialog.py

**WARNING**: this procedure is to repeat every time the bash is closed. The script `run_env_linux.sh` within the `script` folder should set up all this things. You have to add to the `PYTHONPATH` also the plugin folder:

    export PYTHONPATH="${PYTHONPATH}:/home/matteo/.local/share/QGIS/QGIS3/profiles/matteo/python/plugins/"

You have to run the script with:

    source ./scripts/run-env-linux.sh

Having the standard plugin folder structure of the Plugin Builder, the test files are within the `test` folder.
Some import could be tricky. In the following tree view some files are omitted, but the idea is to use the `test/test_data_plotly_dialog.py` to test the functions of the `data_plotly_dialog.py` file in the main directory:

    ├── help
    ├── i18n
    ├── icons
    ├── jsscripts
    ├── scripts
    ├── test
    │   ├── __init__.py
    │   ├── qgis_interface.py
    │   ├── test_data_plotly_dialog.py
    │   ├── test_init.py
    │   ├── test_qgis_environment.py
    │   ├── test_resources.py
    │   ├── test_test_class.py
    │   ├── test_translations.py
    │   └── utilities.py
    ├── ui
    │   └── data_plotly_dialog_base.ui
    ├── data_plotly.py
    ├── data_plotly_dialog.py
    ├── data_plotly_plot.py


Let's have a look at the imports of `test_data_plotly_dialog.py`:

    import qgis
    from qgis.testing import start_app, unittest

    from PyQt5.QtWidgets import QDialogButtonBox, QDialog

    from DataPlotly.data_plotly_dialog import DataPlotlyDialog

    from utilities import get_qgis_app
    QGIS_APP = get_qgis_app()


thanks to the PYTHONPATH addition we can import the `qgis` modules and the `DataPlotly` (or plugin) module.

Without that additions the tests will fail.

So summary:

1. edit the `script/run-env-linux.sh` by modifying the `QGIS_PREFIX_PATH` variable with the QGIS path. For compiled QGIS, it is `/home/matteo/lavori/QGIS/build-qgis3/output`
2. add in the `script/run-env-linux.sh` the `PYTHONPATH` also to the plugin
3. be careful with some import in the `test/test_my_dialog.py` file
4. start the script with `source ./script/run-env-linux.sh`
5. run the test `python3.5 test/test_my_dialog.py`

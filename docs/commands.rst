Ananta commands
===============

Init
----

Initialize Ananta based projects. (setup.py and other sources)

.. code-block:: shell

   $ ananta init


Build
------

Build archive to upload AWS-Lambda.

.. code-block:: shell

   $ ananta -c development.ini build
   $ ls
   ... package.zip ...

Upload
------

Upload archived file.

.. code-block:: shell

   $ ananta -c development.ini upload package.zip
   $ ls
   ... package.zip ...


Deploy
------

Build and upload archive.

.. code-block:: shell

   $ ananta -c production.ini deploy

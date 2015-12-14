Ananta commands
===============

Init
----

Initialize Ananta based projects. (setup.py and other sources)

.. code-block:: shell

   $ ananta init


Package
-------

Build archive to upload AWS-Lambda.

.. code-block:: shell

   $ ananta -c development.ini package


Deploy
------

Build and upload archive.

.. code-block:: shell

   $ ananta -c production.ini deploy

Lettings case
==============

Here we find some User case of Lettings :

For index (list view)
----------------------

What happens when we try to access the lettings index and it succeeds ? :

.. automethod:: lettings.tests.test_views.LettingViewsTest.test_index_view

For letting (detail view)
--------------------------

What happens when we try to drill down on a letting detail and it succeeds ? :

.. automethod:: lettings.tests.test_views.LettingViewsTest.test_letting_view

What happens when we try to drill down into the details of a letting and it fails because the rental ID is unknown ? :

.. automethod:: lettings.tests.test_views.LettingViewsTest.test_letting_view_invalid_id
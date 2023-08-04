Profiles case
==============

Here we find some User case of Profiles :

For index (list view)
----------------------

What happens when we try to access the profiles index and it succeeds ? :

.. automethod:: profiles.tests.test_views.ProfileViewsTest.test_index_view

For profile (detail view)
--------------------------

What happens when we try to drill down on a profile detail and it succeeds ? :

.. automethod:: profiles.tests.test_views.ProfileViewsTest.test_profile_view

What happens when we try to drill down into the details of a profile and it fails because the username is unknown ? :

.. automethod:: profiles.tests.test_views.ProfileViewsTest.test_profile_view_invalid_username
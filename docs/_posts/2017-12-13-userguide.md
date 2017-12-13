---
layout: post
title: Basic user guide
tag: User
category: Docs

excerpt: Basic user guide
---

With PUT_App properly set up when, a user clicks on a shortcut to the program that controls the instrument the logon screen will be displayed.

![Logon]({{site.images}}/logon.png)

All fields are required and all but the password are remembered from the last session of the selected user name. (Limitations on fields could be a nice feature to add to the setup page)

Clicking start with the user password entered will check the password against the hashed and salted password list and if correct, start the instrument software that is set to run and display the Active screen.

![running]({{site.images}}/running.png)

The user also has the ability to change their password by selecting "Change Password" from the "Menu" on the LogOn screen.

![change password]({{site.images}}/changepass.png)

Passwords are hashed and salted and stored in a csv in the local docs folder.


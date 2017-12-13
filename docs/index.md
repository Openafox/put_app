---
layout: default
title: Home
---

# PUT_app
{: style="text-align: center;"}
A Python based application to monitor use of a particular program.

Designed for use with analytical instruments at research institutions where users are generally trusted.
Tech savvy users could easily bypass the logon program (I leave this for you to figure out how).
Also the user info csv is in a public folder allowing anyone access to emails and advisers of users but passwords are hashed and salted.


The working code can be found on [GitHub](https://github.com/openafox/put_app).

  <div class="tags-expo-list" style="text-align: center;">
    {% for tag in site.categories %}
    <a href="{{ site.baseurl }}/blog/categories#{{ tag[0] | slugify }}" class="post-tag">{{ tag[0] }}</a>
    {% endfor %}
  </div>

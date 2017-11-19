---
layout: default
title: Home
---

# PUT_app
{: style="text-align: center;"}
A Python based application to monitor use of a particular program.

The working code can be found on [GitHub](https://github.com/openafox/put_app).

  <div class="tags-expo-list" style="text-align: center;">
    {% for tag in site.categories %}
    <a href="{{ site.baseurl }}/blog/categories#{{ tag[0] | slugify }}" class="post-tag">{{ tag[0] }}</a>
    {% endfor %}
  </div>

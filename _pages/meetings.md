---
layout: page
title: Meeting Minutes
permalink: /meetings/
---

{% for post in site.posts %}
# <a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
{{ post.date | date: "%b %-d, %Y"}}
{{ post.excerpt }} <a href="{{ post.url | prepend: site.baseurl }}">more...</a>
{% endfor %}


---
layout: default
title: Welcome
nav_order: 1
description: "Welcome"
permalink: /
---

# Welcome to the Pearl Jam Encyclopedia

Pearl Jam is an American rock band founded in 1990, in [Seattle, WA](https://google.com). The band’s current lineup consists of [Jeff Ament](https://google.com) (bass guitar), [Matt Cameron](https://google.com) (drums) [Stone Gossard](https://google.com) (rhythm guitar), [Mike McCready](https://google.com) (lead guitar), and [Eddie Vedder](https://google.com) (lead vocals, guitar). Since 2002, keyboardist [Boom Gaspar](https://google.com) has been a session and touring member of the band.

#### Thank you to the contributors for LINC tutorials!
<ul class="list-style-none">
{% for contributor in site.github.contributors %}
  <li class="d-inline-block mr-1">
     <a href="{{ contributor.html_url }}"><img src="{{ contributor.avatar_url }}" width="32" height="32" alt="{{ contributor.login }}"/></a>
  </li>
{% endfor %}
</ul>

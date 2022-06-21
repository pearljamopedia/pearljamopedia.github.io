---
layout: default
title: Welcome
nav_order: 1
description: "Welcome"
permalink: /
---

# Welcome to the Pearl Jam Encyclopedia

Pearl Jam is an American rock band founded in 1990, in Seattle, WA. The band’s current lineup consists of Jeff Ament (bass guitar), Matt Cameron (drums) Stone Gossard (rhythm guitar), Mike McCready (lead guitar), and Eddie Vedder (lead vocals, guitar). Since 2002, keyboardist Boom Gaspar has been a session and touring member of the band.

#### Thank you to the contributors for LINC tutorials!
<ul class="list-style-none">
{% for contributor in site.github.contributors %}
  <li class="d-inline-block mr-1">
     <a href="{{ contributor.html_url }}"><img src="{{ contributor.avatar_url }}" width="32" height="32" alt="{{ contributor.login }}"/></a>
  </li>
{% endfor %}
</ul>

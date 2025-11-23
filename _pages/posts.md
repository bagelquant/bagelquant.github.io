---
title: "Posts"
excerpt: "Everything about quant and life!"
permalink: /posts/
layout: topic
author_profile: true
no_card_header: true
header: 
    overlay_image: /assets/images/headers/topic-header.png
---

{% assign sorted_posts = site.posts | sort: "date" | reverse %}

<div class="archive__content">
  {% for post in sorted_posts %}
  <article class="archive__item">
    {% if post.header and post.header.overlay_image %}
    <a class="archive__item-teaser" href="{{ post.url | relative_url }}">
      <img src="{{ post.header.overlay_image | relative_url }}" alt="{{ post.title }}" loading="lazy" />
    </a>
    {% endif %}

    <div class="archive__item-body">
      <h2 class="archive__item-title">
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      </h2>

      <p class="archive__item-meta">
        {{ post.date | date: "%B %d, %Y" }}
        {% if post.read_time %}
          &bull; {{ post.read_time }} minute read
        {% endif %}
      </p>

      {% if post.excerpt %}
      <p class="archive__item-excerpt">
        {{ post.excerpt | strip_html | truncate: 220 }}
      </p>
      {% endif %}
    </div>
  </article>
  {% endfor %}
</div>

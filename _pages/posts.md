---
title: "Posts by Year"
permalink: /posts/
layout: topic
author_profile: true
---

{% assign posts_by_year = site.posts | group_by_exp: "post", "post.date | date: '%Y'" %}
{% assign posts_by_year = posts_by_year | sort: "name" | reverse %}

<nav class="archive__nav">
  <ul class="taxonomy__index">
    {% for year in posts_by_year %}
      <li>
        <a href="#year-{{ year.name }}">
          <span class="taxonomy__index__label">{{ year.name }}</span>
          <span class="taxonomy__index__count">{{ year.items | size }}</span>
        </a>
      </li>
    {% endfor %}
  </ul>
</nav>

<div class="archive__content">
  {% for year in posts_by_year %}
    {% assign sorted_posts = year.items | sort: "date" | reverse %}
    <section id="year-{{ year.name }}" class="taxonomy__section">
      <h2 class="archive__subtitle">{{ year.name }}</h2>

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
    </section>
  {% endfor %}
</div>

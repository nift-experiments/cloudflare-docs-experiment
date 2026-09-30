---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/manage-recording-config-hierarchy/
  description: Learn how to manage recording configuration hierarchy with RealtimeKit's capabilities. Follow our guide for effective hierarchy management.
  full_title: Manage Recording Config Precedence Order · Cloudflare Realtime docs
  head_html: <title>Manage Recording Config Precedence Order · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to manage recording configuration hierarchy with RealtimeKit&#x27;s capabilities. Follow our guide for effective hierarchy management."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/recording-guide/manage-recording-config-hierarchy/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/recording-guide/manage-recording-config-hierarchy/index.md"><meta property="og:title" content="Manage Recording Config Precedence Order · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to manage recording configuration hierarchy with RealtimeKit&#x27;s capabilities. Follow our guide for effective hierarchy management."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/recording-guide/manage-recording-config-hierarchy/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/recording-guide/manage-recording-config-hierarchy/#page","headline":"Manage Recording Config Precedence Order \u00b7 Cloudflare Realtime docs","description":"Learn how to manage recording configuration hierarchy with RealtimeKit's capabilities. Follow our guide for effective hierarchy management.","url":"https://developers.cloudflare.com/realtime/realtimekit/recording-guide/manage-recording-config-hierarchy/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/recording-guide/manage-recording-config-hierarchy/
  schema: 1
---
<p>This document provides an overview of the precedence structure for managing recording configurations within our system. It explains how various configuration levels interact and prioritize settings. The recording configuration can be defined at three different levels:</p>
<ul>
<li><a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/">Start recording a meeting API</a></li>
<li><a href="/api/resources/realtime_kit/subresources/meetings/methods/create/">Create a meeting API</a></li>
<li>Specified via <a href="https://dash.cloudflare.com/?to=/:account/realtime/kit">Cloudflare RealtimeKit Dashboard</a></li>
</ul>
<h2 id="understand-recording-configuration-precedence">Understand Recording Configuration Precedence</h2>
<p>To comprehend the precedence of recording configurations, it is important to delve into the following details. This understanding becomes crucial when dealing with multiple configurations set through APIs and the developer portal.</p>
<table>
<thead>
<tr>
<th>Precedence</th>
<th>Config</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td><a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/">Start recording API</a> configs</td>
<td>Highest priority in the system. Any settings defined here will take precedence over other configurations.</td>
</tr>
<tr>
<td>2</td>
<td><a href="/api/resources/realtime_kit/subresources/meetings/methods/create/">Create a meeting API</a> configs</td>
<td>Second level of priority in the system. Settings here will supersede Org level config but not Start recording a meeting API configs.</td>
</tr>
<tr>
<td>3</td>
<td>Specified via Dashboard</td>
<td>Lowest priority in the system. Settings defined here will be overridden by both Start recording a meeting API config and Create a meeting API config.</td>
</tr>
</tbody>
</table>
<h2 id="example-scenario">Example Scenario</h2>
<p>To illustrate the precedence order in action, consider the following scenario for the same meeting:</p>
<ol>
<li>
<p>Org Level Config specifies that recordings to be stored in the Cloudflare R2 bucket.</p>
</li>
<li>
<p>Create a Meeting API sets recordings to be stored in the AWS S3 storage bucket using the H264 codec.</p>
</li>
<li>
<p>Start recording a meeting API is configured to store recordings in the GCS bucket using the VP8 codec.</p>
</li>
</ol>
<p>In this scenario, the Start recording a meeting API takes precedence over the Create a Meeting API Config and Org Level Config.
As a result, the meeting's recording will be stored in the GCS bucket using VP8 codec, regardless of the defaults set at other levels.</p>

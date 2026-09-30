---
cp9:
  canonical: https://developers.cloudflare.com/waiting-room/reference/waiting-room-api/
  description: API commands for managing waiting rooms.
  full_title: API commands · Cloudflare Waiting Room docs
  head_html: <title>API commands · Cloudflare Waiting Room docs</title><meta name="generator" content="Nift"><meta name="description" content="API commands for managing waiting rooms."><link rel="canonical" href="https://developers.cloudflare.com/waiting-room/reference/waiting-room-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waiting-room/reference/waiting-room-api/index.md"><meta property="og:title" content="API commands · Cloudflare Waiting Room docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API commands for managing waiting rooms."><meta property="og:url" content="https://developers.cloudflare.com/waiting-room/reference/waiting-room-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Waiting Room"><meta name="algolia_product_filter" content="Waiting Room"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Waiting Room"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waiting-room/reference/waiting-room-api/#page","headline":"API commands \u00b7 Cloudflare Waiting Room docs","description":"API commands for managing waiting rooms.","url":"https://developers.cloudflare.com/waiting-room/reference/waiting-room-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waiting-room/reference/waiting-room-api/
  schema: 1
---
<p>Cloudflare Waiting Room redirect visitors to virtual waiting rooms when they are trying to access web pages that have high volumes of traffic.</p>
<p>The <a href="/api/resources/waiting_rooms/methods/list/">Cloudflare Waiting Room API</a> provides an interface for programmatically managing waiting rooms.</p>
<h2 id="request-url-format">Request URL format</h2>
<p>To invoke a <a href="/api/resources/waiting_rooms/methods/list/">Cloudflare Waiting Room API</a> operation, append the endpoint to the Cloudflare API base URL:</p>
<pre tabindex="0"><code class="language-shell">https://api.cloudflare.com/client/v4&#10;</code></pre>
<p>For authentication instructions, refer to <a href="/fundamentals/api/">Getting Started: Requests</a> in the Cloudflare API documentation.</p>
<p>For help with endpoints and pagination, refer to <a href="/fundamentals/api/">Getting Started: Endpoints</a>.</p>
<h2 id="manage-your-waiting-room">Manage your waiting room</h2>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Method + URL stub</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/api/resources/waiting_rooms/methods/list/">List waiting rooms</a></td>
<td><code>GET zones/{:zone_identifier}/waiting_rooms</code></td>
<td>List all waiting rooms for a zone.</td>
</tr>
<tr>
<td><a href="/api/resources/waiting_rooms/methods/create/">Create waiting room</a></td>
<td><code>POST zones/{:zone_identifier}/waiting_rooms</code></td>
<td>Create a waiting room.</td>
</tr>
<tr>
<td><a href="/api/resources/waiting_rooms/methods/get/">Waiting room details</a></td>
<td><code>GET zones/{:zone_identifier}/waiting_rooms/{:identifier}</code></td>
<td>Fetch a waiting room.</td>
</tr>
<tr>
<td><a href="/api/resources/waiting_rooms/methods/update/">Update waiting room</a></td>
<td><code>PUT zones/{:zone_identifier}/waiting_rooms/{:identifier}</code></td>
<td>Update a waiting room.</td>
</tr>
<tr>
<td><a href="/api/resources/waiting_rooms/methods/delete/">Delete waiting room</a></td>
<td><code>DELETE zones/{:zone_identifier}/waiting_rooms/{:identifier}</code></td>
<td>Delete a waiting room.</td>
</tr>
<tr>
<td><a href="/api/resources/waiting_rooms/methods/edit/">Patch waiting room</a></td>
<td><code>PATCH zones/{:zone_identifier}/waiting_rooms/{:identifier}</code></td>
<td>Patch a configured waiting room.</td>
</tr>
</tbody>
</table>
<h2 id="fetch-the-current-status-of-a-waiting-room">Fetch the current status of a waiting room</h2>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Method + URL stub</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/api/resources/waiting_rooms/subresources/statuses/methods/get/">Get the current status of a waiting room</a></td>
<td><code>GET zones/{:zone_identifier}/waiting_rooms/{:identifier}/status</code></td>
<td><ul><li>Returns <code>queueing</code> if the queue is activated (clients are put in the waiting room).</li><li>Returns <code>not_queueing</code> if the queue is not activated or if the waiting room is suspended.</li></ul></td>
</tr>
</tbody>
</table>

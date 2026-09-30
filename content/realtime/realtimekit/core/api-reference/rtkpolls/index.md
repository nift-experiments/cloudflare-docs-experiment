---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkpolls/
  description: ''
  full_title: RTKPolls · Cloudflare Realtime docs
  head_html: <title>RTKPolls · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkpolls/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkpolls/index.md"><meta property="og:title" content="RTKPolls · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkpolls/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkpolls/#page","headline":"RTKPolls \u00b7 Cloudflare Realtime docs","url":"https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkpolls/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/core/api-reference/rtkpolls/
  schema: 1
---
<!-- Auto Generated Below -->
<p><a name="module_RTKPolls"></a></p>
<p>The RTKPolls module consists of the polls that have been created in the meeting.</p>
<ul>
<li><a href="#module_RTKPolls">RTKPolls</a>
<ul>
<li><a href="#module_RTKPolls+items">.items</a></li>
<li><a href="#module_RTKPolls+create">.create(question, options, anonymous, hideVotes)</a></li>
<li><a href="#module_RTKPolls+vote">.vote(pollId, index)</a></li>
</ul>
</li>
</ul>
<p><a name="module_RTKPolls+items"></a></p>
<h3 id="meeting-polls-items">meeting.polls.items</h3>
An array of poll items.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKPolls"><code>RTKPolls</code></a><br />
<a name="module_RTKPolls+create"></a></p>
<h3 id="meeting-polls-create-question-options-anonymous-hidevotes">meeting.polls.create(question, options, anonymous, hideVotes)</h3>
Creates a poll in the meeting.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKPolls"><code>RTKPolls</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>question</td>
<td></td>
<td>The question that is to be voted for.</td>
</tr>
<tr>
<td>options</td>
<td></td>
<td>The options of the poll.</td>
</tr>
<tr>
<td>anonymous</td>
<td><code>false</code></td>
<td>If true, the poll votes are anonymous.</td>
</tr>
<tr>
<td>hideVotes</td>
<td><code>false</code></td>
<td>If true, the votes on the poll are hidden.</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKPolls+vote"></a></p>
<h3 id="meeting-polls-vote-pollid-index">meeting.polls.vote(pollId, index)</h3>
Casts a vote on an existing poll.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKPolls"><code>RTKPolls</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>pollId</td>
<td>The ID of the poll that is to be voted on.</td>
</tr>
<tr>
<td>index</td>
<td>The index of the option.</td>
</tr>
</tbody>
</table>

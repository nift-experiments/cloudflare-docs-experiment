---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-10-30-tcp-rtt-and-tcp-fields/
  description: New updates and improvements at Cloudflare.
  full_title: New TCP-based fields available in Rulesets · Changelog
  head_html: <title>New TCP-based fields available in Rulesets · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-10-30-tcp-rtt-and-tcp-fields/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="New TCP-based fields available in Rulesets · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-10-30-tcp-rtt-and-tcp-fields/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-30-tcp-rtt-and-tcp-fields/#page","headline":"New TCP-based fields available in Rulesets \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-10-30-tcp-rtt-and-tcp-fields/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-10-30-tcp-rtt-and-tcp-fields/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 30, 2025</time><h2 id="post-title">New TCP-based fields available in Rulesets</h2>
<div class="changelog-badges"><span>rules</span></div><div class="changelog-body"><h4 id="build-rules-based-on-tcp-transport-and-latency">Build rules based on TCP transport and latency</h4>
<p>Cloudflare now provides two new request fields in the Ruleset engine that let you make decisions based on whether a request used TCP and the measured TCP round-trip time between the client and Cloudflare. These fields help you understand protocol usage across your traffic and build policies that respond to network performance. For example, you can distinguish TCP from QUIC traffic or route high latency requests to alternative origins when needed.</p>
<hr />
<h4 id="new-fields">New fields</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.edge.client_tcp</code></td>
<td>Boolean</td>
<td>Indicates whether the request used TCP. A value of true means the client connected using TCP instead of QUIC.</td>
</tr>
<tr>
<td><code>cf.timings.client_tcp_rtt_msec</code></td>
<td>Number</td>
<td>Reports the smoothed TCP round-trip time between the client and Cloudflare in milliseconds. For example, a value of 20 indicates roughly twenty milliseconds of RTT.</td>
</tr>
</tbody>
</table>
<p>Example filter expression:</p>
<pre tabindex="0"><code>cf.edge.client_tcp &amp;&amp; cf.timings.client_tcp_rtt_msec &lt; 100&#10;</code></pre>
<p>More information can be found in the Rules language <a href="/ruleset-engine/rules-language/fields/reference/">fields reference</a>.</p>
</div></article></div>

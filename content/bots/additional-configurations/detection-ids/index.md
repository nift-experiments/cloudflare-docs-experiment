---
cp9:
  canonical: https://developers.cloudflare.com/bots/additional-configurations/detection-ids/
  description: Static rules that identify predictable bot behavior and configurable heuristics.
  full_title: Detection IDs · Cloudflare bot solutions docs
  head_html: <title>Detection IDs · Cloudflare bot solutions docs</title><meta name="generator" content="Nift"><meta name="description" content="Static rules that identify predictable bot behavior and configurable heuristics."><link rel="canonical" href="https://developers.cloudflare.com/bots/additional-configurations/detection-ids/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/bots/additional-configurations/detection-ids/index.md"><meta property="og:title" content="Detection IDs · Cloudflare bot solutions docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Static rules that identify predictable bot behavior and configurable heuristics."><meta property="og:url" content="https://developers.cloudflare.com/bots/additional-configurations/detection-ids/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Bots"><meta name="algolia_product_filter" content="Bots"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Bots"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/bots/additional-configurations/detection-ids/#page","headline":"Detection IDs \u00b7 Cloudflare bot solutions docs","description":"Static rules that identify predictable bot behavior and configurable heuristics.","url":"https://developers.cloudflare.com/bots/additional-configurations/detection-ids/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /bots/additional-configurations/detection-ids/
  schema: 1
---
<p>Detection IDs are static rules that detect predictable bot behavior with no overlap with human traffic. Each ID maps to a specific <a href="/bots/concepts/bot-detection-engines/">detection method</a> such as heuristics, verified bot detections, or anomaly detections. For example, a detection ID can identify when a client sends headers in a different order than what its claimed browser would use.</p>
<p>If you are having an issue with one of our heuristics, detection IDs allow you to decide which heuristics to enforce on your zones using customer configurable heuristics. You can choose unique actions for different bots, detected through Cloudflare’s heuristics engine. You can block, allow, or serve alternate content to specific bots to meet the unique needs of your site’s traffic.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3550.md")
</aside>
<p>You can use <code>cf.bot_management.detection_ids</code> fields in tools such as:</p>
<ul>
<li><a href="/waf/custom-rules/">Custom rules</a></li>
<li><a href="/waf/rate-limiting-rules/">Advanced Rate Limiting</a></li>
<li><a href="/rules/transform/">Transform Rules</a></li>
<li><a href="/workers/">Workers</a> (as <code>request.cf.botManagement.detectionIds</code>)</li>
</ul>
<p>Bot Detection IDs and tags are also available in <a href="/bots/bot-analytics/">Bot Analytics</a> and <a href="/waf/analytics/security-analytics/">Security Analytics</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="beta-detections">Beta detections</h3>
@markup("md", "content/.markup/bodies/3549.md")
</aside>
<hr />
<h2 id="detection-tags">Detection tags</h2>
<p>Detection tags refer to the category associated with the detection ID at the time that Cloudflare has fingerprinted a bot. For example, if a detection tag is <code>go</code>, this means that Cloudflare has observed traffic from that detection ID from a Go programming language bot.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3548.md")
</aside>
<hr />
<h2 id="create-or-edit-an-expression">Create or edit an expression</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3551.md")
</div>
<hr />
<h2 id="use-cases">Use cases</h2>
<h3 id="block-requests-that-match-a-specific-detection-id">Block requests that match a specific detection ID</h3>
<pre tabindex="0"><code class="language-js">any(cf.bot_management.detection_ids[*] eq 3355446)&#10;and not cf.bot_management.verified_bot&#10;and http.request.uri.path eq &quot;/login&quot;&#10;and http.request.method eq &quot;POST&quot;&#10;</code></pre>
<h3 id="run-bot-management-without-specific-detection-ids">Run Bot Management without specific detection IDs</h3>
<pre tabindex="0"><code class="language-js">cf.bot_management.score lt 30&#10;and not cf.bot_management.verified_bot&#10;and http.request.uri.path eq &quot;/login&quot;&#10;and http.request.method eq &quot;POST&quot;&#10;and not any(cf.bot_management.detection_ids[*] in {3355446 12577893})&#10;</code></pre>
<hr />
<h2 id="bot-detection-ids-via-logpush">Bot Detection IDs via Logpush</h2>
<p>You can create or edit existing Logpush jobs to include the new Bot Detection IDs field which will provide an array of IDs for each request that has heuristics match on it. The <code>BotDetectionIDs</code> field is available as part of the HTTP Requests dataset and you can add it to new or existing jobs via the Logpush API or on the Cloudflare dashboard. This is the primary method to discover Detection IDs.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3555.md")
</div></div>
<hr />
<h2 id="availability">Availability</h2>
<p>Detection IDs are available for Enterprise Bot Management customers.</p>

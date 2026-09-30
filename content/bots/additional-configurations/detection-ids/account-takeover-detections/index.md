---
cp9:
  canonical: https://developers.cloudflare.com/bots/additional-configurations/detection-ids/account-takeover-detections/
  description: Detection IDs for identifying and mitigating automated account takeover attacks.
  full_title: Account takeover detections · Cloudflare bot solutions docs
  head_html: <title>Account takeover detections · Cloudflare bot solutions docs</title><meta name="generator" content="Nift"><meta name="description" content="Detection IDs for identifying and mitigating automated account takeover attacks."><link rel="canonical" href="https://developers.cloudflare.com/bots/additional-configurations/detection-ids/account-takeover-detections/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/bots/additional-configurations/detection-ids/account-takeover-detections/index.md"><meta property="og:title" content="Account takeover detections · Cloudflare bot solutions docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Detection IDs for identifying and mitigating automated account takeover attacks."><meta property="og:url" content="https://developers.cloudflare.com/bots/additional-configurations/detection-ids/account-takeover-detections/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Bots"><meta name="algolia_product_filter" content="Bots"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Bots"><meta name="pcx_tags" content="Account takeover"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/bots/additional-configurations/detection-ids/account-takeover-detections/#page","headline":"Account takeover detections \u00b7 Cloudflare bot solutions docs","description":"Detection IDs for identifying and mitigating automated account takeover attacks.","url":"https://developers.cloudflare.com/bots/additional-configurations/detection-ids/account-takeover-detections/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Account takeover"]}</script>
  markdown: true
  noindex: false
  route: /bots/additional-configurations/detection-ids/account-takeover-detections/
  schema: 1
---
<p>Using the detection IDs below, you can detect and mitigate account takeover attacks. You can monitor the number of login requests for a given software and network combination, as well as the percentage of login errors. When it reaches a suspicious level, you can prevent these attacks by using <a href="/waf/custom-rules/">custom rules</a>, <a href="/waf/rate-limiting-rules/">rate limiting rules</a>, and <a href="/workers/">Workers</a>.</p>
<table>
<thead>
<tr>
<th><span style="width:100px">Detection ID</span></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>201326592</code></td>
<td>Matches traffic that is making a suspicious amount of login failures to the zone.</td>
</tr>
<tr>
<td><code>201326593</code></td>
<td>Matches traffic that is making a suspicious amount of login attempts to the zone.</td>
</tr>
<tr>
<td><code>201326598</code></td>
<td>Sets a dynamic threshold based on the normal traffic that is unique to the zone.<br /><br /> When the ID matches a login failure, Bot Management sets the <a href="/bots/concepts/bot-score/">bot score</a> to 29 and uses <a href="/bots/concepts/bot-detection-engines/#anomaly-detection-enterprise">anomaly detection</a> as its score source.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="login-endpoints">Login endpoints</h3>
@markup("md", "content/.markup/bodies/3557.md")
</aside>
<h2 id="challenges-for-account-takeover-detections">Challenges for account takeover detections</h2>
<p>Cloudflare's <a href="/cloudflare-challenges/challenge-types/challenge-pages/#managed-challenge">Managed Challenge</a> can limit brute-force attacks on your login endpoints.</p>
<p>To access account takeover detections:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3558.md")
</div>
<pre tabindex="0"><code class="language-js">&#10;(any(cf.bot_management.detection_ids[*] eq 201326593))&#10;</code></pre>
<h2 id="limit-logins-with-account-takeover-detections">Limit logins with account takeover detections</h2>
<p>Rate limiting rules can limit the number of logins from a particular IP, JA4 fingerprint, or country.</p>
<p>To use rate limiting rules with account takeover detections:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3559.md")
</div>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="enhanced-with-leaked-credential-detections">Enhanced with leaked credential detections</h3>
@markup("md", "content/.markup/bodies/3556.md")
</aside>

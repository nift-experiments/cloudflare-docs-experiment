---
cp9:
  canonical: https://developers.cloudflare.com/ssl/origin-configuration/ssl-tls-recommender/
  description: Get recommendations for the optimal SSL/TLS encryption mode.
  full_title: SSL/TLS Recommender · Cloudflare SSL/TLS docs
  head_html: <title>SSL/TLS Recommender · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Get recommendations for the optimal SSL/TLS encryption mode."><link rel="canonical" href="https://developers.cloudflare.com/ssl/origin-configuration/ssl-tls-recommender/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/origin-configuration/ssl-tls-recommender/index.md"><meta property="og:title" content="SSL/TLS Recommender · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Get recommendations for the optimal SSL/TLS encryption mode."><meta property="og:url" content="https://developers.cloudflare.com/ssl/origin-configuration/ssl-tls-recommender/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/origin-configuration/ssl-tls-recommender/#page","headline":"SSL/TLS Recommender \u00b7 Cloudflare SSL/TLS docs","description":"Get recommendations for the optimal SSL/TLS encryption mode.","url":"https://developers.cloudflare.com/ssl/origin-configuration/ssl-tls-recommender/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/origin-configuration/ssl-tls-recommender/
  schema: 1
---
<p>The SSL/TLS Recommender helps you choose which <a href="/ssl/origin-configuration/ssl-modes/">Encryption mode</a> is best for your application.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13994.md")
</aside>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="common-tasks">Common tasks</h2>
<h3 id="enable-ssl-tls-recommendations">Enable SSL/TLS recommendations</h3>
<p>To make sure you do not inadvertently block the <strong>SSL/TLS Recommender</strong>, review your settings to make sure your domain:</p>
<ul>
<li>Is accessible.</li>
<li>Is not blocking requests from our bot (which uses a user agent of <code>Cloudflare-SSLDetector</code>).</li>
<li>Does not have any active, SSL-specific <a href="/rules/page-rules/">Page Rules</a> or <a href="/rules/configuration-rules/">Configuration rules</a>.</li>
</ul>
<p>Then, you can enable the SSL/TLS recommender.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/13997.md")
</div></div>
<h3 id="manually-trigger-a-new-scan">Manually trigger a new scan</h3>
<p>Once you enable it, the recommender runs future scans periodically — typically every two days — and sends notifications if new recommendations become available.</p>
<p>To manually re-trigger a new scan, disable and then <a href="#enable-ssltls-recommendations">re-enable SSL/TLS recommendations</a>.</p>
<h2 id="how-it-works">How it works</h2>
<p>Once enabled, the SSL/TLS Recommender runs an origin scan using the user agent <code>Cloudflare-SSLDetector</code> and ignores your <code>robots.txt</code> file (except for rules explicitly targeting the user agent).</p>
<p>Based on this initial scan, the Recommender may decide that you could use a stronger <a href="/ssl/origin-configuration/ssl-modes/">SSL encryption mode</a>. It will never recommend a weaker option than what is currently configured.</p>
<p>If so, it will send the application owner an email with the recommended option and add a <em>Recommended by Cloudflare</em> tag to that option on the <strong>SSL/TLS</strong> page. You are not required to use this recommendation.</p>
<p>If you do not receive an email, keep your current <strong>SSL encryption mode</strong>.</p>

---
cp9:
  canonical: https://developers.cloudflare.com/logs/logpull/enabling-log-retention/
  description: Turn log retention on or off for Logpull.
  full_title: Enabling log retention · Cloudflare Logs docs
  head_html: <title>Enabling log retention · Cloudflare Logs docs</title><meta name="generator" content="Nift"><meta name="description" content="Turn log retention on or off for Logpull."><link rel="canonical" href="https://developers.cloudflare.com/logs/logpull/enabling-log-retention/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/logs/logpull/enabling-log-retention/index.md"><meta property="og:title" content="Enabling log retention · Cloudflare Logs docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Turn log retention on or off for Logpull."><meta property="og:url" content="https://developers.cloudflare.com/logs/logpull/enabling-log-retention/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Logs"><meta name="algolia_product_filter" content="Logs"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Logs"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/logs/logpull/enabling-log-retention/#page","headline":"Enabling log retention \u00b7 Cloudflare Logs docs","description":"Turn log retention on or off for Logpull.","url":"https://developers.cloudflare.com/logs/logpull/enabling-log-retention/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /logs/logpull/enabling-log-retention/
  schema: 1
---
<p>By default, your HTTP request logs are not retained. When using the Logpull API for the first time, you will need to enable retention. You can also turn off retention at any time. Note that after retention is turned off, previously saved logs will be available until the retention period expires (refer to <a href="/logs/logpull/understanding-the-basics/#data-retention-period">Data retention period</a>).</p>
<h2 id="endpoints">Endpoints</h2>
<p>There are two endpoints for managing log retention:</p>
<ul>
<li><code>GET /logs/control/retention/flag</code> - returns the current status of retention</li>
<li><code>POST /logs/control/retention/flag</code> - turns retention on or off</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/10480.md")
</aside>
<h2 id="example-api-requests-using-curl">Example API requests using cURL</h2>
<h3 id="check-log-retention-status">Check log retention status</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10484.md")
</div></div>
<p>If the zone has log retention <a href="/logs/logpull/enabling-log-retention/#enabled-response">enabled</a> you get the value <code>true</code>, whereas a value of <code>false</code> is returned when it is <a href="/logs/logpull/enabling-log-retention/#disabled-response">disabled</a>.</p>
<h3 id="turn-on-log-retention">Turn on log retention</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10488.md")
</div></div>
<h4 id="enabled-response">Enabled response</h4>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;flag&quot;: true&#10;}&#10;</code></pre>
<h3 id="turn-off-log-retention">Turn off log retention</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10492.md")
</div></div>
<h4 id="disabled-response">Disabled response</h4>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;flag&quot;: false&#10;}&#10;</code></pre>
<h2 id="audit">Audit</h2>
<p>Turning log retention on or off is recorded in <a href="/fundamentals/account/account-security/review-audit-logs/#access-audit-logs">Cloudflare Audit Logs</a>.</p>

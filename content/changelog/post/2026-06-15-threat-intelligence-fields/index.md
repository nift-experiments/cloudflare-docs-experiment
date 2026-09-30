---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-06-15-threat-intelligence-fields/
  description: New updates and improvements at Cloudflare.
  full_title: Use Cloudforce One threat intelligence in WAF rules · Changelog
  head_html: <title>Use Cloudforce One threat intelligence in WAF rules · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-06-15-threat-intelligence-fields/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Use Cloudforce One threat intelligence in WAF rules · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-06-15-threat-intelligence-fields/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-15-threat-intelligence-fields/#page","headline":"Use Cloudforce One threat intelligence in WAF rules \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-06-15-threat-intelligence-fields/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-06-15-threat-intelligence-fields/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 15, 2026</time><h2 id="post-title">Use Cloudforce One threat intelligence in WAF rules</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>You can now match incoming requests against Cloudforce One threat intelligence in your WAF rules. A new detection looks up the client IP address of each request against the threat intelligence database. If the IP was involved in threat activity in the past seven days, Cloudflare populates <code>cf.intel.ip.*</code> fields that you can use in <a href="/waf/custom-rules/">custom rules</a> and <a href="/waf/rate-limiting-rules/">rate limiting rules</a>.</p>
<p>The detection populates the following fields. Use the <a href="/ruleset-engine/rules-language/functions/#any"><code>any()</code></a> function with the <code>[*]</code> wildcard to match array values:</p>
<ul>
<li><code>cf.intel.ip.datasets</code> — the dataset that flagged the IP address (<code>ddos</code> or <code>waf</code>).</li>
<li><code>cf.intel.ip.target_industries</code> — industries the IP address has targeted.</li>
<li><code>cf.intel.ip.attacker_names</code> — known threat actors associated with the IP address.</li>
<li><code>cf.intel.ip.attacker_countries</code> — source countries of the threat activity.</li>
<li><code>cf.intel.ip.target_countries</code> — countries the IP address has targeted.</li>
</ul>
<p>For example, the following custom rule expression blocks requests from IP addresses associated with DDoS activity that have targeted France:</p>
<pre tabindex="0"><code class="language-txt">any(cf.intel.ip.target_countries[*] == &quot;FR&quot;) and any(cf.intel.ip.datasets[*] == &quot;ddos&quot;)&#10;</code></pre>
<p>These fields work with the Cloudflare API and Terraform. Matches are logged in <a href="/waf/analytics/security-analytics/">Security Analytics</a>.</p>
<p>The threat intelligence detection is available to customers with an active <a href="/security-center/cloudforce-one/">Cloudforce One</a> subscription. For more information, refer to <a href="/waf/detections/threat-intelligence/">Threat intelligence</a>.</p>
</div></article></div>

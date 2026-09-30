---
cp9:
  canonical: https://developers.cloudflare.com/smart-shield/configuration/health-checks/zone-lockdown/
  description: Migrate from Zone Lockdown to WAF custom rules for IP-based access control.
  full_title: Zone lockdown migration guide · Cloudflare Smart Shield docs
  head_html: <title>Zone lockdown migration guide · Cloudflare Smart Shield docs</title><meta name="generator" content="Nift"><meta name="description" content="Migrate from Zone Lockdown to WAF custom rules for IP-based access control."><link rel="canonical" href="https://developers.cloudflare.com/smart-shield/configuration/health-checks/zone-lockdown/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/smart-shield/configuration/health-checks/zone-lockdown/index.md"><meta property="og:title" content="Zone lockdown migration guide · Cloudflare Smart Shield docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Migrate from Zone Lockdown to WAF custom rules for IP-based access control."><meta property="og:url" content="https://developers.cloudflare.com/smart-shield/configuration/health-checks/zone-lockdown/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Smart Shield"><meta name="algolia_product_filter" content="Smart Shield"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Smart Shield"><meta name="pcx_tags" content="Migration"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/smart-shield/configuration/health-checks/zone-lockdown/#page","headline":"Zone lockdown migration guide \u00b7 Cloudflare Smart Shield docs","description":"Migrate from Zone Lockdown to WAF custom rules for IP-based access control.","url":"https://developers.cloudflare.com/smart-shield/configuration/health-checks/zone-lockdown/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Migration"]}</script>
  markdown: true
  noindex: false
  route: /smart-shield/configuration/health-checks/zone-lockdown/
  schema: 1
---
<p>Currently, any Cloudflare customer on a paid plan can configure Health Checks against any host or IP. <a href="/waf/tools/zone-lockdown/">Zone Lockdown</a> specifies a list of one or more IP addresses, CIDR ranges, or networks that are the only IPs allowed to access a domain, subdomain, or URL. It allows multiple destinations in a single rule as well as IPv4 and IPv6 addresses. IP addresses not specified in the Zone Lockdown rule are denied access to the specified resources.</p>
<p>Customers who use zone lockdown and want their health checks to continue passing can use <a href="/waf/custom-rules/create-dashboard/">WAF custom rules</a> to bypass zone lockdown.</p>
<h2 id="bypass-zone-lockdown">Bypass zone lockdown</h2>
<p>To bypass zone lockdown using a WAF custom rule:</p>
<ol>
<li>
<p>Follow the steps to <a href="/waf/custom-rules/create-dashboard/">create a custom rule in the dashboard</a>.</p>
</li>
<li>
<p>Create a custom rule matching on <strong>user agent</strong>.</p>
<p>Cloudflare Health Checks have a user agent of the following format:
<code>Mozilla/5.0 (compatible;Cloudflare-Healthchecks/1.0;+https://www.cloudflare.com/; healthcheck-id: XXX)</code> where <code>XXX</code> is replaced with the first 16 characters of the Health Check ID.</p>
<p>To allow a specific Health Check, verify if the user agent contains the first 16 characters of the Health Check ID.</p>
</li>
<li>
<p>Set the action to <em>Skip</em> and the corresponding feature to <strong>Zone Lockdown</strong> under <strong>More components to skip</strong>.</p>
</li>
</ol>
<h3 id="via-the-api">Via the API</h3>
<p>This example adds a new WAF custom rule to the ruleset with ID <code>{ruleset_id}</code> that skips zone lockdown for incoming requests with a user agent containing <code>1234567890abcdef</code>:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/{zone_id}/rulesets/{ruleset_id}/rules&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;action&quot;: &quot;skip&quot;,&#10;  &quot;action_parameters&quot;: {&#10;    &quot;products&quot;: [&#10;      &quot;zoneLockdown&quot;&#10;    ]&#10;  },&#10;  &quot;expression&quot;: &quot;http.user_agent contains \&quot;1234567890abcdef\&quot;&quot;,&#10;  &quot;description&quot;: &quot;bypass zone lockdown - specific healthcheck&quot;&#10;}&#x27;&#10;</code></pre>

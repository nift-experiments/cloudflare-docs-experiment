---
cp9:
  canonical: https://developers.cloudflare.com/magic-transit/how-to/verify-ddos-protection/
  description: Confirm Magic Transit DDoS protection layers are active and configured.
  full_title: Verify DDoS protection · Cloudflare Magic Transit docs
  head_html: <title>Verify DDoS protection · Cloudflare Magic Transit docs</title><meta name="generator" content="Nift"><meta name="description" content="Confirm Magic Transit DDoS protection layers are active and configured."><link rel="canonical" href="https://developers.cloudflare.com/magic-transit/how-to/verify-ddos-protection/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/magic-transit/how-to/verify-ddos-protection/index.md"><meta property="og:title" content="Verify DDoS protection · Cloudflare Magic Transit docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Confirm Magic Transit DDoS protection layers are active and configured."><meta property="og:url" content="https://developers.cloudflare.com/magic-transit/how-to/verify-ddos-protection/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Magic Transit"><meta name="algolia_product_filter" content="Magic Transit"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Magic Transit"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/magic-transit/how-to/verify-ddos-protection/#page","headline":"Verify DDoS protection \u00b7 Cloudflare Magic Transit docs","description":"Confirm Magic Transit DDoS protection layers are active and configured.","url":"https://developers.cloudflare.com/magic-transit/how-to/verify-ddos-protection/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /magic-transit/how-to/verify-ddos-protection/
  schema: 1
---
<p>After onboarding your IP prefixes to Magic Transit, verify that your DDoS protection layers are active and correctly configured. Magic Transit includes multiple mitigation systems that work together. For a description of each layer and the execution order, refer to <a href="/magic-transit/ddos/">DDoS protection</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you start, make sure you have completed the following:</p>
<ul>
<li><a href="/magic-transit/get-started/">Onboarded your IP prefixes</a> to Magic Transit.</li>
<li><a href="/magic-transit/how-to/advertise-prefixes/">Advertised your prefixes</a> to Cloudflare.</li>
</ul>
<h2 id="verify-ddos-managed-rulesets">Verify DDoS managed rulesets</h2>
<p>The <a href="/ddos-protection/managed-rulesets/network/">network-layer DDoS managed ruleset</a> is always enabled on IP prefixes onboarded to Magic Transit. You cannot turn it off, but you can customize the sensitivity level and action for individual rules.</p>
<p>To review your current configuration:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>L3/4 DDoS protection</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the <strong>Network-layer DDoS Protection</strong> tab.</li>
</ol>
<p>If you have not deployed any overrides, the managed ruleset runs with default settings (High sensitivity, DDoS Dynamic action). This is the recommended configuration for most deployments.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10653.md")
</aside>
<h2 id="verify-advanced-tcp-and-dns-protection">Verify Advanced TCP and DNS Protection</h2>
<p>Advanced TCP Protection and Advanced DNS Protection are automatically enabled in monitoring mode for new Magic Transit customers. In monitoring mode, the systems learn your traffic patterns and show what they would have mitigated without affecting live traffic.</p>
<p>To check the status of Advanced DDoS systems:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>L3/4 DDoS protection</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>Advanced Protection</strong> &gt; <strong>General settings</strong>.</li>
<li>Verify that the system is turned on and that your prefixes are listed.</li>
</ol>
<p>To review individual protection rules:</p>
<ul>
<li>For Advanced TCP Protection, go to <strong>Advanced Protection</strong> &gt; <strong>Advanced TCP Protection</strong>. Check that SYN Flood Protection and Out-of-state TCP Protection rules exist and are set to the expected mode.</li>
<li>For Advanced DNS Protection, go to <strong>Advanced Protection</strong> &gt; <strong>Advanced DNS Protection</strong>. Check that a DNS Protection rule exists.</li>
</ul>
<h3 id="switch-from-monitoring-to-mitigation-mode">Switch from monitoring to mitigation mode</h3>
<p>After your Advanced DDoS systems have collected at least seven days of traffic data, Cloudflare calculates protection thresholds based on the 95th percentile of your traffic over that period. Thresholds are recalculated every 10 minutes.</p>
<p>To switch from monitoring to mitigation:</p>
<ol>
<li>Review your traffic in <a href="/magic-transit/analytics/network-analytics/">Network Analytics</a> to confirm the systems are correctly identifying normal versus anomalous traffic.</li>
<li>Go to the rule you want to update (SYN Flood, Out-of-state TCP, or DNS Protection).</li>
<li>Change the rule mode from <strong>Monitoring</strong> to <strong>Mitigation (Enabled)</strong>.</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10652.md")
</aside>
<h2 id="set-up-alerts">Set up alerts</h2>
<p>Configure DDoS alerts so you are notified when attacks are detected and mitigated:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Notifications</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Add</strong>.</li>
<li>Select <strong>Layer 3/4 DDoS Attack Alert</strong>. Enterprise accounts can select <strong>Advanced Layer 3/4 DDoS Attack Alert</strong> for additional filtering support.</li>
<li>Configure your delivery method (email, webhook, or PagerDuty).</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10651.md")
</aside>
<p>Magic Transit and Spectrum BYOIP customers automatically receive a weekly DDoS summary report by email every Tuesday. The report covers the previous Monday-to-Sunday period and includes total attacks, the largest attack by packets per second and bits per second, and total bytes mitigated.</p>
<h2 id="monitor-with-network-analytics">Monitor with Network Analytics</h2>
<p><a href="/magic-transit/analytics/network-analytics/">Network Analytics</a> is the primary dashboard for monitoring DDoS activity on your Magic Transit prefixes. It shows traffic entering and leaving the Cloudflare network, including traffic blocked by DDoS rules and Network Firewall rules.</p>
<p>To review DDoS activity:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Network analytics</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Filter by mitigations applied to isolate traffic blocked by DDoS managed rulesets or Network Firewall rules.</li>
</ol>
<p>You can also query DDoS analytics programmatically using the <a href="/analytics/graphql-api/">GraphQL Analytics API</a>.</p>
<h2 id="test-your-ddos-protection">Test your DDoS protection</h2>
<p>You can simulate DDoS attacks against your own Magic Transit-protected IP prefixes to verify that detection and mitigation work as expected. You do not need permission from Cloudflare to test against your own properties.</p>
<p>For guidance on testing, refer to <a href="/ddos-protection/reference/simulate-ddos-attack/">Simulate test DDoS attacks</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10650.md")
</aside>

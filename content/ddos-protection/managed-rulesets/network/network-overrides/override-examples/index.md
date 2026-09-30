---
cp9:
  canonical: https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/override-examples/
  description: Example override configurations for Network-layer DDoS Attack Protection rules.
  full_title: Override examples for Network-layer DDoS Attack Protection · Cloudflare DDoS Protection docs
  head_html: <title>Override examples for Network-layer DDoS Attack Protection · Cloudflare DDoS Protection docs</title><meta name="generator" content="Nift"><meta name="description" content="Example override configurations for Network-layer DDoS Attack Protection rules."><link rel="canonical" href="https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/override-examples/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/override-examples/index.md"><meta property="og:title" content="Override examples for Network-layer DDoS Attack Protection · Cloudflare DDoS Protection docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Example override configurations for Network-layer DDoS Attack Protection rules."><meta property="og:url" content="https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/override-examples/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DDoS Protection"><meta name="algolia_product_filter" content="DDoS Protection"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="DDoS Protection"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/override-examples/#page","headline":"Override examples for Network-layer DDoS Attack Protection \u00b7 Cloudflare DDoS Protection docs","description":"Example override configurations for Network-layer DDoS Attack Protection rules.","url":"https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/override-examples/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ddos-protection/managed-rulesets/network/network-overrides/override-examples/
  schema: 1
---
<h2 id="use-cases">Use cases</h2>
<p>The following scenarios detail how you can make use of override rules as a solution to common Network DDoS Protection issues.</p>
<h3 id="vpn-traffic-is-blocked-by-a-udp-rule">VPN traffic is blocked by a UDP rule</h3>
<p>If you have VPN traffic concentrated to a single or a few single destination IP addresses and the traffic is being blocked by a UDP rule, you can create an override rule for the UDP rule to the destination IPs or ranges.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7542.md")
</aside>
<h3 id="attack-traffic-is-flagged-by-the-adaptive-rule-based-on-udp-and-destination-port">Attack traffic is flagged by the adaptive rule based on UDP and destination port</h3>
<p>If you recognize that the traffic flagged by the adaptive rule based on UDP and destination port is an attack, you create an override rule to enable the adaptive rule in mitigation mode, setting the action to block the traffic.</p>
<h3 id="minimize-the-risk-of-false-positives-impacting-production-traffic">Minimize the risk of false positives impacting production traffic</h3>
<p>To avoid disruptions during initial deployment, you can create a <em>Log</em> only – <em>Essentially Off</em> ruleset override that allows all traffic while logging detection results. This lets you safely observe and analyze DDoS activity before enabling enforcement.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Security rules</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Go to the **DDoS protection** tab.
3. On **HTTP DDoS attack protection**, select **Create override**.
4. Set the **Scope** to _Apply to all incoming requests_.
5. Under **Ruleset configuration**:
    - Set the **Ruleset action** to _Log_.
    - Set the **Ruleset sensitivity** to _Essentially Off_. 
6. Select **Save**.

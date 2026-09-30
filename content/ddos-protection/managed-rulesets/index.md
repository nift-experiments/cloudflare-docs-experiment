---
cp9:
  canonical: https://developers.cloudflare.com/ddos-protection/managed-rulesets/
  description: Pre-configured DDoS rulesets that protect against attacks at layers 3, 4, and 7.
  full_title: Managed rulesets · Cloudflare DDoS Protection docs
  head_html: <title>Managed rulesets · Cloudflare DDoS Protection docs</title><meta name="generator" content="Nift"><meta name="description" content="Pre-configured DDoS rulesets that protect against attacks at layers 3, 4, and 7."><link rel="canonical" href="https://developers.cloudflare.com/ddos-protection/managed-rulesets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ddos-protection/managed-rulesets/index.md"><meta property="og:title" content="Managed rulesets · Cloudflare DDoS Protection docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Pre-configured DDoS rulesets that protect against attacks at layers 3, 4, and 7."><meta property="og:url" content="https://developers.cloudflare.com/ddos-protection/managed-rulesets/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DDoS Protection"><meta name="algolia_product_filter" content="DDoS Protection"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="DDoS Protection"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ddos-protection/managed-rulesets/#page","headline":"Managed rulesets \u00b7 Cloudflare DDoS Protection docs","description":"Pre-configured DDoS rulesets that protect against attacks at layers 3, 4, and 7.","url":"https://developers.cloudflare.com/ddos-protection/managed-rulesets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ddos-protection/managed-rulesets/
  schema: 1
---
<p>The DDoS Attack Protection managed rulesets provide comprehensive protection against a <a href="/ddos-protection/about/attack-coverage/">variety of DDoS attacks</a> across L3/4 (network layer) and L7 (application layer) of the <a href="https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/">OSI model</a>.</p>
<p>The available managed rulesets are:</p>
<ul>
<li>
<p><strong><a href="/ddos-protection/managed-rulesets/http/">HTTP DDoS Attack Protection</a></strong></p>
<ul>
<li>This ruleset includes rules to detect and mitigate DDoS attacks over HTTP and HTTPS.</li>
</ul>
</li>
<li>
<p><strong><a href="/ddos-protection/managed-rulesets/network/">Network-layer DDoS Attack Protection</a></strong></p>
<ul>
<li>This ruleset includes rules to detect and mitigate DDoS attacks on L3/4 of the OSI model such as UDP floods, SYN-ACK reflection attacks, SYN Floods, and DNS floods.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="proactive-false-positive-detection-for-new-rules">Proactive false positive detection for new rules</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7459.md")
</aside>
<p>When Cloudflare creates a new managed rule, we check the rule impact against the traffic of Business and Enterprise zones while the rule is not blocking traffic yet.</p>
<p>If a <a href="/ddos-protection/managed-rulesets/http/http-overrides/override-examples/#legitimate-traffic-is-incorrectly-identified-as-an-attack-and-causes-a-false-positive">false positive</a> is detected, we proactively reach out to the affected customers and help them make configuration changes (for example, to lower the sensitivity level of the new rule) before the rule starts mitigating traffic. This prevents the new rule from causing service disruptions and outages to your Internet properties.</p>

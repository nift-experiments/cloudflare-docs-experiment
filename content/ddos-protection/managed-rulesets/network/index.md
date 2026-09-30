---
cp9:
  canonical: https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/
  description: Pre-configured rules that detect and mitigate DDoS attacks at layers 3 and 4.
  full_title: Network-layer DDoS Attack Protection managed ruleset · Cloudflare DDoS Protection docs
  head_html: <title>Network-layer DDoS Attack Protection managed ruleset · Cloudflare DDoS Protection docs</title><meta name="generator" content="Nift"><meta name="description" content="Pre-configured rules that detect and mitigate DDoS attacks at layers 3 and 4."><link rel="canonical" href="https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/index.md"><meta property="og:title" content="Network-layer DDoS Attack Protection managed ruleset · Cloudflare DDoS Protection docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Pre-configured rules that detect and mitigate DDoS attacks at layers 3 and 4."><meta property="og:url" content="https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DDoS Protection"><meta name="algolia_product_filter" content="DDoS Protection"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="DDoS Protection"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/#page","headline":"Network-layer DDoS Attack Protection managed ruleset \u00b7 Cloudflare DDoS Protection docs","description":"Pre-configured rules that detect and mitigate DDoS attacks at layers 3 and 4.","url":"https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ddos-protection/managed-rulesets/network/
  schema: 1
---
<p>The Cloudflare Network-layer <a href="https://www.cloudflare.com/en-gb/learning/ddos/what-is-a-ddos-attack/">DDoS Attack</a> Protection managed ruleset is a set of pre-configured rules used to match <a href="/ddos-protection/about/attack-coverage/">known DDoS attack vectors</a> at levels 3 and 4 of the OSI model.</p>
<p>Cloudflare updates the list of rules in the managed ruleset on a regular basis. Refer to the <a href="/ddos-protection/change-log/network/">changelog</a> for more information on recent and upcoming changes.</p>
<p>The Network-layer DDoS Attack Protection managed ruleset is always enabled — you can only customize its behavior.</p>
<h2 id="ruleset-configuration">Ruleset configuration</h2>
<p>You may need to adjust the behavior of specific rules in case of false positives or due to specific traffic patterns.</p>
<p>Adjust the behavior of the rules in the managed ruleset by modifying the following parameters:</p>
<ul>
<li>The performed <strong>action</strong> when an attack is detected</li>
<li>The <strong>sensitivity level</strong> of attack detection mechanisms</li>
</ul>
<p>To adjust rule behavior, use one of the following methods:</p>
<ul>
<li><a href="/ddos-protection/managed-rulesets/network/network-overrides/configure-dashboard/">Configure the managed ruleset in the Cloudflare dashboard</a>.</li>
<li><a href="/ddos-protection/managed-rulesets/network/network-overrides/configure-api/">Configure the managed ruleset via Cloudflare API</a>.</li>
<li><a href="/terraform/additional-configurations/ddos-managed-rulesets/#example-configure-network-layer-ddos-attack-protection">Configure the managed ruleset using Terraform</a>.</li>
</ul>
<p>You can only configure the behavior of the managed ruleset to set a stronger or weaker mitigation action (depending on the default action of a specific rule, you can change it to <code>Block</code> if the default action is <code>DDoS Dynamic</code> or <code>Log</code>.), or a lower default sensitivity for all rules. Refer to <a href="/ddos-protection/managed-rulesets/network/override-parameters/">Managed ruleset parameters</a> for more information.</p>
<p>Overrides can apply to all <span class="nb-glossary-tooltip" title="data packet">packets</span> or to a subset of incoming packets, depending on the override expression. Refer to <a href="/ddos-protection/managed-rulesets/network/network-overrides/override-expressions/">Override expressions</a> for more information.</p>
<h3 id="network-analytics-rule-display">Network Analytics rule display</h3>
<p>Cloudflare regularly deploys new detection rules to the Network-layer DDoS managed ruleset. To ensure high accuracy and minimize false positives, these rules undergo a testing phase before they are fully promoted.</p>
<p>When a rule is in its testing phase, you may notice specific behaviors in the Cloudflare dashboard.</p>
<p>New rules often default to <code>Log</code> (visible in <strong>DDoS Managed Rules</strong> &gt; <strong>Browse Rules</strong>). This allows Cloudflare to evaluate the rule's performance against real-world traffic without impacting legitimate packets.</p>
<p>In the <a href="/analytics/network-analytics/">Network Analytics</a> dashboard, traffic matched by these testing-phase rules is labeled as <code>Log (rule disabled)</code>. This is a reporting convention indicating the rule is in a pre-production monitoring state.</p>
<p>While you can manually override a rule from <code>Log</code> to <code>Block</code>, consider the following before doing so:</p>
<ul>
<li>
<p>Rules in the testing phase have not yet been fully tuned for broad deployment. Overriding them to a mitigation action (like <code>Block</code>) may increase the risk of dropping legitimate traffic.</p>
</li>
<li>
<p>The default action of a rule is decided during the testing period. Cloudflare may set its default action to <strong>DDoS Dynamic</strong>, which may use rate-limiting or a multi-step mitigation combination based on traffic factors. By applying a manual <code>Block</code> override, you prevent your configuration from automatically inheriting the more nuanced DDoS Dynamic action once it is released.</p>
</li>
</ul>
<p>If you choose to override a testing rule to mitigate an active attack, Cloudflare recommends reviewing that override periodically to see if the rule has been promoted to a permanent default action.</p>
<h2 id="availability">Availability</h2>
<p>The Network-layer DDoS Attack Protection managed ruleset is available in all Cloudflare plans for:</p>
<ul>
<li>Zones <a href="/dns/zone-setups/full-setup/">onboarded to Cloudflare</a> (zones with their traffic routed through the Cloudflare network)</li>
<li>IP applications onboarded to <a href="/spectrum/">Spectrum</a></li>
<li>IP prefixes onboarded to <a href="/magic-transit/">Magic Transit</a></li>
</ul>
<p>However, only Magic Transit and Spectrum customers on an Enterprise plan can customize the managed ruleset.</p>
<h2 id="related-cloudflare-products">Related Cloudflare products</h2>
<p>Magic Transit customers can configure the following additional products:</p>
<ul>
<li>Enable <a href="/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/">Advanced TCP Protection</a> to detect and mitigate sophisticated out-of-state TCP attacks such as randomized and spoofed ACK floods or SYN and SYN-ACK floods.</li>
<li>Create custom <a href="/cloudflare-network-firewall/">Network Firewall</a> rules to block additional network-layer attacks.</li>
</ul>
<p>Spectrum customers can use <a href="/waf/tools/ip-access-rules/">IP Access</a> rules to block additional network-layer attacks.</p>

---
cp9:
  canonical: https://developers.cloudflare.com/ddos-protection/get-started/
  description: Set up and fine-tune DDoS protection for your zones, Spectrum apps, and Magic Transit prefixes.
  full_title: Get started · Cloudflare DDoS Protection docs
  head_html: <title>Get started · Cloudflare DDoS Protection docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up and fine-tune DDoS protection for your zones, Spectrum apps, and Magic Transit prefixes."><link rel="canonical" href="https://developers.cloudflare.com/ddos-protection/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ddos-protection/get-started/index.md"><meta property="og:title" content="Get started · Cloudflare DDoS Protection docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up and fine-tune DDoS protection for your zones, Spectrum apps, and Magic Transit prefixes."><meta property="og:url" content="https://developers.cloudflare.com/ddos-protection/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DDoS Protection"><meta name="algolia_product_filter" content="DDoS Protection"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="DDoS Protection"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ddos-protection/get-started/#page","headline":"Get started \u00b7 Cloudflare DDoS Protection docs","description":"Set up and fine-tune DDoS protection for your zones, Spectrum apps, and Magic Transit prefixes.","url":"https://developers.cloudflare.com/ddos-protection/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ddos-protection/get-started/
  schema: 1
---
<h2 id="free-pro-and-business-plans">Free, Pro, and Business plans</h2>
<p>The DDoS Attack Protection managed rulesets provided by Cloudflare are enabled by default on zones onboarded to Cloudflare, IP applications onboarded to Spectrum, and IP Prefixes onboarded to Magic Transit.</p>
<p>In some situations, the default protection offered by DDoS rules may need to be fine-tuned to your specific situation. You may also want to configure additional protection using other Cloudflare products.</p>
<h3 id="adjust-the-provided-ddos-rules">Adjust the provided DDoS rules</h3>
<p>If one or more DDoS rules provided by Cloudflare affects legitimate traffic, you can adjust them so that they do not perform any mitigation action against this kind of traffic. Follow the steps in <a href="/ddos-protection/managed-rulesets/http/http-overrides/override-examples/#legitimate-traffic-is-incorrectly-identified-as-an-attack-and-causes-a-false-positive">handling a false positive</a> to reduce the sensitivity level of one or more DDoS rules and allow incoming legitimate traffic.</p>
<h3 id="configure-additional-protection">Configure additional protection</h3>
<p>To configure additional protection against DDoS attacks, refer to the related Cloudflare products listed in <a href="/ddos-protection/managed-rulesets/network/#related-cloudflare-products">Network-layer DDoS Attack Protection</a> and <a href="/ddos-protection/managed-rulesets/http/#related-cloudflare-products">HTTP DDoS Attack Protection</a>.</p>
<h2 id="enterprise-plan">Enterprise plan</h2>
<p>Cloudflare's DDoS protection systems automatically detect and mitigate DDoS attacks. Additionally, the systems may flag suspiciously-looking incoming traffic from legacy applications, Internet services, or faulty client applications as malicious and apply mitigation actions. If the traffic is in fact legitimate, the mitigation actions can cause service disruptions and outages in your Internet properties.</p>
<p>To prevent this situation, Cloudflare recommends that you perform these steps to get started:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/1154.md")
</div>
<h3 id="prerequisites">Prerequisites</h3>
<p>You must have one of the following:</p>
<ul>
<li><a href="/dns/zone-setups/full-setup/">A zone onboarded to Cloudflare</a> but without updated DNS records.</li>
<li><a href="/spectrum/get-started/">An IP application onboarded to Spectrum</a>.</li>
<li><a href="/magic-transit/get-started/">An IP Prefix onboarded to Magic Transit</a>.</li>
</ul>
<h3 id="1-configure-ruleset-actions-to-log"><ol>
<li>Configure ruleset actions to Log</li>
</ol></h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1153.md")
</aside>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/1155.md")
</div>
<p>Alternatively, if you are using the API, define an override at the ruleset level to set the action of all managed ruleset rules to <code>log</code> by following these instructions:</p>
<ul>
<li><a href="/ddos-protection/managed-rulesets/http/http-overrides/configure-api/#configure-an-override-for-the-http-ddos-attack-protection-managed-ruleset">Configure an override for the HTTP DDoS Attack Protection managed ruleset</a></li>
<li><a href="/ddos-protection/managed-rulesets/network/network-overrides/configure-api/#configure-an-override-for-the-network-layer-ddos-attack-protection-managed-ruleset">Configure an override for the Network-layer DDoS Attack Protection managed ruleset</a></li>
</ul>
<h3 id="2-review-flagged-traffic"><ol start="2">
<li>Review flagged traffic</li>
</ol></h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/1156.md")
</div>
<h3 id="3-customize-managed-ruleset-rules"><ol start="3">
<li>Customize managed ruleset rules</li>
</ol></h3>
<p>Customize the specific managed ruleset rules you identified, changing their sensitivity or their action, using the Cloudflare dashboard or using the API.</p>
<p>If you are using the Cloudflare dashboard, refer to:</p>
<ul>
<li><a href="/ddos-protection/managed-rulesets/http/http-overrides/configure-dashboard/">Configure HTTP DDoS Attack Protection in the dashboard</a></li>
<li><a href="/ddos-protection/managed-rulesets/network/network-overrides/configure-dashboard/">Configure Network-layer DDoS Attack Protection in the dashboard</a></li>
</ul>
<p>If you are using the API, refer to:</p>
<ul>
<li><a href="/ddos-protection/managed-rulesets/http/http-overrides/configure-api/">Configure HTTP DDoS Attack Protection via API</a></li>
<li><a href="/ddos-protection/managed-rulesets/network/network-overrides/configure-api/">Configure Network-layer DDoS Attack Protection via API</a></li>
</ul>
<p>When using the API, ensure that you add any required rule overrides without removing the ruleset override you configured in <a href="#1-configure-ruleset-actions-to-log">Step 1</a>.</p>
<h3 id="4-switch-ruleset-actions-back-to-the-default"><ol start="4">
<li>Switch ruleset actions back to the default</li>
</ol></h3>
<p>Revert the change you did in <a href="#1-configure-ruleset-actions-to-log">Step 1</a>, changing the action of each managed ruleset rule back to <em>Default</em> in <strong>Ruleset action</strong>.</p>
<p>Alternatively, if you are using the API, <a href="/ddos-protection/managed-rulesets/http/http-overrides/configure-api/#configure-an-override-for-the-http-ddos-attack-protection-managed-ruleset">remove the override</a> you previously configured at the ruleset level for each managed ruleset. Ensure that you only remove the ruleset override and not any of the rule overrides you may have configured in <a href="#3-customize-managed-ruleset-rules">Step 3</a>.</p>

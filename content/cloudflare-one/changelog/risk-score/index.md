---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/changelog/risk-score/
  description: Review recent changes to Cloudflare Zero Trust user risk scoring.
  full_title: Risk score Changelog · Cloudflare One docs
  head_html: <title>Risk score Changelog · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Review recent changes to Cloudflare Zero Trust user risk scoring."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/changelog/risk-score/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/changelog/risk-score/index.md"><link rel="alternate" type="application/rss+xml" href="https://developers.cloudflare.com/cloudflare-one/changelog/risk-score/index.xml"><meta property="og:title" content="Risk score Changelog · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review recent changes to Cloudflare Zero Trust user risk scoring."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/changelog/risk-score/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Changelog"><meta name="algolia_content_type" content="Changelog"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/cloudflare-one/changelog/risk-score/#page","headline":"Risk score Changelog \u00b7 Cloudflare One docs","description":"Review recent changes to Cloudflare Zero Trust user risk scoring.","url":"https://developers.cloudflare.com/cloudflare-one/changelog/risk-score/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/changelog/risk-score/
  schema: 1
---
<h2 id="2026-04-08">2026-04-08</h2>

<strong>User risk scoring for high risk browsing activity</strong>

<p>Cloudflare One's <strong>User Risk Scoring</strong> now incorporates direct signals from <strong>Gateway DNS traffic patterns</strong>. This update allows security teams to automatically elevate a user's risk score when they visit high-risk or malicious domains, providing a more holistic view of internal threats.</p>
<h4 id="2026-04-08-high-risk-browsing-why-this-matters">Why this matters</h4>
<p>Browsing activity is a primary indicator of potential compromise. By tying Gateway DNS logs to specific users, administrators can now flag individuals interacting with:</p>
<ul>
<li><strong>Security threats</strong>: Domains associated with malware, phishing, or command-and-control (C2) centers.</li>
<li><strong>High-risk content</strong>: Categories such as questionable content or violence that may violate corporate compliance.</li>
</ul>
<p>Even if a Gateway policy is set to <strong>Block</strong> the traffic, the interaction is still captured as a &quot;hit&quot; to ensure the user's risk profile reflects the attempted activity.</p>
<h4 id="2026-04-08-high-risk-browsing-new-risk-behaviors">New risk behaviors</h4>
<p>Two new behaviors are now available in the dashboard:</p>
<ul>
<li><strong>Suspicious Security Domain Visited</strong>: Triggers when a user visits a domain in the security threats or security risk categories.</li>
<li><strong>High risk domain visited</strong>: Triggers when a user visits domains categorized as questionable content, violence, or CIPA.</li>
</ul>
<p>To learn more and get started, refer to the <a href="/cloudflare-one/team-and-resources/users/risk-score/">User Risk Scoring documentation</a>.</p>


<h2 id="2026-01-15">2026-01-15</h2>

<strong>Support for CrowdStrike device scores in User Risk Scoring</strong>

<p>Cloudflare One has expanded its [User Risk Scoring] (/cloudflare-one/insights/risk-score/) capabilities by introducing two new behaviors for organizations using the [CrowdStrike integration] (/cloudflare-one/integrations/service-providers/crowdstrike/).</p>
<p>Administrators can now automatically escalate the risk score of a user if their device matches specific CrowdStrike Zero Trust Assessment (ZTA) score ranges. This allows for more granular security policies that respond dynamically to the health of the endpoint.</p>
<p>New risk behaviors
The following risk scoring behaviors are now available:</p>
<ul>
<li>CrowdStrike low device score: Automatically increases a user's risk score when the connected device reports a &quot;Low&quot; score from CrowdStrike.</li>
<li>CrowdStrike medium device score: Automatically increases a user's risk score when the connected device reports a &quot;Medium&quot; score from CrowdStrike.</li>
</ul>
<p>These scores are derived from [CrowdStrike device posture attributes] (/cloudflare-one/integrations/service-providers/crowdstrike/#device-posture-attributes), including OS signals and sensor configurations.</p>


<h2 id="2024-06-17">2024-06-17</h2>

<strong>Exchange user risk scores with Okta</strong>

<p>Beyond the controls in <a href="/cloudflare-one/">Zero Trust</a>, you can now <a href="/cloudflare-one/team-and-resources/users/risk-score/#send-risk-score-to-okta">exchange user risk scores</a> with Okta to inform SSO-level policies.</p>
<p>First, configure Cloudflare One to send user risk scores to Okta.</p>
<ol>
<li>Set up the <a href="/cloudflare-one/integrations/identity-providers/okta/">Okta SSO integration</a>.</li>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</li>
<li>In <strong>Your identity providers</strong>, locate your Okta integration and select <strong>Edit</strong>.</li>
<li>Turn on <strong>Send risk score to Okta</strong>.</li>
<li>Select <strong>Save</strong>.</li>
<li>Upon saving, Cloudflare One will display the well-known URL for your organization. Copy the value.</li>
</ol>
<p>Next, configure Okta to receive your risk scores.</p>
<ol>
<li>On your Okta admin dashboard, go to <strong>Security</strong> &gt; <strong>Device Integrations</strong>.</li>
<li>Go to <strong>Receive shared signals</strong>, then select <strong>Create stream</strong>.</li>
<li>Name your integration. In <strong>Set up integration with</strong>, choose <em>Well-known URL</em>.</li>
<li>In <strong>Well-known URL</strong>, enter the well-known URL value provided by Cloudflare One.</li>
<li>Select <strong>Create</strong>.</li>
</ol>


<h2 id="2024-06-14">2024-06-14</h2>
<p><strong>SentinelOne signal ingestion</strong></p>
<p>You can now configure a <a href="/cloudflare-one/team-and-resources/users/risk-score/#predefined-risk-behaviors">predefined risk behavior</a> to evaluate user risk score using device posture attributes from the <a href="/cloudflare-one/integrations/service-providers/sentinelone/">SentinelOne integration</a>.</p>



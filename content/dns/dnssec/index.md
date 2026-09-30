---
cp9:
  canonical: https://developers.cloudflare.com/dns/dnssec/
  description: Protect your domain from DNS spoofing with DNSSEC.
  full_title: DNSSEC · Cloudflare DNS docs
  head_html: <title>DNSSEC · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Protect your domain from DNS spoofing with DNSSEC."><link rel="canonical" href="https://developers.cloudflare.com/dns/dnssec/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/dnssec/index.md"><meta property="og:title" content="DNSSEC · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Protect your domain from DNS spoofing with DNSSEC."><meta property="og:url" content="https://developers.cloudflare.com/dns/dnssec/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/dnssec/#page","headline":"DNSSEC \u00b7 Cloudflare DNS docs","description":"Protect your domain from DNS spoofing with DNSSEC.","url":"https://developers.cloudflare.com/dns/dnssec/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/dnssec/
  schema: 1
---
<p>DNS Security Extensions (DNSSEC) adds an extra layer of authentication to DNS, ensuring requests are not routed to a spoofed domain.</p>
<p>For additional background on DNSSEC, visit the <a href="https://www.cloudflare.com/learning/dns/dns-security/">Cloudflare Learning Center</a>.</p>
<hr />
<h2 id="disable-dnssec">Disable DNSSEC</h2>
<p>If you are onboarding an existing domain to Cloudflare, make sure DNSSEC <strong>is disabled</strong> at your registrar (where you purchased your domain name). Otherwise, your domain will experience connectivity errors when you change your nameservers.</p>
<details class="nb-details"><summary>Provider-specific DNSSEC instructions</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7690.md")
</div></details>
<details class="nb-details"><summary>Why you have to disable DNSSEC</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7691.md")
</div></details>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7689.md")
</aside>
<hr />
<h2 id="enable-dnssec">Enable DNSSEC</h2>
<p>When you enable DNSSEC, Cloudflare signs your zone, publishes your public signing keys, and generates your <strong>DS</strong> record.</p>
<h3 id="1-activate-dnssec-in-cloudflare"><ol>
<li>Activate DNSSEC in Cloudflare</li>
</ol></h3>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>DNS Settings</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>For <strong>DNSSEC</strong>, click <strong>Enable DNSSEC</strong>.</li>
<li>In the dialog, you have access to several necessary values to help you create a <strong>DS</strong> record at your registrar. Once you close the dialog, you can access this information by clicking <strong>DS record</strong> on the <strong>DNSSEC</strong> card.</li>
</ol>
<h3 id="2-add-ds-record-to-your-registrar"><ol start="2">
<li>Add DS record to your registrar</li>
</ol></h3>
<p>Add the <strong>DS</strong> record to your registrar. If Algorithm 13 - Cloudflare's preferred cipher choice - is not listed by your registrar, it may also be called <em>ECDSA Curve P-256 with SHA-256</em>.</p>
<details class="nb-details"><summary>Provider-specific DNSSEC instructions</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7692.md")
</div></details>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note:</h3>
@markup("md", "content/.markup/bodies/7688.md")
</aside>
<hr />
<h2 id="other-dnssec-setup-options">Other DNSSEC setup options</h2>
<p>If you are using Cloudflare as your Secondary DNS provider and want to configure DNSSEC on your secondary zone(s), you have <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/dnssec-for-secondary/">three options</a> depending on your setup.</p>
<p>If you want to set up DNSSEC on a subdomain zone, refer to <a href="/dns/zone-setups/subdomain-setup/dnssec/">Subdomain DNSSEC</a>.</p>
<hr />
<h2 id="migrate-to-cloudflare-with-dnssec-active">Migrate to Cloudflare with DNSSEC active</h2>
<p>If your current DNS provider supports adding external DNSKEY records, you can use the <a href="/dns/dnssec/dnssec-active-migration/">active migration</a> path for zero-downtime DNSSEC migration using multi-signer DNSSEC.</p>
<p>If your current provider does not support this, use the following approach. This involves a brief window without DNSSEC protection.</p>
<ol>
<li>Remove the DS record at your registrar.</li>
<li>Wait for the DS record TTL to fully expire at the parent zone.
<ul>
<li>Verify with <code>dig DS example.com</code> — commonly 24–48 hours for most TLDs.</li>
</ul>
</li>
<li>Change your nameservers to Cloudflare.</li>
<li>Wait for the previous NS record TTL to expire (typically one hour or less).</li>
<li><a href="#enable-dnssec">Enable DNSSEC in Cloudflare</a> and add the new DS record at your registrar.</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7687.md")
</aside>
<h2 id="roll-back-dnssec">Roll back DNSSEC</h2>
<p>If you need to disable DNSSEC after enabling it:</p>
<ol>
<li>Remove the DS record at your registrar (or disable DNSSEC if using Cloudflare Registrar).</li>
<li>Keep zone signing enabled in Cloudflare until the DS TTL has fully expired at the parent zone.</li>
<li>The rollback window depends on the DS TTL, which varies by TLD.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7686.md")
</aside>
<hr />
<h2 id="limitations">Limitations</h2>
<p>If your registrar does not support DNSSEC with Cloudflare's preferred cipher choice (Algorithm 13), you have several options:</p>
<ul>
<li>Contact your registrar to ask for DNSSEC with modern encryption.</li>
<li>Transfer your domain to a different registrar that supports DNSSEC with Algorithm 13</li>
<li>File a <a href="https://www.icann.org/compliance/complaint">complaint with ICANN</a>, citing your registrar's lack of compliance.</li>
</ul>
<p>If your top-level domain does not support DNSSEC with Algorithm 13 (also known as <em>ECDSA Curve P-256 with SHA-256</em>), <a href="https://www.iana.org/domains/root/db">contact that top-level domain</a>.</p>

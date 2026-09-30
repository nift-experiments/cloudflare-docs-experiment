---
cp9:
  canonical: https://developers.cloudflare.com/email-security/email-configuration/lists/trusted-domains/
  description: Exempt specific domains from Email security proximity and recent domain detections.
  full_title: Trusted domains · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Trusted domains · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Exempt specific domains from Email security proximity and recent domain detections."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/email-configuration/lists/trusted-domains/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/email-configuration/lists/trusted-domains/index.md"><meta property="og:title" content="Trusted domains · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Exempt specific domains from Email security proximity and recent domain detections."><meta property="og:url" content="https://developers.cloudflare.com/email-security/email-configuration/lists/trusted-domains/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/email-configuration/lists/trusted-domains/
  schema: 1
---
<p><strong>Trusted domains</strong> allows you to identify domains that should be exempted from Email security (formerly Area 1) detections.</p>
<h2 id="default-behavior">Default behavior</h2>
<p>When messages come to your recipients from certain domains, Email security triggers certain <a href="/email-security/reference/dispositions-and-attributes/">detections</a> by default:</p>
<ul>
<li><strong>Proximity Domains</strong>: Domains with similar spelling to your existing domain. Will trigger a <code>SPOOF</code> detection.</li>
<li><strong>Recent Domains</strong>: Domains created recently (exact definition set in <a href="/email-security/email-configuration/enhanced-detections/added-detections/">Added Detections</a>). Will trigger a <code>MALICIOUS</code> or <code>SUSPICIOUS</code> detection.</li>
</ul>
<p>However, sometimes those domains are legitimate. For example, your company may have registered several lookalike domains to combat domain squatters.</p>
<p>To exempt specific domains from these detections, you can add trusted domains.</p>
<h2 id="add-a-trusted-domain">Add a trusted domain</h2>
<p>To add a trusted domain:</p>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email security (formerly Area 1) dashboard</a>.</p>
</li>
<li>
<p>Go to <strong>Settings</strong> (the gear icon).</p>
</li>
<li>
<p>On <strong>Email Configuration</strong>, go to <strong>Allow List</strong> &gt; <strong>Trusted Domains</strong>.</p>
</li>
<li>
<p>Select <strong>+ Add Domain</strong>.</p>
</li>
<li>
<p>The exact flow varies based on what you select for your <strong>Pattern Type</strong>:</p>
<ul>
<li><strong>Domain</strong>: Allows you to specify a particular domain and then adjust triggers for <em>Proximity Domain</em> and <em>Recent Domain</em>.</li>
<li><strong>Create Regex</strong>: Allows you to create Regex rules for the domain name, top-level domain (TLDs), and subdomains and then adjust triggers for <em>Proximity Domain</em> and <em>Recent Domain</em>.</li>
</ul>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<h3 id="csv-uploads">CSV uploads</h3>
<p>You can also upload a CSV file of multiple allowed patterns, so long as the file is smaller than 150 KB, starts with a header row of all required values, and contains no additional fields.</p>
<p>An example file would look like this:</p>
<pre tabindex="0"><code class="language-txt">Domain, Notes, Proximity, Recent&#10;mydomain.com, First Person, true, true&#10;testdomain.com, New Hire, false, true&#10;</code></pre>

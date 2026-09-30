---
cp9:
  canonical: https://developers.cloudflare.com/email-security/email-configuration/domains-and-routing/domains/
  description: Create and manage domains in Email security to control email routing and quarantine policies.
  full_title: Domains · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Domains · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Create and manage domains in Email security to control email routing and quarantine policies."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/email-configuration/domains-and-routing/domains/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/email-configuration/domains-and-routing/domains/index.md"><meta property="og:title" content="Domains · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create and manage domains in Email security to control email routing and quarantine policies."><meta property="og:url" content="https://developers.cloudflare.com/email-security/email-configuration/domains-and-routing/domains/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/email-configuration/domains-and-routing/domains/
  schema: 1
---
<p>Email security works through a system of domain-based routing, where Cloudflare receives and evaluates incoming email from a domain.</p>
<h2 id="create-a-domain">Create a domain</h2>
<p>To create a new domain in Email security:</p>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</p>
</li>
<li>
<p>Go to <strong>Settings</strong> (the gear icon).</p>
</li>
<li>
<p>Go to <strong>Email Configuration</strong> &gt; <strong>Domains &amp; Routing</strong> &gt; <strong>Domains</strong>.</p>
</li>
<li>
<p>Select <strong>New Domain</strong>.</p>
</li>
<li>
<p>Enter the following information:</p>
<ul>
<li><strong>Domain</strong>: The domain name receiving email traffic.</li>
<li><strong>Configured As</strong>: Choose <strong>MX Records</strong> or specify a number of <strong>Hops</strong> (depending on your email architecture).</li>
<li><strong>Forwarding To</strong>: Enter the hostname of your email provider.</li>
<li><strong>IP Restrictions</strong> (optional): Restrict incoming traffic to the IP addresses of your mail servers.</li>
<li><strong>Inbound TLS</strong> (only available for non-MX domains): Applies TLS to incoming traffic.</li>
<li><strong>Outbound TLS</strong>: Choose between <strong>Forward all messages over TLS</strong> (recommended) or <strong>Forward all messages using opportunistic TLS</strong>.</li>
<li><strong>Quarantine Policy</strong>: Choose the <span class="nb-glossary-tooltip" title="disposition">dispositions</span> you want to send to <a href="/email-security/email-configuration/admin-quarantine/">Admin quarantine</a>.</li>
</ul>
</li>
<li>
<p>Select <strong>Publish Domain</strong>.</p>
</li>
</ol>
<hr />
<h2 id="edit-a-domain">Edit a domain</h2>
<p>To edit an existing domain:</p>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</li>
<li>Go to <strong>Settings</strong> (the gear icon).</li>
<li>Go to <strong>Email Configuration</strong> &gt; <strong>Domains &amp; Routing</strong> &gt; <strong>Domains</strong>.</li>
<li>On a specific domain, select <strong>...</strong> &gt; <strong>Edit</strong>.</li>
<li>Make changes as needed.</li>
<li>Select <strong>Update Domain</strong>.</li>
</ol>
<hr />
<h2 id="delete-a-domain">Delete a domain</h2>
<p>To delete a domain:</p>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</li>
<li>Go to <strong>Settings</strong> (the gear icon).</li>
<li>Go to <strong>Email Configuration</strong> &gt; <strong>Domains &amp; Routing</strong> &gt; <strong>Domains</strong>.</li>
<li>On a specific domain, select <strong>...</strong> &gt; <strong>Delete</strong>.</li>
</ol>

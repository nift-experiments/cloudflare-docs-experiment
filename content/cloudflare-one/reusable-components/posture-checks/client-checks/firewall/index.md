---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/firewall/
  description: Firewall in Zero Trust.
  full_title: Firewall · Cloudflare One docs
  head_html: <title>Firewall · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Firewall in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/firewall/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/firewall/index.md"><meta property="og:title" content="Firewall · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Firewall in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/firewall/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Posture"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/firewall/#page","headline":"Firewall \u00b7 Cloudflare One docs","description":"Firewall in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/firewall/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Posture"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/reusable-components/posture-checks/client-checks/firewall/
  schema: 1
---
<p>The Firewall device posture attribute ensures that a firewall is running on a device.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li></li>
</ul>
<p>Cloudflare One Client is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">deployed</a> on the device. For a list of supported modes and operating systems, refer to <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/">Cloudflare One Client Checks</a>.</p>
<h2 id="enable-the-firewall-check">Enable the firewall check</h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Reusable components</strong> &gt; <strong>Posture checks</strong>.</li>
<li>Go to <strong>Cloudflare One Client checks</strong> and select <strong>Add a check</strong>.</li>
<li>Select <strong>Firewall</strong>.</li>
<li>Enter a descriptive name for the check.</li>
<li>Select your operating system.</li>
<li>Configure <strong>Enable firewall check</strong> based on your desired security policy:
<ul>
<li><strong>Enabled</strong>: (Recommended) The posture check passes only if the firewall is running.</li>
<li><strong>Disabled</strong>: The posture check passes only if the firewall is turned off.</li>
</ul>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5917.md")
</aside>
7. Select **Save**.
<p>Next, go to <strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>Posture logs</strong> and verify that the firewall check is returning the expected results.</p>
<h2 id="validate-firewall-status">Validate firewall status</h2>
<p>Operating systems determine firewall configuration in various ways. Follow the steps below to understand how the Cloudflare One Client determines if the firewall is enabled.</p>
<h3 id="on-macos">On macOS</h3>
<p>macOS has two firewalls: an application-based firewall and a port-based firewall. The Cloudflare One Client will report a firewall is enabled if either firewall is running.</p>
<h4 id="application-based-firewall">Application-based firewall</h4>
<ol>
<li>Open <strong>System Settings</strong> and go to <strong>Network</strong>.</li>
<li>Verify that <strong>Firewall</strong> is <code>Active</code>.</li>
</ol>
<h4 id="port-based-firewall">Port-based firewall</h4>
<ol>
<li>Open Terminal and run:</li>
</ol>
<pre tabindex="0"><code class="language-sh">sudo /sbin/pfctl -s info&#10;</code></pre>
<ol start="2">
<li>Verify that <strong>Status</strong> is <code>Enabled</code>.</li>
</ol>
<h3 id="on-windows">On Windows</h3>
<ol>
<li>Open PowerShell and run:</li>
</ol>
<pre tabindex="0"><code class="language-powershell">Get-NetFirewallProfile -PolicyStore ActiveStore -Name Public&#10;</code></pre>
<ol start="2">
<li>Verify that <strong>Enabled</strong> is <code>True</code>.</li>
</ol>

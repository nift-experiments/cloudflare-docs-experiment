---
cp9:
  canonical: https://developers.cloudflare.com/tunnel/guides/update-cloudflared/
  description: Update cloudflared to the latest version.
  full_title: Update cloudflared · Cloudflare Docs
  head_html: <title>Update cloudflared · Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="Update cloudflared to the latest version."><link rel="canonical" href="https://developers.cloudflare.com/tunnel/guides/update-cloudflared/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/tunnel/guides/update-cloudflared/index.md"><meta property="og:title" content="Update cloudflared · Cloudflare Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Update cloudflared to the latest version."><meta property="og:url" content="https://developers.cloudflare.com/tunnel/guides/update-cloudflared/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Tunnel"><meta name="algolia_product_filter" content="Cloudflare Tunnel"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Tunnel"><meta name="pcx_tags" content="Docker"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/tunnel/guides/update-cloudflared/#page","headline":"Update cloudflared \u00b7 Cloudflare Docs","description":"Update cloudflared to the latest version.","url":"https://developers.cloudflare.com/tunnel/guides/update-cloudflared/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Docker"]}</script>
  markdown: true
  noindex: false
  route: /tunnel/guides/update-cloudflared/
  schema: 1
---
<p>Updates will cause <code>cloudflared</code> to restart which will impact traffic currently being served. You can perform zero-downtime upgrades by using Cloudflare's <a href="#update-with-cloudflare-load-balancer">Load Balancer product</a> or by using <a href="#update-with-multiple-cloudflared-instances">multiple <code>cloudflared</code> instances</a>.</p>
<h2 id="update-the-cloudflared-service">Update the <code>cloudflared</code> service</h2>
<p>Refer to the following commands to update <code>cloudflared</code> for a <span class="nb-glossary-tooltip" title="remotely-managed tunnel">remotely-managed tunnel</span> or a <span class="nb-glossary-tooltip" title="locally-managed tunnel">locally-managed tunnel</span>. Locally-managed tunnels must be set up to <a href="/tunnel/features/locally-managed-tunnels/as-a-service/">run as a service</a> for the following commands to execute successfully.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14916.md")
</div></div>
<h2 id="update-with-cloudflare-load-balancer">Update with Cloudflare Load Balancer</h2>
<p>You can update <code>cloudflared</code> without downtime by using Cloudflare's Load Balancer product with your Cloudflare Tunnel deployment.</p>
<ol>
<li>Install a new instance of <code>cloudflared</code> and <a href="/tunnel/get-started/">create</a> a new Tunnel.</li>
<li>Configure the instance to point traffic to the same locally-available service as your current, active instance of <code>cloudflared</code>.</li>
<li><a href="/tunnel/concepts/routing/#add-a-tunnel-to-a-load-balancer-pool">Add the address</a> of the new instance of <code>cloudflared</code> into your Load Balancer pool as priority 2.</li>
<li>Swap the priority such that the new instance is now priority 1 and monitor to confirm traffic is being served.</li>
<li>Once confirmed, you can remove the older version from the Load Balancer pool.</li>
</ol>
<h2 id="update-with-multiple-cloudflared-instances">Update with multiple <code>cloudflared</code> instances</h2>
<p>If you are not using Cloudflare's Load Balancer, you can use multiple instances of <code>cloudflared</code> to update without the risk of downtime.</p>
<ol>
<li>Install a new instance of <code>cloudflared</code> and <a href="/tunnel/get-started/">create</a> a new Tunnel.</li>
<li>Configure the instance to point traffic to the same locally-available service as your current, active instance of <code>cloudflared</code>.</li>
<li>In the Cloudflare DNS dashboard, <a href="/tunnel/concepts/routing/#dns-records">replace</a> the address of the current instance of <code>cloudflared</code> with the address of the new instance. Save the record.</li>
<li>Remove the now-inactive instance of <code>cloudflared</code>.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="traffic-handling">Traffic handling</h3>
@markup("md", "content/.markup/bodies/14906.md")
</aside>
<h3 id="run-multiple-instances-in-windows">Run multiple instances in Windows</h3>
<p>Windows systems require services to have a unique name and display name. You can run multiple instances of <code>cloudflared</code> by creating <code>cloudflared</code> services with unique names.</p>
<ol>
<li>Install and configure <code>cloudflared</code>.</li>
<li>Next, create a service with a unique name and point to the <code>cloudflared</code> executable and configuration file.</li>
</ol>
<pre tabindex="0"><code class="language-powershell">sc.exe create &lt;unique-name&gt; binPath=&#x27;&lt;path-to-exe&gt;&#x27; --config &#x27;&lt;path-to-config&gt;&#x27; displayname=&quot;Unique Name&quot;&#10;</code></pre>
<ol start="3">
<li>
<p>Proceed to create additional services with unique names.</p>
</li>
<li>
<p>You can now start each unique service.</p>
</li>
</ol>
<pre tabindex="0"><code class="language-powershell">sc.exe start &lt;unique-name&gt;&#10;</code></pre>

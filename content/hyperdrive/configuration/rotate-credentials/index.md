---
cp9:
  canonical: https://developers.cloudflare.com/hyperdrive/configuration/rotate-credentials/
  description: Update or rotate database credentials for an existing Hyperdrive configuration.
  full_title: Rotating database credentials · Cloudflare Hyperdrive docs
  head_html: <title>Rotating database credentials · Cloudflare Hyperdrive docs</title><meta name="generator" content="Nift"><meta name="description" content="Update or rotate database credentials for an existing Hyperdrive configuration."><link rel="canonical" href="https://developers.cloudflare.com/hyperdrive/configuration/rotate-credentials/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/hyperdrive/configuration/rotate-credentials/index.md"><meta property="og:title" content="Rotating database credentials · Cloudflare Hyperdrive docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Update or rotate database credentials for an existing Hyperdrive configuration."><meta property="og:url" content="https://developers.cloudflare.com/hyperdrive/configuration/rotate-credentials/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Hyperdrive"><meta name="algolia_product_filter" content="Hyperdrive"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Hyperdrive"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/hyperdrive/configuration/rotate-credentials/#page","headline":"Rotating database credentials \u00b7 Cloudflare Hyperdrive docs","description":"Update or rotate database credentials for an existing Hyperdrive configuration.","url":"https://developers.cloudflare.com/hyperdrive/configuration/rotate-credentials/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /hyperdrive/configuration/rotate-credentials/
  schema: 1
---
<p>You can change the connection information and credentials of your Hyperdrive configuration in one of two ways:</p>
<ol>
<li>Create a new Hyperdrive configuration with the new connection information, and update your Worker to use the new Hyperdrive configuration.</li>
<li>Update the existing Hyperdrive configuration with the new connection information and credentials.</li>
</ol>
<h2 id="use-a-new-hyperdrive-configuration">Use a new Hyperdrive configuration</h2>
<p>Creating a new Hyperdrive configuration to update your database credentials allows you to keep your existing Hyperdrive configuration unchanged, gradually migrate your Worker to the new Hyperdrive configuration, and easily roll back to the previous configuration if needed.</p>
<p>To create a Hyperdrive configuration that connects to an existing PostgreSQL or MySQL database, use the <a href="/workers/wrangler/install-and-update/">Wrangler</a> CLI or the <a href="https://dash.cloudflare.com/?to=/:account/workers/hyperdrive">Cloudflare dashboard</a>.</p>
<pre tabindex="0"><code class="language-sh">&#35; wrangler v3.11 and above required&#10;npx wrangler hyperdrive create my-updated-hyperdrive --connection-string=&quot;&lt;YOUR_CONNECTION_STRING&gt;&quot;&#10;</code></pre>
<p>The command above will output the ID of your Hyperdrive. Set this ID in the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> for your Workers project:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9045.md")
</div>
<p>To update your Worker to use the new Hyperdrive configuration, redeploy your Worker or use <a href="/workers/versions-and-deployments/gradual-deployments/">gradual deployments</a>.</p>
<h2 id="update-the-existing-hyperdrive-configuration">Update the existing Hyperdrive configuration</h2>
<p>You can update the configuration of an existing Hyperdrive configuration using the <a href="/workers/wrangler/install-and-update/">wrangler CLI</a>.</p>
<pre tabindex="0"><code class="language-sh">&#35; wrangler v3.11 and above required&#10;npx wrangler hyperdrive update &lt;HYPERDRIVE_CONFIG_ID&gt; --origin-host &lt;YOUR_ORIGIN_HOST&gt; --origin-password &lt;YOUR_ORIGIN_PASSWORD&gt; --origin-user &lt;YOUR_ORIGIN_USERNAME&gt; --database &lt;YOUR_DATABASE&gt; --origin-port &lt;YOUR_ORIGIN_PORT&gt;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9044.md")
</aside>

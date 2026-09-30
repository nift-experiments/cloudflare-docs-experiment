---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/tutorials/access-workers/
  description: This tutorial covers how to use a Cloudflare Worker to add custom headers to traffic. The headers will be sent to origin services protected by Cloudflare Access.
  full_title: Create custom headers for Cloudflare Access-protected origins with Workers · Cloudflare One docs
  head_html: <title>Create custom headers for Cloudflare Access-protected origins with Workers · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="This tutorial covers how to use a Cloudflare Worker to add custom headers to traffic. The headers will be sent to origin services protected by Cloudflare Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/tutorials/access-workers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/tutorials/access-workers/index.md"><meta property="og:title" content="Create custom headers for Cloudflare Access-protected origins with Workers · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This tutorial covers how to use a Cloudflare Worker to add custom headers to traffic. The headers will be sent to origin services protected by Cloudflare Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/tutorials/access-workers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Workers,Access"><meta name="pcx_tags" content="JavaScript"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/tutorials/access-workers/#page","headline":"Create custom headers for Cloudflare Access-protected origins with Workers \u00b7 Cloudflare One docs","description":"This tutorial covers how to use a Cloudflare Worker to add custom headers to traffic. The headers will be sent to origin services protected by Cloudflare Access.","url":"https://developers.cloudflare.com/cloudflare-one/tutorials/access-workers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["JavaScript"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/tutorials/access-workers/
  schema: 1
---
<p>This tutorial covers how to use a <a href="/workers/">Cloudflare Worker</a> to add custom HTTP headers to traffic, and how to send those custom headers to your origin services protected by <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a>.</p>
<p>Some applications and networking implementations require specific custom headers to be passed to the origin, which can be difficult to implement for traffic moving through a Zero Trust proxy. You can configure a Worker to send the <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/">user authorization headers</a> required by Access.</p>
<hr />
<h2 id="before-you-begin">Before you begin</h2>
<ul>
<li>Secure your origin server with Cloudflare Access</li>
</ul>
<h2 id="before-you-begin-1">Before you begin</h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>If this is your first Worker, select <strong>Create Worker</strong>. Otherwise, select <strong>Create application</strong>, then select <strong>Create Worker</strong>.</p>
</li>
<li>
<p>Enter an identifiable name for the Worker, then select <strong>Deploy</strong>.</p>
</li>
<li>
<p>Select <strong>Edit code</strong>.</p>
</li>
<li>
<p>Input the following Worker:</p>
</li>
</ol>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/4332.md")
</div>
<ol start="6">
<li>Select <strong>Save and deploy</strong>.</li>
</ol>
<p>Your Worker is now ready to send custom headers to your Access-protected origin services.</p>
<h2 id="apply-the-worker-to-your-hostname">Apply the Worker to your hostname</h2>
<ol>
<li>Select the Worker you created, then go to <strong>Triggers</strong>.</li>
<li>In <strong>Routes</strong>, select <strong>Add route</strong>.</li>
<li>Enter the hostname and zone for your origin, then select <strong>Add route</strong>.</li>
</ol>
<p>The Worker will now insert a custom header into requests that match the defined route. For example:</p>
<pre tabindex="0"><code class="language-http">&quot;Accept&quot;: &quot;text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7&quot;,&#10;    &quot;Accept-Encoding&quot;: &quot;gzip&quot;,&#10;    &quot;Accept-Language&quot;: &quot;en-US,en;q=0.9&quot;,&#10;    &quot;Cf-Access-Authenticated-User-Email&quot;: &quot;user@example.com&quot;,&#10;    &quot;Company-User-Id&quot;: &quot;user@example.com&quot;,&#10;    &quot;Connection&quot;: &quot;keep-alive&quot;&#10;</code></pre>

---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/worker-as-origin/
  description: Learn how to use a Worker as the fallback origin for your SaaS zone.
  full_title: Workers as your fallback origin · Cloudflare for Platforms docs
  head_html: <title>Workers as your fallback origin · Cloudflare for Platforms docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to use a Worker as the fallback origin for your SaaS zone."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/worker-as-origin/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/worker-as-origin/index.md"><meta property="og:title" content="Workers as your fallback origin · Cloudflare for Platforms docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to use a Worker as the fallback origin for your SaaS zone."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/worker-as-origin/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare for Platforms"><meta name="algolia_product_filter" content="Cloudflare for Platforms"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare for SaaS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/worker-as-origin/#page","headline":"Workers as your fallback origin \u00b7 Cloudflare for Platforms docs","description":"Learn how to use a Worker as the fallback origin for your SaaS zone.","url":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/worker-as-origin/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/worker-as-origin/
  schema: 1
---
<p>If you are building your application on <a href="/workers/">Cloudflare Workers</a>, you can use a Worker as the origin for your SaaS zone (also known as your fallback origin).</p>
<h2 id="how-custom-hostname-traffic-reaches-your-worker">How custom hostname traffic reaches your Worker</h2>
<p>When customers point their domains to your SaaS zone (for example, <code>mystore.customer.com</code> CNAMEs to <code>service.saasprovider.com</code>), their traffic enters your Cloudflare zone. Any Worker routes configured on your zone will match this incoming traffic.</p>
<p>For example, if you have:</p>
<ul>
<li>Your SaaS zone: <code>saasprovider.com</code></li>
<li>Your fallback origin: <code>service.saasprovider.com</code></li>
<li>Customer's custom hostname: <code>mystore.customer.com</code> (pointed to your zone via CNAME)</li>
<li>Worker route: <code>*/*</code></li>
</ul>
<p>When a visitor requests <code>mystore.customer.com</code>, Cloudflare routes that request through your zone. The <code>*/*</code> route pattern matches all traffic entering your zone, including traffic from custom hostnames like <code>mystore.customer.com</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4164.md")
</aside>
<h2 id="set-up-a-worker-as-your-fallback-origin">Set up a Worker as your fallback origin</h2>
<ol>
<li>
<p>In your SaaS zone, <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/#1-create-fallback-origin">create and set a fallback origin</a>. Ensure the fallback origin only has an <a href="/dns/manage-dns-records/how-to/create-dns-records/#originless-setups">originless DNS record</a>:</p>
<ul>
<li><strong>Example</strong>: <code>service.example.com AAAA 100::</code></li>
</ul>
</li>
<li>
<p>In that same zone, navigate to <strong>Workers Routes</strong>.</p>
</li>
<li>
<p>Click <strong>Add route</strong>.</p>
</li>
<li>
<p>Configure a route to send traffic to your Worker. Choose one of the following options based on your needs:</p>
<ul>
<li>
<p><strong>Route all traffic to the Worker</strong> (recommended for most SaaS applications):</p>
<ul>
<li><strong>Route</strong>: <code>*/*</code></li>
<li><strong>Worker</strong>: Select the Worker used for your SaaS application.</li>
</ul>
<p>This pattern routes all traffic entering your zone to the Worker, including requests from custom hostnames (for example, <code>mystore.customer.com</code>) and requests to your own subdomains (for example, <code>app.saasprovider.com</code>).</p>
</li>
<li>
<p><strong>Route all but specific routes to worker</strong>:</p>
<ul>
<li><strong>Route</strong>: <code>*/*</code></li>
<li><strong>Worker</strong>: Select the Worker used for your SaaS application.</li>
<li>Add a second route for your zone's own hostnames with <strong>Worker</strong> set to <strong>None</strong> to exclude them.</li>
</ul>
<p>For example, if your zone is <code>saasprovider.com</code> and you want <code>api.saasprovider.com</code> to bypass the Worker, create an additional route <code>api.saasprovider.com/*</code> with no Worker assigned. More specific routes take precedence over wildcard routes.</p>
</li>
<li>
<p><strong>Route only custom hostname traffic to the Worker</strong>:</p>
</li>
<li>
<p><strong>Route</strong>: <code>vanity.customer.com</code></p>
</li>
<li>
<p><strong>Worker</strong>: Select the Worker used for your SaaS application.</p>
</li>
</ul>
</li>
<li>
<p>Click <strong>Save</strong>.</p>
</li>
</ol>
<hr />
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="zone-name-restriction">Zone name restriction</h3>
@markup("md", "content/.markup/bodies/4163.md")
</aside>
<h2 id="interaction-with-custom-origin-server">Interaction with custom origin server</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4162.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/cloudflare-for-platforms/workers-for-platforms/configuration/hostname-routing/">Hostname routing</a> - Learn about advanced routing patterns, including dispatch Workers and O2O behavior.</li>
<li><a href="/workers/configuration/routing/routes/">Workers routes</a> - Learn more about route pattern matching and validity rules.</li>
</ul>

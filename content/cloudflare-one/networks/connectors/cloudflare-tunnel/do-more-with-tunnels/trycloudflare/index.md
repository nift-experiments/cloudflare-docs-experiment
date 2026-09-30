---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/trycloudflare/
  description: How Quick Tunnels works in Zero Trust networking.
  full_title: Quick Tunnels · Cloudflare One docs
  head_html: <title>Quick Tunnels · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="How Quick Tunnels works in Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/trycloudflare/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/trycloudflare/index.md"><meta property="og:title" content="Quick Tunnels · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How Quick Tunnels works in Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/trycloudflare/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/trycloudflare/#page","headline":"Quick Tunnels \u00b7 Cloudflare One docs","description":"How Quick Tunnels works in Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/trycloudflare/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/trycloudflare/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5317.md")
</aside>
<p>Developers can use the TryCloudflare tool to experiment with Cloudflare Tunnel without adding a site to Cloudflare's DNS. TryCloudflare will launch a process that generates a random subdomain on <code>trycloudflare.com</code>. Requests to that subdomain will be proxied through the Cloudflare network to your web server running on localhost.</p>
<h2 id="use-trycloudflare">Use TryCloudflare</h2>
<ol>
<li>Follow <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/">these instructions</a> to install <code>cloudflared</code>. If you have an older copy, update to 2020.5.1 or later.</li>
<li>Launch a web server that is available over localhost to <code>cloudflared</code>.</li>
<li>Run the following terminal command to start a free tunnel.</li>
</ol>
<pre tabindex="0"><code class="language-sh">cloudflared tunnel --url http://localhost:8080&#10;</code></pre>
<p><code>cloudflared</code> will generate a random subdomain when connecting to the Cloudflare network and print it in the terminal for you to use and share. The output will serve traffic from the server on your local machine to the public Internet at a public URL.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5316.md")
</aside>
<h2 id="faq">FAQ</h2>
<h3 id="what-are-some-example-use-cases-for-trycloudflare">What are some example use cases for TryCloudflare?</h3>
<ul>
<li>Create a web server for a project on your laptop that you want to share with others on different networks</li>
<li>Test browser compatibility for a new site by creating a free Tunnel and testing the link in different browsers</li>
<li>Run speed tests from different regions by using a tool like Pingdom or WebPageTest to connect to the randomly-generated subdomain created by TryCloudflare</li>
</ul>
<h3 id="why-does-cloudflare-provide-this-service-for-free">Why does Cloudflare provide this service for free?</h3>
<ul>
<li>We want more users to experience the speed and security improvements of Cloudflare Tunnel. We hope you test it with TryCloudflare and decide to add it to your production sites.</li>
<li>Cloudflare's features historically require you to own a domain, set that domain's DNS to Cloudflare's nameservers, and configure its DNS records before you can begin to use any services. We hope to make more and more of our products available to trial without that burden.</li>
<li>We don't guarantee any SLA or uptime of TryCloudflare - we plan to test new Cloudflare Tunnel features and improvements on these free tunnels. This provides us with a group of connections to test before we deploy to production customers. Free tunnels are meant to be used for testing and development, not for deploying a production website.</li>
</ul>
<h3 id="limitations">Limitations</h3>
<ul>
<li>Quick Tunnels are subject to a hard limit on the number of concurrent requests that can be proxied at any point in time. Currently, this limit is 200 in-flight requests. If a Quick Tunnel hits this limit, the HTTP response will return a <code>429</code> status code.</li>
<li>Quick Tunnels do not support Server-Sent Events (SSE).</li>
</ul>
<p>These limitations only apply to Quick Tunnels. To avoid these limitations, <a href="https://dash.cloudflare.com/sign-up">sign up</a> for a Cloudflare account and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/">create a Cloudflare Tunnel</a>.</p>
<h3 id="legal">Legal</h3>
<p>Your installation of cloudflared software constitutes a symbol of your signature indicating that you accept the terms of the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/license/">Cloudflare License</a>, <a href="https://www.cloudflare.com/terms/">Terms</a> and <a href="https://www.cloudflare.com/privacypolicy/">Privacy Policy</a>.</p>

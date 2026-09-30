---
cp9:
  canonical: https://developers.cloudflare.com/tunnel/
  description: Securely connect your origin servers, APIs, and services to Cloudflare with post-quantum encrypted tunnels — no public IPs required.
  full_title: Cloudflare Tunnel · Cloudflare Docs
  head_html: <title>Cloudflare Tunnel · Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="Securely connect your origin servers, APIs, and services to Cloudflare with post-quantum encrypted tunnels — no public IPs required."><link rel="canonical" href="https://developers.cloudflare.com/tunnel/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/tunnel/index.md"><meta property="og:title" content="Cloudflare Tunnel · Cloudflare Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Securely connect your origin servers, APIs, and services to Cloudflare with post-quantum encrypted tunnels — no public IPs required."><meta property="og:url" content="https://developers.cloudflare.com/tunnel/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Tunnel"><meta name="algolia_product_filter" content="Cloudflare Tunnel"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Cloudflare Tunnel"><meta name="pcx_tags" content="Post-quantum"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/tunnel/#page","headline":"Cloudflare Tunnel \u00b7 Cloudflare Docs","description":"Securely connect your origin servers, APIs, and services to Cloudflare with post-quantum encrypted tunnels \u2014 no public IPs required.","url":"https://developers.cloudflare.com/tunnel/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Post-quantum"]}</script>
  markdown: true
  noindex: false
  route: /tunnel/
  schema: 1
---
<div class="nb-description">
@markup("md", "content/.markup/bodies/249.md")
</div>
<div class="nb-plan">
<p>Available on all plans</p>
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="looking-for-private-networking-or-zero-trust">Looking for private networking or Zero Trust?</h3>
@markup("md", "content/.markup/bodies/248.md")
</aside>
<p>Cloudflare Tunnel connects your infrastructure to Cloudflare through an outbound-only, <a href="/ssl/post-quantum-cryptography/">post-quantum encrypted</a> connection. Instead of exposing a public IP, you install a lightweight daemon called <code>cloudflared</code> on your server. It creates a persistent tunnel to Cloudflare's global network, so all traffic to your origins flows through Cloudflare — where CDN caching, WAF, Bot Management, and DDoS protection are applied automatically.</p>
<p>No open inbound ports. No public IPs. No attack surface.</p>
<div class="video-frame"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/4fa0fe257187f18929c07754a4a4df09/iframe?preload=true&amp;letterboxColor=transparent&amp;poster=https%3A%2F%2Fimagedelivery.net%2FxDOJvHcv1KwTQn6S-BGFIw%2Fecc233ab-9a33-46e3-b339-b2d592fc0d00%2Fpublic" title="What is Cloudflare Tunnel?" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<h2 id="how-it-works">How it works</h2>
<ol>
<li>Install <code>cloudflared</code> on your server or network.</li>
<li><code>cloudflared</code> establishes outbound, post-quantum encrypted connections to Cloudflare — no inbound ports or firewall changes required.</li>
<li>Map public hostnames to local services (for example, <code>app.example.com</code> to <code>http://localhost:8080</code>).</li>
<li>Traffic flows through Cloudflare's network to your origin, with full CDN and security applied.</li>
</ol>
<p>Each tunnel maintains four long-lived connections to two Cloudflare data centers for built-in redundancy. You can run multiple <code>cloudflared</code> <a href="/tunnel/configuration/#replicas-and-high-availability">replicas</a> for additional high availability.</p>
<p><img src="/assets/upstream/images/cloudflare-one/connections/connect-apps/handshake.jpg" alt="How an HTTP request reaches an origin connected with Cloudflare Tunnel" /></p>
<h2 id="use-cases">Use cases</h2>
<ul>
<li><strong>Secure origin connectivity</strong> — Eliminate public origin IPs. All traffic flows through Cloudflare with CDN, WAF, and DDoS protection applied.</li>
<li><strong>Public ingress routing</strong> — Publish internal applications to the internet by mapping public hostnames to local services. Supports HTTP, HTTPS, TCP, SSH, RDP, and <a href="/tunnel/concepts/routing/#supported-protocols">more</a>.</li>
<li><strong>Workers VPC</strong> — Enable <a href="/workers-vpc/">Cloudflare Workers</a> to securely access private databases, APIs, and services through your tunnel.</li>
<li><strong>Load Balancing</strong> — Use tunnels as origin endpoints in <a href="/load-balancing/">Cloudflare Load Balancer</a> pools for high availability and intelligent traffic steering.</li>
</ul>
<h2 id="get-started">Get started</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/254.md")
</div>

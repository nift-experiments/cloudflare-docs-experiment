---
cp9:
  canonical: https://developers.cloudflare.com/web3/get-started/
  description: Set up a Cloudflare Web3 gateway for Ethereum or IPFS.
  full_title: Get started · Cloudflare Web3 docs
  head_html: <title>Get started · Cloudflare Web3 docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up a Cloudflare Web3 gateway for Ethereum or IPFS."><link rel="canonical" href="https://developers.cloudflare.com/web3/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/web3/get-started/index.md"><meta property="og:title" content="Get started · Cloudflare Web3 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up a Cloudflare Web3 gateway for Ethereum or IPFS."><meta property="og:url" content="https://developers.cloudflare.com/web3/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Web3"><meta name="algolia_product_filter" content="Web3"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Web3"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/web3/get-started/#page","headline":"Get started \u00b7 Cloudflare Web3 docs","description":"Set up a Cloudflare Web3 gateway for Ethereum or IPFS.","url":"https://developers.cloudflare.com/web3/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /web3/get-started/
  schema: 1
---
<p>Use this tutorial to set up a Cloudflare Web3 gateway, which gives your application HTTP access to the IPFS or Ethereum network without running your own node.</p>
<h2 id="before-you-begin">Before you begin</h2>
<p>Before you start, make sure you have <a href="/fundamentals/account/">set up an account</a> and <a href="/fundamentals/manage-domains/add-site/">added your website</a> to Cloudflare.</p>
<h2 id="step-1-subscribe-to-a-gateway">Step 1 - Subscribe to a gateway</h2>
<p>Web3 gateways are a paid add-on. To get access, <a href="/web3/how-to/enable-gateways/">subscribe to a gateway</a>.</p>
<h2 id="step-2-create-a-gateway">Step 2 - Create a gateway</h2>
<p>After purchasing a gateway subscription, create a gateway.</p>
<details class="nb-details"><summary>Create via dashboard</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/89.md")
</div></details>
<details class="nb-details"><summary>Create via API</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/90.md")
</div></details>
<p>When you create a gateway, Cloudflare automatically:</p>
<ul>
<li>Creates and adds <a href="/web3/reference/gateway-dns-records/">records to your Cloudflare DNS</a> so your gateway can receive and route traffic appropriately.</li>
<li><a href="/dns/proxy-status/">Proxies</a> traffic to that hostname.</li>
<li>Issues an SSL/TLS certificate to cover the specified hostname.</li>
</ul>
<h2 id="step-3-customize-cloudflare-settings">Step 3 - Customize Cloudflare settings</h2>
<p>Once your gateway becomes <a href="/web3/reference/gateway-status/">active</a>, you can customize the Cloudflare settings associated with your hostname.</p>
<p>Since your traffic is automatically proxied through Cloudflare, you customize your website settings to take advantage of various <a href="/fundamentals/concepts/how-cloudflare-works/#cloudflare-as-a-reverse-proxy">security, performance, and reliability</a> benefits.</p>
<h2 id="step-4-restrict-gateway-access-optional">Step 4 - Restrict gateway access (optional)</h2>
<p>If you are using your gateway for backend services, you may want to use Cloudflare Zero Trust to <a href="/web3/how-to/restrict-gateway-access/">restrict gateway access</a>.</p>
<h2 id="step-5-set-up-usage-notifications">Step 5 - Set up usage notifications</h2>
<p>Since this is a service with <a href="/billing/understand/usage-based-billing/">usage-based billing</a>, Cloudflare recommends that you set up usage-based billing notifications to avoid unexpected bills.</p>
<p>To set up those notifications:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Notifications</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>On <strong>Alert Type</strong> of <strong>Usage Based Billing</strong>, click <strong>Select</strong>.</p>
</li>
<li>
<p>Fill out the following information:</p>
<ul>
<li><strong>Name</strong></li>
<li><strong>Product</strong></li>
<li><strong>Notification limit</strong> (exact metric will vary based on product)</li>
<li><strong>Notification email</strong></li>
</ul>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/88.md")
</aside>
<ol start="4">
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="step-6-use-the-gateway">Step 6 - Use the gateway</h2>
<p>Once you have created a gateway and updated your Cloudflare settings, you can start using your <a href="/web3/how-to/use-ipfs-gateway/">IPFS</a> or <a href="/web3/how-to/use-ethereum-gateway/">Ethereum</a>.</p>

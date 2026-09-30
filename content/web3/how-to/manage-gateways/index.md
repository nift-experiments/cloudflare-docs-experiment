---
cp9:
  canonical: https://developers.cloudflare.com/web3/how-to/manage-gateways/
  description: Create, edit, and delete Web3 gateways.
  full_title: Manage gateways · Cloudflare Web3 docs
  head_html: <title>Manage gateways · Cloudflare Web3 docs</title><meta name="generator" content="Nift"><meta name="description" content="Create, edit, and delete Web3 gateways."><link rel="canonical" href="https://developers.cloudflare.com/web3/how-to/manage-gateways/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/web3/how-to/manage-gateways/index.md"><meta property="og:title" content="Manage gateways · Cloudflare Web3 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create, edit, and delete Web3 gateways."><meta property="og:url" content="https://developers.cloudflare.com/web3/how-to/manage-gateways/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Web3"><meta name="algolia_product_filter" content="Web3"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Web3"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/web3/how-to/manage-gateways/#page","headline":"Manage gateways \u00b7 Cloudflare Web3 docs","description":"Create, edit, and delete Web3 gateways.","url":"https://developers.cloudflare.com/web3/how-to/manage-gateways/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /web3/how-to/manage-gateways/
  schema: 1
---
<p>A Cloudflare Web3 gateway provides HTTP-accessible interfaces to various Web3 networks. You can interact with a gateway in several ways.</p>
<h2 id="create-a-gateway">Create a gateway</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15784.md")
</div></div>
<p>When you create a gateway, Cloudflare automatically:</p>
<ul>
<li>Creates and adds <a href="/web3/reference/gateway-dns-records/">records to your Cloudflare DNS</a> so your gateway can receive and route traffic appropriately.</li>
<li><a href="/dns/proxy-status/">Proxies</a> traffic to that hostname.</li>
<li>Issues an SSL/TLS certificate to cover the specified hostname.</li>
</ul>
<hr />
<h2 id="edit-a-gateway">Edit a gateway</h2>
<p>Once you have <a href="#create-a-gateway">created a gateway</a>, you can only edit the <strong>Gateway Description</strong> and — if it is an <strong>IPFS</strong> gateway — also edit the value for the <a href="/web3/ipfs-gateway/concepts/dnslink/">DNSLink</a> field.</p>
<p>If you need to edit other fields, <a href="#delete-a-gateway">delete the gateway</a> and create a new one.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15787.md")
</div></div>
<hr />
<h2 id="refresh-a-gateway">Refresh a gateway</h2>
<p>When your gateway is stuck in an <strong>Error</strong> <a href="/web3/reference/gateway-status/">status</a>, you should try refreshing the gateway, which attempts to re-create the associated DNS records for the hostname.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15790.md")
</div></div>
<hr />
<h2 id="update-blocklist">Update blocklist</h2>
<p>When you set up a <a href="/web3/ipfs-gateway/concepts/universal-gateway/">IPFS Universal Path gateway</a>, you may want to add items to the gateway blocklist, which allows you to block access to specific content.</p>
<p>You have the ability to block access to one or more:</p>
<ul>
<li>CIDs (<code>QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB</code>)</li>
<li>IPFS content paths (<code>/ipfs/QmYwAPJzv5CZsnA625s3Xf2nemtYgPpHdWEz79ojWnPbdG/readme</code>)</li>
<li>IPNS content paths (<code>/ipns/example.com</code>)</li>
</ul>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15793.md")
</div></div>
<hr />
<h2 id="delete-a-gateway">Delete a gateway</h2>
<p>When you delete a gateway, Cloudflare will automatically remove all associated hostname DNS records. This action will impact your traffic and cannot be undone.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15796.md")
</div></div>

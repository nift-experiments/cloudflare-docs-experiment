---
cp9:
  canonical: https://developers.cloudflare.com/web3/ipfs-gateway/concepts/universal-gateway/
  description: Access any IPFS content through the Universal Path gateway.
  full_title: Universal Path gateway · Cloudflare Web3 docs
  head_html: <title>Universal Path gateway · Cloudflare Web3 docs</title><meta name="generator" content="Nift"><meta name="description" content="Access any IPFS content through the Universal Path gateway."><link rel="canonical" href="https://developers.cloudflare.com/web3/ipfs-gateway/concepts/universal-gateway/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/web3/ipfs-gateway/concepts/universal-gateway/index.md"><meta property="og:title" content="Universal Path gateway · Cloudflare Web3 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Access any IPFS content through the Universal Path gateway."><meta property="og:url" content="https://developers.cloudflare.com/web3/ipfs-gateway/concepts/universal-gateway/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Web3"><meta name="algolia_product_filter" content="Web3"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Web3"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/web3/ipfs-gateway/concepts/universal-gateway/#page","headline":"Universal Path gateway \u00b7 Cloudflare Web3 docs","description":"Access any IPFS content through the Universal Path gateway.","url":"https://developers.cloudflare.com/web3/ipfs-gateway/concepts/universal-gateway/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /web3/ipfs-gateway/concepts/universal-gateway/
  schema: 1
---
<p>A Universal Path gateway is a gateway without a DNSLink record. It allows users to access any content hosted on the IPFS network by specifying a CID or IPNS path in the URL.</p>
<p>This differs from a <a href="/web3/ipfs-gateway/concepts/dnslink/">restricted gateway</a>, which limits the gateway to a single piece of content (a specific CID or IPNS hostname).</p>
<h2 id="how-is-it-used-with-cloudflare">How is it used with Cloudflare?</h2>
<p>You can set up a Universal Path gateway the same way you <a href="/web3/how-to/manage-gateways/">create any gateway</a>.</p>
<p>Because a Universal Path gateway is open by default, you may want to use the <a href="/web3/how-to/manage-gateways/#update-blocklist">gateway blocklist</a> to prevent access to specific content. You can block one or more:</p>
<ul>
<li>CIDs (<code>QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB</code>)</li>
<li>IPFS content paths (<code>/ipfs/QmYwAPJzv5CZsnA625s3Xf2nemtYgPpHdWEz79ojWnPbdG/readme</code>)</li>
<li>IPNS content paths (<code>/ipns/example.com</code>)</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15800.md")
</aside>

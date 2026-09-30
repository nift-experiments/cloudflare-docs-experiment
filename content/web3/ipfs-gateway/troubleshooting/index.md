---
cp9:
  canonical: https://developers.cloudflare.com/web3/ipfs-gateway/troubleshooting/
  description: Resolve common IPFS Gateway issues including 523 and 524 errors.
  full_title: Troubleshooting · Cloudflare Web3 docs
  head_html: <title>Troubleshooting · Cloudflare Web3 docs</title><meta name="generator" content="Nift"><meta name="description" content="Resolve common IPFS Gateway issues including 523 and 524 errors."><link rel="canonical" href="https://developers.cloudflare.com/web3/ipfs-gateway/troubleshooting/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/web3/ipfs-gateway/troubleshooting/index.md"><meta property="og:title" content="Troubleshooting · Cloudflare Web3 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Resolve common IPFS Gateway issues including 523 and 524 errors."><meta property="og:url" content="https://developers.cloudflare.com/web3/ipfs-gateway/troubleshooting/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Web3"><meta name="algolia_product_filter" content="Web3"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Web3"><meta name="pcx_tags" content="Debugging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/web3/ipfs-gateway/troubleshooting/#page","headline":"Troubleshooting \u00b7 Cloudflare Web3 docs","description":"Resolve common IPFS Gateway issues including 523 and 524 errors.","url":"https://developers.cloudflare.com/web3/ipfs-gateway/troubleshooting/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Debugging"]}</script>
  markdown: true
  noindex: false
  route: /web3/ipfs-gateway/troubleshooting/
  schema: 1
---
<h2 id="cloudflare-specific">Cloudflare-specific</h2>
<h3 id="no-link-named-ipfs">No link named &quot;ipfs&quot;</h3>
<p>If you get a <code>no link named &quot;ipfs&quot; under &lt;&lt;CID&gt;&gt;</code> error message when trying to access content through Cloudflare's IPFS gateway, that means you have created a gateway without a value for the <a href="/web3/ipfs-gateway/concepts/dnslink">DNSLink</a>.</p>
<p>Since Cloudflare currently only supports restricted gateways - and not <a href="/web3/ipfs-gateway/concepts/universal-gateway/">universal gateways</a> - these requests will continue to fail until you specify a DNSLink value.</p>
<h3 id="check-cloudflare-s-status">Check Cloudflare's status</h3>
<p>It is worth checking for recent incidents on Cloudflare's <a href="https://www.cloudflarestatus.com/">status
dashboard</a> that may have affected our
gateway, but the best place to get up-to-date information about issues facing
IPFS is the <a href="https://discuss.ipfs.io/">IPFS Discussion Forum</a>.</p>
<h2 id="generic-ipfs">Generic IPFS</h2>
<p>IPFS is still a developing protocol and content is often unavailable or slow to
load for reasons outside of Cloudflare's control. Usually, this happens for one
of the following reasons.</p>
<h3 id="the-content-was-uploaded-to-a-free-anonymous-pinning-service">The content was uploaded to a free/anonymous pinning service.</h3>
<p>Free and anonymous pinning services can often be used to get content on IPFS in
a pinch, but they'll often stop pinning content soon after it's uploaded.
Running your own server or using a pinning service are the recommended
alternatives, and will keep your content online more reliably.</p>
<h3 id="no-node-with-the-requested-content-is-online">No node with the requested content is online.</h3>
<p>Content will only stay on the IPFS network as long as there's at least one node
that's serving it. If all of the nodes that were serving a given piece of
content go offline, the content will be inaccessible until one of them comes
back online.</p>
<h3 id="the-nodes-with-the-requested-content-are-not-publicly-addressable">The nodes with the requested content are not publicly addressable.</h3>
<p>It's common for people who run an IPFS node on their home Wi-Fi to have very long
wait times or a high rate of request failure. This is because the rest of the
nodes in the IPFS network have difficulty connecting to them through their NAT
(Internet router). This can be solved by setting up Port Forwarding on the
router, to direct external connections to port 4001 to the host with the IPFS
node, or by moving the node to a hosted server/VM.</p>
<h3 id="the-nodes-with-the-requested-content-are-not-pinning-it">The nodes with the requested content are not pinning it.</h3>
<p>If several minutes have passed since files were uploaded to an IPFS node and
they're still not discoverable by other gateways, it's possible the node is
having trouble announcing the files to the rest of the network. You can make
sure the node with the content has pinned it by running:</p>
<pre tabindex="0"><code class="language-txt">ipfs pin -r &lt;content id&gt;&#10;</code></pre>
<p>And you can force the actual announcement by running:</p>
<pre tabindex="0"><code class="language-txt">ipfs dht provide -rv &lt;content id&gt;&#10;</code></pre>
<p>The second command will run indefinitely and has quite complicated output, so
you may want to run it in the background and omit the <code>-v</code> flag.</p>
<h3 id="the-nodes-with-the-requested-content-are-too-old">The nodes with the requested content are too old.</h3>
<p>IPFS issues mandatory updates from time to time that introduce breaking protocol
changes. Cloudflare tries to say ahead of these updates and may, as a result,
lose connectivity with older nodes.</p>

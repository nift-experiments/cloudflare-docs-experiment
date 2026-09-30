---
cp9:
  canonical: https://developers.cloudflare.com/network/onion-routing/
  description: Serve content directly through the Tor network with Onion Routing.
  full_title: Onion Routing and Tor support · Cloudflare Network settings docs
  head_html: <title>Onion Routing and Tor support · Cloudflare Network settings docs</title><meta name="generator" content="Nift"><meta name="description" content="Serve content directly through the Tor network with Onion Routing."><link rel="canonical" href="https://developers.cloudflare.com/network/onion-routing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/network/onion-routing/index.md"><meta property="og:title" content="Onion Routing and Tor support · Cloudflare Network settings docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Serve content directly through the Tor network with Onion Routing."><meta property="og:url" content="https://developers.cloudflare.com/network/onion-routing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Network"><meta name="algolia_product_filter" content="Network"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Network"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/network/onion-routing/#page","headline":"Onion Routing and Tor support \u00b7 Cloudflare Network settings docs","description":"Serve content directly through the Tor network with Onion Routing.","url":"https://developers.cloudflare.com/network/onion-routing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /network/onion-routing/
  schema: 1
---
<p>Improve the Tor user experience by enabling Onion Routing, which enables Cloudflare to serve your website’s content directly through the Tor network and without requiring exit nodes.</p>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="how-it-works">How it works</h2>
<p>Onion Routing helps improve Tor browsing as follows:</p>
<ul>
<li>Tor users no longer access your site via exit nodes, which can sometimes be compromised, and may snoop on user traffic.</li>
<li>Human Tor users and bots can be distinguished by our Onion services, such that interactive challenges are only served to malicious bot traffic.</li>
</ul>
<p><a href="https://tb-manual.torproject.org/about/">Tor Browser</a> users receive an <a href="https://httpwg.org/specs/rfc7838.html#alt-svc">alt-svc header</a> as part of the response to the first request to your website. The browser then creates a Tor Circuit to access this website using the <code>.onion</code> TLD service provided by this header.</p>
<p>You should note that the visible domain in the user interface remains unchanged, as the host header and the SNI are preserved. However, the underlying connection changes to be routed through Tor, as the <a href="https://tb-manual.torproject.org/managing-identities/#managing-identities">UI denotes on the left of the address bar</a> with a Tor Circuit. Cloudflare does not provide a certificate for the <code>.onion</code> domain provided as part of alt-svc flow, which therefore cannot be accessed via HTTPS.</p>
<h2 id="enable-onion-routing">Enable Onion Routing</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/674.md")
</div></div>

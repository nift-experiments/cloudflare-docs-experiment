---
cp9:
  canonical: https://developers.cloudflare.com/privacy-proxy/concepts/geolocation/
  description: Privacy Proxy preserves user geolocation using geohashes to select egress IPs that match the client's geographic region.
  full_title: Geolocation · Cloudflare Privacy Proxy docs
  head_html: <title>Geolocation · Cloudflare Privacy Proxy docs</title><meta name="generator" content="Nift"><meta name="description" content="Privacy Proxy preserves user geolocation using geohashes to select egress IPs that match the client&#x27;s geographic region."><link rel="canonical" href="https://developers.cloudflare.com/privacy-proxy/concepts/geolocation/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/privacy-proxy/concepts/geolocation/index.md"><meta property="og:title" content="Geolocation · Cloudflare Privacy Proxy docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Privacy Proxy preserves user geolocation using geohashes to select egress IPs that match the client&#x27;s geographic region."><meta property="og:url" content="https://developers.cloudflare.com/privacy-proxy/concepts/geolocation/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Privacy Proxy"><meta name="algolia_product_filter" content="Privacy Proxy"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Privacy Proxy"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/privacy-proxy/concepts/geolocation/#page","headline":"Geolocation \u00b7 Cloudflare Privacy Proxy docs","description":"Privacy Proxy preserves user geolocation using geohashes to select egress IPs that match the client's geographic region.","url":"https://developers.cloudflare.com/privacy-proxy/concepts/geolocation/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /privacy-proxy/concepts/geolocation/
  schema: 1
---
<p>Privacy Proxy preserves user geolocation without exposing real IP addresses. This ensures location-based services work correctly while maintaining privacy.</p>
<h2 id="why-geolocation-matters">Why geolocation matters</h2>
<p>Many online services use IP addresses to determine user location:</p>
<ul>
<li>Search engines return locally relevant results.</li>
<li>Content providers enforce regional licensing restrictions.</li>
<li>E-commerce sites show local pricing and shipping options.</li>
<li>News sites display region-specific content.</li>
</ul>
<p>Traditional VPNs and proxies often break these services because traffic exits from data centers far from the user's actual location. Privacy Proxy solves this by selecting egress IP addresses that match the user's geographic region.</p>
<h2 id="how-geolocation-works">How geolocation works</h2>
<p>Privacy Proxy uses geohashes to preserve location without revealing precise coordinates.</p>
<h3 id="geohash-encoding">Geohash encoding</h3>
<p>A <a href="https://en.wikipedia.org/wiki/Geohash">geohash</a> is a compact representation of latitude and longitude. Geohashes use a hierarchical encoding where longer strings represent more precise locations:</p>
<table>
<thead>
<tr>
<th>Geohash length</th>
<th>Approximate area</th>
</tr>
</thead>
<tbody>
<tr>
<td>1 character</td>
<td>~5,000 km</td>
</tr>
<tr>
<td>2 characters</td>
<td>~1,250 km</td>
</tr>
<tr>
<td>3 characters</td>
<td>~150 km</td>
</tr>
<tr>
<td>4 characters</td>
<td>~40 km</td>
</tr>
<tr>
<td>5 characters</td>
<td>~5 km</td>
</tr>
</tbody>
</table>
<p>Privacy Proxy uses reduced-precision geohashes (typically four to five characters) to locate users to a city or region without pinpointing their exact location.</p>
<h3 id="egress-ip-selection">Egress IP selection</h3>
<p>When a client connects to Privacy Proxy:</p>
<ol>
<li>The client (or first-hop proxy in double-hop deployments) determines the user's approximate location.</li>
<li>The client sends a geohash in the <code>sec-ch-geohash</code> header.</li>
<li>Privacy Proxy validates the geohash and selects an egress IP address from a pool registered to that geographic area.</li>
<li>Destination servers see the egress IP and geolocate the user to the correct region.</li>
</ol>
<h3 id="geohash-header-format">Geohash header format</h3>
<p>The <code>sec-ch-geohash</code> header includes the geohash and country code:</p>
<pre tabindex="0"><code class="language-http">sec-ch-geohash: xn76c-JP&#10;</code></pre>
<p>The format is <code>&lt;geohash&gt;-&lt;country_code&gt;</code>. The country code helps resolve edge cases where geohashes span country borders.</p>
<h2 id="geolocation-accuracy">Geolocation accuracy</h2>
<p>Cloudflare maintains egress IP pools in hundreds of cities worldwide. When you register egress IPs with geolocation databases, they map to specific locations.</p>
<p>Privacy Proxy achieves:</p>
<ul>
<li><strong>City-level accuracy</strong> by default, so users get locally relevant search results.</li>
<li><strong>Country-level accuracy</strong> as a fallback if city-level is not available.</li>
</ul>
<p>Users can opt for coarser geolocation (country and timezone only) if they prefer less precise location sharing.</p>
<h3 id="the-pizza-test">The pizza test</h3>
<p>A simple way to verify geolocation accuracy is to search for &quot;pizza near me&quot; through the proxy. If results show pizza places in the user's actual city rather than a distant data center, geolocation is working correctly.</p>
<h2 id="ipv6-and-geolocation-precision">IPv6 and geolocation precision</h2>
<p>Privacy Proxy achieves better geolocation precision over IPv6. If your origin servers support IPv6 (AAAA DNS records), the proxy prefers IPv6 egress addresses, which are registered with greater geographic precision than IPv4 equivalents.</p>
<p>To maximize geolocation accuracy for your users, ensure your services are reachable over IPv6.</p>
<h2 id="geolocation-in-double-hop-deployments">Geolocation in double-hop deployments</h2>
<p>In <a href="/privacy-proxy/concepts/deployment-models/#double-hop">double-hop deployments</a>, Proxy A (which you operate) is responsible for determining and forwarding the geohash:</p>
<ol>
<li>Proxy A geolocates the client's IP address.</li>
<li>Proxy A converts the location to a geohash with appropriate precision.</li>
<li>Proxy A includes the geohash in the forwarded CONNECT request to Proxy B.</li>
<li>Proxy B (Cloudflare) selects an egress IP based on the geohash.</li>
</ol>
<p>The geohash is cryptographically protected to prevent clients from spoofing their location.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://blog.cloudflare.com/geoexit-improving-warp-user-experience-larger-network/">Geo-egress: Improving WARP user experience on a larger network</a> - How Cloudflare implements geolocation-aware egress.</li>
</ul>

---
cp9:
  canonical: https://developers.cloudflare.com/realtime/turn/rfc-matrix/
  description: Supported TURN protocols, RFCs, and STUN features on Cloudflare Realtime TURN.
  full_title: TURN Feature Matrix · Cloudflare Realtime docs
  head_html: <title>TURN Feature Matrix · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Supported TURN protocols, RFCs, and STUN features on Cloudflare Realtime TURN."><link rel="canonical" href="https://developers.cloudflare.com/realtime/turn/rfc-matrix/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/turn/rfc-matrix/index.md"><meta property="og:title" content="TURN Feature Matrix · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Supported TURN protocols, RFCs, and STUN features on Cloudflare Realtime TURN."><meta property="og:url" content="https://developers.cloudflare.com/realtime/turn/rfc-matrix/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/turn/rfc-matrix/#page","headline":"TURN Feature Matrix \u00b7 Cloudflare Realtime docs","description":"Supported TURN protocols, RFCs, and STUN features on Cloudflare Realtime TURN.","url":"https://developers.cloudflare.com/realtime/turn/rfc-matrix/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/turn/rfc-matrix/
  schema: 1
---
<h2 id="turn-client-to-turn-server-protocols">TURN client to TURN server protocols</h2>
<table>
<thead>
<tr>
<th>Protocol</th>
<th>Support</th>
<th>Relevant specification</th>
</tr>
</thead>
<tbody>
<tr>
<td>UDP</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/rfc5766">RFC 5766</a></td>
</tr>
<tr>
<td>TCP</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/rfc5766">RFC 5766</a></td>
</tr>
<tr>
<td>TLS</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/rfc5766">RFC 5766</a></td>
</tr>
<tr>
<td>DTLS</td>
<td>No</td>
<td><a href="http://tools.ietf.org/html/draft-petithuguenin-tram-turn-dtls-00">draft-petithuguenin-tram-turn-dtls-00</a></td>
</tr>
</tbody>
</table>
<h2 id="turn-client-to-turn-server-protocols-1">TURN client to TURN server protocols</h2>
<table>
<thead>
<tr>
<th>Protocol</th>
<th>Support</th>
<th>Relevant specification</th>
</tr>
</thead>
<tbody>
<tr>
<td>TURN (base RFC)</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/rfc5766">RFC 5766</a></td>
</tr>
<tr>
<td>TURN REST API</td>
<td>✅ (See <a href="/realtime/turn/faq/#does-cloudflare-realtime-turn-support-the-expired-ietf-rfc-draft-draft-uberti-behave-turn-rest-00">FAQ</a>)</td>
<td><a href="http://tools.ietf.org/html/draft-uberti-behave-turn-rest-00">draft-uberti-behave-turn-rest-00</a></td>
</tr>
<tr>
<td>Origin field in TURN (Multi-tenant TURN Server)</td>
<td>✅</td>
<td><a href="https://tools.ietf.org/html/draft-ietf-tram-stun-origin-06">draft-ietf-tram-stun-origin-06</a></td>
</tr>
<tr>
<td>ALPN support for STUN &amp; TURN</td>
<td>✅</td>
<td><a href="https://datatracker.ietf.org/doc/html/rfc7443">RFC 7443</a></td>
</tr>
<tr>
<td>TURN Bandwidth draft specs</td>
<td>No</td>
<td><a href="http://tools.ietf.org/html/draft-thomson-tram-turn-bandwidth-01">draft-thomson-tram-turn-bandwidth-01</a></td>
</tr>
<tr>
<td>TURN-bis (with dual allocation) draft specs</td>
<td>No</td>
<td><a href="http://tools.ietf.org/html/draft-ietf-tram-turnbis-04">draft-ietf-tram-turnbis-04</a></td>
</tr>
<tr>
<td>TCP relaying TURN extension</td>
<td>No</td>
<td><a href="https://datatracker.ietf.org/doc/html/rfc6062">RFC 6062</a></td>
</tr>
<tr>
<td>IPv6 extension for TURN</td>
<td>No</td>
<td><a href="https://datatracker.ietf.org/doc/html/rfc6156">RFC 6156</a></td>
</tr>
<tr>
<td>oAuth third-party TURN/STUN authorization</td>
<td>No</td>
<td><a href="https://datatracker.ietf.org/doc/html/rfc7635">RFC 7635</a></td>
</tr>
<tr>
<td>DTLS support (for TURN)</td>
<td>No</td>
<td><a href="https://datatracker.ietf.org/doc/html/draft-petithuguenin-tram-stun-dtls-00">draft-petithuguenin-tram-stun-dtls-00</a></td>
</tr>
<tr>
<td>Mobile ICE (MICE) support</td>
<td>No</td>
<td><a href="http://tools.ietf.org/html/draft-wing-tram-turn-mobility-02">draft-wing-tram-turn-mobility-02</a></td>
</tr>
</tbody>
</table>

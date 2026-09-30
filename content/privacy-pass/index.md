---
cp9:
  canonical: https://developers.cloudflare.com/privacy-pass/
  description: Overview of entire document – what's in the docs, why Privacy Pass matters, high-level use case descriptions, and why customers can trust Cloudflare to run Privacy Pass infrastructure.
  full_title: Privacy Pass · Cloudflare Privacy Pass docs
  head_html: <title>Privacy Pass · Cloudflare Privacy Pass docs</title><meta name="generator" content="Nift"><meta name="description" content="Overview of entire document – what&#x27;s in the docs, why Privacy Pass matters, high-level use case descriptions, and why customers can trust Cloudflare to run Privacy Pass infrastructure."><link rel="canonical" href="https://developers.cloudflare.com/privacy-pass/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/privacy-pass/index.md"><meta property="og:title" content="Privacy Pass · Cloudflare Privacy Pass docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Overview of entire document – what&#x27;s in the docs, why Privacy Pass matters, high-level use case descriptions, and why customers can trust Cloudflare to run Privacy Pass infrastructure."><meta property="og:url" content="https://developers.cloudflare.com/privacy-pass/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Privacy Pass"><meta name="algolia_product_filter" content="Privacy Pass"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Privacy Pass"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/privacy-pass/#page","headline":"Privacy Pass \u00b7 Cloudflare Privacy Pass docs","description":"Overview of entire document \u2013 what's in the docs, why Privacy Pass matters, high-level use case descriptions, and why customers can trust Cloudflare to run Privacy Pass infrastructure.","url":"https://developers.cloudflare.com/privacy-pass/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /privacy-pass/
  schema: 1
---
<p>Privacy Pass, an <a href="https://datatracker.ietf.org/doc/html/rfc9576">IETF standard</a> that Cloudflare helped pioneer in 2017, offers a way for users to prove something about themselves–that they have passed a CAPTCHA, are of age, are part of a subscription class–to the site they are accessing, without revealing an identifier. The main mechanic is Privacy Pass tokens, which are the cryptographic tool that lets a service provider verify information about a user without learning who that user is or being able to track them across requests.</p>
<hr />
<h2 id="what-is-in-these-docs">What is in these docs</h2>
<ul>
<li><strong><a href="/privacy-pass/getting-started/">Getting started</a></strong> — two self-serve ways to see Privacy Pass work: get a real token with the demo tool, or run the issuance and redemption flow locally.</li>
<li><strong><a href="/privacy-pass/concepts/privacy-pass-protocol/">Privacy Pass Protocol</a></strong> — the four roles, an architecture diagram, and the issuance and redemption flow.</li>
<li><strong><a href="/privacy-pass/concepts/deployment-models/">Deployment Models</a></strong> — who operates each role, detailed example deployment models, and Privacy Pass as a part of other products.</li>
<li><strong><a href="/privacy-pass/production-deployment-testing/">Production Deployment Testing</a></strong> — validate a real, Cloudflare-operated deployment end to end, once you and Cloudflare have built it together.</li>
<li><strong><a href="/privacy-pass/references/">References</a></strong> — the external resources cited across these docs.</li>
</ul>
<hr />
<h2 id="why-it-matters">Why it matters</h2>
<p>Verifying users on the Internet usually forces a trade-off between user experience and privacy, coming at the cost of either time spent solving CAPTCHAs or privacy lost to a trackable identifier. Privacy Pass eases that trade-off: a user proves a claim once, and receives tokens that can be redeemed later without revealing their identity or linking their activity.</p>
<p>So far, the main use cases have been providing a privacy-preserving CAPTCHA alternative, such as through <a href="/turnstile/">Turnstile</a> and verification for Cloudflare's <a href="/privacy-proxy/">Privacy Proxy</a> and <a href="/privacy-gateway/">Privacy Gateway</a> products. However, by adjusting the deployment, Privacy Pass tokens can attest to any other information a service provider wants to prove.</p>
<hr />
<h2 id="use-cases">Use cases</h2>
<p>Every Privacy Pass use case comes down to the same idea: let clients prove something to an origin server without revealing any other information. Some examples include:</p>
<ul>
<li>
<p><strong>Authentication for other privacy products</strong> – Privacy Pass can be used as a verification layer for other privacy products, such as Privacy Proxy and Privacy Gateway, to help them complete their functions while preserving the privacy of their users.</p>
</li>
<li>
<p><strong>Privacy-preserving bot management</strong> – Apple uses their token deployment, Private Access Tokens, to <a href="https://blog.cloudflare.com/eliminating-captchas-on-iphones-and-macs-using-new-standard/">automatically reduce CAPTCHAs</a> when using iOS 16+ devices on participating websites. Privacy Pass tokens are similarly <a href="https://blog.cloudflare.com/privacy-pass-standard/">built into Turnstile</a> as a signal in its application layer challenge decisions.</p>
</li>
<li>
<p><strong>Attribute verification</strong> – Privacy Pass can help attest to whether a user  has a valid subscription to the service or meets age requirement without that service learning their identity or linking it to their activity.</p>
</li>
<li>
<p><strong>Rate limiting</strong>: While production use cases are still in development, Privacy Pass tokens can be used to meter usage without identifying users. Refer to the <a href="https://datatracker.ietf.org/doc/draft-ietf-privacypass-batched-tokens/">Batched Token issuance protocol</a>, <a href="https://datatracker.ietf.org/doc/draft-ietf-privacypass-arc-protocol/">ARC issuance protocol</a>, and <a href="https://datatracker.ietf.org/doc/draft-meunier-privacypass-reverse-flow/">Privacy Pass Reverse Flow</a> IETF drafts.</p>
</li>
</ul>
<hr />
<h2 id="why-cloudflare-operates-privacy-pass-infrastructure">Why Cloudflare operates Privacy Pass infrastructure</h2>
<ul>
<li><strong>Reliability and scale.</strong> Issuers face high request volumes and must stay highly available so that user experience isn't affected by attacks or latency, something Cloudflare's global network is built to handle. Cloudflare is one of the few providers running Privacy Pass at scale.</li>
<li><strong>Redemption at the edge.</strong> Because Cloudflare sits in front of many origins, it can verify tokens at the edge on the Origin's behalf. Furthermore, Cloudflare Workers natively supports redemption, offering additional infrastructure to ease Privacy Pass integration.</li>
<li><strong>A shared public issuer.</strong> Rather than building and maintaining your own issuer, you can rely on Cloudflare's public, RFC 9578-compliant issuer deployments. We follow Privacy Pass guidelines and adhere to public, auditable commitments you can trust.</li>
</ul>
<hr />
<h2 id="related-products">Related products</h2>
<p><strong><a href="/privacy-proxy/">Privacy Proxy</a></strong></p>
<p>A MASQUE-based forward proxy that uses Privacy Pass tokens to authenticate users without revealing their identity.</p>
<p><strong><a href="/privacy-gateway/">Privacy Gateway</a></strong></p>
<p>Implements the Oblivious HTTP (OHTTP) standard for request-level privacy, hiding client IP addresses from application backends with Privacy Pass authentication.</p>
<p><strong><a href="/turnstile/">Turnstile</a></strong></p>
<p>Cloudflare's smart CAPTCHA alternative that can be embedded into any website, using Privacy Pass tokens as one of the signals used to decide whether or not a challenge is shown to a visitor.</p>

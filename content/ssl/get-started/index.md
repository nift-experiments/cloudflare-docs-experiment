---
cp9:
  canonical: https://developers.cloudflare.com/ssl/get-started/
  description: Set up SSL/TLS encryption between visitors, Cloudflare, and your origin server.
  full_title: Get started with SSL/TLS · Cloudflare SSL/TLS docs
  head_html: <title>Get started with SSL/TLS · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up SSL/TLS encryption between visitors, Cloudflare, and your origin server."><link rel="canonical" href="https://developers.cloudflare.com/ssl/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/get-started/index.md"><meta property="og:title" content="Get started with SSL/TLS · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up SSL/TLS encryption between visitors, Cloudflare, and your origin server."><meta property="og:url" content="https://developers.cloudflare.com/ssl/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/get-started/#page","headline":"Get started with SSL/TLS \u00b7 Cloudflare SSL/TLS docs","description":"Set up SSL/TLS encryption between visitors, Cloudflare, and your origin server.","url":"https://developers.cloudflare.com/ssl/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/get-started/
  schema: 1
---
<p>Set up encrypted connections for your domain by choosing a certificate, selecting an encryption mode, and enforcing HTTPS.</p>
<h2 id="before-you-begin">Before you begin</h2>
<ul>
<li><a href="/fundamentals/account/">Create an account and register an application</a></li>
</ul>
<h2 id="choose-an-edge-certificate">Choose an edge certificate</h2>
<p><a href="/ssl/concepts/#edge-certificate">Edge certificates</a> are the SSL/TLS certificates that Cloudflare presents to visitors connecting to your domain. Cloudflare offers several types:</p>
<ul>
<li>
<p><a href="/ssl/edge-certificates/universal-ssl/"><strong>Universal certificates</strong></a>: <div class="nb-glossary-definition"><p>By default, Cloudflare issues — and <a href="/ssl/reference/certificate-validity-periods/#universal-ssl">renews</a> — free, unshared, publicly trusted SSL certificates to all domains <a href="/fundamentals/manage-domains/add-site/">added to</a> and <a href="/dns/zone-setups/reference/domain-status/">activated on</a> Cloudflare.</p></div></p>
</li>
<li>
<p><a href="/ssl/edge-certificates/advanced-certificate-manager/"><strong>Advanced certificates</strong></a>:
Use advanced certificates when you want something more customizable than <a href="/ssl/edge-certificates/universal-ssl/">Universal SSL</a> but still want the convenience of SSL certificate issuance and renewal.</p>
</li>
<li>
<p><a href="/ssl/edge-certificates/custom-certificates/"><strong>Custom certificates</strong></a>:
Custom certificates are meant for Business and Enterprise customers who want to use their own SSL certificates.</p>
</li>
<li>
<p><a href="/ssl/keyless-ssl/"><strong>Keyless certificates</strong></a> (Enterprise only):
Keyless SSL allows security-conscious clients to upload their own custom certificates and benefit from Cloudflare, but without exposing their TLS private keys.</p>
</li>
</ul>
<p>For help deciding which certificate type fits your use case, refer to <a href="/ssl/edge-certificates/">Edge certificates</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="for-saas-providers">For SaaS providers</h3>
@markup("md", "content/.markup/bodies/313.md")
</aside>
<h2 id="choose-your-encryption-mode">Choose your encryption mode</h2>
<p>Once you have chosen your edge certificate, <a href="/ssl/origin-configuration/ssl-modes/">choose an encryption mode</a>.</p>
<p>Encryption modes control how Cloudflare manages two separate connections: one between visitors and Cloudflare, and another between Cloudflare and your origin server. Modes range from no encryption to strict validation of your origin certificate. For more context, refer to the <a href="/ssl/concepts/#ssltls-certificate">concepts page</a>.</p>
<p><a href="/ssl/origin-configuration/ssl-modes/full-strict/">Full (strict)</a> mode — the most secure option — requires a valid, unexpired certificate on your origin server. You can use a certificate from a publicly trusted certificate authority (CA), or generate a free <a href="/ssl/origin-configuration/origin-ca/">Origin CA certificate</a> from Cloudflare. Each encryption mode page lists its specific requirements.</p>
<h2 id="enforce-https-connections">Enforce HTTPS connections</h2>
<p>Even if your application has an active edge certificate, visitors can still access resources over unsecured HTTP connections.</p>
<p>Using various Cloudflare settings, however, you can force all or most visitor connections to <a href="/ssl/edge-certificates/encrypt-visitor-traffic/">use HTTPS</a>.</p>
<h2 id="seo-considerations">SEO considerations</h2>
<p>Using HTTPS can improve user trust and may be used as a ranking signal by search engines. For related guidance, refer to <a href="/fundamentals/performance/improve-seo/">Improve SEO</a>.</p>
<h2 id="optional-enable-additional-features">Optional - Enable additional features</h2>
<p>After you have chosen your encryption mode and enforced HTTPS connections, evaluate the following settings:</p>
<ul>
<li><a href="/ssl/edge-certificates/additional-options/">Edge certificates</a>: Customize different aspects of your edge certificates, from enabling <strong>Opportunistic Encryption</strong> to specifying a <strong>Minimum TLS Version</strong>.</li>
<li><a href="/ssl/origin-configuration/authenticated-origin-pull/">Authenticated origin pull</a>: Ensure all requests to your origin server originate from the Cloudflare network.</li>
<li><a href="/notifications/notification-available/">Notifications</a>: Set up alerts related to certificate validation status, issuance, renewal, and expiration.</li>
</ul>

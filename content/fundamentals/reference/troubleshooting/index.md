---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/reference/troubleshooting/
  description: Resolve common error messages and unexpected behavior when setting up your Cloudflare account and domain.
  full_title: Troubleshooting · Cloudflare Fundamentals docs
  head_html: <title>Troubleshooting · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Resolve common error messages and unexpected behavior when setting up your Cloudflare account and domain."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/reference/troubleshooting/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/reference/troubleshooting/index.md"><meta property="og:title" content="Troubleshooting · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Resolve common error messages and unexpected behavior when setting up your Cloudflare account and domain."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/reference/troubleshooting/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/reference/troubleshooting/#page","headline":"Troubleshooting \u00b7 Cloudflare Fundamentals docs","description":"Resolve common error messages and unexpected behavior when setting up your Cloudflare account and domain.","url":"https://developers.cloudflare.com/fundamentals/reference/troubleshooting/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/reference/troubleshooting/
  schema: 1
---
<p>When you <a href="/fundamentals/account/">set up Cloudflare</a>, you may experience the following issues or error messages.</p>
<h2 id="error-messages">Error messages</h2>
<ul>
<li><a href="/ssl/troubleshooting/too-many-redirects/"><code>ERR_TOO_MANY_REDIRECTS</code></a></li>
<li><a href="/ssl/troubleshooting/too-many-redirects/"><code>525</code> or <code>526</code> errors</a></li>
<li><a href="/dns/manage-dns-records/troubleshooting/records-with-same-name/">Cannot add DNS records with the same name</a></li>
<li><a href="/ssl/troubleshooting/version-cipher-mismatch/"><code>ERR_SSL_VERSION_OR_CIPHER_MISMATCH</code> or <code>SSL_ERROR_NO_CYPHER_OVERLAP</code></a></li>
<li><a href="/dns/troubleshooting/dns-probe-finished-nxdomain/"><code>DNS_PROBE_FINISHED_NXDOMAIN</code></a></li>
<li><a href="/dns/manage-dns-records/troubleshooting/exposed-ip-address/">Record exposing origin server IP address</a></li>
<li><a href="/ssl/troubleshooting/mixed-content-errors/">Mixed content errors</a></li>
<li><a href="/ssl/troubleshooting/general-ssl-errors/">SSL errors in appear in my browser</a></li>
</ul>
<h2 id="behavior">Behavior</h2>
<ul>
<li><a href="/support/troubleshooting/restoring-visitor-ips/restoring-original-visitor-ips/">Why are Cloudflare's IPs in my origin web server logs?</a></li>
<li><a href="#is-cloudflare-attacking-me">Is Cloudflare attacking me?</a></li>
<li><a href="/dns/zone-setups/troubleshooting/cannot-add-domain/">Cannot add domain to Cloudflare</a></li>
<li><a href="/dns/troubleshooting/email-issues/">My domain’s email stopped working</a></li>
<li><a href="/ssl/edge-certificates/encrypt-visitor-traffic/">Why is my site served over HTTP instead of HTTPS?</a></li>
<li><a href="/ssl/troubleshooting/general-ssl-errors/#only-some-of-your-subdomains-return-ssl-errors">SSL is not working for my second-level subdomain, such as <code>dev.www.example.com</code></a></li>
<li><a href="/dns/zone-setups/troubleshooting/domain-deleted/">Why was my domain deleted from Cloudflare?</a></li>
</ul>
<h2 id="cloudflare">Cloudflare</h2>
<ul>
<li><a href="/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/">Gather information to troubleshoot site issues</a></li>
<li><a href="/support/contacting-cloudflare-support/">Contact Cloudflare support</a></li>
<li><a href="/fundamentals/user-profiles/customize-account/#notifications">Manage email notifications</a></li>
</ul>
<h2 id="general-resources">General resources</h2>
<ul>
<li><a href="/dns/faq/">DNS FAQ</a></li>
<li><a href="/ssl/faq/">SSL/TLS FAQ</a></li>
</ul>
<h2 id="is-cloudflare-attacking-me">Is Cloudflare attacking me</h2>
<p>Two common scenarios falsely lead to the perception that Cloudflare is attacking your site:</p>
<ul>
<li>Unless you <a href="/support/troubleshooting/restoring-visitor-ips/restoring-original-visitor-ips/">restore the original visitor IP addresses</a>, Cloudflare IP addresses appear in your server logs for all proxied requests.</li>
<li>The attacker is spoofing Cloudflare's IPs. Cloudflare only <a href="/fundamentals/reference/network-ports/">sends traffic to your origin web server over a few specific ports</a> unless you use <a href="/spectrum/">Cloudflare Spectrum</a>.</li>
</ul>
<p>Ideally, because Cloudflare is a reverse proxy, your hosting provider observes attack traffic connecting from <a href="https://www.cloudflare.com/ips/">Cloudflare IP addresses</a>. In contrast, if you notice connections from IP addresses that do not belong to Cloudflare, the attack is direct to your origin web server. Cloudflare cannot stop attacks directly to your origin IP address because the traffic bypasses Cloudflare's network.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8771.md")
</aside>

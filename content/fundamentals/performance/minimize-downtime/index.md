---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/performance/minimize-downtime/
  description: Learn how to minimize downtime while onboarding your domain onto Cloudflare.
  full_title: Minimize downtime · Cloudflare Fundamentals docs
  head_html: <title>Minimize downtime · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to minimize downtime while onboarding your domain onto Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/performance/minimize-downtime/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/performance/minimize-downtime/index.md"><meta property="og:title" content="Minimize downtime · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to minimize downtime while onboarding your domain onto Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/performance/minimize-downtime/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/performance/minimize-downtime/#page","headline":"Minimize downtime \u00b7 Cloudflare Fundamentals docs","description":"Learn how to minimize downtime while onboarding your domain onto Cloudflare.","url":"https://developers.cloudflare.com/fundamentals/performance/minimize-downtime/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/performance/minimize-downtime/
  schema: 1
---
<p>When making any change to the routing of an Internet application, there is always a possibility of downtime due to certificate issuance, misconfigured settings, or limitations at your origin server. To avoid downtime when going live, it is important to review the most common configurations.</p>
<h2 id="update-and-review-dns-records">Update and review DNS records</h2>
<p>Before activating your domain on Cloudflare (exact steps depend on your <a href="/dns/zone-setups/">DNS setup</a>), review the DNS records in your Cloudflare account.</p>
<h3 id="start-with-unproxied-records">Start with unproxied records</h3>
<p>With a new domain, make sure all of your DNS records have a <a href="/dns/proxy-status/">proxy status</a> of <strong>DNS-only</strong>.</p>
<p>This setting prevents Cloudflare from proxying your traffic before you have an active edge certificate or before you have allowed Cloudflare IP addresses.</p>
<h3 id="confirm-record-accuracy">Confirm record accuracy</h3>
<p>Take extra time to confirm the accuracy of your DNS records before activating your domain, paying special attention to:</p>
<ul>
<li><a href="/dns/manage-dns-records/how-to/create-zone-apex/">Zone apex records (<code>example.com</code>)</a></li>
<li><a href="/dns/manage-dns-records/how-to/create-subdomain/">Subdomain records (<code>www.example.com</code> or <code>blog.example.com</code>)</a></li>
<li><a href="/dns/manage-dns-records/how-to/email-records/">Email records</a></li>
</ul>
<p>If you add DNS records to your authoritative DNS provider between onboarding your domain and activating your domain, you may need to also add these records within Cloudflare.</p>
<h2 id="activate-your-domain">Activate your domain</h2>
<p>Finish the <a href="/dns/zone-setups/">DNS setup</a> for your domain, moving the <a href="/dns/zone-setups/reference/domain-status/">domain status</a> to <strong>Active</strong>:</p>
<ul>
<li><a href="/dns/zone-setups/full-setup/setup/">Full setups</a>: Update the authoritative nameservers at your registrar and wait for that change to be authenticated.</li>
<li><a href="/dns/zone-setups/partial-setup/setup/">Partial setups</a>: Add the verification TXT record to your authoritative DNS and wait for that change to be authenticated.</li>
</ul>
<h2 id="verify-ssl-tls-edge-certificates">Verify SSL/TLS edge certificates</h2>
<p>Before proxying your traffic through Cloudflare, <a href="/ssl/reference/certificate-statuses/#monitor-certificate-statuses">verify</a> that Cloudflare has an active <strong>Edge Certificate</strong> for your domain.</p>
<p>For more details about timing and certificate recommendations, refer to <a href="/ssl/edge-certificates/universal-ssl/enable-universal-ssl/#full-dns-setup">Certificate issuance</a>.</p>
<h2 id="optional-test-configuration">Optional - Test configuration</h2>
<p>You may want to test your configuration using your local machine or proxying traffic from a development domain or subdomain.</p>
<p>If you experience issues, you should make sure that you have <a href="/fundamentals/concepts/cloudflare-ip-addresses/">allowed Cloudflare IP addresses</a> at your origin server.</p>
<h2 id="update-proxy-status">Update proxy status</h2>
<p>Once you have verified that your SSL/TLS edge certificate is active and you have allowed Cloudflare IP addresses, change the <a href="/dns/proxy-status/">proxy status</a> of appropriate DNS records to <strong>Proxied</strong>.</p>

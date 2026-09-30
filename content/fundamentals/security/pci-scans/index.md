---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/security/pci-scans/
  description: Run PCI compliance scans against your origin server or Cloudflare proxy and interpret the results.
  full_title: Scan for PCI compliance · Cloudflare Fundamentals docs
  head_html: <title>Scan for PCI compliance · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Run PCI compliance scans against your origin server or Cloudflare proxy and interpret the results."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/security/pci-scans/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/security/pci-scans/index.md"><meta property="og:title" content="Scan for PCI compliance · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Run PCI compliance scans against your origin server or Cloudflare proxy and interpret the results."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/security/pci-scans/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/security/pci-scans/#page","headline":"Scan for PCI compliance \u00b7 Cloudflare Fundamentals docs","description":"Run PCI compliance scans against your origin server or Cloudflare proxy and interpret the results.","url":"https://developers.cloudflare.com/fundamentals/security/pci-scans/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/security/pci-scans/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8769.md")
</aside>
<p>PCI scanners are tools used to identify security weaknesses. When a business undergoes a compliance audit, PCI scan results are used for compliance verification.</p>
<h2 id="initiate-a-scan">Initiate a scan</h2>
<ol>
<li>
<p>Identify which server your scan should target. Are you scanning against your origin server, where your applications are hosted, or at a proxy server sitting in front of your origin, such as Cloudflare?</p>
</li>
<li>
<p>On your scanner tool, enter a public URL or an IP address. If you enter a public website URL, the scanner will resolve the hostname and scan the resulting the IP address. To scan your origin server, be sure to enter your origin server's IP address or a hostname that resolves to the origin server's IP, not a proxy server.</p>
</li>
<li>
<p>Start the scan and analyze the results.</p>
</li>
<li>
<p>(Optional) Run another scan for a different origin server.</p>
</li>
</ol>
<h3 id="open-ports-versus-blocked-traffic">Open ports versus blocked traffic</h3>
<p>Cloudflare's anycast network operates in a way that keeps ports other than 80 and 443 open, allowing it to serve traffic for other customers on these ports.</p>
<p>However, customers can easily block all unwanted traffic to these ports by using Cloudflare <a href="/fundamentals/reference/network-ports/#how-to-block-traffic-on-additional-ports">WAF Managed Rules</a> or <a href="/waf/custom-rules/">custom rules</a>. The PCI scan will show the ports being open, but the traffic will not reach your origin server. This concern is often misunderstood.</p>
<h2 id="additional-resources">Additional resources</h2>
<p>You can find all our public compliance resources in the following pages:</p>
<ul>
<li><a href="https://www.cloudflare.com/trust-hub/compliance-resources/">Certifications and compliance resources</a></li>
<li><a href="/fundamentals/reference/policies-compliances/compliance-docs/">Compliance documentation</a></li>
</ul>
<p>You can access Compliance documents in the Cloudflare dashboard by selecting your account where you are a Super Administrator and then navigating to <strong>Support</strong> &gt; <strong>Compliance Documents</strong>.</p>

---
cp9:
  canonical: https://developers.cloudflare.com/dmarc-management/
  description: Stop brand impersonation.
  full_title: Overview · Cloudflare DMARC Management docs
  head_html: <title>Overview · Cloudflare DMARC Management docs</title><meta name="generator" content="Nift"><meta name="description" content="Stop brand impersonation."><link rel="canonical" href="https://developers.cloudflare.com/dmarc-management/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dmarc-management/index.md"><meta property="og:title" content="Overview · Cloudflare DMARC Management docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Stop brand impersonation."><meta property="og:url" content="https://developers.cloudflare.com/dmarc-management/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DMARC Management"><meta name="algolia_product_filter" content="DMARC Management"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="DMARC Management"><meta name="pcx_tags" content="DNS,Phishing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/dmarc-management/#page","headline":"Overview \u00b7 Cloudflare DMARC Management docs","description":"Stop brand impersonation.","url":"https://developers.cloudflare.com/dmarc-management/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["DNS","Phishing"]}</script>
  markdown: true
  noindex: false
  route: /dmarc-management/
  schema: 1
---
<div class="nb-description">
@markup("md", "content/.markup/bodies/1138.md")
</div>
<div class="nb-plan">
<p>Available on all plans</p>
</div>
<p>When someone receives an email that claims to be from your domain, email servers check whether that message is authentic. Three DNS-based mechanisms handle this verification:</p>
<ul>
<li><strong><a href="https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/">SPF (Sender Policy Framework)</a></strong> confirms the email was sent from an IP address or domain your domain authorizes.</li>
<li><strong><a href="https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/">DKIM (DomainKeys Identified Mail)</a></strong> authenticates the sender's domain and verifies the email content was not altered in transit, using a cryptographic signature.</li>
<li><strong><a href="https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/">DMARC (Domain-based Message Authentication Reporting and Conformance)</a></strong> ties SPF and DKIM together and tells receiving servers what to do when a check fails (for example, reject the email, quarantine it, or take no action).</li>
</ul>
<p>Cloudflare DMARC Management helps you track every source that is sending emails from your domain and review DMARC reports for each source. These reports show whether messages sent from your domain are passing SPF, DKIM, and DMARC checks — so you can identify unauthorized senders and protect your domain from being used in phishing or spoofing attacks.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1137.md")
</aside>
<hr />
<h2 id="related-products">Related products</h2>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/1139.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/1140.md")
</div>

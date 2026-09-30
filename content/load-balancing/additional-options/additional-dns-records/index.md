---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/additional-options/additional-dns-records/
  description: Use additional DNS records with load balancers.
  full_title: Load balance additional DNS records · Cloudflare Load Balancing docs
  head_html: <title>Load balance additional DNS records · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Use additional DNS records with load balancers."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/additional-options/additional-dns-records/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/additional-options/additional-dns-records/index.md"><meta property="og:title" content="Load balance additional DNS records · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use additional DNS records with load balancers."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/additional-options/additional-dns-records/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/load-balancing/additional-options/additional-dns-records/#page","headline":"Load balance additional DNS records \u00b7 Cloudflare Load Balancing docs","description":"Use additional DNS records with load balancers.","url":"https://developers.cloudflare.com/load-balancing/additional-options/additional-dns-records/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /load-balancing/additional-options/additional-dns-records/
  schema: 1
---
<p>In addition to load balancing between DNS records used for IP resolution — <code>A</code>, <code>AAAA</code>, and <code>CNAME</code> records — Enterprise customers can also load balance between <strong>MX</strong> and <strong>SRV</strong> records.</p>
<h2 id="mx-records">MX records</h2>
<p>To load balance between multiple mail servers:</p>
<ol>
<li>Make sure you have the <a href="/dns/manage-dns-records/how-to/email-records/#send-and-receive-email">required DNS records</a> for your mail servers.</li>
<li><a href="/load-balancing/monitors/create-monitor/">Create a monitor</a> with a <strong>Type</strong> of <em>SMTP</em>.</li>
<li><a href="/load-balancing/pools/create-pool/">Create a pool</a> with your mail servers and attach the newly created monitor.</li>
<li><a href="/load-balancing/load-balancers/create-load-balancer/">Create a load balancer</a> that includes your newly created pools. Since it will forward SMTP traffic, the load balancer should be <a href="/load-balancing/understand-basics/proxy-modes/#dns-only-load-balancing">unproxied (DNS-only)</a>.</li>
</ol>
<h2 id="srv-records">SRV records</h2>
<p>To load balance between different <strong>SRV</strong> records, which contain significantly more information than many other DNS records:</p>
<ol>
<li><a href="/dns/manage-dns-records/how-to/create-dns-records/#create-dns-records">Create your SRV records</a>.</li>
<li><a href="/load-balancing/monitors/create-monitor/">Create a monitor</a> with a <strong>Type</strong> of <em>UDP-ICMP</em> or <em>TCP</em>.</li>
<li><a href="/load-balancing/pools/create-pool/">Create a pool</a> with your various SRV records and attach the newly created monitor.</li>
<li><a href="/load-balancing/load-balancers/create-load-balancer/">Create a load balancer</a> that includes your newly created pools. This load balancer should be <a href="/load-balancing/understand-basics/proxy-modes/#dns-only-load-balancing">unproxied (DNS-only)</a>.</li>
</ol>

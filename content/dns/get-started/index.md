---
cp9:
  canonical: https://developers.cloudflare.com/dns/get-started/
  description: Set up Cloudflare DNS for your domain.
  full_title: Get started with Cloudflare DNS · Cloudflare DNS docs
  head_html: <title>Get started with Cloudflare DNS · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up Cloudflare DNS for your domain."><link rel="canonical" href="https://developers.cloudflare.com/dns/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/get-started/index.md"><meta property="og:title" content="Get started with Cloudflare DNS · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up Cloudflare DNS for your domain."><meta property="og:url" content="https://developers.cloudflare.com/dns/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/dns/get-started/#page","headline":"Get started with Cloudflare DNS \u00b7 Cloudflare DNS docs","description":"Set up Cloudflare DNS for your domain.","url":"https://developers.cloudflare.com/dns/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/get-started/
  schema: 1
---
<p>You can use Cloudflare DNS with a variety of <a href="/dns/zone-setups/">setups</a>. For an overview of what these setups are and an introduction to specific DNS terminology, refer to <a href="/dns/concepts/">Concepts</a>.</p>
<p>In the most common setup (full), you <a href="/fundamentals/manage-domains/add-site/">add your domain</a>, import your <a href="/dns/manage-dns-records/">DNS records</a>, and <a href="/dns/nameservers/update-nameservers/">update your nameservers</a> to make Cloudflare your primary authoritative DNS provider.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1123.md")
</aside>
<p>Once the setup is completed:</p>
<ul>
<li>
<p>You <a href="/dns/manage-dns-records/how-to/create-dns-records/">manage DNS records</a> through the Cloudflare dashboard or API. This is how you control which resources are available on the apex domain (<code>example.com</code>) or specific subdomains (<code>blog.example.com</code>) of your website, as well as control other configurations.</p>
</li>
<li>
<p>Cloudflare <a href="/fundamentals/concepts/how-cloudflare-works/">responds to all DNS queries</a> for your hostnames and your DNS records are propagated across the <a href="https://www.cloudflare.com/network/">Cloudflare global network</a>, speeding up your domain.</p>
</li>
</ul>
<h2 id="resources">Resources</h2>
<p>The following links introduce important concepts and will guide you through actions you may need to take while having your website or application on Cloudflare.</p>
<ul>
<li>
<p><a href="/dns/manage-dns-records/">DNS records</a>: DNS records contain information about your domain and are used to make your website or application available to visitors and other web services.</p>
</li>
<li>
<p><a href="/dns/nameservers/">Nameservers</a>: In the context of Cloudflare DNS, nameservers refer to authoritative nameservers. When a nameserver is authoritative for <code>example.com</code>, it means that DNS resolvers will consider responses from this nameserver when a user tries to access <code>example.com</code>.</p>
</li>
<li>
<p><a href="/dns/proxy-status/">Proxy status</a>: Proxy status affects how Cloudflare treats incoming HTTP/S requests to A, AAAA, and CNAME records. When a record is proxied, Cloudflare responds with <a href="/fundamentals/concepts/cloudflare-ip-addresses/">anycast IPs</a>, which speeds up and protects HTTP/S traffic with our <a href="/cache/">cache</a>/<a href="https://www.cloudflare.com/learning/cdn/what-is-a-cdn/">CDN</a>, <a href="/ddos-protection/">DDoS protection</a>, <a href="/waf/">WAF</a>, and <a href="/directory/?product-group=Application+performance%2CApplication+security">more</a>.</p>
</li>
</ul>
<h2 id="further-reading">Further reading</h2>
<ul>
<li>
<p><a href="/fundamentals/concepts/how-cloudflare-works/">How Cloudflare works</a>: An overview of how Cloudflare works as a DNS provider and as a reverse proxy.</p>
</li>
<li>
<p><a href="/dns/additional-options/analytics/">DNS analytics</a>: An overview of the different data sources and insights you can get when using Cloudflare DNS.</p>
</li>
<li>
<p><a href="/dns/troubleshooting/">Troubleshooting</a>: A full resources list for when something is not working.</p>
</li>
</ul>

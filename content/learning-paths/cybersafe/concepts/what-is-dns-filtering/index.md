---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/cybersafe/concepts/what-is-dns-filtering/
  description: Learn how DNS filtering blocks threats.
  full_title: What is DNS filtering? · Cloudflare Learning Paths
  head_html: <title>What is DNS filtering? · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Learn how DNS filtering blocks threats."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/cybersafe/concepts/what-is-dns-filtering/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/cybersafe/concepts/what-is-dns-filtering/index.md"><meta property="og:title" content="What is DNS filtering? · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how DNS filtering blocks threats."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/cybersafe/concepts/what-is-dns-filtering/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="Gateway,Email security (formerly Area 1),Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/cybersafe/concepts/what-is-dns-filtering/#page","headline":"What is DNS filtering? \u00b7 Cloudflare Learning Paths","description":"Learn how DNS filtering blocks threats.","url":"https://developers.cloudflare.com/learning-paths/cybersafe/concepts/what-is-dns-filtering/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/cybersafe/concepts/what-is-dns-filtering/
  schema: 1
---
<p>DNS filtering is a technique to block access to websites or online content. DNS filtering is implemented by specialized DNS resolvers (such as Cloudflare Gateway) that allow you to define a blocklist of domains or content categories. The DNS resolver acts as a filter by refusing to resolve queries for domains on the blocklist, thus preventing users from loading those websites.</p>
<h2 id="purpose-of-dns-filtering">Purpose of DNS filtering</h2>
<p>DNS filtering is commonly used to:</p>
<ul>
<li>Protect school data from phishing, ransomware, and malware.</li>
<li>Block websites that go against school acceptable use policy, such as adult content, gambling, and piracy.</li>
<li>Restrict access to websites that may impact student productivity, such as gaming, social media, and video streaming.</li>
</ul>
<h2 id="how-dns-filtering-works">How DNS filtering works</h2>
<p>DNS filtering involves configuring your browser, device, or router to send all DNS requests to a DNS filtering service. The DNS filtering service checks the domain or IP against your DNS policies. If the domain or IP matches a block policy, the DNS filtering service can redirect the request to an alternative IP address or block it altogether. The diagram below shows the logic for Cloudflare Gateway's DNS filtering service.</p>
<pre tabindex="0"><code class="language-mermaid">flowchart LR&#10;accTitle: DNS filtering&#10;A[Browser] --  What is the IP address of www.example.com? --&gt; B&#10;&#10;subgraph ide1 [Cloudflare Gateway]&#10;    direction TB&#10;    B(DNS policies)-.-&gt;C((DNS resolver))&#10;end&#10;C --&gt; D[(Nameservers)]&#10;</code></pre>
<pre tabindex="0"><code class="language-mermaid">flowchart TD&#10;accTitle: DNS filtering logic&#10;A[Blocked by DNS policy?] --Yes --&gt; B[Block page is configured?] --Yes--&gt; C[Return IP of block page]&#10;B--No--&gt;E[Return 0.0.0.0]&#10;A --No --&gt; D[Return IP of www.example.com]&#10;</code></pre>
<h2 id="dns-filtering-vs-secure-web-gateway">DNS filtering vs. Secure Web Gateway</h2>
<p>A URL assumes the form: <code>protocol://subdomain.domain.tld:port/path?query</code></p>
<p>DNS filtering only applies to the hostname — <code>subdomain.domain.tld</code>. You cannot block specific protocols, ports, paths, or query types. Additionally, users can bypass DNS policies if they already know the IP address of the website, or by connecting through a Virtual Private Network (VPN) or proxy server.</p>
<p>Secure Web Gateways (SWGs) offer a greater set of capabilities, including:</p>
<ul>
<li><a href="https://www.cloudflare.com/learning/access-management/what-is-url-filtering/">URL filtering</a> to block specific paths and queries</li>
<li>L4 firewalls to block ports and protocols</li>
<li>Antivirus scanning</li>
<li><a href="https://www.cloudflare.com/learning/access-management/what-is-dlp/">Data loss prevention</a></li>
<li><a href="https://www.cloudflare.com/learning/access-management/what-is-browser-isolation/">Browser isolation</a></li>
</ul>
<p>However, this can make SWGs more complex to deploy. Therefore, many organizations will start with DNS filtering as an initial layer of defense against Internet threats.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li>For more background information on DNS filtering, refer to our <a href="https://www.cloudflare.com/learning/access-management/what-is-dns-filtering/">Learning Center</a>.</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<p>In the remaining modules, you will learn how to set up DNS filtering on your devices using Cloudflare Gateway.</p>

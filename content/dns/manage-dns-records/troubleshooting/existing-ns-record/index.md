---
cp9:
  canonical: https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/existing-ns-record/
  description: Resolve conflicts with existing NS records.
  full_title: Existing NS records block new record creation · Cloudflare DNS docs
  head_html: <title>Existing NS records block new record creation · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Resolve conflicts with existing NS records."><link rel="canonical" href="https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/existing-ns-record/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/existing-ns-record/index.md"><meta property="og:title" content="Existing NS records block new record creation · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Resolve conflicts with existing NS records."><meta property="og:url" content="https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/existing-ns-record/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/existing-ns-record/#page","headline":"Existing NS records block new record creation \u00b7 Cloudflare DNS docs","description":"Resolve conflicts with existing NS records.","url":"https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/existing-ns-record/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/manage-dns-records/troubleshooting/existing-ns-record/
  schema: 1
---
<p>As you try to create a new DNS record, Cloudflare displays the following error:</p>
<pre tabindex="0"><code class="language-txt">NS records with that host already exist. (Code:81056)&#10;</code></pre>
<h2 id="causes">Causes</h2>
<p>When a child domain (<code>blog.example.com</code>) of your domain (<code>example.com</code>) has been set up as a separate <a href="/dns/zone-setups/subdomain-setup/">subdomain zone</a>, corresponding <code>NS</code> records must have been placed within the parent zone.</p>
<p>When you are managing DNS records for the parent zone (in this example, <code>example.com</code>), you cannot create IP address resolution records (<code>A</code>, <code>AAAA</code>, or <code>CNAME</code>) with a name that specifies the same subdomain that already exists as a separate subdomain zone.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@input("content/.markup/bodies/7768.md")
</div>
<h2 id="solution">Solution</h2>
<p>Before creating such records, remove any <code>NS</code> records with the same name.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/7767.md")
</aside>

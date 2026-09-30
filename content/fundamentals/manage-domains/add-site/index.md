---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/manage-domains/add-site/
  description: Learn how to onboard your domain to Cloudflare, to speed up and protect your website or application.
  full_title: Onboard a domain · Cloudflare Fundamentals docs
  head_html: <title>Onboard a domain · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to onboard your domain to Cloudflare, to speed up and protect your website or application."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/manage-domains/add-site/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/manage-domains/add-site/index.md"><meta property="og:title" content="Onboard a domain · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to onboard your domain to Cloudflare, to speed up and protect your website or application."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/manage-domains/add-site/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/manage-domains/add-site/#page","headline":"Onboard a domain \u00b7 Cloudflare Fundamentals docs","description":"Learn how to onboard your domain to Cloudflare, to speed up and protect your website or application.","url":"https://developers.cloudflare.com/fundamentals/manage-domains/add-site/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/manage-domains/add-site/
  schema: 1
---
<p>After you onboard your domain, Cloudflare will act as the <a href="/fundamentals/concepts/how-cloudflare-works/#cloudflare-as-a-reverse-proxy">reverse proxy</a> and <a href="/fundamentals/concepts/how-cloudflare-works/#cloudflare-as-a-dns-provider">DNS provider</a> for your site.</p>
<p>This guide applies to existing domains that were purchased from another provider, and will use a <a href="/dns/zone-setups/full-setup">full DNS setup</a>, which is the most common configuration. To set this up, you will have to complete a few steps at Cloudflare, but also update some settings at your domain registrar<sup><a href="#footnote-1">1</a></sup>, and at your previous DNS provider (if you were using one).</p>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="cloudflare-registrar">Cloudflare Registrar</h3>
@markup("md", "content/.markup/bodies/8914.md")
</aside>
<h2 id="1-add-your-domain"><ol>
<li>Add your domain</li>
</ol></h2>
<ol>
<li>Log in to the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Onboard a domain</strong>.</li>
<li>Enter your website's <span class="nb-glossary-tooltip" title="apex domain">apex domain</span> (for example, <code>example.com</code>), choose how you would like to add your DNS records, and select <strong>Continue</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8913.md")
</aside>
<ol start="4">
<li>Select a <a href="https://www.cloudflare.com/plans/#compare-features">plan</a>.</li>
</ol>
<h2 id="2-review-dns-records"><ol start="2">
<li>Review DNS records</li>
</ol></h2>
<p>Your DNS records must be accurate for your domain to work properly. If you don't know what DNS records are, consider the video below for a quick explanation.</p>
<div class="video-frame"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/07e42365d5c40f2a46a6bde2844f370f/iframe?preload=true&amp;letterboxColor=transparent&amp;poster=https%3A%2F%2Fimagedelivery.net%2FxDOJvHcv1KwTQn6S-BGFIw%2F7e8cdb06-7280-4139-8f13-256e03027f00%2Fpublic" title="Review your DNS records" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<ol>
<li></li>
</ol>
<p>Since the quick scan is not guaranteed to find all existing DNS records, you need to review your records, paying special attention to the following:</p>
<ul>
<li>
<p><a href="/dns/manage-dns-records/how-to/create-zone-apex/">Zone apex records (<code>example.com</code>)</a></p>
  <details class="nb-details"><summary>More about zone apex records</summary><div class="nb-details-body">
</li>
</ul>
@markup("md", "content/.markup/bodies/8916.md")
</div></details>
<ul>
<li>
<p><a href="/dns/manage-dns-records/how-to/create-subdomain/">Subdomain records (<code>www.example.com</code> or <code>blog.example.com</code>)</a></p>
<details class="nb-details"><summary>More about subdomain records</summary><div class="nb-details-body">
</li>
</ul>
@markup("md", "content/.markup/bodies/8917.md")
</div></details>
<ul>
<li>
<p><a href="/dns/manage-dns-records/how-to/email-records/">Email records</a></p>
<details class="nb-details"><summary>More about email records</summary><div class="nb-details-body">
</li>
</ul>
@markup("md", "content/.markup/bodies/8918.md")
</div></details>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8912.md")
</aside>
<ol start="2">
<li>
<p>If you find any missing records, <a href="/dns/manage-dns-records/how-to/create-dns-records/">manually add</a> those records.</p>
</li>
<li>
<p>Depending on your site setup, you may want to adjust the <span class="nb-glossary-tooltip" title="proxy status">proxy status</span> for certain <code>A</code>, <code>AAAA</code>, or <code>CNAME</code> records. Each record has a proxy status toggle:</p>
<ul>
<li><strong>Proxied</strong> (orange cloud): web traffic goes through the Cloudflare network, which provides caching, DDoS protection, and other security features.</li>
<li><strong>DNS only</strong> (gray cloud): Cloudflare returns the DNS record value but does not proxy traffic. Use this for CNAME records that verify your domain for third-party services.</li>
</ul>
</li>
<li>
<p>Select <strong>Continue</strong>.</p>
</li>
</ol>
<h2 id="3-update-nameservers"><ol start="3">
<li>Update nameservers</li>
</ol></h2>
<p>Your domain will be assigned two authoritative Cloudflare nameservers. Nameservers are specialized servers that store your domain's DNS records and &quot;answer&quot; requests from browsers by providing the specific IP address needed to connect to your website.</p>
<p>Usually, you need to add these nameservers at your registrar. Refer to <a href="/dns/nameservers/update-nameservers/">Update nameservers</a> for more information.</p>
<details class="nb-details" open><summary>Provider-specific instructions</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/8920.md")
</div></details>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="dnssec">DNSSEC</h3>
@markup("md", "content/.markup/bodies/8911.md")
</aside>
<h2 id="4-complete-ssl-tls-setup"><ol start="4">
<li>Complete SSL/TLS setup</li>
</ol></h2>
<p>To prevent insecure connections and visitor browser errors, review your <a href="/ssl/get-started/">SSL/TLS certificates</a>. Many Cloudflare services will automatically protect and speed up your web traffic after your nameservers are updated and your DNS records are proxied. For further guidance, refer to <a href="/dns/proxy-status/">Proxy status</a>.</p>
<p>If you encounter unexpected results when changing your nameservers, refer to the <a href="/dns/zone-setups/full-setup/troubleshooting/">DNS Full Setup troubleshooting</a>.</p>
<h2 id="further-options">Further options</h2>
<h3 id="other-dns-setups">Other DNS setups</h3>
- To use Cloudflare as a reverse proxy but maintain your DNS provider, refer to [partial setup](/dns/zone-setups/partial-setup/).
- To use one or more DNS providers, refer to [DNS Zone transfers](/dns/zone-setups/zone-transfers/).
- Enterprise customers can onboard lower-level subdomains using [Subdomain setup](/dns/zone-setups/subdomain-setup/).
<h3 id="minimize-downtime">Minimize downtime</h3>
<ul>
<li></li>
</ul>
<p>If your domain is particularly sensitive to downtime, review our suggestions to <a href="/fundamentals/performance/minimize-downtime/">minimize downtime</a>.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">The provider you purchased your domain from</li>
<li id="footnote-2">Enterprise customers can onboard these using [Subdomain setup](/dns/zone-setups/subdomain-setup/).</li>
<li id="footnote-3">A security feature that protects DNS records from spoofing</li></ol></section>

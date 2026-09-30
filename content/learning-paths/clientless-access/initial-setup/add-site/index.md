---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/clientless-access/initial-setup/add-site/
  description: Add your domain to Cloudflare DNS.
  full_title: Add a site · Cloudflare Learning Paths
  head_html: <title>Add a site · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Add your domain to Cloudflare DNS."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/clientless-access/initial-setup/add-site/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/clientless-access/initial-setup/add-site/index.md"><meta property="og:title" content="Add a site · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Add your domain to Cloudflare DNS."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/clientless-access/initial-setup/add-site/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Access,Cloudflare Tunnel,Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/learning-paths/clientless-access/initial-setup/add-site/#page","headline":"Add a site \u00b7 Cloudflare Learning Paths","description":"Add your domain to Cloudflare DNS.","url":"https://developers.cloudflare.com/learning-paths/clientless-access/initial-setup/add-site/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/clientless-access/initial-setup/add-site/
  schema: 1
---
<p>In clientless access deployments, users connect to internal applications via public hostnames. You will need to own a domain, add it to Cloudflare, and configure Cloudflare as the <a href="/dns/zone-setups/full-setup/setup/#34-update-your-registrar">authoritative DNS provider</a> for that domain. Enterprise customers who cannot change their authoritative DNS provider have the option to configure a <a href="/dns/zone-setups/partial-setup/">CNAME setup</a>.</p>
<p>You only need to add one domain to Cloudflare, since you can create an infinite number of subdomains to manage all of your private applications.</p>
<h2 id="add-a-site-to-cloudflare">Add a site to Cloudflare</h2>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/login">Cloudflare dashboard</a>.</li>
<li>Select <strong>Onboard a domain</strong>.</li>
<li>Enter your website's apex domain (<code>example.com</code>).</li>
<li>Select a <a href="https://www.cloudflare.com/plans/#compare-features">plan</a> for this website. Everything you need to do with the domain in Cloudflare Zero Trust is available on the <strong>Free</strong> plan.</li>
<li>Select <strong>Continue</strong>. Cloudflare will scan your website for any configured DNS records.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9673.md")
</aside>
<ol start="5">
<li>
<p>Review your DNS records and select <strong>Continue</strong>.</p>
</li>
<li>
<p>Before your domain can begin using Cloudflare for DNS resolution, you need to <a href="/dns/nameservers/update-nameservers/">add these nameservers</a> at your registrar. Make sure <a href="/dns/dnssec/">DNSSEC</a> is turned off before proceeding.</p>
<details class="nb-details"><summary>Provider-specific instructions</summary><div class="nb-details-body">
</li>
</ol>
@markup("md", "content/.markup/bodies/9674.md")
</div></details>
<p>If you cannot change your domain nameservers, you can still use Cloudflare on your website by activating Cloudflare through a <a href="https://www.cloudflare.com/en-gb/partners/technology-partners/">certified hosting partner</a>.</p>
<ol start="7">
<li>(Optional) Follow the <strong>Quick Start Guide</strong> to configure security and performance settings.</li>
</ol>
<p>Registrars can take up to 24 hours to process nameserver changes. Your domain must be in an <strong>Active</strong> status before you can use it for clientless access.</p>

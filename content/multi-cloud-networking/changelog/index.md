---
cp9:
  canonical: https://developers.cloudflare.com/multi-cloud-networking/changelog/
  description: Review recent changes to Cloudflare One Multi-Cloud Networking (formerly Magic Cloud Networking) (beta).
  full_title: Changelog · Cloudflare Multi-Cloud Networking docs
  head_html: <title>Changelog · Cloudflare Multi-Cloud Networking docs</title><meta name="generator" content="Nift"><meta name="description" content="Review recent changes to Cloudflare One Multi-Cloud Networking (formerly Magic Cloud Networking) (beta)."><link rel="canonical" href="https://developers.cloudflare.com/multi-cloud-networking/changelog/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/multi-cloud-networking/changelog/index.md"><link rel="alternate" type="application/rss+xml" href="https://developers.cloudflare.com/multi-cloud-networking/changelog/index.xml"><meta property="og:title" content="Changelog · Cloudflare Multi-Cloud Networking docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review recent changes to Cloudflare One Multi-Cloud Networking (formerly Magic Cloud Networking) (beta)."><meta property="og:url" content="https://developers.cloudflare.com/multi-cloud-networking/changelog/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_product" content="Multi-Cloud Networking"><meta name="algolia_product_filter" content="Multi-Cloud Networking"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Changelog"><meta name="algolia_content_type" content="Changelog"><meta name="pcx_additional_products" content="Multi-Cloud Networking"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/multi-cloud-networking/changelog/#page","headline":"Changelog \u00b7 Cloudflare Multi-Cloud Networking docs","description":"Review recent changes to Cloudflare One Multi-Cloud Networking (formerly Magic Cloud Networking) (beta).","url":"https://developers.cloudflare.com/multi-cloud-networking/changelog/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /multi-cloud-networking/changelog/
  schema: 1
---
<h2 id="2024-12-05">2024-12-05</h2>

<strong>Generate customized terraform files for building cloud network on-ramps</strong>

<p>You can now generate customized terraform files for building cloud network on-ramps to <a href="/cloudflare-wan/">Magic WAN</a>.</p>
<p><a href="/multi-cloud-networking/">Magic Cloud</a> can scan and discover existing network resources and generate the required terraform files to automate cloud resource deployment using their existing infrastructure-as-code workflows for cloud automation.</p>
<p>You might want to do this to:</p>
<ul>
<li>Review the proposed configuration for an on-ramp before deploying it with Cloudflare.</li>
<li>Deploy the on-ramp using your own infrastructure-as-code pipeline instead of deploying it with Cloudflare.</li>
</ul>
<p>For more details, refer to <a href="/multi-cloud-networking/cloud-on-ramps/#set-up-with-terraform">Set up with Terraform</a>.</p>


<h2 id="2024-11-21">2024-11-21</h2>
<p><strong>Import cloud resources for VMs and LBs</strong></p>
<p>Cloud network discovery now includes cloud native virtual machine (VM) and load-balancer (LB) resources.</p>
<h2 id="2024-11-21-1">2024-11-21</h2>
<p><strong>Export resource catalog</strong></p>
<p>Customers can export their resource catalog including all discovered resource metadata to a downloadable JSON file, suitable for offline analysis.</p>
<h2 id="2024-10-01">2024-10-01</h2>
<p><strong>Cost visibility for managed cloud configuration</strong></p>
<p>Customers can now see the cloud provider list price of discovered network resources and will be informed of total cost and delta cost when deploying managed configuration.</p>
<h2 id="2024-08-14">2024-08-14</h2>
<p><strong>GCP on-ramps</strong></p>
<p>Magic Cloud Networking supports Google Cloud Platform.</p>
<h2 id="2024-07-01">2024-07-01</h2>
<p><strong>Closed beta launch</strong></p>
<p>The Magic Cloud Networking closed beta release is available, with the managed cloud on-ramps feature.</p>



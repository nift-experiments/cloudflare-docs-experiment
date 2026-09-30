---
cp9:
  canonical: https://developers.cloudflare.com/terraform/tutorial/
  description: Step-by-step Cloudflare Terraform tutorials from initialization to advanced configuration.
  full_title: Tutorials · Cloudflare Terraform docs
  head_html: <title>Tutorials · Cloudflare Terraform docs</title><meta name="generator" content="Nift"><meta name="description" content="Step-by-step Cloudflare Terraform tutorials from initialization to advanced configuration."><link rel="canonical" href="https://developers.cloudflare.com/terraform/tutorial/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/terraform/tutorial/index.md"><meta property="og:title" content="Tutorials · Cloudflare Terraform docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Step-by-step Cloudflare Terraform tutorials from initialization to advanced configuration."><meta property="og:url" content="https://developers.cloudflare.com/terraform/tutorial/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Terraform"><meta name="algolia_product_filter" content="Terraform"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Terraform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/terraform/tutorial/#page","headline":"Tutorials \u00b7 Cloudflare Terraform docs","description":"Step-by-step Cloudflare Terraform tutorials from initialization to advanced configuration.","url":"https://developers.cloudflare.com/terraform/tutorial/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /terraform/tutorial/
  schema: 1
---
<p>Before you begin, <a href="/terraform/installing/">install Terraform</a>. Each tutorial builds on the previous, so you should complete the tutorials in the order shown below.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14760.md")
</aside>
<h2 id="1-initialize-terraform-terraform-tutorial-initialize-terraform"><a href="/terraform/tutorial/initialize-terraform/">1 – Initialize Terraform</a></h2>
<ul>
<li>Brief introduction.</li>
<li>Introduction of <code>terraform init</code>, <code>plan</code>, <code>apply</code>, and <code>show</code>.</li>
<li>Resource covered: <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/dns_record"><code>cloudflare_dns_record</code></a> (DNS record).</li>
</ul>
<h2 id="2-track-your-history-terraform-tutorial-track-history"><a href="/terraform/tutorial/track-history/">2 – Track your history</a></h2>
<ul>
<li>Store Cloudflare configuration in source control.</li>
</ul>
<h2 id="3-configure-https-settings-terraform-tutorial-configure-https-settings"><a href="/terraform/tutorial/configure-https-settings/">3 – Configure HTTPS settings</a></h2>
<ul>
<li>Modify zone settings.</li>
<li>Resource covered: <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zone_setting"><code>cloudflare_zone_setting</code></a>.</li>
</ul>
<h2 id="4-improve-performance-and-reliability-terraform-tutorial-use-load-balancing"><a href="/terraform/tutorial/use-load-balancing/">4 – Improve performance and reliability</a></h2>
<ul>
<li>Add load balancing rules.</li>
<li>Resources covered:
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/load_balancer"><code>cloudflare_load_balancer</code></a></li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/load_balancer_pool"><code>cloudflare_load_balancer_pool</code></a></li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/load_balancer_monitor"><code>cloudflare_load_balancer_monitor</code></a></li>
</ul>
</li>
</ul>
<h2 id="5-add-exceptions-with-page-rules-terraform-tutorial-add-page-rules"><a href="/terraform/tutorial/add-page-rules/">5 – Add exceptions with page rules</a></h2>
<ul>
<li>Add page rule.</li>
<li>Resource covered: <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/page_rule"><code>cloudflare_page_rule</code></a>.</li>
<li>Increase security level for a specific URL: <code>/expensive-db-call</code>.</li>
<li>Add a redirect (URL forward) with a <code>301</code> status code from <code>/old-location.php</code> to <code>/expensive-db-call</code>.</li>
</ul>
<h2 id="6-revert-configuration-terraform-tutorial-revert-configuration"><a href="/terraform/tutorial/revert-configuration/">6 – Revert configuration</a></h2>
<ul>
<li>Review change history.</li>
<li>Roll back changes.</li>
</ul>

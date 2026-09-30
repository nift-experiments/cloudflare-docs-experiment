---
cp9:
  canonical: https://developers.cloudflare.com/terraform/how-to/create-secondary-zone/
  description: Automate the setup of a Cloudflare subdomain zone for Enterprise accounts using Terraform.
  full_title: Create a subdomain zone using Terraform · Cloudflare Terraform docs
  head_html: <title>Create a subdomain zone using Terraform · Cloudflare Terraform docs</title><meta name="generator" content="Nift"><meta name="description" content="Automate the setup of a Cloudflare subdomain zone for Enterprise accounts using Terraform."><link rel="canonical" href="https://developers.cloudflare.com/terraform/how-to/create-secondary-zone/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/terraform/how-to/create-secondary-zone/index.md"><meta property="og:title" content="Create a subdomain zone using Terraform · Cloudflare Terraform docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Automate the setup of a Cloudflare subdomain zone for Enterprise accounts using Terraform."><meta property="og:url" content="https://developers.cloudflare.com/terraform/how-to/create-secondary-zone/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Terraform"><meta name="algolia_product_filter" content="Terraform"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Terraform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/terraform/how-to/create-secondary-zone/#page","headline":"Create a subdomain zone using Terraform \u00b7 Cloudflare Terraform docs","description":"Automate the setup of a Cloudflare subdomain zone for Enterprise accounts using Terraform.","url":"https://developers.cloudflare.com/terraform/how-to/create-secondary-zone/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /terraform/how-to/create-secondary-zone/
  schema: 1
---
<p>A <a href="/dns/zone-setups/subdomain-setup/">subdomain zone</a> lets you manage a subdomain in a separate Cloudflare zone from the parent domain. This is useful for access control and team management. This guide shows how to automate the setup using the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Cloudflare Terraform provider</a>. It is only available for Enterprise accounts</p>
<blockquote>
<p>NOTE: subdomain setup is only available for Enterprise accounts</p>
</blockquote>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Terraform installed. Refer to <a href="/terraform/installing/">Get started</a>.</li>
<li>Your Cloudflare account ID and a configured provider block. Refer to <a href="/terraform/tutorial/initialize-terraform/">Initialize Terraform</a>.</li>
</ul>
<h2 id="create-the-zone">Create the zone</h2>
<p>Create a <code>cloudflare_zone</code> resource for the subdomain zone. The following example creates a zone for <code>subdomain.example.com</code>:</p>
<pre tabindex="0"><code class="language-hcl">resource &quot;cloudflare_zone&quot; &quot;subdomain_example_com&quot; {&#10;  account = {&#10;    id = var.cloudflare_account_id&#10;  }&#10;  name = &quot;subdomain.example.com&quot;&#10;  type = &quot;full&quot;&#10;}&#10;</code></pre>
<p>Terraform creates the zone in a <strong>Pending</strong> state. You must add NS delegation records to the parent zone before Cloudflare activates it.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14763.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/dns/zone-setups/subdomain-setup/">Subdomain setup</a></li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zone"><code>cloudflare_zone</code> resource</a></li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/dns_record"><code>cloudflare_dns_record</code> resource</a></li>
</ul>

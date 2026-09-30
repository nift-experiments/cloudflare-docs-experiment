---
cp9:
  canonical: https://developers.cloudflare.com/terraform/how-to/create-partial-zone/
  description: Automate the setup of a Cloudflare partial (CNAME) zone using the Terraform provider.
  full_title: Create a partial zone using Terraform · Cloudflare Terraform docs
  head_html: <title>Create a partial zone using Terraform · Cloudflare Terraform docs</title><meta name="generator" content="Nift"><meta name="description" content="Automate the setup of a Cloudflare partial (CNAME) zone using the Terraform provider."><link rel="canonical" href="https://developers.cloudflare.com/terraform/how-to/create-partial-zone/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/terraform/how-to/create-partial-zone/index.md"><meta property="og:title" content="Create a partial zone using Terraform · Cloudflare Terraform docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Automate the setup of a Cloudflare partial (CNAME) zone using the Terraform provider."><meta property="og:url" content="https://developers.cloudflare.com/terraform/how-to/create-partial-zone/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Terraform"><meta name="algolia_product_filter" content="Terraform"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Terraform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/terraform/how-to/create-partial-zone/#page","headline":"Create a partial zone using Terraform \u00b7 Cloudflare Terraform docs","description":"Automate the setup of a Cloudflare partial (CNAME) zone using the Terraform provider.","url":"https://developers.cloudflare.com/terraform/how-to/create-partial-zone/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /terraform/how-to/create-partial-zone/
  schema: 1
---
<p>A <a href="/dns/zone-setups/partial-setup/">partial zone</a> lets you use Cloudflare for a subdomain while keeping your existing authoritative DNS provider for the parent domain. This guide shows how to automate the setup using the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Cloudflare Terraform provider</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14765.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Terraform installed. Refer to <a href="/terraform/installing/">Get started</a>.</li>
<li>Your Cloudflare account ID and a configured provider block. Refer to <a href="/terraform/tutorial/initialize-terraform/">Initialize Terraform</a>.</li>
</ul>
<h2 id="create-the-zone">Create the zone</h2>
<p>Add the zone configuration and apply the change to create the zone:</p>
<pre tabindex="0"><code class="language-hcl">resource &quot;cloudflare_zone&quot; &quot;subdomain_example_com&quot; {&#10;  account = {&#10;    id = var.cloudflare_account_id&#10;  }&#10;  name = &quot;subdomain.example.com&quot;&#10;}&#10;</code></pre>
<p>Then, in a new Terraform plan and apply cycle, upgrade the zone to a Business plan or higher:</p>
<pre tabindex="0"><code class="language-hcl">resource &quot;cloudflare_zone_subscription&quot; &quot;example_zone_subscription&quot; {&#10;  zone_id = cloudflare_zone.subdomain_example_com.id&#10;  frequency = &quot;monthly&quot;&#10;  rate_plan = {&#10;    id = &quot;business&quot;&#10;    currency = &quot;USD&quot;&#10;  }&#10;}&#10;</code></pre>
<p>Then, again in a new Terraform plan and apply cycle, update your Terraform configuration to add <code>type = &quot;partial&quot;</code> to the zone:</p>
<pre tabindex="0"><code class="language-hcl">resource &quot;cloudflare_zone&quot; &quot;subdomain_example_com&quot; {&#10;  account = {&#10;    id = var.cloudflare_account_id&#10;  }&#10;  name = &quot;subdomain.example.com&quot;&#10;  type = &quot;partial&quot;&#10;}&#10;</code></pre>
<p>Terraform places the zone in a <strong>Pending</strong> state. You must add the necessary DNS records and verify domain ownership before Cloudflare activates it.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14764.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/dns/zone-setups/partial-setup/">Partial zone setup</a></li>
<li><a href="/dns/zone-setups/conversions/convert-full-to-partial/">Convert a full zone to partial</a></li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zone"><code>cloudflare_zone</code> resource</a></li>
</ul>

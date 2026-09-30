---
cp9:
  canonical: https://developers.cloudflare.com/rules/origin-rules/tutorials/point-to-pages-with-custom-domain/
  description: This tutorial will instruct you how to configure an origin rule and a DNS record to point to a Pages deployment with a custom domain.
  full_title: Point to Pages with a custom domain · Cloudflare Rules docs
  head_html: <title>Point to Pages with a custom domain · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="This tutorial will instruct you how to configure an origin rule and a DNS record to point to a Pages deployment with a custom domain."><link rel="canonical" href="https://developers.cloudflare.com/rules/origin-rules/tutorials/point-to-pages-with-custom-domain/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/origin-rules/tutorials/point-to-pages-with-custom-domain/index.md"><meta property="og:title" content="Point to Pages with a custom domain · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This tutorial will instruct you how to configure an origin rule and a DNS record to point to a Pages deployment with a custom domain."><meta property="og:url" content="https://developers.cloudflare.com/rules/origin-rules/tutorials/point-to-pages-with-custom-domain/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Pages,Origin Rules"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/origin-rules/tutorials/point-to-pages-with-custom-domain/#page","headline":"Point to Pages with a custom domain \u00b7 Cloudflare Rules docs","description":"This tutorial will instruct you how to configure an origin rule and a DNS record to point to a Pages deployment with a custom domain.","url":"https://developers.cloudflare.com/rules/origin-rules/tutorials/point-to-pages-with-custom-domain/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /rules/origin-rules/tutorials/point-to-pages-with-custom-domain/
  schema: 1
---
<p>This tutorial will instruct you how to configure an origin rule and a DNS record to point to a Pages deployment with a custom domain.</p>
<p>The procedure will use the following example values:</p>
<table>
<thead>
<tr>
<th align="right"></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td align="right">URL that website visitors will access</td>
<td><code>mycustomerexample.com/blog/*</code></td>
</tr>
<tr>
<td align="right">Zone domain</td>
<td><code>mycustomerexample.com</code></td>
</tr>
<tr>
<td align="right">Cloudflare Pages subdomain</td>
<td><code>myblog.pages.dev</code></td>
</tr>
<tr>
<td align="right">Cloudflare Pages custom domain</td>
<td><code>blogmirror.example.com</code></td>
</tr>
</tbody>
</table>
<p>When configuring your Pages custom domain, use a custom domain that you do not plan to use in production (<code>blogmirror.example.com</code> in this example).</p>
<h2 id="1-configure-custom-domain-in-your-pages-project"><ol>
<li>Configure custom domain in your Pages project</li>
</ol></h2>
<p>To add the custom domain to your Pages deployment:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13072.md")
</div>
<p>When you add the custom domain to your Pages deployment, Cloudflare automatically creates a <code>CNAME</code> DNS record for the custom domain.</p>
<h2 id="2-create-origin-rule-to-rewrite-host-header-and-override-dns-record"><ol start="2">
<li>Create origin rule to rewrite host header and override DNS record</li>
</ol></h2>
<p>In your <code>mycustomerexample.com</code> zone, create an origin rule with the following configuration:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13073.md")
</div>
<h2 id="3-optional-configure-url-rewrite"><ol start="3">
<li>(Optional) Configure URL rewrite</li>
</ol></h2>
<p>In this example, the URL that website visitors will access starts with <code>/blog</code>. However, the Pages deployment does not have this initial URL segment.</p>
<p>Use a URL rewrite to remove the <code>/blog</code> segment from the URL path.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13074.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13071.md")
</aside>
<h2 id="more-resources">More resources</h2>
<ul>
<li><a href="/rules/origin-rules/tutorials/change-uri-path-and-host-header/">Tutorial: Change URI Path and Host Header</a></li>
<li><a href="/pages/configuration/custom-domains/">Cloudflare Pages: Custom domains</a></li>
<li><a href="/dns/manage-dns-records/">DNS records</a></li>
</ul>

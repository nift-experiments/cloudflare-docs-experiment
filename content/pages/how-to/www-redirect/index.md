---
cp9:
  canonical: https://developers.cloudflare.com/pages/how-to/www-redirect/
  description: Redirect a www subdomain to your apex domain on Cloudflare Pages using Bulk Redirects.
  full_title: Redirecting www to domain apex · Cloudflare Pages docs
  head_html: <title>Redirecting www to domain apex · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Redirect a www subdomain to your apex domain on Cloudflare Pages using Bulk Redirects."><link rel="canonical" href="https://developers.cloudflare.com/pages/how-to/www-redirect/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/how-to/www-redirect/index.md"><meta property="og:title" content="Redirecting www to domain apex · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Redirect a www subdomain to your apex domain on Cloudflare Pages using Bulk Redirects."><meta property="og:url" content="https://developers.cloudflare.com/pages/how-to/www-redirect/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/how-to/www-redirect/#page","headline":"Redirecting www to domain apex \u00b7 Cloudflare Pages docs","description":"Redirect a www subdomain to your apex domain on Cloudflare Pages using Bulk Redirects.","url":"https://developers.cloudflare.com/pages/how-to/www-redirect/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/how-to/www-redirect/
  schema: 1
---
<p>Learn how to redirect a <code>www</code> subdomain to your apex domain (<code>example.com</code>).</p>
<p>This setup assumes that you already have a <a href="/pages/configuration/custom-domains/">custom domain</a> attached to your Pages project.</p>
<h2 id="setup">Setup</h2>
<p>To redirect your <code>www</code> subdomain to your domain apex:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Bulk Redirects</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. [Create a bulk redirect list](/rules/url-forwarding/bulk-redirects/create-dashboard/#1-create-a-bulk-redirect-list) modeled after the following (but replacing the values as appropriate):
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@input("content/.markup/bodies/10884.md")
</div>
<ol start="4">
<li><a href="/rules/url-forwarding/bulk-redirects/create-dashboard/#2-create-a-bulk-redirect-rule">Create a bulk redirect rule</a> using the list you just created.</li>
<li>Go to <strong>DNS</strong>.</li>
<li><a href="/dns/manage-dns-records/how-to/create-dns-records/#create-dns-records">Create a DNS record</a> for the <code>www</code> subdomain using the following values:</li>
</ol>
<div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@input("content/.markup/bodies/10885.md")
</div>
<p>It may take a moment for this DNS change to propagate, but once complete, you can run the following command in your terminal.</p>
<pre tabindex="0"><code class="language-sh">curl --head -i https://www.example.com/&#10;</code></pre>
<p>Then, inspect the output to verify that the <code>location</code> header and status code are being set as configured.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/pages/how-to/redirect-to-custom-domain/">Redirect <code>*.pages.dev</code> to a custom domain</a></li>
<li><a href="/rules/url-forwarding/bulk-redirects/">Handle redirects with Bulk Redirects</a></li>
</ul>

---
cp9:
  canonical: https://developers.cloudflare.com/pages/how-to/redirect-to-custom-domain/
  description: Use Bulk Redirects to redirect your pages.dev subdomain to a custom domain.
  full_title: Redirecting *.pages.dev to a Custom Domain · Cloudflare Pages docs
  head_html: <title>Redirecting *.pages.dev to a Custom Domain · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Bulk Redirects to redirect your pages.dev subdomain to a custom domain."><link rel="canonical" href="https://developers.cloudflare.com/pages/how-to/redirect-to-custom-domain/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/how-to/redirect-to-custom-domain/index.md"><meta property="og:title" content="Redirecting *.pages.dev to a Custom Domain · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Bulk Redirects to redirect your pages.dev subdomain to a custom domain."><meta property="og:url" content="https://developers.cloudflare.com/pages/how-to/redirect-to-custom-domain/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/how-to/redirect-to-custom-domain/#page","headline":"Redirecting *.pages.dev to a Custom Domain \u00b7 Cloudflare Pages docs","description":"Use Bulk Redirects to redirect your pages.dev subdomain to a custom domain.","url":"https://developers.cloudflare.com/pages/how-to/redirect-to-custom-domain/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/how-to/redirect-to-custom-domain/
  schema: 1
---
<p>Learn how to use <a href="/rules/url-forwarding/bulk-redirects/">Bulk Redirects</a> to redirect your <code>*.pages.dev</code> subdomain to your <a href="/pages/configuration/custom-domains/">custom domain</a>.</p>
<p>You may want to do this to ensure that your site's content is served only on the custom domain, and not the <code>&lt;project&gt;.pages.dev</code> site automatically generated on your first Pages deployment.</p>
<h2 id="setup">Setup</h2>
<p>To redirect a <code>&lt;project&gt;.pages.dev</code> subdomain to your custom domain:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Pages project.
3. Go to **Custom domains** and make sure that your custom domain is listed. If it is not, add it by clicking **Set up a custom domain**.
4. Go **Bulk Redirects**.
5. [Create a bulk redirect list](/rules/url-forwarding/bulk-redirects/create-dashboard/#1-create-a-bulk-redirect-list) modeled after the following (but replacing the values as appropriate):
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@input("content/.markup/bodies/10891.md")
</div>
<ol start="6">
<li><a href="/rules/url-forwarding/bulk-redirects/create-dashboard/#2-create-a-bulk-redirect-rule">Create a bulk redirect rule</a> using the list you just created.</li>
</ol>
<p>To test that your redirect worked, go to your <code>&lt;project&gt;.pages.dev</code> domain. If the URL is now set to your custom domain, then the rule has propagated.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/pages/how-to/www-redirect/">Redirect www to domain apex</a></li>
<li><a href="/rules/url-forwarding/bulk-redirects/">Handle redirects with Bulk Redirects</a></li>
</ul>

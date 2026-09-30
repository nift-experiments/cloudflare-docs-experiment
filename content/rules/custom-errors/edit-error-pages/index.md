---
cp9:
  canonical: https://developers.cloudflare.com/rules/custom-errors/edit-error-pages/
  description: Edit and customize the HTML content of error pages.
  full_title: Edit Error Pages · Cloudflare Rules docs
  head_html: <title>Edit Error Pages · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Edit and customize the HTML content of error pages."><link rel="canonical" href="https://developers.cloudflare.com/rules/custom-errors/edit-error-pages/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/custom-errors/edit-error-pages/index.md"><meta property="og:title" content="Edit Error Pages · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Edit and customize the HTML content of error pages."><meta property="og:url" content="https://developers.cloudflare.com/rules/custom-errors/edit-error-pages/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Rules"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/custom-errors/edit-error-pages/#page","headline":"Edit Error Pages \u00b7 Cloudflare Rules docs","description":"Edit and customize the HTML content of error pages.","url":"https://developers.cloudflare.com/rules/custom-errors/edit-error-pages/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /rules/custom-errors/edit-error-pages/
  schema: 1
---
<p>You can define custom <a href="/rules/custom-errors/#error-pages">Error Pages</a> for the following errors and challenges:</p>
<ul>
<li>WAF block</li>
<li>IP/Country block</li>
<li>IP/Country challenge</li>
<li>500 class errors</li>
<li>1000 class errors</li>
<li>Managed challenge / I'm Under Attack Mode</li>
<li>Rate limiting block</li>
</ul>
<p>For more information on the different types of Error Pages, refer to <a href="/rules/custom-errors/reference/error-page-types/">Error page types</a>.</p>
<p>To return custom error responses for requests that match specific conditions, use <a href="/rules/custom-errors/#custom-error-rules">Custom Error Rules</a> instead.</p>
<h2 id="1-design-your-custom-error-page"><ol>
<li>Design your custom error page</li>
</ol></h2>
<p>Before defining a custom error page in your Cloudflare account, you will need to design and code that page. It can be hosted on your own web server or using a Cloudflare product like <a href="/rules/snippets/">Snippets</a>.</p>
<p>When designing your custom error page, you can include page-specific <a href="/rules/custom-errors/reference/error-tokens/">custom error tokens</a>. Each custom error token provides diagnostic information that appears on the error page.</p>
<p>To display a custom page for each error, create a separate page per error. For example, to create a custom error page for both <strong>IP/Country Block</strong> and <strong>WAF block</strong>, you must design and publish two separate pages.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/12991.md")
</aside>
<p>You can use the following template to start building your error page:</p>
<pre tabindex="0"><code class="language-html">&lt;html&gt;&#10;	&lt;head&gt;&lt;/head&gt;&#10;	&lt;body&gt;&#10;		::[REPLACE WITH CUSTOM ERROR TOKEN NAME]::&#10;	&lt;/body&gt;&#10;&lt;/html&gt;&#10;</code></pre>
<details class="nb-details"><summary>Example error page for 5XX errors</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/12992.md")
</div></details>
<hr />
<h2 id="2-update-an-error-page-in-the-dashboard"><ol start="2">
<li>Update an error page in the dashboard</li>
</ol></h2>
<p>You can define an error page at the zone level or for your entire account. Zone-level error pages have priority over account-level error pages.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12997.md")
</div></div>
<h2 id="fetch-custom-error-page-again">Fetch custom error page again</h2>
<p>After successfully setting the content of the custom error page in <strong>Error Pages</strong>, you can remove the page from your origin server.</p>
<p>If in the future, you need to update your custom error page, you must fetch the page again, even if the page URL remains unchanged. In this case, next to the page type you want to update, select the three dots &gt; <strong>Fetch custom page again</strong>.</p>

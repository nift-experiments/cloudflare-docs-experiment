---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/api/get-started/keys/
  description: Retrieve or change your Cloudflare Global API key, a legacy authentication method with full account access.
  full_title: Get Global API key (legacy) · Cloudflare Fundamentals docs
  head_html: <title>Get Global API key (legacy) · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Retrieve or change your Cloudflare Global API key, a legacy authentication method with full account access."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/api/get-started/keys/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/api/get-started/keys/index.md"><meta property="og:title" content="Get Global API key (legacy) · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Retrieve or change your Cloudflare Global API key, a legacy authentication method with full account access."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/api/get-started/keys/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Fundamentals,API documentation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/api/get-started/keys/#page","headline":"Get Global API key (legacy) \u00b7 Cloudflare Fundamentals docs","description":"Retrieve or change your Cloudflare Global API key, a legacy authentication method with full account access.","url":"https://developers.cloudflare.com/fundamentals/api/get-started/keys/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/api/get-started/keys/
  schema: 1
---
<p>Global API key is the previous authorization scheme for interacting with the Cloudflare API. When possible, use <a href="/fundamentals/api/get-started/create-token/">API tokens</a> instead of Global API key.</p>
<p>New and rolled Global API Keys use the <code>cfk_</code> prefixed <a href="/fundamentals/api/get-started/token-formats/">scannable format</a>, which allows credential scanning tools to detect leaked keys.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8999.md")
</aside>
<h2 id="limitations">Limitations</h2>
<p>Global API key has multiple limitations when compared to API tokens:</p>
<ul>
<li>
<p><strong>Access to all Cloudflare resources</strong> - Global API key has access to all of a user's resources. This makes it impossible to safely use Global API key to access non-production resources when a user also has access to production resources.</p>
</li>
<li>
<p><strong>Full permissions</strong> - Similarly, Global API key has the exact same permissions as the user, which means if the user can delete zones or change DNS records, so can the Global API key.</p>
</li>
<li>
<p><strong>Limited to one per user</strong> - Only one Global API key can be provisioned per user. This complicates using Cloudflare's API in production systems where maintaining two secrets for accessing the API is important in the case one needs to be rolled.</p>
</li>
<li>
<p><strong>Lack of advanced limits on usage</strong> - API tokens can be limited to specific time windows and expire or be limited to use from specific IP ranges.</p>
</li>
</ul>
<p>For these reasons, Global API key is not recommended for new customers. Current customers using Global API key are encouraged to migrate and use API tokens instead.</p>
<h2 id="view-your-global-api-key">View your Global API key</h2>
<p>To retrieve your Global API key:</p>
<ol>
<li>In the Cloudflare dashboard and select <strong>User Profile</strong> &gt; <strong>API Tokens</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In the <strong>API Keys</strong> section, click <code>View</code> button of <strong>Global API Key</strong>.</li>
</ol>
<h2 id="change-your-global-api-key">Change your Global API key</h2>
<p>If your API key might be compromised, change your API key:</p>
<ol>
<li>Log in to the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>My Profile</strong> &gt; <strong>API Tokens</strong>.</li>
<li>In the <strong>API Keys</strong> section, find your key.</li>
<li>Select <strong>Change</strong>.</li>
</ol>

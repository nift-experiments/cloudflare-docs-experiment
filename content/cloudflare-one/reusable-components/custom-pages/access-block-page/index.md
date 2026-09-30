---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/reusable-components/custom-pages/access-block-page/
  description: Access custom block pages in Zero Trust.
  full_title: Access custom block pages · Cloudflare One docs
  head_html: <title>Access custom block pages · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Access custom block pages in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/reusable-components/custom-pages/access-block-page/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/reusable-components/custom-pages/access-block-page/index.md"><meta property="og:title" content="Access custom block pages · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Access custom block pages in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/reusable-components/custom-pages/access-block-page/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/reusable-components/custom-pages/access-block-page/#page","headline":"Access custom block pages \u00b7 Cloudflare One docs","description":"Access custom block pages in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/reusable-components/custom-pages/access-block-page/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/reusable-components/custom-pages/access-block-page/
  schema: 1
---
<p>You can customize the block page that displays when users fail to authenticate to an Access application. Each application can have a different block page.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="gateway-block-page">Gateway block page</h3>
@markup("md", "content/.markup/bodies/5905.md")
</aside>
<h2 id="types-of-block-pages">Types of block pages</h2>
<p>Cloudflare Access offers three different block page options:</p>
<ul>
<li><strong>Default</strong>: Displays a Cloudflare branded block page.</li>
<li><strong>Custom Redirect URL</strong> - Redirects blocked requests to the specified URL. For example, you could redirect the user to a <a href="https://github.com/cloudflare/cf-identity-dynamic">dynamic Access Denied page</a> that fetches their identity and shows the exact reason they were blocked.</li>
<li><strong>Custom Page Template</strong> - (Only available on Pay-as-you-go and Enterprise plans) Displays a <a href="/cloudflare-one/reusable-components/custom-pages/access-block-page/#create-a-custom-block-page">custom HTML page</a> hosted by Cloudflare.</li>
</ul>
<h3 id="identity-versus-non-identity">Identity versus non-identity</h3>
<p>You can display a different <a href="/cloudflare-one/reusable-components/custom-pages/access-block-page/#types-of-block-pages">type of block page</a> to users who fail an identity-based policy versus a non-identity policy.</p>
<ul>
<li><strong>Identity failure block page</strong>: Displays when the user is blocked by an identity-based Access policy (such as email, user group, or external evaluation rule), after logging in to their identity provider.</li>
<li><strong>Non-identity failure block page</strong>: Displays when the user is blocked by a non-identity Access policy (such as country, IP, or device posture). Cloudflare checks non-identity attributes before prompting the user to login.</li>
</ul>
<h2 id="create-a-custom-block-page">Create a custom block page</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5904.md")
</aside>
<p>To create a custom block page for Access:</p>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Reusable components</strong> &gt; <strong>Custom pages</strong>.</p>
</li>
<li>
<p>Find the <strong>Access Custom Pages</strong> setting and select <strong>Manage</strong>.</p>
</li>
<li>
<p>Select <strong>Add a page template</strong>.</p>
</li>
<li>
<p>Enter a unique name for the block page.</p>
</li>
<li>
<p>In <strong>Type</strong>, select whether this is an <a href="/cloudflare-one/reusable-components/custom-pages/access-block-page/#identity-versus-non-identity">identity or non-identity block page</a>.</p>
</li>
<li>
<p>In <strong>Custom HTML</strong>, enter the HTML code for your custom page. For example,</p>
</li>
</ol>
<pre tabindex="0"><code class="language-html">&lt;!doctype html&gt;&#10;&lt;html&gt;&#10;	&lt;body&gt;&#10;		&lt;h1&gt;Access denied.&lt;/h1&gt;&#10;&#10;		&lt;p&gt;To obtain access, contact your IT administrator.&lt;/p&gt;&#10;	&lt;/body&gt;&#10;&lt;/html&gt;&#10;</code></pre>
<ol start="7">
<li>
<p>To check the appearance of your custom page, select <strong>Download</strong> and open the HTML file in a browser.</p>
</li>
<li>
<p>Once you are satisfied with your custom page, select <strong>Save</strong>.</p>
</li>
</ol>
<p>You can now select this block page when you <a href="/cloudflare-one/access-controls/applications/http-apps/">configure an Access application</a>.</p>

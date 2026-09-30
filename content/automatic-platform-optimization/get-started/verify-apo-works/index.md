---
cp9:
  canonical: https://developers.cloudflare.com/automatic-platform-optimization/get-started/verify-apo-works/
  description: 'When APO is working, three headers are present: CF-Cache-Status, cf-apo-via,cf-edge-cache. APO works correctly when the headers exactly match the headers below.'
  full_title: Verify APO works · Cloudflare Automatic Platform Optimization docs
  head_html: '<title>Verify APO works · Cloudflare Automatic Platform Optimization docs</title><meta name="generator" content="Nift"><meta name="description" content="When APO is working, three headers are present: CF-Cache-Status, cf-apo-via,cf-edge-cache. APO works correctly when the headers exactly match the headers below."><link rel="canonical" href="https://developers.cloudflare.com/automatic-platform-optimization/get-started/verify-apo-works/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/automatic-platform-optimization/get-started/verify-apo-works/index.md"><meta property="og:title" content="Verify APO works · Cloudflare Automatic Platform Optimization docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="When APO is working, three headers are present: CF-Cache-Status, cf-apo-via,cf-edge-cache. APO works correctly when the headers exactly match the headers below."><meta property="og:url" content="https://developers.cloudflare.com/automatic-platform-optimization/get-started/verify-apo-works/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Automatic Platform Optimization"><meta name="algolia_product_filter" content="Automatic Platform Optimization"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Automatic Platform Optimization"><meta name="pcx_tags" content="WordPress,Headers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/automatic-platform-optimization/get-started/verify-apo-works/#page","headline":"Verify APO works \u00b7 Cloudflare Automatic Platform Optimization docs","description":"When APO is working, three headers are present: CF-Cache-Status, cf-apo-via,cf-edge-cache. APO works correctly when the headers exactly match the headers below.","url":"https://developers.cloudflare.com/automatic-platform-optimization/get-started/verify-apo-works/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["WordPress","Headers"]}</script>'
  markdown: true
  noindex: false
  route: /automatic-platform-optimization/get-started/verify-apo-works/
  schema: 1
---
<p>You can check whether or not APO is working by verifying APO headers are present. When APO is working, three headers are present: <code>CF-Cache-Status</code>, <code>cf-apo-via</code>, <code>cf-edge-cache</code>.</p>
<ol>
<li>Visit <a href="https://www.uptrends.com/tools/http-response-header-check">Uptrends.com</a>.</li>
<li>In the text field, enter the URL for your WordPress homepage including the <code>https://www.</code>.</li>
<li>Select <strong>Start test</strong>. The <strong>Response Headers</strong> table displays.</li>
<li>Locate the three header responses and their description. APO is working correctly when the headers exactly match the headers below.</li>
</ol>
<ul>
<li><code>CF-Cache-Status</code> | <code>HIT</code>
<ul>
<li>The <code>cf-cache-status</code> header displays if the asset is served from the cache or was considered dynamic and served from the origin.</li>
</ul>
</li>
<li><code>cf-apo-via</code> | <code>tcache</code>
<ul>
<li>The <code>cf-apo-via</code> header returns the APO status for the given request.</li>
</ul>
</li>
<li><code>cf-edge-cache</code> | <code>cache, platform=wordpress</code>
<ul>
<li>The <code>cf-edge-cache</code> headers confirms the WordPress plugin is installed and enabled.</li>
</ul>
</li>
</ul>
<p>In a terminal, use the following cURL. Include the <code>'accept: text/html'</code> header so the request is treated as a browser-like HTML request. This makes the test result deterministic. APO can also cache requests that omit the header, depending on the URL path. For more information, refer to <a href="/automatic-platform-optimization/troubleshooting/faq/">FAQ on <code>cf-cache-status</code> results</a>.</p>
<pre tabindex="0"><code class="language-sh">curl -svo /dev/null -A &quot;CF&quot; &#x27;https://example.com/&#x27; -H &#x27;accept: text/html&#x27; 2&gt;&amp;1 | grep &#x27;cf-cache-status\|cf-edge\|cf-apo-via&#x27;&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">&lt; cf-cache-status: HIT&#10;&lt; cf-apo-via: cache&#10;&lt; cf-edge-cache: cache,platform=wordpress&#10;</code></pre>
<p>As always, <code>cf-cache-status</code> displays if the asset hit the cache or was considered dynamic and served from the origin.</p>
<ul>
<li><code>cf-apo-via</code> | <code>tcache</code>
<ul>
<li>The <code>cf-apo-via</code> header returns the APO status for the given request.</li>
</ul>
</li>
<li><code>cf-edge-cache</code> | <code>cache, platform=wordpress</code>
<ul>
<li>The <code>cf-edge-cache</code> headers confirms the WordPress plugin is installed and enabled.</li>
</ul>
</li>
</ul>
<h2 id="verify-the-apo-integration-and-wordpress-integration-work">Verify the APO integration and WordPress integration work</h2>
<p>Open your WordPress site and publish a change. When the integration is working, the page is cached with <code>cf-cache-status: HIT</code> and <code>cf-apo-via: tcache</code>.</p>

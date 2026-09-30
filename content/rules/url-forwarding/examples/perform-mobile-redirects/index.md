---
cp9:
  canonical: https://developers.cloudflare.com/rules/url-forwarding/examples/perform-mobile-redirects/
  description: Create a redirect rule to redirect visitors using mobile devices to a different hostname.
  full_title: Perform mobile redirects · Cloudflare Rules docs
  head_html: <title>Perform mobile redirects · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Create a redirect rule to redirect visitors using mobile devices to a different hostname."><link rel="canonical" href="https://developers.cloudflare.com/rules/url-forwarding/examples/perform-mobile-redirects/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/url-forwarding/examples/perform-mobile-redirects/index.md"><meta property="og:title" content="Perform mobile redirects · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create a redirect rule to redirect visitors using mobile devices to a different hostname."><meta property="og:url" content="https://developers.cloudflare.com/rules/url-forwarding/examples/perform-mobile-redirects/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Redirect Rules"><meta name="pcx_tags" content="Redirects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/url-forwarding/examples/perform-mobile-redirects/#page","headline":"Perform mobile redirects \u00b7 Cloudflare Rules docs","description":"Create a redirect rule to redirect visitors using mobile devices to a different hostname.","url":"https://developers.cloudflare.com/rules/url-forwarding/examples/perform-mobile-redirects/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Redirects"]}</script>
  markdown: true
  noindex: false
  route: /rules/url-forwarding/examples/perform-mobile-redirects/
  schema: 1
---
<p class="article-summary">Create a redirect rule to redirect visitors using mobile devices to a different hostname.</p>
<p>The following examples will redirect visitors using mobile devices — based on the request user agent string — to a different hostname.</p>
<h2 id="redirect-mobile-users-dropping-the-original-uri-path">Redirect mobile users dropping the original URI path</h2>
<p>This example static redirect will redirect requests for the current zone (<code>example.com</code>) from mobile users to <code>m.example.com</code> without preserving the URI path in the original HTTP request.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13206.md")
</div>
<p>Notes about this example:</p>
<ul>
<li>The <code>not http.host in {&quot;m.example.com&quot;}</code> condition prevents redirect loops.</li>
<li>The user agent condition follows <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/User-Agent/Firefox#device-specific_user_agent_strings">Mozilla's recommendation</a> for identifying mobile devices.</li>
<li>The <strong>Then</strong> &gt; <strong>URL</strong> value should be the same as the one you entered in the <code>http.host</code> condition of the rule's filter expression.</li>
<li>You can redirect users to other zones on Cloudflare or to other hostnames not on Cloudflare.</li>
</ul>
<h2 id="redirect-mobile-users-keeping-the-original-path">Redirect mobile users keeping the original path</h2>
<p>This example single redirect will redirect requests for the current zone (<code>example.com</code>) from mobile users to <code>m.example.com</code>, keeping the URI path of the original HTTP request.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@markup("md", "content/.markup/bodies/13207.md")
</div>
<p>Notes about this example:</p>
<ul>
<li>The <code>not http.host in {&quot;m.example.com&quot;}</code> condition prevents redirect loops.</li>
<li>The user agent condition follows <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/User-Agent/Firefox#device-specific_user_agent_strings">Mozilla's recommendation</a> for identifying mobile devices.</li>
<li>The hostname in <strong>Then</strong> &gt; <strong>Expression</strong> should be the same as the one you entered in the <code>http.host</code> condition of the rule's filter expression.</li>
<li>Depending on your use case, you may want to enable <strong>Then</strong> &gt; <strong>Preserve query string</strong> to also keep the query string of the original request.</li>
<li>You can redirect users to other zones on Cloudflare or to other hostnames not on Cloudflare.</li>
</ul>

---
cp9:
  canonical: https://developers.cloudflare.com/rules/reference/troubleshooting/
  description: Review common troubleshooting scenarios for Rules features.
  full_title: Rules troubleshooting · Cloudflare Rules docs
  head_html: <title>Rules troubleshooting · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Review common troubleshooting scenarios for Rules features."><link rel="canonical" href="https://developers.cloudflare.com/rules/reference/troubleshooting/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/reference/troubleshooting/index.md"><meta property="og:title" content="Rules troubleshooting · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review common troubleshooting scenarios for Rules features."><meta property="og:url" content="https://developers.cloudflare.com/rules/reference/troubleshooting/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Rules"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/reference/troubleshooting/#page","headline":"Rules troubleshooting \u00b7 Cloudflare Rules docs","description":"Review common troubleshooting scenarios for Rules features.","url":"https://developers.cloudflare.com/rules/reference/troubleshooting/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /rules/reference/troubleshooting/
  schema: 1
---
<h2 id="interaction-between-redirects-and-other-cloudflare-products">Interaction between redirects and other Cloudflare products</h2>
<p>Your redirects may interfere with Cloudflare products and features such as challenges. Consider excluding the <a href="/fundamentals/reference/cdn-cgi-endpoint/"><code>/cdn-cgi/*</code> URI path</a> in your rule expression to avoid issues. Alternatively, you may exclude only a sub-path such as <code>/cdn-cgi/challenge-platform/*</code> to avoid issues with specific features (in this example, <a href="#interaction-between-cloudflare-challenges-and-rules-features">Cloudflare challenges</a>).</p>
<p>You may also want to exclude the <code>/.well-known/*</code> URL path used by several validation services. Refer to <a href="#interaction-between-redirects-and-verification-procedures-like-http-dcv">Interaction between redirects and verification procedures like HTTP DCV</a> for more information.</p>
<h2 id="interaction-between-cloudflare-challenges-and-rules-features">Interaction between Cloudflare challenges and Rules features</h2>
<p>If you are issuing a <a href="/cloudflare-challenges/">challenge</a> for a given URI path that has one or more Rules features enabled, you should exclude URI paths starting with <code>/cdn-cgi/challenge-platform/</code> in your rule expressions to avoid challenge loops.</p>
<p>For example, define a compound expression for your rule using the <code>and</code> operator and the <a href="/ruleset-engine/rules-language/functions/#starts_with"><code>starts_with()</code></a> function:</p>
<pre tabindex="0"><code class="language-txt">&lt;OTHER_RULE_CONDITIONS&gt; and not starts_with(http.request.uri, &quot;/cdn-cgi/challenge-platform/&quot;)&#10;</code></pre>
<h2 id="interaction-between-redirects-and-verification-procedures-like-http-dcv">Interaction between redirects and verification procedures like HTTP DCV</h2>
<p>Paths used in validation procedures such as custom hostname verification (<a href="/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a>), <a href="/pages/configuration/debugging-pages/">Pages domain validation</a>, or <a href="/ssl/edge-certificates/changing-dcv-method/methods/http/">HTTP domain control validation (DCV)</a> may be affected by redirects.</p>
<p>Consider excluding the <code>/.well-known/*</code> URI path from your rule to avoid issues.</p>
<h2 id="content-length-header-removed-from-response">Content-Length header removed from response</h2>
<p>Cloudflare may remove the <code>Content-Length</code> header from responses delivered to website visitors. If the visitor must receive the <code>Content-Length</code> header, configure the origin server to include a <code>cache-control: no-transform</code> HTTP header in the response.</p>
<h2 id="this-rule-may-not-apply-to-your-traffic">This rule may not apply to your traffic</h2>
<p>If your rule expression is matching a hostname for which you have neither created a DNS record nor enabled proxying traffic through Cloudflare, you will get a pop-up window with a couple of options:</p>
<ul>
<li><strong>If no DNS record exists for the hostname</strong>: Whether to proceed with the rule creation or to create a new proxied DNS record for that hostname.</li>
<li><strong>If there is a DNS record for the hostname, but traffic is not being proxied</strong>: Whether to proceed with the rule creation or to enable proxying for the existing DNS record.</li>
</ul>
<p>If you choose to create a new DNS record, the new record will have a <code>rules</code> tag and the following associated comment:</p>
<pre tabindex="0"><code class="language-txt">Created during Cloudflare Rules deployment process for &lt;RULE_NAME&gt;&#10;</code></pre>
<h2 id="url-rewrites-affect-other-rules-features-executed-later">URL rewrites affect other Rules features executed later</h2>
<p>If you rewrite a URI path using a <a href="/rules/transform/url-rewrite/">URL rewrite</a>, this may affect other Rules features executed later — such as <a href="/rules/origin-rules/">Origin Rules</a> — if they include the URI path in their filter expression.</p>
<p>Consider the following origin rule configuration:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/12791.md")
</div>
<p>If you configure a new URL rewrite with the following configuration:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@markup("md", "content/.markup/bodies/12792.md")
</div>
<p>The origin rule will no longer match <code>/downloads/*</code> paths, since URL rewrites run before Origin Rules and the URI path will be rewritten from <code>&quot;/downloads/&quot;</code> to <code>&quot;/&quot;</code>.</p>
<h3 id="solution">Solution</h3>
<p>To prevent this situation, use raw fields in your rule expression. Raw fields are immutable during the entire request evaluation workflow, and they are not affected by the actions of previously matched rules.</p>
<p>In the current example, you could use the <code>raw.http.request.uri.path</code> field in both rules:</p>
<p><strong>URL rewrite</strong></p>
<div class="nb-example"><h3 class="nb-component-title" id="example-2">Example</h3>
@markup("md", "content/.markup/bodies/12793.md")
</div>
<p><strong>Origin rule</strong></p>
<div class="nb-example"><h3 class="nb-component-title" id="example-3">Example</h3>
@markup("md", "content/.markup/bodies/12794.md")
</div>
<p>This way, the two rules will work as intended. Additionally, this allows you to use the same expression in the two rules, even when the first rule is updating the URI path value.</p>
<p>For a list of raw fields, refer to the <a href="/ruleset-engine/rules-language/fields/reference/?field-category=Raw+fields">Fields reference</a>.</p>

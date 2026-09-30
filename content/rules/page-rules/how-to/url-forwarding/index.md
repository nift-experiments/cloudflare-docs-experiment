---
cp9:
  canonical: https://developers.cloudflare.com/rules/page-rules/how-to/url-forwarding/
  description: Create URL forwarding rules with Page Rules.
  full_title: URL forwarding with Page Rules · Cloudflare Rules docs
  head_html: <title>URL forwarding with Page Rules · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Create URL forwarding rules with Page Rules."><link rel="canonical" href="https://developers.cloudflare.com/rules/page-rules/how-to/url-forwarding/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/page-rules/how-to/url-forwarding/index.md"><meta property="og:title" content="URL forwarding with Page Rules · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create URL forwarding rules with Page Rules."><meta property="og:url" content="https://developers.cloudflare.com/rules/page-rules/how-to/url-forwarding/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Rules"><meta name="pcx_tags" content="Redirects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/page-rules/how-to/url-forwarding/#page","headline":"URL forwarding with Page Rules \u00b7 Cloudflare Rules docs","description":"Create URL forwarding rules with Page Rules.","url":"https://developers.cloudflare.com/rules/page-rules/how-to/url-forwarding/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Redirects"]}</script>
  markdown: true
  noindex: false
  route: /rules/page-rules/how-to/url-forwarding/
  schema: 1
---
<p>Page Rules allow you to forward or redirect traffic to a different URL, though they are just one of the <a href="/fundamentals/reference/redirects/">options provided by Cloudflare</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13120.md")
</aside>
<hr />
<h2 id="redirect-with-page-rules">Redirect with Page Rules</h2>
<p>To configure URL forwarding or redirects using Page Rules:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13121.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13119.md")
</aside>
<hr />
<h2 id="forwarding-examples">Forwarding examples</h2>
<p>Imagine you want site visitors to reach your website for a variety of URL patterns. For instance, the page rule URL patterns <code>*www.example.com/products</code> and <code>*example.com/products</code> match:</p>
<pre tabindex="0"><code class="language-txt">http://example.com/products&#10;&#10;http://www.example.com/products&#10;&#10;https://www.example.com/products&#10;&#10;https://blog.example.com/products&#10;&#10;https://www.blog.example.com/products&#10;</code></pre>
<p>but do not match:</p>
<pre tabindex="0"><code class="language-txt">http://www.example.com/blog/products (extra directory)&#10;or&#10;http://www.example.comproducts (no trailing slash)&#10;</code></pre>
<p>Once you have created the pattern that matches what you want, select the <strong>Forwarding</strong> toggle. This will display a field where you can enter the address you want requests forwarded to.</p>
<pre tabindex="0"><code class="language-txt">https://example.com/products&#10;</code></pre>
<p>If you enter the address above in the forwarding box and select <strong>Add Rule</strong>, within a few seconds any requests that match the pattern you entered will automatically be forwarded with an <code>HTTP 302</code> redirect status code to the new URL.</p>
<hr />
<h2 id="advanced-forwarding-options">Advanced forwarding options</h2>
<p>If you use a basic redirect, such as forwarding the apex domain (<code>example.com</code>) to <code>www.example.com</code>, then you lose anything else in the URL.</p>
<p>For example, you could set up the pattern:</p>
<pre tabindex="0"><code class="language-txt">example.com&#10;</code></pre>
<p>And have it forward to:</p>
<pre tabindex="0"><code class="language-txt">http://www.example.com&#10;</code></pre>
<p>However, if someone entered <code>example.com/some-particular-page.html</code>, they would be redirected to:</p>
<pre tabindex="0"><code class="language-txt">www.example.com&#10;</code></pre>
<p>Instead of:</p>
<pre tabindex="0"><code class="language-txt">www.example.com/some-particular-page.html&#10;</code></pre>
<p>The solution is to use variables. Each wildcard corresponds to a variable when can be referenced in the forwarding address. The variables are represented by a <code>$</code> (dollar sign) followed by a number. To refer to the first wildcard you would use <code>$1</code>, to refer to the second wildcard you would use <code>$2</code>, and so on.</p>
<p>To fix the forwarding from the apex to <code>www</code> in the above example, you could use the same pattern:</p>
<pre tabindex="0"><code class="language-txt">example.com/*&#10;</code></pre>
<p>You would then set up the following URL for traffic to forward to:</p>
<pre tabindex="0"><code class="language-txt">http://www.example.com/$1&#10;</code></pre>
<p>In this case, if someone went to:</p>
<pre tabindex="0"><code class="language-txt">example.com/some-particular-page.html&#10;</code></pre>
<p>They would be redirected to:</p>
<pre tabindex="0"><code class="language-txt">http://www.example.com/some-particular-page.html&#10;</code></pre>

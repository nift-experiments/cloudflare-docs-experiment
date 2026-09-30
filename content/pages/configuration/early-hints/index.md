---
cp9:
  canonical: https://developers.cloudflare.com/pages/configuration/early-hints/
  description: Improve page load performance on Cloudflare Pages with Early Hints for preloading assets.
  full_title: Early Hints · Cloudflare Pages docs
  head_html: <title>Early Hints · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Improve page load performance on Cloudflare Pages with Early Hints for preloading assets."><link rel="canonical" href="https://developers.cloudflare.com/pages/configuration/early-hints/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/configuration/early-hints/index.md"><meta property="og:title" content="Early Hints · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Improve page load performance on Cloudflare Pages with Early Hints for preloading assets."><meta property="og:url" content="https://developers.cloudflare.com/pages/configuration/early-hints/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/configuration/early-hints/#page","headline":"Early Hints \u00b7 Cloudflare Pages docs","description":"Improve page load performance on Cloudflare Pages with Early Hints for preloading assets.","url":"https://developers.cloudflare.com/pages/configuration/early-hints/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/configuration/early-hints/
  schema: 1
---
<p><a href="/cache/advanced-configuration/early-hints/">Early Hints</a> help the browser to load webpages faster. Early Hints is enabled automatically on all <code>pages.dev</code> domains and custom domains.</p>
<p>Early Hints automatically caches any <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Link_types/preload"><code>preload</code></a> and <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Link_types/preconnect"><code>preconnect</code></a> type <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Link"><code>Link</code> headers</a> to send as Early Hints to the browser. The hints are sent to the browser before the full response is prepared, and the browser can figure out how to load the webpage faster for the end user. There are two ways to create these <code>Link</code> headers in Pages:</p>
<h2 id="configure-early-hints">Configure Early Hints</h2>
<p>Early Hints can be created with either of the two methods detailed below.</p>
<h3 id="1-configure-your-headers-file"><ol>
<li>Configure your <code>_headers</code> file</li>
</ol></h3>
<p>Create custom headers using the <a href="/pages/configuration/headers/"><code>_headers</code> file</a>. If you include a particular stylesheet on your <code>/blog/</code> section of your website, you would create the following rule:</p>
<pre tabindex="0"><code class="language-txt">/blog/*&#10;  Link: &lt;/styles.css&gt;; rel=preload; as=style&#10;</code></pre>
<p>Pages will attach this <code>Link: &lt;/styles.css&gt;; rel=preload; as=style</code> header. Early Hints will then emit this header as an Early Hint once cached.</p>
<h3 id="2-automatic-link-header-generation"><ol start="2">
<li>Automatic <code>Link</code> header generation</li>
</ol></h3>
<p>In order to make the authoring experience easier, Pages also automatically generates <code>Link</code> headers from any <code>&lt;link&gt;</code> HTML elements with the following attributes:</p>
<ul>
<li><code>href</code></li>
<li><code>as</code> (optional)</li>
<li><code>rel</code> (one of <code>preconnect</code>, <code>preload</code>, or <code>modulepreload</code>)</li>
</ul>
<p><code>&lt;link&gt;</code> elements which contain any other additional attributes (for example, <code>fetchpriority</code>, <code>crossorigin</code> or <code>data-do-not-generate-a-link-header</code>) will not be used to generate <code>Link</code> headers in order to prevent accidentally losing any custom prioritization logic that would otherwise be dropped as an Early Hint.</p>
<p>This allows you to directly create Early Hints as you are writing your document, without needing to alternate between your HTML and <code>_headers</code> file.</p>
<pre tabindex="0"><code class="language-html">&lt;html&gt;&#10;	&lt;head&gt;&#10;		&lt;link rel=&quot;preload&quot; href=&quot;/style.css&quot; as=&quot;style&quot; /&gt;&#10;		&lt;link rel=&quot;stylesheet&quot; href=&quot;/style.css&quot; /&gt;&#10;	&lt;/head&gt;&#10;&lt;/html&gt;&#10;</code></pre>
<h3 id="disable-automatic-link-header-generation-automatic-link-header">Disable automatic <code>Link</code> header generation Automatic <code>Link</code> header</h3>
<p>Remove any automatically generated <code>Link</code> headers by adding the following to your <code>_headers</code> file:</p>
<pre tabindex="0"><code class="language-txt">/*&#10;  ! Link&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/11065.md")
</aside>

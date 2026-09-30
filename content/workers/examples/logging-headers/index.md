---
cp9:
  canonical: https://developers.cloudflare.com/workers/examples/logging-headers/
  description: Examine the contents of a Headers object by logging to console with a Map.
  full_title: Logging headers to console · Cloudflare Workers docs
  head_html: <title>Logging headers to console · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Examine the contents of a Headers object by logging to console with a Map."><link rel="canonical" href="https://developers.cloudflare.com/workers/examples/logging-headers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/examples/logging-headers/index.md"><meta property="og:title" content="Logging headers to console · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Examine the contents of a Headers object by logging to console with a Map."><meta property="og:url" content="https://developers.cloudflare.com/workers/examples/logging-headers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Workers"><meta name="pcx_tags" content="Debugging,Headers,JavaScript,Rust,TypeScript,Python"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/examples/logging-headers/#page","headline":"Logging headers to console \u00b7 Cloudflare Workers docs","description":"Examine the contents of a Headers object by logging to console with a Map.","url":"https://developers.cloudflare.com/workers/examples/logging-headers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Debugging","Headers","JavaScript","Rust","TypeScript","Python"]}</script>
  markdown: true
  noindex: false
  route: /workers/examples/logging-headers/
  schema: 1
---
<p class="article-summary">Examine the contents of a Headers object by logging to console with a Map.</p>
<p>If you want to get started quickly, click on the button below.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/logging-headers"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16426.md")
</div></div>
<hr />
<h2 id="console-logging-headers">Console-logging headers</h2>
<p>Use a <code>Map</code> if you need to log a <code>Headers</code> object to the console:</p>
<pre tabindex="0"><code class="language-js">console.log(new Map(request.headers));&#10;</code></pre>
<p>Use the <code>spread</code> operator if you need to quickly stringify a <code>Headers</code> object:</p>
<pre tabindex="0"><code class="language-js">let requestHeaders = JSON.stringify([...request.headers]);&#10;</code></pre>
<p>Use <code>Object.fromEntries</code> to convert the headers to an object:</p>
<pre tabindex="0"><code class="language-js">let requestHeaders = Object.fromEntries(request.headers);&#10;</code></pre>
<h3 id="the-problem">The problem</h3>
<p>When debugging Workers, examine the headers on a request or response. A common mistake is to try to log headers to the developer console via code like this:</p>
<pre tabindex="0"><code class="language-js">console.log(request.headers);&#10;</code></pre>
<p>Or this:</p>
<pre tabindex="0"><code class="language-js">console.log(`Request headers: ${JSON.stringify(request.headers)}`);&#10;</code></pre>
<p>Both attempts result in what appears to be an empty object — the string <code>&quot;{}&quot;</code> — even though calling <code>request.headers.has(&quot;Your-Header-Name&quot;)</code> might return true. This is the same behavior that browsers implement.</p>
<p>The reason this happens is because <a href="https://developer.mozilla.org/en-US/docs/Web/API/Headers">Headers</a> objects do not store headers in enumerable JavaScript properties, so the developer console and JSON stringifier do not know how to read the names and values of the headers. It is not actually an empty object, but rather an opaque object.</p>
<p><code>Headers</code> objects are iterable, which you can take advantage of to develop a couple of quick one-liners for debug-printing headers.</p>
<h3 id="pass-headers-through-a-map">Pass headers through a Map</h3>
<p>The first common idiom for making Headers <code>console.log()</code>-friendly is to construct a <code>Map</code> object from the <code>Headers</code> object and log the <code>Map</code> object.</p>
<pre tabindex="0"><code class="language-js">console.log(new Map(request.headers));&#10;</code></pre>
<p>This works because:</p>
<ul>
<li>
<p><code>Map</code> objects can be constructed from iterables, like <code>Headers</code>.</p>
</li>
<li>
<p>The <code>Map</code> object does store its entries in enumerable JavaScript properties, so the developer console can see into it.</p>
</li>
</ul>
<h3 id="spread-headers-into-an-array">Spread headers into an array</h3>
<p>The <code>Map</code> approach works for calls to <code>console.log()</code>. If you need to stringify your headers, you will discover that stringifying a <code>Map</code> yields nothing more than <code>[object Map]</code>.</p>
<p>Even though a <code>Map</code> stores its data in enumerable properties, those properties are <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol">Symbol</a>-keyed. Because of this, <code>JSON.stringify()</code> will <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol#symbols_and_json.stringify">ignore Symbol-keyed properties</a> and you will receive an empty <code>{}</code>.</p>
<p>Instead, you can take advantage of the iterability of the <code>Headers</code> object in a new way by applying the <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax">spread operator</a> (<code>...</code>) to it.</p>
<pre tabindex="0"><code class="language-js">let requestHeaders = JSON.stringify([...request.headers], null, 2);&#10;console.log(`Request headers: ${requestHeaders}`);&#10;</code></pre>
<h3 id="convert-headers-into-an-object-with-object-fromentries-es2019">Convert headers into an object with Object.fromEntries (ES2019)</h3>
<p>ES2019 provides <a href="https://github.com/tc39/proposal-object-from-entries"><code>Object.fromEntries</code></a> which is a call to convert the headers into an object:</p>
<pre tabindex="0"><code class="language-js">let headersObject = Object.fromEntries(request.headers);&#10;let requestHeaders = JSON.stringify(headersObject, null, 2);&#10;console.log(`Request headers: ${requestHeaders}`);&#10;</code></pre>
<p>This results in something like:</p>
<pre tabindex="0"><code class="language-js">Request headers: {&#10;  &quot;accept&quot;: &quot;text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8&quot;,&#10;  &quot;accept-encoding&quot;: &quot;gzip&quot;,&#10;  &quot;accept-language&quot;: &quot;en-US,en;q=0.9&quot;,&#10;  &quot;cf-ipcountry&quot;: &quot;US&quot;,&#10;  // ...&#10;}&quot;&#10;</code></pre>

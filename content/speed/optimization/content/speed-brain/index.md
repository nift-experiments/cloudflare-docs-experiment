---
cp9:
  canonical: https://developers.cloudflare.com/speed/optimization/content/speed-brain/
  description: Learn how Speed Brain enhances web performance by prefetching likely next pages, improving metrics like LCP and TTFB.
  full_title: Speed Brain · Cloudflare Speed docs
  head_html: <title>Speed Brain · Cloudflare Speed docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how Speed Brain enhances web performance by prefetching likely next pages, improving metrics like LCP and TTFB."><link rel="canonical" href="https://developers.cloudflare.com/speed/optimization/content/speed-brain/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/speed/optimization/content/speed-brain/index.md"><meta property="og:title" content="Speed Brain · Cloudflare Speed docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how Speed Brain enhances web performance by prefetching likely next pages, improving metrics like LCP and TTFB."><meta property="og:url" content="https://developers.cloudflare.com/speed/optimization/content/speed-brain/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Speed"><meta name="algolia_product_filter" content="Speed"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Speed"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/speed/optimization/content/speed-brain/#page","headline":"Speed Brain \u00b7 Cloudflare Speed docs","description":"Learn how Speed Brain enhances web performance by prefetching likely next pages, improving metrics like LCP and TTFB.","url":"https://developers.cloudflare.com/speed/optimization/content/speed-brain/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /speed/optimization/content/speed-brain/
  schema: 1
---
<p>Speed Brain is a tool for improving web page performance by prefetching the most likely next navigation.</p>
<hr />
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Enabled by default</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="requirements">Requirements</h2>
<p>Speed Brain works under the following conditions:</p>
<ul>
<li>The Speed Brain feature is enabled in Cloudflare.</li>
<li>The browser of the web page visitor is using a Chromium-based browser version 121 or later.</li>
<li>The web page requested by the prefetch is eligible for cache.</li>
<li>The page requested by the prefetch does not invoke a Worker.</li>
</ul>
<h2 id="what-is-speed-brain">What is Speed Brain?</h2>
<p>The overall goal of Speed Brain is to try to download a webpage to the browser before a user navigates to it.</p>
<p>Cloudflare leverages the <a href="https://developer.mozilla.org/en-US/docs/Web/API/Speculation_Rules_API">Speculation Rules API</a> to improve web page performance by instructing the browser to consider prefetching future navigations. Speed Brain does not improve page load time for the first page that is visited on a website, but it can improve it for subsequent web pages that are navigated to on the same site.</p>
<p>By prefetching pages that the browser considers likely to be navigated to, Speed Brain can enhance key metrics like <a href="https://web.dev/articles/lcp">Largest Content Paint</a> (LCP), <a href="https://web.dev/articles/ttfb">Time to First Byte</a> (TTFB) and overall page load time.</p>
<h2 id="how-speed-brain-works">How Speed Brain works</h2>
<p>When Cloudflare's Speed Brain feature is enabled, an HTTP header called <code>Speculation-Rules</code> is added to web page responses. The value for this header is a URL that hosts an opinionated Speculation-Rules configuration. This configuration instructs the browser to consider prefetching any future navigations with a <code>conservative</code> <a href="https://developer.chrome.com/docs/web-platform/prerender-pages#eagerness">eagerness</a>.</p>
<p>The configuration looks like this:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;prefetch&quot;: [&#10;		{&#10;			&quot;source&quot;: &quot;document&quot;,&#10;			&quot;where&quot;: {&#10;				&quot;and&quot;: [{ &quot;href_matches&quot;: &quot;/*&quot;, &quot;relative_to&quot;: &quot;document&quot; }]&#10;			},&#10;			&quot;eagerness&quot;: &quot;conservative&quot;&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>This configuration instructs the browser to initiate prefetch requests for future navigations. These prefetch requests will include the <code>sec-purpose: prefetch</code> HTTP request header. Prefetches that are not successful will respond with a <code>503</code> status code. Prefetches that are successful will respond with a <code>200</code> status code.</p>
<h2 id="test-speed-brain">Test Speed Brain</h2>
<p>To test that Speed Brain is enabled, you can check that your HTTP response headers for your web pages include the <code>Speculation-Rules</code> header. However, note that during the beta phase of Speed Brain, this behavior might not be 100% consistent.</p>
<p>To test whether your browser is making prefetch requests, open the <strong>Network</strong> tab in Chrome DevTools. Then, mouse-down on a link on a webpage with Speed Brain enabled. This action should initiate a prefetch request, which will be  visible in the <strong>Network</strong> tab. However, note that there are several reasons why the browser might choose not to initiate a prefetch. Refer to the <a href="https://developer.chrome.com/docs/web-platform/prerender-pages#chrome-limits">Chrome Limits guide</a> for more details. For more general information about debugging Speculation-Rules, refer to the <a href="https://developer.chrome.com/docs/devtools/application/debugging-speculation-rules">Chrome Speculation Debugging guide</a>.</p>
<h2 id="rum-integration">RUM integration</h2>
<p>Speed Brain is designed to integrate with Web Analytics &amp; Real User Measurements (RUM). This integration allows you to understand the web performance implications of Speed Brain within the Web Analytics interface in Cloudflare's Dashboard.</p>
<p>While you can use Speed Brain without RUM enabled, you will not have visibility into how the feature is affecting the performance of your web pages. For further details on how to set up RUM, refer to the <a href="/web-analytics/">Web Analytics &amp; RUM</a> documentation.</p>
<h2 id="enable-and-disable-speed-brain">Enable and disable Speed Brain</h2>
<p>Speed Brain is available in Cloudflare's <strong>Speed</strong> tab of the dashboard and also in the API.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/13929.md")
</div></div>
<h2 id="caveats">Caveats</h2>
<ul>
<li>
<p>Since prefetch responses are not guaranteed to be rendered by the browser, Speed Brain includes two safeguards to minimize the risk of <a href="https://developer.mozilla.org/en-US/docs/Web/API/Speculation_Rules_API#unsafe_prefetching">unsafe prefetching</a>:</p>
<ul>
<li>
<p>Speed Brain will not prefetch on routes that run Workers. Without this safeguard, prefetch requests could inadvertently run Worker logic that assumes the incoming request is a normal (that is, not a prefetch) request. An example of this could be an incrementing page view counter running in a Worker. A page view counter should not increment if the page is not actually rendered in the browser.</p>
</li>
<li>
<p>Prefetch requests will never reach origin servers. Prefetch requests only serve content that is stored in Cloudflare’s Cache. If the content is not in Cache, the prefetch request will not continue to origin servers. Without this safeguard, origin server state could be modified despite the prefetch response not being rendered in the browser. An example of this could be a prefetch <code>GET</code> request to a sign-out URL inadvertently triggering a sign-out action on the server.</p>
</li>
</ul>
</li>
<li>
<p>If origin server responses include the <code>Speculation-Rules</code> header, it will not be overridden.</p>
</li>
<li>
<p>Speed Brain will not work with restrictive <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/script-src">Content Security Policy</a> configurations using <code>strict-dynamic</code> or <code>nonce-{hash}</code> attributes.</p>
</li>
<li>
<p>Currently, Speed Brain is not compatible with websites that use or rely on <code>pages.dev</code>.</p>
</li>
</ul>

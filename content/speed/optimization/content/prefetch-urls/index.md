---
cp9:
  canonical: https://developers.cloudflare.com/speed/optimization/content/prefetch-urls/
  description: Prefetch URLs to load resources before visitors request them.
  full_title: Prefetch URLs · Cloudflare Speed docs
  head_html: <title>Prefetch URLs · Cloudflare Speed docs</title><meta name="generator" content="Nift"><meta name="description" content="Prefetch URLs to load resources before visitors request them."><link rel="canonical" href="https://developers.cloudflare.com/speed/optimization/content/prefetch-urls/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/speed/optimization/content/prefetch-urls/index.md"><meta property="og:title" content="Prefetch URLs · Cloudflare Speed docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Prefetch URLs to load resources before visitors request them."><meta property="og:url" content="https://developers.cloudflare.com/speed/optimization/content/prefetch-urls/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Speed"><meta name="algolia_product_filter" content="Speed"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Speed"><meta name="pcx_tags" content="Caching"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/speed/optimization/content/prefetch-urls/#page","headline":"Prefetch URLs \u00b7 Cloudflare Speed docs","description":"Prefetch URLs to load resources before visitors request them.","url":"https://developers.cloudflare.com/speed/optimization/content/prefetch-urls/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Caching"]}</script>
  markdown: true
  noindex: false
  route: /speed/optimization/content/prefetch-urls/
  schema: 1
---
<p>URL prefetching means that Cloudflare pre-populates the cache with content a visitor is likely to request next. This setting — when combined with <a href="#setup">additional setup</a> — leads to a higher cache hit rate and thus a faster experience for the user.</p>
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
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="setup">Setup</h2>
<p>For Cloudflare to start prefetching URLs, you will need to <a href="#enable-prefetch-urls">enable the feature</a> and <a href="#choose-urls-to-prefetch">include a list of URLs to prefetch</a>.</p>
<h3 id="enable-prefetch-urls">Enable Prefetch URLs</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/13938.md")
</div></div>
<h3 id="choose-urls-to-prefetch">Choose URLs to prefetch</h3>
<p>After you <a href="#enable-prefetch-urls">enable the feature</a>, you also need to indicate which URLs Cloudflare should prefetch.</p>
<p>To do this, include a Link HTTP response header pointing to a manifest file with the <code>rel=&quot;prefetch&quot;</code> attribute and then serve the manifest file with <code>text/plain</code> as the Content-type response header.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13939.md")
</div>
<p>The manifest file should contain URIs, protocol-relative URLs or full URLs, separated by new lines. These files must be on your websites that are on Cloudflare. If you reference HTML pages, only the HTML page itself will be pre-fetched - any sub-requests from that HTML will not be fetched unless they are also defined explicitly in your manifest.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/13935.md")
</aside>
<h3 id="prefetch-files-limits">Prefetch files limits</h3>
<p>The prefetch files limits are the following:</p>
<ul>
<li>The maximum number of manifest files is 16.</li>
<li>The maximum number of files per manifest file is 100.</li>
<li>A manifest file has a size limit of 1 MB.</li>
</ul>
<h2 id="limitations">Limitations</h2>
<ul>
<li>
<p>Cloudflare will only prefetch files listed in the manifest file if the resources are those <a href="/cache/concepts/default-cache-behavior/#default-cached-file-extensions">cached by default</a>.</p>
</li>
<li>
<p>Prefetch is not compatible with the custom cache key configuration. For more information, refer to <a href="/cache/how-to/cache-keys/#limitations">Cache Key limitations</a>.</p>
</li>
</ul>

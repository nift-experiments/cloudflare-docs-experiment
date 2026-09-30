---
cp9:
  canonical: https://developers.cloudflare.com/rules/compression-rules/settings/
  description: Available compression algorithms and content type settings for Compression Rules.
  full_title: Compression Rules settings · Cloudflare Rules docs
  head_html: <title>Compression Rules settings · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Available compression algorithms and content type settings for Compression Rules."><link rel="canonical" href="https://developers.cloudflare.com/rules/compression-rules/settings/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/compression-rules/settings/index.md"><meta property="og:title" content="Compression Rules settings · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Available compression algorithms and content type settings for Compression Rules."><meta property="og:url" content="https://developers.cloudflare.com/rules/compression-rules/settings/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Rules"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/compression-rules/settings/#page","headline":"Compression Rules settings \u00b7 Cloudflare Rules docs","description":"Available compression algorithms and content type settings for Compression Rules.","url":"https://developers.cloudflare.com/rules/compression-rules/settings/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /rules/compression-rules/settings/
  schema: 1
---
<p>Compression Rules support the configuration settings covered in the following sections.</p>
<h2 id="dashboard-configuration-settings">Dashboard configuration settings</h2>
<h3 id="enable-zstandard-zstd-compression">Enable Zstandard (Zstd) compression <span class="nb-badge">Beta</span></h3>
<p>Sets Zstandard as the preferred compression algorithm. If it is not supported, will automatically fall back to Brotli, Gzip, or uncompressed data.</p>
<h3 id="enable-brotli-and-gzip-compression">Enable Brotli and Gzip compression</h3>
<p>Enables Cloudflare's default compression setting. Brotli is the preferred compression algorithm. It will automatically fall back to Gzip or to uncompressed data.</p>
<h3 id="disable-compression">Disable compression</h3>
<p>Disables compression for matching requests. Also disables Cloudflare's <a href="/speed/optimization/content/compression/">default compression behavior</a>.</p>
<h3 id="custom">Custom</h3>
<p>Defines a custom order for compression algorithms.</p>
<p>Allowed values are the following:</p>
<ul>
<li><strong>Gzip</strong>: Use the Gzip compression algorithm, if supported by the website visitor.</li>
<li><strong>Brotli</strong>: Use the Brotli compression algorithm, if supported by the website visitor.</li>
<li><strong>Zstandard</strong>: Use the Zstandard (Zstd) compression algorithm, if supported by the website visitor.</li>
<li><strong>Auto</strong>: Compress the response according to the algorithms supported by the website visitor (if any). Cloudflare will define the order of preference for the compression algorithms, which may change in the future. Has the same behavior of the <strong>Enable compression</strong> option.</li>
<li><strong>Default</strong>: Use Cloudflare's <a href="/speed/optimization/content/compression/">default compression behavior</a>, which depends on the response content type.</li>
</ul>
<p>If you specify only <em>Gzip</em>, <em>Brotli</em>, or <em>Zstandard</em> and no algorithm matches, the response will have no compression. To configure a fallback compression mechanism, add <em>Auto</em> to the list.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13026.md")
</aside>
<hr />
<h2 id="api-configuration-settings">API configuration settings</h2>
<p>The configuration object supported by the <code>compress_response</code> action has the following format:</p>
<pre tabindex="0"><code class="language-json">&quot;action_parameters&quot;: {&#10;  &quot;algorithms&quot;: [&#10;    { &quot;name&quot;: &quot;&lt;VALUE1&gt;&quot; },&#10;    { &quot;name&quot;: &quot;&lt;VALUE2&gt;&quot; },&#10;    // ...&#10;  ]&#10;}&#10;</code></pre>
<p>The <code>algorithms</code> list must contain at least one item.</p>
<p>The supported algorithm values are:</p>
<ul>
<li><code>gzip</code>: Use the Gzip compression algorithm, if supported by the website visitor.</li>
<li><code>brotli</code>: Use the Brotli compression algorithm, if supported by the website visitor.</li>
<li><code>zstd</code>: Use the Zstandard compression algorithm, if supported by the website visitor.</li>
<li><code>none</code>: Do not use any compression algorithm.</li>
<li><code>auto</code>: Compress the response according to the algorithms supported by the website visitor (if any). Cloudflare will define the order of preference for the compression algorithms, which may change in the future.</li>
<li><code>default</code>: Use Cloudflare's <a href="/speed/optimization/content/compression/#compression-between-cloudflare-and-website-visitors">default compression behavior</a>, which depends on the response content type.</li>
</ul>
<p>If you include <code>none</code>, <code>default</code>, or <code>auto</code> in the list, it must be the last value in the list.</p>
<p>When you specify only the <code>gzip</code>, <code>brotli</code>, or <code>zstd</code> algorithms, if no algorithm matches then the response will have no compression. To configure a fallback compression mechanism, add <code>auto</code> to the list.</p>
<p>For API examples, refer to the <a href="/rules/compression-rules/examples/">Examples gallery</a>.</p>

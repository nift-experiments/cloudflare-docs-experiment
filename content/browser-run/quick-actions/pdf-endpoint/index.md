---
cp9:
  canonical: https://developers.cloudflare.com/browser-run/quick-actions/pdf-endpoint/
  description: Generate a PDF from a webpage or custom HTML using the Browser Run /pdf endpoint.
  full_title: /pdf - Render PDF · Cloudflare Browser Run docs
  head_html: <title>/pdf - Render PDF · Cloudflare Browser Run docs</title><meta name="generator" content="Nift"><meta name="description" content="Generate a PDF from a webpage or custom HTML using the Browser Run /pdf endpoint."><link rel="canonical" href="https://developers.cloudflare.com/browser-run/quick-actions/pdf-endpoint/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/browser-run/quick-actions/pdf-endpoint/index.md"><meta property="og:title" content="/pdf - Render PDF · Cloudflare Browser Run docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Generate a PDF from a webpage or custom HTML using the Browser Run /pdf endpoint."><meta property="og:url" content="https://developers.cloudflare.com/browser-run/quick-actions/pdf-endpoint/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Browser Run"><meta name="algolia_product_filter" content="Browser Run"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Browser Run"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/browser-run/quick-actions/pdf-endpoint/#page","headline":"/pdf - Render PDF \u00b7 Cloudflare Browser Run docs","description":"Generate a PDF from a webpage or custom HTML using the Browser Run /pdf endpoint.","url":"https://developers.cloudflare.com/browser-run/quick-actions/pdf-endpoint/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /browser-run/quick-actions/pdf-endpoint/
  schema: 1
---
<p>The <code>/pdf</code> endpoint instructs the browser to generate a PDF of a webpage or custom HTML using Cloudflare's headless Browser Run service.</p>
<p>You can use this endpoint in two ways:</p>
<ul>
<li><strong>REST API</strong>: <a href="/fundamentals/api/get-started/create-token/">Create a custom API Token</a> with <code>Browser Rendering - Edit</code> permission.</li>
<li><strong>Workers Bindings</strong>: Call the endpoint directly from a <a href="/workers/">Cloudflare Worker</a> using the <a href="/browser-run/reference/wrangler/#bindings">Workers Bindings</a>. No API token is needed.</li>
</ul>
<p>For more information, refer to <a href="/browser-run/quick-actions/#before-you-begin">Quick Actions: Before you begin</a>.</p>
<h2 id="endpoint">Endpoint</h2>
<pre tabindex="0"><code class="language-txt">https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/pdf&#10;</code></pre>
<h2 id="required-fields">Required fields</h2>
<p>You must provide either <code>url</code> or <code>html</code>:</p>
<ul>
<li><code>url</code> (string)</li>
<li><code>html</code> (string)</li>
</ul>
<h2 id="common-use-cases">Common use cases</h2>
<ul>
<li>Capture a PDF of a webpage</li>
<li>Generate PDFs, such as invoices, licenses, reports, and certificates, directly from HTML</li>
</ul>
<h2 id="basic-usage">Basic usage</h2>
<h3 id="convert-a-url-to-pdf">Convert a URL to PDF</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3615.md")
</div></div>
<h3 id="convert-custom-html-to-pdf">Convert custom HTML to PDF</h3>
<p>If you have raw HTML you want to generate a PDF from, use the <code>html</code> option. You can still apply custom styles using the <code>addStyleTag</code> parameter.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/pdf \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;  &quot;html&quot;: &quot;&lt;html&gt;&lt;body&gt;Advanced Snapshot&lt;/body&gt;&lt;/html&gt;&quot;,&#10;	&quot;addStyleTag&quot;: [&#10;      { &quot;content&quot;: &quot;body { font-family: Arial; }&quot; },&#10;      { &quot;url&quot;: &quot;https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css&quot; }&#10;    ]&#10;}&#x27; \&#10;  &#45;-output &quot;invoice.pdf&quot;&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="request-size-limits">Request size limits</h3>
@markup("md", "content/.markup/bodies/3611.md")
</aside>
<h2 id="advanced-usage">Advanced usage</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="looking-for-more-parameters">Looking for more parameters?</h3>
@markup("md", "content/.markup/bodies/3610.md")
</aside>
<h3 id="advanced-page-load-with-custom-headers-and-viewport">Advanced page load with custom headers and viewport</h3>
<p>Navigate to <code>https://example.com</code>, setting additional HTTP headers and configuring the page size (viewport). The PDF generation will wait until there are no more than two network connections for at least 500 ms, or until the maximum timeout of 4500 ms is reached, before rendering.</p>
<p>The <code>goToOptions</code> parameter exposes most of <a href="https://pptr.dev/api/puppeteer.gotooptions">Puppeteer's API</a>.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/pdf&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com/&quot;,&#10;    &quot;setExtraHTTPHeaders&quot;: {&#10;      &quot;X-Custom-Header&quot;: &quot;value&quot;&#10;    },&#10;    &quot;viewport&quot;: {&#10;      &quot;width&quot;: 1200,&#10;      &quot;height&quot;: 800&#10;    },&#10;    &quot;gotoOptions&quot;: {&#10;      &quot;waitUntil&quot;: &quot;networkidle2&quot;,&#10;      &quot;timeout&quot;: 45000&#10;    }&#10;  }&#x27; \&#10;  &#45;-output &quot;advanced-output.pdf&quot;&#10;</code></pre>
<h3 id="blocking-images-and-styles-when-generating-a-pdf">Blocking images and styles when generating a PDF</h3>
<p>The options <code>rejectResourceTypes</code> and <code>rejectRequestPattern</code> can be used to block requests during rendering. The opposite can also be done, <em>only</em> allow certain requests using <code>allowResourceTypes</code> and <code>allowRequestPattern</code>.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/pdf \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;  &quot;url&quot;: &quot;https://cloudflare.com/&quot;,&#10;  &quot;rejectResourceTypes&quot;: [&quot;image&quot;],&#10;  &quot;rejectRequestPattern&quot;: [&quot;/^.*\\.(css)&quot;]&#10;}&#x27; \&#10;  &#45;-output &quot;cloudflare.pdf&quot;&#10;</code></pre>
<h3 id="customize-page-headers-and-footers">Customize page headers and footers</h3>
<p>You can customize page headers and footers with HTML templates using the <code>headerTemplate</code> and <code>footerTemplate</code> options. Enable <code>displayHeaderFooter</code> to include them in your output. This example generates an A5 PDF with a branded header, a footer message, and page numbering.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/pdf&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com&quot;,&#10;    &quot;pdfOptions&quot;: {&#10;      &quot;format&quot;: &quot;a5&quot;,&#10;      &quot;headerTemplate&quot;: &quot;&lt;div style=\&quot;font-size: 10px; text-align: center; width: 100%; padding: 5px;\&quot;&gt;&lt;span&gt;brand name&lt;/span&gt;&lt;/div&gt;&quot;,&#10;      &quot;displayHeaderFooter&quot;: true,&#10;      &quot;footerTemplate&quot;: &quot;&lt;div style=\&quot;color: lightgray; border-top: solid lightgray 1px; font-size: 10px; padding-top: 5px; text-align: center; width: 100%;\&quot;&gt;&lt;span&gt;This is a test message&lt;/span&gt; - &lt;span class=\&quot;pageNumber\&quot;&gt;&lt;/span&gt;&lt;/div&gt;&quot;,&#10;      &quot;margin&quot;: {&#10;        &quot;top&quot;: &quot;70px&quot;,&#10;        &quot;bottom&quot;: &quot;70px&quot;&#10;      }&#10;    }&#10;  }&#x27; \&#10;  &#45;-output &quot;header-footer.pdf&quot;&#10;</code></pre>
<h3 id="include-dynamic-placeholders-from-page-metadata">Include dynamic placeholders from page metadata</h3>
<p>You can include dynamic placeholders such as <code>title</code>, <code>date</code>, <code>pageNumber</code>, and <code>totalPages</code> in the header or footer to display metadata on each page. This example produces an A4 PDF with a company-branded header, current date and title, and page numbering in the footer.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/pdf&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://news.ycombinator.com&quot;,&#10;    &quot;pdfOptions&quot;: {&#10;      &quot;format&quot;: &quot;a4&quot;,&#10;      &quot;landscape&quot;: false,&#10;      &quot;printBackground&quot;: true,&#10;      &quot;preferCSSPageSize&quot;: true,&#10;      &quot;displayHeaderFooter&quot;: true,&#10;      &quot;scale&quot;: 1.0,&#10;      &quot;headerTemplate&quot;: &quot;&lt;div style=\&quot;width: 100%; font-size: 10px; padding: 10px; text-align: center;\&quot;&gt;&lt;div style=\&quot;border-bottom: 1px solid #ddd;\&quot;&gt;&lt;span style=\&quot;color: #666;\&quot;&gt;Company Name&lt;/span&gt; | &lt;span class=\&quot;date\&quot;&gt;&lt;/span&gt; | &lt;span class=\&quot;title\&quot;&gt;&lt;/span&gt;&lt;/div&gt;&lt;/div&gt;&quot;,&#10;      &quot;footerTemplate&quot;: &quot;&lt;div style=\&quot;width: 100%; font-size: 10px; padding: 10px; text-align: center;\&quot;&gt;&lt;div style=\&quot;border-top: 1px solid #ddd;\&quot;&gt;Page &lt;span class=\&quot;pageNumber\&quot;&gt;&lt;/span&gt; of &lt;span class=\&quot;totalPages\&quot;&gt;&lt;/span&gt;&lt;/div&gt;&lt;/div&gt;&quot;,&#10;      &quot;margin&quot;: {&#10;        &quot;top&quot;: &quot;100px&quot;,&#10;        &quot;bottom&quot;: &quot;80px&quot;,&#10;        &quot;right&quot;: &quot;30px&quot;,&#10;        &quot;left&quot;: &quot;30px&quot;&#10;      },&#10;      &quot;timeout&quot;: 30000&#10;    }&#10;  }&#x27; \&#10;  &#45;-output &quot;dynamic-header-footer.pdf&quot;&#10;</code></pre>
<h3 id="use-custom-fonts">Use custom fonts</h3>
<p>If your PDF requires a font that is not pre-installed in the Browser Run environment, you can load custom fonts using the <code>addStyleTag</code> parameter. For instructions and examples, refer to <a href="/browser-run/features/custom-fonts/#quick-actions">Use your own custom font</a>.</p>
<h3 id="handling-javascript-heavy-pages">Handling JavaScript-heavy pages</h3>
<p>For JavaScript-heavy pages or Single Page Applications (SPAs), the default page load behavior may return empty or incomplete results. This happens because the browser considers the page loaded before JavaScript has finished rendering the content.</p>
<p>The simplest solution is to use the <code>gotoOptions.waitUntil</code> parameter set to <code>networkidle0</code> or <code>networkidle2</code>:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;url&quot;: &quot;https://example.com&quot;,&#10;	&quot;gotoOptions&quot;: {&#10;		&quot;waitUntil&quot;: &quot;networkidle0&quot;&#10;	}&#10;}&#10;</code></pre>
<p>For faster responses, advanced users can use <code>waitForSelector</code> to wait for a specific element instead of waiting for all network activity to stop. This requires knowing which CSS selector indicates the content you need has loaded. For more details, refer to <a href="/browser-run/reference/timeouts/">Quick Actions timeouts</a>.</p>
<h3 id="set-a-custom-user-agent">Set a custom user agent</h3>
<p>You can change the user agent at the page level by passing <code>userAgent</code> as a top-level parameter in the JSON body. This is useful if the target website serves different content based on the user agent.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3609.md")
</aside>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If you have questions or encounter an error, see the <a href="/browser-run/faq/">Browser Run FAQ and troubleshooting guide</a>.</p>

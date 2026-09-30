---
cp9:
  canonical: https://developers.cloudflare.com/logs/logpull/additional-details/
  description: Estimate data volume and troubleshoot Logpull.
  full_title: Additional details · Cloudflare Logs docs
  head_html: <title>Additional details · Cloudflare Logs docs</title><meta name="generator" content="Nift"><meta name="description" content="Estimate data volume and troubleshoot Logpull."><link rel="canonical" href="https://developers.cloudflare.com/logs/logpull/additional-details/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/logs/logpull/additional-details/index.md"><meta property="og:title" content="Additional details · Cloudflare Logs docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Estimate data volume and troubleshoot Logpull."><meta property="og:url" content="https://developers.cloudflare.com/logs/logpull/additional-details/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Logs"><meta name="algolia_product_filter" content="Logs"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Logs"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/logs/logpull/additional-details/#page","headline":"Additional details \u00b7 Cloudflare Logs docs","description":"Estimate data volume and troubleshoot Logpull.","url":"https://developers.cloudflare.com/logs/logpull/additional-details/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /logs/logpull/additional-details/
  schema: 1
---
<h2 id="estimating-daily-data-volume">Estimating daily data volume</h2>
<p>To estimate the amount of data for a zone per day (the number of log lines and the amount of bytes they take up), request a 1% or 10% sample of data for a 1-hour period (use 10% if your volume is low). Note that <code>start=2018-12-15T00:00:00Z</code> and <code>end=2018-12-15T01:00:00Z</code> span a 1-hour period, and <code>sample=0.1</code>.</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/logs/received?start=2018-12-15T00:00:00Z&amp;end=2018-12-15T01:00:00Z&amp;sample=0.1&quot; \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot; \&#10;&gt; sample.log&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">wc -l sample.log&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">83 sample.log&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">ls -lh sample.log&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">&#45;rw-r--r-- 1 mik mik 25K Dec 17 15:49 sample.log&#10;</code></pre>
<p>Based on this information, the approximate number of messages/day is 19,920 (83 × 10 × 24), and the byte size is 6MB (25K × 10 × 24). The size estimate is based on the default response field set. Changing the response field set (refer to <a href="/logs/logpull/requesting-logs/#fields">Fields</a>) will change the response size.</p>
<p>To get a good estimate of daily traffic, it is best to get at least 30 log lines in your hourly sample. If the response size is too small (or too large), adjust the sample value, not the time range.</p>
<h2 id="compression">Compression</h2>
<p>Responses are compressed by default (gzip). <code>cURL</code> decompresses responses transparently, unless called with:</p>
<p><code>--header &quot;Accept-Encoding: gzip&quot;</code></p>
<p>In that case, the output remains gzipped. Compressed data is approximately 5-10% of its uncompressed size. This means that a 1GB uncompressed response gets compressed down to 50-100MB.</p>
<h2 id="service-expectations">Service expectations</h2>
<h3 id="successful-requests">Successful requests</h3>
<p>If the response or timeout limit is exceeded or there is any problem fetching the response, a <code>200</code> status will be returned and the response will end with the non-JSON text line “Error streaming data.” Because responses are streamed, there is no way to identify the error ahead of time. A response is successful if it does not end with the “Error streaming data&quot; text line.</p>
<p>Once you receive a successful response for a given zone and time range, the following is true for all subsequent requests:</p>
<ul>
<li>The number and content of returned records will be same.</li>
<li>The order of records returned may (and is likely to) be different.</li>
</ul>
<h3 id="response-fields">Response fields</h3>
<p>Regarding the inclusion of the <strong>fields</strong> parameter:</p>
<ul>
<li>When fields are explicitly included in the request URL, the fields returned will not change.</li>
<li>When not specified in the URL, the default fields are returned.</li>
<li>The default fields may change at any time.</li>
</ul>
<h3 id="limits">Limits</h3>
<p>The following usage restrictions apply:</p>
<ul>
<li><strong>Rate limits:</strong> Exceeding these limit results in a <code>429</code> error response:
<ul>
<li>15 requests/min per zone.</li>
<li>180 requests/min per user (email address).</li>
</ul>
</li>
<li><strong>Time range:</strong> The maximum difference between the <strong>start</strong> and <strong>end</strong> parameters can be 1 hour.</li>
<li><strong>Response size:</strong> The maximum response size is 10GiB per request, which is equivalent to about 15M records when about 55 fields are selected (more records can be retrieved when less fields are selected because the per record size will be smaller).</li>
<li><strong>Timeout:</strong> The response will fail with a terminated connection after 10 minutes.</li>
<li><strong>Stream Timeout:</strong> The request will be terminated with a <code>408</code> error response if the connection is idle for 30s. This timeout usually means that the request is probably too exhaustive (frequent timeouts (&gt; 12/hr) will result in subsequent queries to be blocked with status code 429 for 1hr) and so:
<ul>
<li>try requesting records using lesser number of fields.</li>
<li>try with smaller <strong>start</strong> and <strong>end</strong> parameters.</li>
</ul>
</li>
</ul>

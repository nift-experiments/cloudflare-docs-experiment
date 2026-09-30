---
cp9:
  canonical: https://developers.cloudflare.com/logs/logpush/parsing-json-log-data/
  description: Parse and analyze downloaded Cloudflare Logs data.
  full_title: Parse Cloudflare Logs JSON data · Cloudflare Logs docs
  head_html: <title>Parse Cloudflare Logs JSON data · Cloudflare Logs docs</title><meta name="generator" content="Nift"><meta name="description" content="Parse and analyze downloaded Cloudflare Logs data."><link rel="canonical" href="https://developers.cloudflare.com/logs/logpush/parsing-json-log-data/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/logs/logpush/parsing-json-log-data/index.md"><meta property="og:title" content="Parse Cloudflare Logs JSON data · Cloudflare Logs docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Parse and analyze downloaded Cloudflare Logs data."><meta property="og:url" content="https://developers.cloudflare.com/logs/logpush/parsing-json-log-data/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Logs"><meta name="algolia_product_filter" content="Logs"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Logpush"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/logs/logpush/parsing-json-log-data/#page","headline":"Parse Cloudflare Logs JSON data \u00b7 Cloudflare Logs docs","description":"Parse and analyze downloaded Cloudflare Logs data.","url":"https://developers.cloudflare.com/logs/logpush/parsing-json-log-data/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /logs/logpush/parsing-json-log-data/
  schema: 1
---
<p>After downloading your Cloudflare Logs data, you can use different tools to parse and analyze your logs.</p>
<p>One of those tools used to parse your JSON log data is <code>jq</code>.</p>
<p>Refer to <a href="https://jqlang.github.io/jq/download/">Download jq</a> for more information on obtaining and installing <code>jq</code>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/10471.md")
</aside>
<h2 id="aggregate-fields">Aggregate fields</h2>
<p>To aggregate a field appearing in the log, such as by IP address, URI, or referrer, you can use several <code>jq</code> commands. This is useful to identify any patterns in traffic; for example, to identify your most popular pages or to block an attack.</p>
<p>The following examples match on a field name and provide a count of each field instance, sorted in ascending order by count.</p>
<pre tabindex="0"><code class="language-bash">jq -r .ClientRequestURI logs.json | sort -n | uniq -c | sort -n | tail&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">2 /nginx-logo.png&#10;2 /poweredby.png&#10;2 /testagain&#10;3 /favicon.ico&#10;3 /testing&#10;3 /testing123&#10;6 /test&#10;7 /testing1234&#10;10 /cdn-cgi/nexp/dok3v=1613a3a185/cloudflare/rocket.js&#10;54 /&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">jq -r .ClientRequestUserAgent logs.json | sort -n | uniq -c | sort -n | tail&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">1 python-requests/2.9.1&#10;2 Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.56 Safari/537.17&#10;4 Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36&#10;5 curl/7.47.2-DEV&#10;36 Mozilla/5.0 (X11; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0&#10;51 curl/7.46.0-DEV&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">jq -r .ClientRequestReferer logs.json | sort -n | uniq -c | sort -n | tail&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">2 http://example.com/testagain&#10;3 http://example.com/testing&#10;5 http://example.com/&#10;5 http://example.com/testing123&#10;7 http://example.com/testing1234&#10;77 null&#10;</code></pre>
<h2 id="filter-fields">Filter fields</h2>
<p>Another common use case involves filtering data for a specific field value and then aggregating after that. This helps answer questions like <em>Which URLs saw the most 502 errors?</em> For example:</p>
<pre tabindex="0"><code class="language-bash">jq &#x27;select(.OriginResponseStatus == 502) | .ClientRequestURI&#x27; logs.json | sort -n | uniq -c | sort -n | tail&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">1 &quot;/favicon.ico&quot;&#10;1 &quot;/testing&quot;&#10;3 &quot;/testing123&quot;&#10;6 &quot;/test&quot;&#10;6 &quot;/testing1234&quot;&#10;18 &quot;/&quot;&#10;</code></pre>
<p>To find out the top IP addresses blocked by the Cloudflare WAF, use the following query:</p>
<pre tabindex="0"><code class="language-bash">jq -r &#x27;select(.SecurityAction == &quot;block&quot;) | .ClientIP&#x27; logs.json | sort -n | uniq -c | sort -n&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">1 127.0.0.1&#10;</code></pre>
<h2 id="show-cached-requests">Show cached requests</h2>
<p>To retrieve your cache ratios, try the following query:</p>
<pre tabindex="0"><code class="language-bash">jq -r &#x27;.CacheCacheStatus&#x27; logs.json | sort -n | uniq -c | sort -n&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">3 hit&#10;3 null&#10;3 stale&#10;4 expired&#10;6 miss&#10;81 unknown&#10;</code></pre>
<h2 id="show-tls-versions">Show TLS versions</h2>
<p>To find out which TLS versions your visitors are using — for example, to decide if you can disable TLS versions that are older than 1.2 — use the following query:</p>
<pre tabindex="0"><code class="language-bash">jq -r &#x27;.ClientSSLProtocol&#x27; logs.json | sort -n | uniq -c | sort -n&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">42 none&#10;58 TLSv1.2&#10;</code></pre>

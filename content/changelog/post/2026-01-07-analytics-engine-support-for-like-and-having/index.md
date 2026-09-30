---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-01-07-analytics-engine-support-for-like-and-having/
  description: New updates and improvements at Cloudflare.
  full_title: Workers Analytics Engine SQL now supports filtering using HAVING and LIKE · Changelog
  head_html: <title>Workers Analytics Engine SQL now supports filtering using HAVING and LIKE · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-01-07-analytics-engine-support-for-like-and-having/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Workers Analytics Engine SQL now supports filtering using HAVING and LIKE · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-01-07-analytics-engine-support-for-like-and-having/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-07-analytics-engine-support-for-like-and-having/#page","headline":"Workers Analytics Engine SQL now supports filtering using HAVING and LIKE \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-01-07-analytics-engine-support-for-like-and-having/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-01-07-analytics-engine-support-for-like-and-having/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 7, 2026</time><h2 id="post-title">Workers Analytics Engine SQL now supports filtering using HAVING and LIKE</h2>
<div class="changelog-badges"><span>workers-analytics-engine</span><span>workers</span></div><div class="changelog-body"><p>You can now use the <code>HAVING</code> clause and <code>LIKE</code> pattern matching operators in <a href="https://developers.cloudflare.com/analytics/analytics-engine/">Workers Analytics Engine</a>.</p>
<p>Workers Analytics Engine allows you to ingest and store high-cardinality data at scale and query your data through a simple SQL API.</p>
<h4 id="filtering-using-having">Filtering using <code>HAVING</code></h4>
<p>The <code>HAVING</code> clause complements the <code>WHERE</code> clause by enabling you to filter groups based on aggregate values. While <code>WHERE</code> filters rows before aggregation, <code>HAVING</code> filters groups after aggregation is complete.</p>
<p>You can use <code>HAVING</code> to filter groups where the average exceeds a threshold:</p>
<pre tabindex="0"><code class="language-sql">SELECT&#10;    blob1 AS probe_name,&#10;    avg(double1) AS average_temp&#10;FROM temperature_readings&#10;GROUP BY probe_name&#10;HAVING average_temp &gt; 10&#10;</code></pre>
<p>You can also filter groups based on aggregates such as the number of items in the group:</p>
<pre tabindex="0"><code class="language-sql">SELECT&#10;    blob1 AS probe_name,&#10;    count() AS num_readings&#10;FROM temperature_readings&#10;GROUP BY probe_name&#10;HAVING num_readings &gt; 100&#10;</code></pre>
<h4 id="pattern-matching-using-like">Pattern matching using <code>LIKE</code></h4>
<p>The new pattern matching operators enable you to search for strings that match specific patterns using wildcard characters:</p>
<ul>
<li><code>LIKE</code> - case-sensitive pattern matching</li>
<li><code>NOT LIKE</code> - case-sensitive pattern exclusion</li>
<li><code>ILIKE</code> - case-insensitive pattern matching</li>
<li><code>NOT ILIKE</code> - case-insensitive pattern exclusion</li>
</ul>
<p>Pattern matching supports two wildcard characters: <code>%</code> (matches zero or more characters) and <code>_</code> (matches exactly one character).</p>
<p>You can match strings starting with a prefix:</p>
<pre tabindex="0"><code class="language-sql">SELECT *&#10;FROM logs&#10;WHERE blob1 LIKE &#x27;error%&#x27;&#10;</code></pre>
<p>You can also match file extensions (case-insensitive):</p>
<pre tabindex="0"><code class="language-sql">SELECT *&#10;FROM requests&#10;WHERE blob2 ILIKE &#x27;%.jpg&#x27;&#10;</code></pre>
<p>Another example is excluding strings containing specific text:</p>
<pre tabindex="0"><code class="language-sql">SELECT *&#10;FROM events&#10;WHERE blob3 NOT ILIKE &#x27;%debug%&#x27;&#10;</code></pre>
<h4 id="ready-to-get-started">Ready to get started?</h4>
<p>Learn more about the <a href="/analytics/analytics-engine/sql-reference/statements/#having-clause"><code>HAVING</code> clause</a> or <a href="/analytics/analytics-engine/sql-reference/operators/#pattern-matching-operators">pattern matching operators</a> in the Workers Analytics Engine SQL reference documentation.</p>
</div></article></div>

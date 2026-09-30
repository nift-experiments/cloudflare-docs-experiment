---
cp9:
  canonical: https://developers.cloudflare.com/d1/worker-api/return-object/
  description: Understand the D1Result and D1ExecResult objects returned by D1 Worker Binding API query methods.
  full_title: Return objects · Cloudflare D1 docs
  head_html: <title>Return objects · Cloudflare D1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand the D1Result and D1ExecResult objects returned by D1 Worker Binding API query methods."><link rel="canonical" href="https://developers.cloudflare.com/d1/worker-api/return-object/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/d1/worker-api/return-object/index.md"><meta property="og:title" content="Return objects · Cloudflare D1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand the D1Result and D1ExecResult objects returned by D1 Worker Binding API query methods."><meta property="og:url" content="https://developers.cloudflare.com/d1/worker-api/return-object/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="D1"><meta name="algolia_product_filter" content="D1"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="D1"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/d1/worker-api/return-object/#page","headline":"Return objects \u00b7 Cloudflare D1 docs","description":"Understand the D1Result and D1ExecResult objects returned by D1 Worker Binding API query methods.","url":"https://developers.cloudflare.com/d1/worker-api/return-object/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /d1/worker-api/return-object/
  schema: 1
---
<p>Some D1 Worker Binding APIs return a typed object.</p>
<table>
<thead>
<tr>
<th>D1 Worker Binding API</th>
<th>Return object</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/d1/worker-api/prepared-statements/#run"><code>D1PreparedStatement::run</code></a>, <a href="/d1/worker-api/d1-database/#batch"><code>D1Database::batch</code></a></td>
<td><code>D1Result</code></td>
</tr>
<tr>
<td><a href="/d1/worker-api/d1-database/#exec"><code>D1Database::exec</code></a></td>
<td><code>D1ExecResult</code></td>
</tr>
</tbody>
</table>
<h2 id="d1result"><code>D1Result</code></h2>
<p>The methods <a href="/d1/worker-api/prepared-statements/#run"><code>D1PreparedStatement::run</code></a> and <a href="/d1/worker-api/d1-database/#batch"><code>D1Database::batch</code></a> return a typed <a href="#d1result"><code>D1Result</code></a> object for each query statement. This object contains:</p>
<ul>
<li>The success status</li>
<li>A meta object with the internal duration of the operation in milliseconds</li>
<li>The results (if applicable) as an array</li>
</ul>
<pre tabindex="0"><code class="language-js">{&#10;  success: boolean, // true if the operation was successful, false otherwise&#10;  meta: {&#10;    served_by: string // the version of Cloudflare&#x27;s backend Worker that returned the result&#10;    served_by_region: string // the region of the database instance that executed the query&#10;    served_by_primary: boolean // true if (and only if) the database instance that executed the query was the primary&#10;    timings: {&#10;      sql_duration_ms: number // the duration of the SQL query execution by the database instance (not including any network time)&#10;    }&#10;    duration: number, // the duration of the SQL query execution only, in milliseconds&#10;		changes: number, // the number of changes made to the database&#10;		last_row_id: number, // the last inserted row ID, only applies when the table is defined without the `WITHOUT ROWID` option&#10;		changed_db: boolean, // true if something on the database was changed&#10;    size_after: number, // the size of the database after the query is successfully applied&#10;    rows_read: number, // the number of rows read (scanned) by this query&#10;    rows_written: number // the number of rows written by this query&#10;    total_attempts: number //the number of total attempts to successfully execute the query, including retries&#10;  }&#10;  results: array | null, // [] if empty, or null if it does not apply&#10;}&#10;</code></pre>
<h3 id="example">Example</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7163.md")
</div></div>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;success&quot;: true,&#10;  &quot;meta&quot;: {&#10;    &quot;served_by&quot;: &quot;miniflare.db&quot;,&#10;    &quot;served_by_region&quot;: &quot;WEUR&quot;,&#10;    &quot;served_by_primary&quot;: true,&#10;    &quot;timings&quot;: {&#10;      &quot;sql_duration_ms&quot;: 0.2552&#10;    },&#10;    &quot;duration&quot;: 0.2552,&#10;    &quot;changes&quot;: 0,&#10;    &quot;last_row_id&quot;: 0,&#10;    &quot;changed_db&quot;: false,&#10;    &quot;size_after&quot;: 16384,&#10;    &quot;rows_read&quot;: 4,&#10;    &quot;rows_written&quot;: 0&#10;  },&#10;  &quot;results&quot;: [&#10;    {&#10;      &quot;CustomerId&quot;: 11,&#10;      &quot;CompanyName&quot;: &quot;Bs Beverages&quot;,&#10;      &quot;ContactName&quot;: &quot;Victoria Ashworth&quot;&#10;    },&#10;    {&#10;      &quot;CustomerId&quot;: 13,&#10;      &quot;CompanyName&quot;: &quot;Bs Beverages&quot;,&#10;      &quot;ContactName&quot;: &quot;Random Name&quot;&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<h2 id="d1execresult"><code>D1ExecResult</code></h2>
<p>The method <a href="/d1/worker-api/d1-database/#exec"><code>D1Database::exec</code></a> returns a typed <a href="#d1execresult"><code>D1ExecResult</code></a> object for each query statement. This object contains:</p>
<ul>
<li>The number of executed queries</li>
<li>The duration of the operation in milliseconds</li>
</ul>
<pre tabindex="0"><code class="language-js">{&#10;	&quot;count&quot;: number, // the number of executed queries&#10;	&quot;duration&quot;: number // the duration of the operation, in milliseconds&#10;}&#10;</code></pre>
<h3 id="example-1">Example</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7166.md")
</div></div>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;count&quot;: 1,&#10;  &quot;duration&quot;: 1&#10;}&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="storing-large-numbers">Storing large numbers</h3>
@markup("md", "content/.markup/bodies/7160.md")
</aside>

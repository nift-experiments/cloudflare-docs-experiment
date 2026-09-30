---
cp9:
  canonical: https://developers.cloudflare.com/d1/platform/alpha-migration/
  description: Migrate D1 alpha databases to the production-ready storage backend.
  full_title: Alpha database migration guide · Cloudflare D1 docs
  head_html: <title>Alpha database migration guide · Cloudflare D1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Migrate D1 alpha databases to the production-ready storage backend."><link rel="canonical" href="https://developers.cloudflare.com/d1/platform/alpha-migration/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/d1/platform/alpha-migration/index.md"><meta property="og:title" content="Alpha database migration guide · Cloudflare D1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Migrate D1 alpha databases to the production-ready storage backend."><meta property="og:url" content="https://developers.cloudflare.com/d1/platform/alpha-migration/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="D1"><meta name="algolia_product_filter" content="D1"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="D1"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/d1/platform/alpha-migration/#page","headline":"Alpha database migration guide \u00b7 Cloudflare D1 docs","description":"Migrate D1 alpha databases to the production-ready storage backend.","url":"https://developers.cloudflare.com/d1/platform/alpha-migration/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /d1/platform/alpha-migration/
  schema: 1
---
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7346.md")
</aside>
<p>D1's open beta launched in October 2023, and newly created databases use a different underlying architecture that is significantly more reliable and performant, with increased database sizes, improved query throughput, and reduced latency.</p>
<p>This guide will instruct you to recreate alpha D1 databases on our production-ready system.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>You have the <a href="/workers/wrangler/install-and-update/"><code>wrangler</code> command-line tool</a> installed</li>
<li>You are using <code>wrangler</code> version <code>3.33.0</code> or later (released March 2024) as earlier versions do not have the <a href="/d1/platform/release-notes/#2024-03-12"><code>--remote</code> flag</a> required as part of this guide</li>
<li>An 'alpha' D1 database. All databases created before July 27th, 2023 (<a href="/d1/platform/release-notes/#2024-03-12">release notes</a>) use the alpha storage backend, which is no longer supported and was not recommended for production.</li>
</ol>
<h2 id="1-verify-that-a-database-is-alpha"><ol>
<li>Verify that a database is alpha</li>
</ol></h2>
<pre tabindex="0"><code class="language-sh">npx wrangler d1 info &lt;database_name&gt;&#10;</code></pre>
<p>If the database is alpha, the output of the command will include <code>version</code> set to <code>alpha</code>:</p>
<pre tabindex="0"><code>...&#10;│ version           │ alpha                                 │&#10;...&#10;</code></pre>
<h2 id="2-create-a-manual-backup"><ol start="2">
<li>Create a manual backup</li>
</ol></h2>
<pre tabindex="0"><code class="language-sh">npx wrangler d1 backup create &lt;alpha_database_name&gt;&#10;</code></pre>
<h2 id="3-download-the-manual-backup"><ol start="3">
<li>Download the manual backup</li>
</ol></h2>
<p>The command below will download the manual backup of the alpha database as <code>.sqlite3</code> file:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler d1 backup download &lt;alpha_database_name&gt; &lt;backup_id&gt; # See available backups with wrangler d1 backup list &lt;database_name&gt;&#10;</code></pre>
<h2 id="4-convert-the-manual-backup-into-sql-statements"><ol start="4">
<li>Convert the manual backup into SQL statements</li>
</ol></h2>
<p>The command below will convert the manual backup of the alpha database from the downloaded <code>.sqlite3</code> file into SQL statements which can then be imported into the new database:</p>
<pre tabindex="0"><code class="language-sh">sqlite3 db_dump.sqlite3 .dump &gt; db.sql&#10;</code></pre>
<p>Once you have run the above command, you will need to edit the output SQL file to be compatible with D1:</p>
<ol>
<li>Remove <code>BEGIN TRANSACTION</code> and <code>COMMIT;</code> from the file.</li>
<li>Remove the following table creation statement:</li>
</ol>
<pre tabindex="0"><code class="language-sql">CREATE TABLE _cf_KV (&#10; 	key TEXT PRIMARY KEY,&#10; 	value BLOB&#10;) WITHOUT ROWID;&#10;</code></pre>
<h2 id="5-create-a-new-d1-database"><ol start="5">
<li>Create a new D1 database</li>
</ol></h2>
<p>All new D1 databases use the updated architecture by default.</p>
<p>Run the following command to create a new database:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler d1 create &lt;new_database_name&gt;&#10;</code></pre>
<h2 id="6-run-sql-statements-against-the-new-d1-database"><ol start="6">
<li>Run SQL statements against the new D1 database</li>
</ol></h2>
<pre tabindex="0"><code class="language-sh">npx wrangler d1 execute &lt;new_database_name&gt; --remote --file=./db.sql&#10;</code></pre>
<h2 id="7-delete-your-alpha-database"><ol start="7">
<li>Delete your alpha database</li>
</ol></h2>
<p>To delete your previous alpha database, run:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler d1 delete &lt;alpha_database_name&gt;&#10;</code></pre>

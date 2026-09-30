---
cp9:
  canonical: https://developers.cloudflare.com/r2-data-catalog/get-started/
  description: Learn how to enable the R2 Data Catalog on your bucket, load sample data, and run your first query.
  full_title: Getting started · Cloudflare R2 Data Catalog docs
  head_html: <title>Getting started · Cloudflare R2 Data Catalog docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to enable the R2 Data Catalog on your bucket, load sample data, and run your first query."><link rel="canonical" href="https://developers.cloudflare.com/r2-data-catalog/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2-data-catalog/get-started/index.md"><meta property="og:title" content="Getting started · Cloudflare R2 Data Catalog docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to enable the R2 Data Catalog on your bucket, load sample data, and run your first query."><meta property="og:url" content="https://developers.cloudflare.com/r2-data-catalog/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2 Data Catalog"><meta name="algolia_product_filter" content="R2 Data Catalog"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="R2 Data Catalog"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2-data-catalog/get-started/#page","headline":"Getting started \u00b7 Cloudflare R2 Data Catalog docs","description":"Learn how to enable the R2 Data Catalog on your bucket, load sample data, and run your first query.","url":"https://developers.cloudflare.com/r2-data-catalog/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /r2-data-catalog/get-started/
  schema: 1
---
<p>This guide will instruct you through:</p>
<ul>
<li>Creating your first <a href="/r2/buckets/">R2 bucket</a> and enabling its <a href="/r2-data-catalog/">data catalog</a>.</li>
<li>Creating an <a href="/r2/api/tokens/">API token</a> needed for query engines to authenticate with your data catalog.</li>
<li>Using <a href="https://py.iceberg.apache.org/">PyIceberg</a> to create your first Iceberg table in a <a href="https://marimo.io/">marimo</a> Python notebook.</li>
<li>Using <a href="https://py.iceberg.apache.org/">PyIceberg</a> to load sample data into your table and query it.</li>
</ul>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/558.md")
</div></details>
<h2 id="1-create-an-r2-bucket-and-enable-the-data-catalog"><ol>
<li>Create an R2 bucket and enable the data catalog</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/563.md")
</div></div>
<h2 id="2-create-an-api-token"><ol start="2">
<li>Create an API token</li>
</ol></h2>
<p>Iceberg clients (including <a href="https://py.iceberg.apache.org/">PyIceberg</a>) must authenticate to the catalog with an <a href="/r2/api/tokens/">R2 API token</a> that has both R2 and catalog permissions.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/564.md")
</div>
<h2 id="3-install-uv"><ol start="3">
<li>Install uv</li>
</ol></h2>
<p>You need to install a Python package manager. In this guide, use <a href="https://docs.astral.sh/uv/">uv</a>. If you do not already have uv installed, follow the <a href="https://docs.astral.sh/uv/getting-started/installation/">installing uv guide</a>.</p>
<h2 id="4-install-marimo-and-set-up-your-project-with-uv"><ol start="4">
<li>Install marimo and set up your project with uv</li>
</ol></h2>
<p>We will use <a href="https://github.com/marimo-team/marimo">marimo</a> as a Python notebook.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/565.md")
</div>
<h2 id="5-create-a-python-notebook-to-interact-with-the-data-warehouse"><ol start="5">
<li>Create a Python notebook to interact with the data warehouse</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/566.md")
</div>
<p>In the Python notebook above, you:</p>
<ol>
<li>Connect to your catalog.</li>
<li>Create the <code>default</code> namespace.</li>
<li>Create a simple PyArrow table.</li>
<li>Create (or load) the <code>people</code> table in the <code>default</code> namespace.</li>
<li>Append sample data to the table.</li>
<li>Print the contents of the table.</li>
<li>(Optional) Drop the <code>people</code> table we created for this tutorial.</li>
</ol>
<h2 id="learn-more">Learn more</h2>
<div class="nb-card nb-link-card"><h3 id="card-managing-catalogs-r2-data-catalog-manage-catalogs"><a href="/r2-data-catalog/manage-catalogs/">Managing catalogs</a></h3><p>Enable or disable R2 Data Catalog on your bucket, retrieve configuration details, and authenticate your Iceberg engine.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-connect-to-iceberg-engines-r2-data-catalog-config-examples"><a href="/r2-data-catalog/config-examples/">Connect to Iceberg engines</a></h3><p>Find detailed setup instructions for Apache Spark and other common query engines.</p></div>

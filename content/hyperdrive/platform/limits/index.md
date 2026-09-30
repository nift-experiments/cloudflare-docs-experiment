---
cp9:
  canonical: https://developers.cloudflare.com/hyperdrive/platform/limits/
  description: Configuration, connection, and query limits that apply to Hyperdrive.
  full_title: Limits · Cloudflare Hyperdrive docs
  head_html: <title>Limits · Cloudflare Hyperdrive docs</title><meta name="generator" content="Nift"><meta name="description" content="Configuration, connection, and query limits that apply to Hyperdrive."><link rel="canonical" href="https://developers.cloudflare.com/hyperdrive/platform/limits/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/hyperdrive/platform/limits/index.md"><meta property="og:title" content="Limits · Cloudflare Hyperdrive docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configuration, connection, and query limits that apply to Hyperdrive."><meta property="og:url" content="https://developers.cloudflare.com/hyperdrive/platform/limits/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Hyperdrive"><meta name="algolia_product_filter" content="Hyperdrive"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Hyperdrive"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/hyperdrive/platform/limits/#page","headline":"Limits \u00b7 Cloudflare Hyperdrive docs","description":"Configuration, connection, and query limits that apply to Hyperdrive.","url":"https://developers.cloudflare.com/hyperdrive/platform/limits/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /hyperdrive/platform/limits/
  schema: 1
---
<p>The following limits apply to Hyperdrive configurations, connections, and queries made to your configured origin databases.</p>
<h2 id="configuration-limits">Configuration limits</h2>
<p>These limits apply when creating or updating Hyperdrive configurations.</p>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Free</th>
<th>Paid</th>
</tr>
</thead>
<tbody>
<tr>
<td>Maximum configured databases</td>
<td>10 per account</td>
<td>25 per account</td>
</tr>
<tr>
<td>Maximum username length <sup><a href="#footnote-1">1</a></sup></td>
<td>63 characters (bytes)</td>
<td>63 characters (bytes)</td>
</tr>
<tr>
<td>Maximum database name length <sup><a href="#footnote-1">1</a></sup></td>
<td>63 characters (bytes)</td>
<td>63 characters (bytes)</td>
</tr>
</tbody>
</table>
<h2 id="connection-limits">Connection limits</h2>
<p>These limits apply to connections between Hyperdrive and your origin database.</p>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Free</th>
<th>Paid</th>
</tr>
</thead>
<tbody>
<tr>
<td>Initial connection timeout</td>
<td>15 seconds</td>
<td>15 seconds</td>
</tr>
<tr>
<td>Idle connection timeout</td>
<td>10 minutes</td>
<td>10 minutes</td>
</tr>
<tr>
<td>Maximum origin database connections (per configuration) <sup><a href="#footnote-2">2</a></sup></td>
<td>~20 connections</td>
<td>~100 connections</td>
</tr>
</tbody>
</table>
<p>Hyperdrive does not limit the number of concurrent client connections from your Workers. However, Hyperdrive limits connections to your origin database because most hosted databases have connection limits.</p>
<h3 id="connection-errors">Connection errors</h3>
<p>When Hyperdrive cannot acquire a connection to your origin database, you may see one of the following errors:</p>
<table>
<thead>
<tr>
<th>Error message</th>
<th>Cause</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Failed to acquire a connection from the pool.</code></td>
<td>The connection pool is exhausted because connections are held open too long. Long-running queries or transactions are a common cause.</td>
</tr>
<tr>
<td><code>Server connection attempt failed: connection_refused</code></td>
<td>Your origin database is rejecting connections. This can occur when a firewall blocks Hyperdrive, or when your database provider's connection limit is exceeded.</td>
</tr>
</tbody>
</table>
<p>For a complete list of error codes, refer to <a href="/hyperdrive/observability/troubleshooting/">Troubleshoot and debug</a>.</p>
<h2 id="query-limits">Query limits</h2>
<p>These limits apply to queries sent through Hyperdrive.</p>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Free</th>
<th>Paid</th>
</tr>
</thead>
<tbody>
<tr>
<td>Maximum query (statement) duration</td>
<td>60 seconds</td>
<td>60 seconds</td>
</tr>
<tr>
<td>Maximum cached query response size</td>
<td>50 MB</td>
<td>50 MB</td>
</tr>
</tbody>
</table>
<p>Queries exceeding the maximum duration are terminated. Query responses larger than 50 MB are not cached but are still returned to your Worker.</p>
<h2 id="request-a-limit-increase">Request a limit increase</h2>
<p>You can request adjustments to limits that conflict with your project goals by contacting Cloudflare. Not all limits can be increased.</p>
<p>To request an increase, submit a <a href="https://forms.gle/eX6pXvit1wBv77Yw5">Limit Increase Request form</a>. You can also ask questions in the Hyperdrive channel on <a href="https://discord.cloudflare.com/">Cloudflare's Discord community</a>.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">This is a limit enforced by PostgreSQL. Some database providers may enforce smaller limits.</li>
<li id="footnote-2">Hyperdrive is a distributed system, so a client may be unable to reach an existing pool. In this scenario, a new pool is established with its own connection allocation. This prioritizes availability over strict limit enforcement, which means connection counts may occasionally exceed the listed limits.</li></ol></section>

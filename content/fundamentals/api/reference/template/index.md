---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/api/reference/template/
  description: Explore Cloudflare's API token templates to efficiently manage permissions. Start with a template and customize token permissions and resources as needed.
  full_title: API token templates · Cloudflare Fundamentals docs
  head_html: <title>API token templates · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Explore Cloudflare&#x27;s API token templates to efficiently manage permissions. Start with a template and customize token permissions and resources as needed."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/api/reference/template/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/api/reference/template/index.md"><meta property="og:title" content="API token templates · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Explore Cloudflare&#x27;s API token templates to efficiently manage permissions. Start with a template and customize token permissions and resources as needed."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/api/reference/template/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Fundamentals,API documentation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/api/reference/template/#page","headline":"API token templates \u00b7 Cloudflare Fundamentals docs","description":"Explore Cloudflare's API token templates to efficiently manage permissions. Start with a template and customize token permissions and resources as needed.","url":"https://developers.cloudflare.com/fundamentals/api/reference/template/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/api/reference/template/
  schema: 1
---
<p>Below is a table of the currently available API token templates and the default <a href="/fundamentals/api/reference/permissions/">token permissions</a> they grant. You can start creating a token with one of these templates and modify the permissions and resources from there.</p>
<table>
<tbody>
<tr>
<th>Template Name</th>
<th>Permission</th>
<th>Resource</th>
</tr>
<tr>
<td>Edit Zone DNS</td>
<td>DNS Write</td>
<td>Zone</td>
</tr>
<tr>
<td rowspan="2">Read billing info</td>
<td>Billing Read</td>
<td>Account</td>
</tr>
<tr>
<td>Account resources: Include all accounts</td>
<td></td>
</tr>
<tr>
<td rowspan="2">Read analytics and logs</td>
<td>Analytics Read</td>
<td>Zone</td>
</tr>
<tr>
<td>Logs Read</td>
<td>Zone</td>
</tr>
<tr>
<td rowspan="8">Edit Cloudflare Workers</td>
<td>Workers Routes Write</td>
<td>Zone</td>
</tr>
<tr>
<td>Workers Scripts Write</td>
<td>Account</td>
</tr>
<tr>
<td>Workers KV Storage Write</td>
<td>Account</td>
</tr>
<tr>
<td>Workers Tail Read</td>
<td>Account</td>
</tr>
<tr>
<td>Workers R2 Storage Write</td>
<td>Account</td>
</tr>
<tr>
<td>Account Settings Read</td>
<td>Account</td>
</tr>
<tr>
<td>User Details Read</td>
<td>User</td>
</tr>
<tr>
<td>User Memberships Read</td>
<td>User</td>
</tr>
<tr>
<td rowspan="2">Edit load balancing configuration</td>
<td>Load Balancing: Monitors and Pools Write</td>
<td>Account</td>
</tr>
<tr>
<td>Load Balancers Write</td>
<td>Zone</td>
</tr>
<tr>
<td rowspan="8">WordPress</td>
<td>Analytics Read</td>
<td>Zone</td>
</tr>
<tr>
<td>Zone Read</td>
<td>Zone</td>
</tr>
<tr>
<td>Zone Settings Write</td>
<td>Zone</td>
</tr>
<tr>
<td>Account Settings Read</td>
<td>Account</td>
</tr>
<tr>
<td>DNS Read</td>
<td>Zone</td>
</tr>
<tr>
<td>Cache Purge</td>
<td>Zone</td>
</tr>
<tr>
<td>Account resources: Include all accounts</td>
<td></td>
</tr>
<tr>
<td>Zone resources: Include all zones</td>
<td></td>
</tr>
<tr>
<td>Create Additional Tokens</td>
<td>API Tokens Write</td>
<td>User</td>
</tr>
<tr>
<td rowspan="3">Read All Resources</td>
<td>
				<em>(All read permissions)</em>
</td>
<td>Account, Zone, User</td>
</tr>
<tr>
<td>Account resources: Include all accounts</td>
<td></td>
</tr>
<tr>
<td>Zone resources: Include all zones</td>
<td></td>
</tr>
</tbody>
</table>

---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/reference/cloudflare-ray-id/
  description: Use Cloudflare Ray IDs to identify and trace individual requests through Security Events, Log Explorer, and server logs.
  full_title: Cloudflare Ray ID · Cloudflare Fundamentals docs
  head_html: <title>Cloudflare Ray ID · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Cloudflare Ray IDs to identify and trace individual requests through Security Events, Log Explorer, and server logs."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/reference/cloudflare-ray-id/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/reference/cloudflare-ray-id/index.md"><meta property="og:title" content="Cloudflare Ray ID · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Cloudflare Ray IDs to identify and trace individual requests through Security Events, Log Explorer, and server logs."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/reference/cloudflare-ray-id/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/reference/cloudflare-ray-id/#page","headline":"Cloudflare Ray ID \u00b7 Cloudflare Fundamentals docs","description":"Use Cloudflare Ray IDs to identify and trace individual requests through Security Events, Log Explorer, and server logs.","url":"https://developers.cloudflare.com/fundamentals/reference/cloudflare-ray-id/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/reference/cloudflare-ray-id/
  schema: 1
---
<p>A <strong>Cloudflare Ray ID</strong> is an identifier given to every request that goes through Cloudflare.</p>
<p>Ray IDs are particularly useful when evaluating Security Events for patterns or false positives or more generally understanding your application traffic.</p>
<p>Ray IDs are added as a <a href="/fundamentals/reference/http-headers/#cf-ray">request header, cf-ray</a>, to the connection from Cloudflare to the origin web server.
As such the Ray IDs can be found using the Developer Tools in your browser or using curl with the <code>-v</code> option to show the headers.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8807.md")
</aside>
<h2 id="look-up-ray-ids">Look up Ray IDs</h2>
<h3 id="security-events">Security events</h3>
<p>All customers can view Ray IDs and associated information — IP address, user agent, ASN, etc. — by looking through <a href="/waf/analytics/security-events/#sampled-logs">sampled logs</a> in Security Events.</p>
<p><img src="/assets/upstream/images/fundamentals/ray-id.png" alt="Example list of events in sampled logs, with the Ray ID highlighted from one of the expanded events to show its details" /></p>
<p>Additionally, you can <a href="/waf/analytics/security-events/#adjust-displayed-data">add filters</a> to look for specific Ray IDs.</p>
<p><img src="/assets/upstream/images/waf/events-add-filter.png" alt="Example of adding a new filter in Security Events for the Block action" /></p>
<p>Please note that Security Events may use sampled data to improve performance. If sampled data is applied to your search, you might not see all events, and filters might not return the expected results. To display more events, select a smaller timeframe.</p>
<h3 id="log-explorer">Log Explorer</h3>
<p><a href="/log-explorer/">Log Explorer</a> provides access to Cloudflare logs with all the context available within the Cloudflare platform.
You can monitor security and performance issues with custom dashboards or investigate and troubleshoot issues with log search.
Log explorer allows you to <a href="/log-explorer/log-search/">build queries</a> for filtering specific Ray IDs.</p>
<h3 id="logs">Logs</h3>
<p>Enterprise customers can enable Ray ID as a field in their <a href="/logs/">Cloudflare Logs</a>.</p>
<h3 id="server-logs">Server logs</h3>
<p>For more details about sending Ray IDs to your server logs, refer to the <a href="/fundamentals/reference/http-headers/#cf-ray">Cf-Ray</a> header.</p>

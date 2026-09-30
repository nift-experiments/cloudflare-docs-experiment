---
cp9:
  canonical: https://developers.cloudflare.com/zaraz/reference/properties-reference/
  description: Built-in properties available in Zaraz events.
  full_title: Properties reference · Cloudflare Zaraz docs
  head_html: <title>Properties reference · Cloudflare Zaraz docs</title><meta name="generator" content="Nift"><meta name="description" content="Built-in properties available in Zaraz events."><link rel="canonical" href="https://developers.cloudflare.com/zaraz/reference/properties-reference/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/zaraz/reference/properties-reference/index.md"><meta property="og:title" content="Properties reference · Cloudflare Zaraz docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Built-in properties available in Zaraz events."><meta property="og:url" content="https://developers.cloudflare.com/zaraz/reference/properties-reference/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Zaraz"><meta name="algolia_product_filter" content="Zaraz"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Zaraz"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/zaraz/reference/properties-reference/#page","headline":"Properties reference \u00b7 Cloudflare Zaraz docs","description":"Built-in properties available in Zaraz events.","url":"https://developers.cloudflare.com/zaraz/reference/properties-reference/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /zaraz/reference/properties-reference/
  schema: 1
---
<p>Cloudflare Zaraz offers properties that you can use when configuring the product. They are helpful to send data to a third-party tool or to create triggers as they have context about a specific user's browser session and the actions they take on the website. Below is a list of the properties you can access from the Cloudflare dashboard and their values.</p>
<h2 id="web-api">Web API</h2>
<table>
<thead>
<tr>
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Event Name</em></td>
<td>Returns the name of the event sent using the Track method of the Web API. Refer to the <a href="/zaraz/web-api/track/">Track method</a> for more information.</td>
</tr>
<tr>
<td><em>Track Property name:</em></td>
<td>Returns the value of a <code>zaraz.track()</code> <code>eventProperties</code> key. The key can either be directly used in <code>zaraz.track()</code> or set using <code>zaraz.set()</code>. Set the name of your key here. Refer to the <a href="/zaraz/web-api/set/">Set method</a> for more information.</td>
</tr>
</tbody>
</table>
<h2 id="page-properties">Page Properties</h2>
<table>
<thead>
<tr>
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Page character encoding</em></td>
<td>Returns the document character encoding from <code>document.characterSet</code>.</td>
</tr>
<tr>
<td><em>Page referrer</em></td>
<td>Returns the page referrer from <code>document.referrer</code>.</td>
</tr>
<tr>
<td><em>Page title</em></td>
<td>Returns the page title.</td>
</tr>
<tr>
<td><em>Query param name:</em></td>
<td>Returns the value of a URL query parameter. When you choose this variable, you need to set the name of your parameter.</td>
</tr>
<tr>
<td><em>URL</em></td>
<td>Returns a string containing the entire URL.</td>
</tr>
<tr>
<td><em>URL base domain</em></td>
<td>Returns the base domain part of the URL, without any subdomains.</td>
</tr>
<tr>
<td><em>URL host</em></td>
<td>Returns the domain (that is, the hostname) followed by a <code>:</code> and the port of the URL (if a port was specified).</td>
</tr>
<tr>
<td><em>URL hostname</em></td>
<td>Returns the domain of the URL.</td>
</tr>
<tr>
<td><em>URL origin</em></td>
<td>Returns the origin of the URL — that is, its scheme, domain, and port.</td>
</tr>
<tr>
<td><em>URL password</em></td>
<td>Returns the password specified before the domain name.</td>
</tr>
<tr>
<td><em>URL pathname</em></td>
<td>Returns the path of the URL, including the initial <code>/</code>. Does not include the query string or fragment.</td>
</tr>
<tr>
<td><em>URL port</em></td>
<td>Returns the port number of the URL.</td>
</tr>
<tr>
<td><em>URL protocol scheme</em></td>
<td>Returns the protocol scheme of the URL, including the final <code>:</code>.</td>
</tr>
<tr>
<td><em>URL query parameters</em></td>
<td>Returns query parameters provided, beginning with the leading <code>?</code> character.</td>
</tr>
<tr>
<td><em>URL username</em></td>
<td>Returns the username specified before the domain name.</td>
</tr>
</tbody>
</table>
<h2 id="cookies">Cookies</h2>
<table>
<thead>
<tr>
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Cookie name:</em></td>
<td>Returns cookies obtained from the browser <code>document</code>.</td>
</tr>
</tbody>
</table>
<h2 id="device-properties">Device properties</h2>
<table>
<thead>
<tr>
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Browser engine</em></td>
<td>Returns the type of browser engine (for example, <code>WebKit</code>).</td>
</tr>
<tr>
<td><em>Browser engine version</em></td>
<td>Returns the version of the browser’s engine.</td>
</tr>
<tr>
<td><em>Browser name</em></td>
<td>Returns the browser’s name.</td>
</tr>
<tr>
<td><em>Browser version</em></td>
<td>Returns the browser’s version.</td>
</tr>
<tr>
<td><em>Device CPU</em></td>
<td>Returns the device’s CPU.</td>
</tr>
<tr>
<td><em>Device IP address</em></td>
<td>Returns the incoming IP address.</td>
</tr>
<tr>
<td><em>Device language</em></td>
<td>Returns the language used.</td>
</tr>
<tr>
<td><em>Device screen resolution</em></td>
<td>Returns the screen resolution of the device.</td>
</tr>
<tr>
<td><em>Device type</em></td>
<td>Returns the type of device used (for example, <code>iPhone</code>).</td>
</tr>
<tr>
<td><em>Device viewport</em></td>
<td>Returns the visible web page area in user’s device.</td>
</tr>
<tr>
<td><em>Operating system name</em></td>
<td>Returns the operating system.</td>
</tr>
<tr>
<td><em>Operating system version</em></td>
<td>Returns the version of the operating system.</td>
</tr>
<tr>
<td><em>User-agent string</em></td>
<td>Returns the browser’s user agent.</td>
</tr>
</tbody>
</table>
<h2 id="device-location">Device location</h2>
<table>
<thead>
<tr>
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>City</em></td>
<td>Returns the city of the incoming request. For example, <code>Lisbon</code>.</td>
</tr>
<tr>
<td><em>Continent</em></td>
<td>Returns the continent of the incoming request. For example, <code>EU</code></td>
</tr>
<tr>
<td><em>Country</em> code</td>
<td>Returns the country code of the incoming request. For example, <code>PT</code>.</td>
</tr>
<tr>
<td><em>EU</em> country</td>
<td>Returns a <code>1</code> if the country of the incoming request is in the European Union, and a <code>0</code> if it is not.</td>
</tr>
<tr>
<td><em>Region</em></td>
<td>Returns the <a href="https://en.wikipedia.org/wiki/ISO_3166-2">ISO 3166-2</a> name for the first level region associated with the IP address of the incoming request. For example, <code>Lisbon</code>.</td>
</tr>
<tr>
<td><em>Region</em> code</td>
<td>Returns the <a href="https://en.wikipedia.org/wiki/ISO_3166-2">ISO 3166-2</a> region code associated with the IP address of the incoming request. For example, <code>11</code>.</td>
</tr>
<tr>
<td><em>Timezone</em></td>
<td>Returns the timezone of the incoming request. For example, <code>Europe/Lisbon</code>.</td>
</tr>
</tbody>
</table>
<h2 id="miscellaneous">Miscellaneous</h2>
<table>
<thead>
<tr>
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Random number</em></td>
<td>Returns a random number unique to each request.</td>
</tr>
<tr>
<td><em>Timestamp (milliseconds)</em></td>
<td>Returns the Unix time in milliseconds.</td>
</tr>
<tr>
<td><em>Timestamp (seconds)</em></td>
<td>Returns the Unix time in seconds.</td>
</tr>
</tbody>
</table>

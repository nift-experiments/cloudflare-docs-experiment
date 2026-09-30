---
cp9:
  canonical: https://developers.cloudflare.com/zaraz/reference/context/
  description: Data available in the Zaraz context object for triggers and actions.
  full_title: Zaraz Context · Cloudflare Zaraz docs
  head_html: <title>Zaraz Context · Cloudflare Zaraz docs</title><meta name="generator" content="Nift"><meta name="description" content="Data available in the Zaraz context object for triggers and actions."><link rel="canonical" href="https://developers.cloudflare.com/zaraz/reference/context/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/zaraz/reference/context/index.md"><meta property="og:title" content="Zaraz Context · Cloudflare Zaraz docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Data available in the Zaraz context object for triggers and actions."><meta property="og:url" content="https://developers.cloudflare.com/zaraz/reference/context/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Zaraz"><meta name="algolia_product_filter" content="Zaraz"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Zaraz"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/zaraz/reference/context/#page","headline":"Zaraz Context \u00b7 Cloudflare Zaraz docs","description":"Data available in the Zaraz context object for triggers and actions.","url":"https://developers.cloudflare.com/zaraz/reference/context/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /zaraz/reference/context/
  schema: 1
---
<p>The Zaraz Context is a versatile object that provides a set of configurable properties for Zaraz, a web analytics tool for tracking user behavior on websites. These properties can be accessed and utilized across various components, including <a href="/zaraz/variables/worker-variables/">Worker Variables</a> and <a href="/zaraz/advanced/using-jsonata/">JSONata expressions</a>.</p>
<p>System properties, which are automatically collected by Zaraz, provide insights into the user's environment and device, while Client properties, obtained through <a href="/zaraz/web-api/">Zaraz Web API</a> calls like zaraz.track(), offer additional information on user behavior and actions.</p>
<h2 id="system-properties">System properties</h2>
<h3 id="page-information">Page information</h3>
<table>
<thead>
<tr>
<th>Property</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>system.page.query</code></td>
<td>Object</td>
<td>Key-Value object containing all query parameters in the current URL.</td>
</tr>
<tr>
<td><code>system.page.title</code></td>
<td>String</td>
<td>Current page title.</td>
</tr>
<tr>
<td><code>system.page.url</code></td>
<td>URL</td>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/URL">URL</a> Object containing information about the current URL</td>
</tr>
<tr>
<td><code>system.page.referrer</code></td>
<td>String</td>
<td>Current page referrer from <code>document.referrer</code>.</td>
</tr>
<tr>
<td><code>system.page.encoding</code></td>
<td>String</td>
<td>Current page character encoding from <code>document.characterSet</code>.</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<h3 id="cookies">Cookies</h3>
<table>
<thead>
<tr>
<th>Property</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>system.cookies</code></td>
<td>Object</td>
<td>Key-Value object containing all present cookies.</td>
</tr>
</tbody>
</table>
<p>The keys inside the <code>system.cookies</code> are the cookies name. The property <code>system.cookies.foo</code> will return the value of the a cookie named <code>foo</code>.</p>
<h3 id="device-information">Device information</h3>
<table>
<thead>
<tr>
<th>Property</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>system.device.ip</code></td>
<td>String</td>
<td>Visitor incoming IP address.</td>
</tr>
<tr>
<td><code>system.device.resolution</code></td>
<td>String</td>
<td>Screen resolution for device.</td>
</tr>
<tr>
<td><code>system.device.viewport</code></td>
<td>String</td>
<td>Visible web page area in user’s device.</td>
</tr>
<tr>
<td><code>system.device.language</code></td>
<td>String</td>
<td>Language used in user's device.</td>
</tr>
<tr>
<td><code>system.device.location</code></td>
<td>Object</td>
<td>All location-related keys from <a href="/workers/runtime-apis/request/#incomingrequestcfproperties">IncomingRequestCfProperties</a></td>
</tr>
<tr>
<td><code>system.device.user-agent.ua</code></td>
<td>String</td>
<td>Browser user agent.</td>
</tr>
<tr>
<td><code>system.device.user-agent.browser.name</code></td>
<td>String</td>
<td>Browser name.</td>
</tr>
<tr>
<td><code>system.device.user-agent.browser.version</code></td>
<td>String</td>
<td>Browser version.</td>
</tr>
<tr>
<td><code>system.device.user-agent.engine.name</code></td>
<td>String</td>
<td>Type of browser engine (for example, WebKit).</td>
</tr>
<tr>
<td><code>system.device.user-agent.engine.version</code></td>
<td>String</td>
<td>Version of the browser engine.</td>
</tr>
<tr>
<td><code>system.device.user-agent.os.name</code></td>
<td>String</td>
<td>Operating system.</td>
</tr>
<tr>
<td><code>system.device.user-agent.os.version</code></td>
<td>String</td>
<td>Version of the operating system.</td>
</tr>
<tr>
<td><code>system.device.user-agent.device</code></td>
<td>String</td>
<td>Type of device used (for example, iPhone).</td>
</tr>
<tr>
<td><code>system.device.user-agent.cpu</code></td>
<td>String</td>
<td>Device’s CPU.</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<h3 id="consent-management">Consent Management</h3>
<table>
<thead>
<tr>
<th>Property</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>system.consent</code></td>
<td>Object</td>
<td>Key-value object containing the current consent status from the Zaraz Consent Manager.</td>
</tr>
</tbody>
</table>
<p>The keys inside the <code>system.consent</code> object are purpose IDs, and values are <code>true</code> for consent, <code>false</code> for lack of consent.</p>
<h3 id="managed-components">Managed Components</h3>
<table>
<thead>
<tr>
<th>Property</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>system.clientKV</code></td>
<td>Object</td>
<td>Key-value object containing all the KV data from your Managed Components.</td>
</tr>
</tbody>
</table>
<p>The keys inside the <code>system.clientKV</code> object are formatted as Tool ID, underscore, Key name. Assuming you want to read the value of the <code>ga4</code> key used by a tool with ID <code>abcd</code>, the path would be <code>system.clientKV.abcd_ga4</code>.</p>
<h3 id="miscellaneous">Miscellaneous</h3>
<table>
<thead>
<tr>
<th>Property</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>system.misc.random</code></td>
<td>Number</td>
<td>Random number unique to each request.</td>
</tr>
<tr>
<td><code>system.misc.timestamp</code></td>
<td>Number</td>
<td>Unix time in seconds.</td>
</tr>
<tr>
<td><code>system.misc.timestampMilliseconds</code></td>
<td>Number</td>
<td>Unix time in milliseconds.</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<h2 id="event-properties">Event properties</h2>
<table>
<thead>
<tr>
<th>Property</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>client.__zarazTrack</code></td>
<td>String</td>
<td>Returns the name of the event sent using the Track method of the Web API. Refer to <a href="/zaraz/web-api/track/">Zaraz Track</a> for more information.</td>
</tr>
<tr>
<td><code>client.&lt;KEY_NAME&gt;</code></td>
<td>String</td>
<td>Returns the value of a <code>zaraz.track()</code> <code>eventProperties</code> key. The key can either be directly used in <code>zaraz.track()</code> or set using <code>zaraz.set()</code>. Replace <code>&lt;KEY_NAME&gt;</code> with the name of your key. Refer to <a href="/zaraz/web-api/track/">Zaraz Track</a> for more information.</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/build-the-page/components/api-request/
  description: Generate curl commands from OpenAPI schema.
  full_title: API request · Cloudflare Style Guide
  head_html: <title>API request · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Generate curl commands from OpenAPI schema."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/build-the-page/components/api-request/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/build-the-page/components/api-request/index.md"><meta property="og:title" content="API request · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Generate curl commands from OpenAPI schema."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/build-the-page/components/api-request/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/build-the-page/components/api-request/#page","headline":"API request \u00b7 Cloudflare Style Guide","description":"Generate curl commands from OpenAPI schema.","url":"https://developers.cloudflare.com/style-guide/build-the-page/components/api-request/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/build-the-page/components/api-request/
  schema: 1
---
<h2 id="import">Import</h2>
<pre tabindex="0"><code class="language-mdx">import { APIRequest } from &quot;~/components&quot;;&#10;</code></pre>
<h2 id="usage">Usage</h2>
<pre tabindex="0"><code class="language-mdx">import { APIRequest } from &quot;~/components&quot;;&#10;&#10;&lt;APIRequest&#10;	path=&quot;/zones/{zone_id}/api_gateway/settings/schema_validation&quot;&#10;	method=&quot;PUT&quot;&#10;	json={{&#10;		validation_default_mitigation_action: &quot;block&quot;,&#10;	}}&#10;	code={{&#10;		mark: [5, &quot;block&quot;],&#10;	}}&#10;	roles=&quot;Domain&quot;&#10;/&gt;&#10;&#10;&lt;APIRequest&#10;	path=&quot;/zones/{zone_id}/hostnames/settings/{setting_id}/{hostname}&quot;&#10;	method=&quot;DELETE&quot;&#10;	parameters={{&#10;		setting_id: &quot;ciphers&quot;,&#10;	}}&#10;/&gt;&#10;&#10;&lt;APIRequest&#10;	path=&quot;/accounts/{account_id}/images/v2/direct_upload&quot;&#10;	method=&quot;POST&quot;&#10;	form={{&#10;		requireSignedURLs: true,&#10;		metadata: &#x27;{&quot;key&quot;:&quot;value&quot;}&#x27;,&#10;	}}&#10;/&gt;&#10;&#10;&lt;APIRequest&#10;	path=&quot;/zones/{zone_id}/cloud_connector/rules&quot;&#10;	method=&quot;PUT&quot;&#10;	json={[&#10;		{&#10;			expression: &#x27;http.request.uri.path wildcard &quot;/images/*&quot;&#x27;,&#10;			provider: &quot;cloudflare_r2&quot;,&#10;			description: &quot;Connect to R2 bucket containing images&quot;,&#10;			parameters: {&#10;				host: &quot;mybucketcustomdomain.example.com&quot;,&#10;			},&#10;		},&#10;	]}&#10;/&gt;&#10;&#10;&lt;APIRequest&#10;	path=&quot;/zones/{zone_id}/page_shield/scripts&quot;&#10;	method=&quot;GET&quot;&#10;	parameters={{&#10;		direction: &quot;asc&quot;,&#10;	}}&#10;/&gt;&#10;</code></pre>
<h2 id="props"><code>&lt;APIRequest&gt;</code> Props</h2>
<h3 id="path"><code>path</code></h3>
<p><strong>required</strong></p>
<p><strong>type:</strong> <code>string</code></p>
<p>The path for the API endpoint.</p>
<p>This can be found in our <a href="https://api.cloudflare.com">API documentation</a>, under the name of the endpoint.</p>
<h3 id="method"><code>method</code></h3>
<p><strong>required</strong></p>
<p><strong>type:</strong> <code>&quot;GET&quot; | &quot;POST&quot; | &quot;PUT&quot; | &quot;PATCH&quot; | &quot;DELETE&quot; | &quot;HEAD&quot;</code></p>
<p>The HTTP method to use.</p>
<h3 id="parameters"><code>parameters</code></h3>
<p><strong>type:</strong> <code>Record&lt;string, any&gt;</code></p>
<p>The parameters to substitute - either in the URL path or as query parameters.</p>
<p>For example, <code>/zones/{zone_id}/page_shield/scripts</code> can be transformed into <code>/zones/123/page_shield/scripts?direction=asc</code> with the following:</p>
<pre tabindex="0"><code class="language-mdx">parameters={{&#10;	zone_id: &quot;123&quot;,&#10;	direction: &quot;asc&quot;&#10;}}&#10;</code></pre>
<p>If not provided, the component will default to an environment variable. For example, <code>{setting_id}</code> will be replaced with <code>$SETTING_ID</code>.</p>
<h3 id="json"><code>json</code></h3>
<p><strong>type:</strong> <code>Record&lt;string, any&gt; | Record&lt;string, any&gt;[]</code></p>
<p>The JSON payload to send.</p>
<p>If required properties are missing, the component will throw an error.</p>
<p>Functionally, <a href="https://everything.curl.dev/http/post/json.html">the <code>--json</code> option</a> is equivalent to the <code>--data</code> option in cURL, but handles a few additional headers automatically.</p>
<h3 id="form"><code>form</code></h3>
<p><strong>type:</strong> <code>Record&lt;string, any&gt;</code></p>
<p>The FormData payload to send.</p>
<p>This field is not currently validated against the schema.</p>
<h3 id="code"><code>code</code></h3>
<p><strong>type:</strong> <code>object</code></p>
<p>An object of Astro <code>Code</code> props. Refer to the <a href="https://docs.astro.build/en/reference/api-reference/#code-">Astro <code>Code</code> component documentation</a> for available props.</p>
<h3 id="roles"><code>roles</code></h3>
<p><strong>type:</strong> <code>string | boolean</code></p>
<p><strong>default:</strong> <code>true</code></p>
<p>If set to <code>true</code>, which is the default, all API token roles will show.</p>
<p>If set to <code>false</code>, API token roles will not be displayed.</p>
<p>If set to a string, the API token roles will be filtered using it as a substring (i.e, <code>roles=&quot;domain&quot;</code> to filter out <code>Account API Gateway</code> and only leave <code>Domain API Gateway</code>).</p>

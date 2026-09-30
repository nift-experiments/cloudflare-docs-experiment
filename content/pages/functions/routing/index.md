---
cp9:
  canonical: https://developers.cloudflare.com/pages/functions/routing/
  description: Learn how Pages Functions uses file-based routing to map URL patterns to function files.
  full_title: Routing · Cloudflare Pages docs
  head_html: <title>Routing · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how Pages Functions uses file-based routing to map URL patterns to function files."><link rel="canonical" href="https://developers.cloudflare.com/pages/functions/routing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/functions/routing/index.md"><meta property="og:title" content="Routing · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how Pages Functions uses file-based routing to map URL patterns to function files."><meta property="og:url" content="https://developers.cloudflare.com/pages/functions/routing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/functions/routing/#page","headline":"Routing \u00b7 Cloudflare Pages docs","description":"Learn how Pages Functions uses file-based routing to map URL patterns to function files.","url":"https://developers.cloudflare.com/pages/functions/routing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/functions/routing/
  schema: 1
---
<p>Functions utilize file-based routing. Your <code>/functions</code> directory structure determines the designated routes that your Functions will run on. You can create a <code>/functions</code> directory with as many levels as needed for your project's use case. Review the following directory:</p>
<pre tabindex="0" class="nb-file-tree">&#10;&#10;&#10;@markup("md", "content/.markup/bodies/10946.md")&#10;&#10;&#10;</pre>
<p>The following routes will be generated based on the above file structure. These routes map the URL pattern to the <code>/functions</code> file that will be invoked when a visitor goes to the URL:</p>
<table>
<thead>
<tr>
<th>File path</th>
<th>Route</th>
</tr>
</thead>
<tbody>
<tr>
<td>/functions/index.js</td>
<td>example.com</td>
</tr>
<tr>
<td>/functions/helloworld.js</td>
<td>example.com/helloworld</td>
</tr>
<tr>
<td>/functions/howdyworld.js</td>
<td>example.com/howdyworld</td>
</tr>
<tr>
<td>/functions/fruits/index.js</td>
<td>example.com/fruits</td>
</tr>
<tr>
<td>/functions/fruits/apple.js</td>
<td>example.com/fruits/apple</td>
</tr>
<tr>
<td>/functions/fruits/banana.js</td>
<td>example.com/fruits/banana</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="trailing-slash">Trailing slash</h3>
@markup("md", "content/.markup/bodies/10945.md")
</aside>
<p>If no Function is matched, it will fall back to a static asset if there is one. Otherwise, the Function will fall back to the <a href="/pages/configuration/serving-pages/">default routing behavior</a> for Pages' static assets.</p>
<h2 id="dynamic-routes">Dynamic routes</h2>
<p>Dynamic routes allow you to match URLs with parameterized segments. This can be useful if you are building dynamic applications. You can accept dynamic values which map to a single path by changing your filename.</p>
<h3 id="single-path-segments">Single path segments</h3>
<p>To create a dynamic route, place one set of brackets around your filename – for example, <code>/users/[user].js</code>. By doing this, you are creating a placeholder for a single path segment:</p>
<table>
<thead>
<tr>
<th>Path</th>
<th>Matches?</th>
</tr>
</thead>
<tbody>
<tr>
<td>/users/nevi</td>
<td>Yes</td>
</tr>
<tr>
<td>/users/daniel</td>
<td>Yes</td>
</tr>
<tr>
<td>/profile/nevi</td>
<td>No</td>
</tr>
<tr>
<td>/users/nevi/foobar</td>
<td>No</td>
</tr>
<tr>
<td>/nevi</td>
<td>No</td>
</tr>
</tbody>
</table>
<h3 id="multipath-segments">Multipath segments</h3>
<p>By placing two sets of brackets around your filename – for example, <code>/users/[[user]].js</code> – you are matching any depth of route after <code>/users/</code>:</p>
<table>
<thead>
<tr>
<th>Path</th>
<th>Matches?</th>
</tr>
</thead>
<tbody>
<tr>
<td>/users/nevi</td>
<td>Yes</td>
</tr>
<tr>
<td>/users/daniel</td>
<td>Yes</td>
</tr>
<tr>
<td>/profile/nevi</td>
<td>No</td>
</tr>
<tr>
<td>/users/nevi/foobar</td>
<td>Yes</td>
</tr>
<tr>
<td>/users/daniel/xyz/123</td>
<td>Yes</td>
</tr>
<tr>
<td>/nevi</td>
<td>No</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="route-specificity">Route specificity</h3>
@markup("md", "content/.markup/bodies/10944.md")
</aside>
<h4 id="dynamic-route-examples">Dynamic route examples</h4>
<p>Review the following <code>/functions/</code> directory structure:</p>
<pre tabindex="0" class="nb-file-tree">&#10;&#10;&#10;@markup("md", "content/.markup/bodies/10947.md")&#10;&#10;&#10;</pre>
<p>The following requests will match the following files:</p>
<table>
<thead>
<tr>
<th>Request</th>
<th>File</th>
</tr>
</thead>
<tbody>
<tr>
<td>/foo</td>
<td>Will route to a static asset if one is available.</td>
</tr>
<tr>
<td>/date</td>
<td>/date.js</td>
</tr>
<tr>
<td>/users/daniel</td>
<td>/users/[user].js</td>
</tr>
<tr>
<td>/users/nevi</td>
<td>/users/[user].js</td>
</tr>
<tr>
<td>/users/special</td>
<td>/users/special.js</td>
</tr>
<tr>
<td>/users/daniel/xyz/123</td>
<td>/users/[[catchall]].js</td>
</tr>
</tbody>
</table>
<p>The URL segment(s) that match the placeholder (<code>[user]</code>) will be available in the request <a href="/pages/functions/api-reference/#eventcontext"><code>context</code></a> object. The <a href="/pages/functions/api-reference/#eventcontext"><code>context.params</code></a> object can be used to find the matched value for a given filename placeholder.</p>
<p>For files which match a single URL segment (use a single set of brackets), the values are returned as a string:</p>
<pre tabindex="0"><code class="language-js">export function onRequest(context) {&#10;	return new Response(context.params.user);&#10;}&#10;</code></pre>
<p>The above logic will return <code>daniel</code> for requests to <code>/users/daniel</code>.</p>
<p>For files which match against multiple URL segments (use a double set of brackets), the values are returned as an array:</p>
<pre tabindex="0"><code class="language-js">export function onRequest(context) {&#10;	return new Response(JSON.stringify(context.params.catchall));&#10;}&#10;</code></pre>
<p>The above logic will return <code>[&quot;daniel&quot;, &quot;xyz&quot;, &quot;123&quot;]</code> for requests to <code>/users/daniel/xyz/123</code>.</p>
<h2 id="functions-invocation-routes">Functions invocation routes</h2>
<p>On a purely static project, Pages offers unlimited free requests. However, once you add Functions on a Pages project, all requests by default will invoke your Function. To continue receiving unlimited free static requests, exclude your project's static routes by creating a <code>_routes.json</code> file. This file will be automatically generated if a <code>functions</code> directory is detected in your project when you publish your project with Pages CI or Wrangler.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10943.md")
</aside>
<h3 id="create-a-routes-json-file">Create a <code>_routes.json</code> file</h3>
<p>Create a <code>_routes.json</code> file to control when your Function is invoked. It should be placed in the build directory of your project.</p>
<details class="nb-details"><summary>Default build directories</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10948.md")
</div></details>
<p>This file will include three different properties:</p>
<ul>
<li><strong>version</strong>: Defines the version of the schema. Currently there is only one version of the schema (version 1), however, we may add more in the future and aim to be backwards compatible.</li>
<li><strong>include</strong>: Defines routes that will be invoked by Functions. Accepts wildcard behavior.</li>
<li><strong>exclude</strong>: Defines routes that will not be invoked by Functions. Accepts wildcard behavior. <code>exclude</code> always take priority over <code>include</code>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10942.md")
</aside>
<h4 id="example-configuration">Example configuration</h4>
<p>Below is an example of a <code>_routes.json</code>.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;version&quot;: 1,&#10;	&quot;include&quot;: [&quot;/*&quot;],&#10;	&quot;exclude&quot;: []&#10;}&#10;</code></pre>
<p>This <code>_routes.json</code> will invoke your Functions on all routes.</p>
<p>Below is another example of a <code>_routes.json</code> file. Any route inside the <code>/build</code> directory will not invoke the Function and will not incur a Functions invocation charge.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;version&quot;: 1,&#10;	&quot;include&quot;: [&quot;/*&quot;],&#10;	&quot;exclude&quot;: [&quot;/build/*&quot;]&#10;}&#10;</code></pre>
<h2 id="fail-open-closed">Fail open / closed</h2>
<p>If on the Workers Free plan, you can configure how Pages behaves when your daily free tier allowance of Pages Functions requests is exhausted. If, for example, you are performing authentication checks or other critical functionality in your Pages Functions, you may wish to disable your Pages project when the allowance is exhausted.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Pages project.
3. Go to **Settings** > **Runtime** > **Fail open / closed**.
<p>&quot;Fail open&quot; means that static assets will continue to be served, even if Pages Functions would ordinarily have run first. &quot;Fail closed&quot; means an error page will be returned, rather than static assets.</p>
<p>The daily request limit for Pages Functions can be removed entirely by upgrading to <a href="/workers/platform/pricing/#workers">Workers Standard</a>.</p>
<h3 id="limits">Limits</h3>
<p>Functions invocation routes have the following limits:</p>
<ul>
<li>You must have at least one include rule.</li>
<li>You may have no more than 100 include/exclude rules combined.</li>
<li>Each rule may have no more than 100 characters.</li>
</ul>

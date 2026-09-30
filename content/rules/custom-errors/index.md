---
cp9:
  canonical: https://developers.cloudflare.com/rules/custom-errors/
  description: Serve custom error pages for Cloudflare or origin server errors.
  full_title: Custom Errors · Cloudflare Rules docs
  head_html: <title>Custom Errors · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Serve custom error pages for Cloudflare or origin server errors."><link rel="canonical" href="https://developers.cloudflare.com/rules/custom-errors/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/custom-errors/index.md"><meta property="og:title" content="Custom Errors · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Serve custom error pages for Cloudflare or origin server errors."><meta property="og:url" content="https://developers.cloudflare.com/rules/custom-errors/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Rules"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/custom-errors/#page","headline":"Custom Errors \u00b7 Cloudflare Rules docs","description":"Serve custom error pages for Cloudflare or origin server errors.","url":"https://developers.cloudflare.com/rules/custom-errors/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /rules/custom-errors/
  schema: 1
---
<p>Use Custom Errors to replace default Cloudflare error pages with your own custom content. Custom error content is shown to visitors when an HTTP error occurs, whether the error comes from your origin server, a Cloudflare product (including <a href="/workers/">Cloudflare Workers</a>), or a <a href="/cloudflare-challenges/">security challenge</a>.</p>
<p>You can configure custom error content using the following methods:</p>
<ul>
<li><a href="#error-pages"><strong>Error Page</strong></a>: An HTML page shown to website visitors when a specific error occurs (refer to the different <a href="/rules/custom-errors/reference/error-page-types/">error page types</a>) or when showing a security challenge. Error Pages can be defined at the zone level and at the account level on paid plans, with zone-level configurations taking precedence.</li>
<li><a href="#custom-error-rules"><strong>Custom Error Rule</strong></a>: Defines the conditions under which Cloudflare will serve a custom error response to visitors in case of HTTP errors (status codes <code>400</code> and above), and the exact content that will be served. A matching custom error rule has priority over an Error Page configured at the account or at the zone level that would apply to the same error.</li>
</ul>
<p>Custom Errors require that you <a href="/dns/proxy-status/">proxy the DNS records</a> of your domain (or subdomain) through Cloudflare.</p>
<h2 id="how-it-works">How it works</h2>
<p>Cloudflare has a set of default pages for presenting errors and challenges to your website visitors. You can customize those pages using Error Pages and Custom Error Rules.</p>
<p>When an error of a <a href="/rules/custom-errors/reference/error-page-types/">specific type</a> occurs, Cloudflare does the following:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/12978.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12977.md")
</aside>
<h2 id="availability">Availability</h2>
<p>Custom Errors are available to all paid plans. The exact features depend on your Cloudflare plan.</p>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Number of rules</td>
<td>0</td>
<td>25</td>
<td>50</td>
<td>300</td>
</tr>
<tr>
<td>Number of assets</td>
<td>0</td>
<td>25</td>
<td>50</td>
<td>300</td>
</tr>
<tr>
<td>Error Pages</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Origin Error Pages</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="error-pages">Error Pages</h2>
<p>Cloudflare uses a wide range of <a href="/support/troubleshooting/http-status-codes/">error codes</a> to identify issues in handling request traffic. By default, these error pages mention Cloudflare; however, you can create custom error pages to provide a consistent brand experience for your users.</p>
<p>Error Pages do not apply to responses with an HTTP status code of <code>500</code>, <code>501</code>, <code>503</code>, or <code>505</code>. These exceptions help avoid issues with specific API endpoints and other web applications. You can still customize responses for these status codes using Custom Error Rules.</p>
<p>If you are on a Cloudflare paid plan, you can create custom error pages at the zone level or for your entire account. Zone-level error pages have priority over account-level error pages.</p>
<p>Additionally, Enterprise customers can customize 5XX error pages (except errors <code>520</code>-<code>527</code>) at their origin by turning on <strong>Origin Error Pages</strong> in <strong>Error Pages</strong> in the dashboard.</p>
<p>You can design custom error pages to appear during a security challenge or when an error occurs. For more information on the different error page types, refer to <a href="/rules/custom-errors/reference/error-page-types/">Error page types</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12976.md")
</aside>
<h2 id="custom-error-rules">Custom Error Rules</h2>
<p>A custom error rule defines the conditions under which Cloudflare will serve custom error content to visitors in case of HTTP errors (status codes <code>400</code> and above), and the exact content that will be served to visitors.</p>
<p>When defining the content to serve, you provide either an inline response or the URL of an existing webpage. The URL can point to a webpage or to a different resource such as JSON content.</p>
<p>When you provide a URL, Cloudflare will gather any required images, CSS, and JavaScript code and save a minified version of the full page in the Cloudflare global network. This resource is called a <a href="#custom-error-assets">custom error asset</a>, which you can use in one or more custom error rules in the same scope of the asset (zone or account).</p>
<p>When a custom error rule is triggered, Cloudflare will replace the body with the response you previously defined and (optionally) the response HTTP status code sent to the visitor. Cloudflare will keep any existing HTTP response headers except for <code>Content-Type</code> and <code>Content-Length</code>.</p>
<p>Additionally, you can configure <a href="/rules/transform/response-header-modification/">Response Header Transform Rules</a> for error responses to add, change, or remove HTTP headers from the response.</p>
<p>Custom error rules have priority over <a href="#error-pages">Error Pages</a>.</p>
<h2 id="custom-error-assets">Custom Error Assets</h2>
<p>A custom error asset corresponds to a web resource such as an HTML web page (including any referenced images, CSS, and JavaScript code) that Cloudflare fetches and saves based on a URL you provide, to be served to visitors as an error page.</p>
<p>Once the custom error asset is stored in Cloudflare's global network, the URL you initially provided no longer needs to be available. You can update an existing custom error asset by fetching it again. The metadata associated with each custom error asset includes the timestamp when the last fetch occurred, and this information is displayed in the dashboard.</p>
<p>You can use a custom error asset in one or more <a href="#custom-error-rules">custom error rules</a> in the same scope where you defined the asset (zone or account).</p>
<h3 id="size-limits">Size limits</h3>
<p>When you provide a URL for a custom error asset, Cloudflare fetches the page and inlines all referenced resources into the HTML. Images and other binary resources (including those referenced from CSS via <code>url(...)</code>) are inlined as base64-encoded data URLs. CSS and JavaScript files are inlined as plain text inside <code>&lt;style&gt;</code> and <code>&lt;script&gt;</code> tags. The processed page must not exceed approximately 1.5 MB.</p>
<p>If your custom error asset exceeds this size, reduce the number or size of referenced resources. You can also host large resources externally, as long as they remain accessible from Cloudflare's network when the asset is fetched.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="large-assets-increase-bandwidth">Large assets increase bandwidth</h3>
@markup("md", "content/.markup/bodies/12975.md")
</aside>

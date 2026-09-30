---
cp9:
  canonical: https://developers.cloudflare.com/turnstile/get-started/client-side-rendering/
  description: Embed a Turnstile widget on your website with JavaScript or HTML.
  full_title: Embed the widget · Cloudflare Turnstile docs
  head_html: <title>Embed the widget · Cloudflare Turnstile docs</title><meta name="generator" content="Nift"><meta name="description" content="Embed a Turnstile widget on your website with JavaScript or HTML."><link rel="canonical" href="https://developers.cloudflare.com/turnstile/get-started/client-side-rendering/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/turnstile/get-started/client-side-rendering/index.md"><meta property="og:title" content="Embed the widget · Cloudflare Turnstile docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Embed a Turnstile widget on your website with JavaScript or HTML."><meta property="og:url" content="https://developers.cloudflare.com/turnstile/get-started/client-side-rendering/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Turnstile"><meta name="algolia_product_filter" content="Turnstile"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Turnstile"><meta name="pcx_tags" content="JavaScript,SPA"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/turnstile/get-started/client-side-rendering/#page","headline":"Embed the widget \u00b7 Cloudflare Turnstile docs","description":"Embed a Turnstile widget on your website with JavaScript or HTML.","url":"https://developers.cloudflare.com/turnstile/get-started/client-side-rendering/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["JavaScript","SPA"]}</script>
  markdown: true
  noindex: false
  route: /turnstile/get-started/client-side-rendering/
  schema: 1
---
<p>Learn how to add the Turnstile widget to your webpage using implicit or explicit rendering methods.</p>
<p>Turnstile offers two ways to add widgets to your page. <strong>Implicit rendering</strong> automatically scans your HTML for widget containers when the page loads. <strong>Explicit rendering</strong> gives you programmatic control to create widgets at any time using JavaScript. Use implicit rendering for static pages where forms exist at page load. Use explicit rendering for dynamic content and single-page applications (SPAs) where forms are created after the initial page load.</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Implicit rendering</th>
<th>Explicit rendering</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Ease of setup</strong></td>
<td>Simple, minimal code</td>
<td>Requires additional JavaScript</td>
</tr>
<tr>
<td><strong>Control over timing</strong></td>
<td>Renders automatically on page load</td>
<td>Full control over rendering timing</td>
</tr>
<tr>
<td><strong>Use cases</strong></td>
<td>Static content</td>
<td>Dynamic or interactive content</td>
</tr>
<tr>
<td><strong>Customization</strong></td>
<td>Limited to HTML attributes</td>
<td>Extensive via JavaScript API</td>
</tr>
</tbody>
</table>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you begin, you must have:</p>
<ul>
<li>A Cloudflare account</li>
<li><a href="/turnstile/get-started/#1-create-your-widget">A Turnstile widget</a> with a sitekey</li>
<li>Access to edit your website's HTML</li>
<li>Basic knowledge of HTML and JavaScript</li>
</ul>
<h2 id="process">Process</h2>
<ol>
<li>Page load: The Turnstile script loads and scans for elements or waits for programmatic calls.</li>
<li>Widget rendering: Widgets are created and begin running challenges.</li>
<li>Token generation: When a challenge is completed, a token is generated.</li>
<li>Form integration: The token is made available via callbacks or hidden form fields.</li>
<li>Server validation: Your server receives the token and validates it using the Siteverify API.</li>
</ol>
<h2 id="implicit-rendering">Implicit rendering</h2>
<p>Implicit rendering automatically scans your HTML for elements with the <code>cf-turnstile</code> class and renders widgets without additional JavaScript code. This set up is ideal for static pages where you want the widget to load immediately when the page loads.</p>
<h3 id="use-cases">Use cases</h3>
<p>Cloudflare recommends using implicit rendering on the following scenarios:</p>
<ul>
<li>You have simple implementations and want a quick integration.</li>
<li>You have static websites with straightforward forms.</li>
<li>You want widgets to appear immediately on pageload.</li>
<li>You do not need programmatic control of the widget.</li>
</ul>
<h3 id="implementation">Implementation</h3>
<h4 id="1-add-the-turnstile-script"><ol>
<li>Add the Turnstile script</li>
</ol></h4>
<p><strong>Include the Turnstile Script</strong>: Add the Turnstile JavaScript API to your HTML file within the <code>&lt;head&gt;</code> section or just before the closing <code>&lt;/body&gt;</code> tag.</p>
<pre tabindex="0"><code class="language-html">&lt;script&#10;	src=&quot;https://challenges.cloudflare.com/turnstile/v0/api.js&quot;&#10;	async&#10;	defer&#10;&gt;&lt;/script&gt;&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15071.md")
</aside>
<h4 id="2-optional-optimize-performance-with-resource-hints"><ol start="2">
<li>(Optional) Optimize performance with resource hints</li>
</ol></h4>
<p>Add resource hints to improve loading performance by establishing early connections to Cloudflare servers. Place this <code>&lt;link&gt;</code> tag in your HTML <code>&lt;head&gt;</code> section before the Turnstile script.</p>
<pre tabindex="0"><code class="language-html">&lt;link rel=&quot;preconnect&quot; href=&quot;https://challenges.cloudflare.com&quot; /&gt;&#10;</code></pre>
<h4 id="3-add-widget-elements"><ol start="3">
<li>Add widget elements</li>
</ol></h4>
<p>Add widget containers where you want the challenges to appear on your website.</p>
<pre tabindex="0"><code class="language-html">&lt;div class=&quot;cf-turnstile&quot; data-sitekey=&quot;&lt;YOUR-SITE-KEY&gt;&quot;&gt;&lt;/div&gt;&#10;</code></pre>
<h4 id="4-configure-with-data-attributes"><ol start="4">
<li>Configure with data attributes</li>
</ol></h4>
<p><a href="/turnstile/get-started/client-side-rendering/widget-configurations/">Customize your widgets</a> using data attributes. Insert a <code>div</code> element where you want the widget to appear.</p>
<pre tabindex="0"><code class="language-html">&lt;div&#10;	class=&quot;cf-turnstile&quot;&#10;	data-sitekey=&quot;&lt;YOUR-SITE-KEY&gt;&quot;&#10;	data-theme=&quot;light&quot;&#10;	data-size=&quot;normal&quot;&#10;	data-callback=&quot;onSuccess&quot;&#10;&gt;&lt;/div&gt;&#10;</code></pre>
<p>Once a challenge has been solved, a token is passed to the success callback. This token must be validated against our <a href="/turnstile/get-started/server-side-validation/">Siteverify endpoint</a>.</p>
<h3 id="complete-implicit-rendering-examples-by-use-case">Complete implicit rendering examples by use case</h3>
<details class="nb-details"><summary>Basic login form</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15072.md")
</div></details>
<details class="nb-details"><summary>Advanced form with callbacks</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15073.md")
</div></details>
<details class="nb-details"><summary>Multiple widgets with different configurations</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15074.md")
</div></details>
<details class="nb-details"><summary>Automatic form integration</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15075.md")
</div></details>
<hr />
<h2 id="explicit-rendering">Explicit rendering</h2>
<p>Explicit rendering gives you programmatic control over when and where the widget appears and how the widgets are created using JavaScript functions. This method is suitable for dynamic content, single-page applications (SPAs), or conditional rendering based on user interactions.</p>
<h3 id="use-cases-1">Use cases</h3>
<p>Cloudflare recommends using explicit rendering on the following scenarios:</p>
<ul>
<li>You have dynamic websites and single-page applications (SPAs).</li>
<li>You need to control the timing of widget creation.</li>
<li>You want to conditionally render the widget based on visitor interactions.</li>
<li>You want multiple widgets with different configurations.</li>
<li>You have complex applications requiring widget lifecycle management.</li>
</ul>
<h3 id="implementation-1">Implementation</h3>
<h4 id="1-add-the-script-to-your-website-with-explicit-rendering"><ol>
<li>Add the script to your website with explicit rendering</li>
</ol></h4>
<pre tabindex="0"><code class="language-html">&lt;script&#10;	src=&quot;https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit&quot;&#10;	defer&#10;&gt;&lt;/script&gt;&#10;</code></pre>
<h4 id="2-create-container-elements"><ol start="2">
<li>Create container elements</li>
</ol></h4>
<p>Create containers without the <code>cf-turnstile</code> class.</p>
<pre tabindex="0"><code class="language-html">&lt;div id=&quot;turnstile-container&quot;&gt;&lt;/div&gt;&#10;</code></pre>
<h4 id="3-render-the-widgets-programmatically"><ol start="3">
<li>Render the widgets programmatically</li>
</ol></h4>
<p>Call <code>turnstile.render()</code> when you are ready to create the widget.</p>
<pre tabindex="0"><code class="language-js">const widgetId = turnstile.render(&quot;#turnstile-container&quot;, {&#10;	sitekey: &quot;&lt;YOUR-SITE-KEY&gt;&quot;,&#10;	callback: function (token) {&#10;		console.log(&quot;Success:&quot;, token);&#10;	},&#10;});&#10;</code></pre>
<h3 id="optional-calls">Optional calls</h3>
<p>After rendering the Turnstile widget explicitly, you may need to interact with it based on your application's requirements. Refer to the sections below to manage the widget's state.</p>
<h4 id="reset-a-widget">Reset a widget</h4>
<p>To reset the widget if the given widget timed out or expired, you can use the function:</p>
<pre tabindex="0"><code class="language-js">turnstile.reset(widgetId);&#10;</code></pre>
<h4 id="get-the-response-token">Get the response token</h4>
<p>Retrieve the current response token at any time:</p>
<pre tabindex="0"><code class="language-js">const responseToken = turnstile.getResponse(widgetId);&#10;</code></pre>
<h4 id="remove-a-widget">Remove a widget</h4>
<p>When a widget is no longer needed, it can be removed from the page using:</p>
<pre tabindex="0"><code class="language-js">turnstile.remove(widgetId);&#10;</code></pre>
<p>This will not call any callback and will remove all related DOM elements.</p>
<h3 id="complete-explicit-rendering-examples-by-use-case">Complete explicit rendering examples by use case</h3>
<details class="nb-details"><summary>Basic explicit implementation</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15076.md")
</div></details>
<details class="nb-details"><summary>Using onload callback</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15077.md")
</div></details>
<details class="nb-details"><summary>Advanced SPA implementation</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15078.md")
</div></details>
<h3 id="widget-lifecycle-management">Widget lifecycle management</h3>
<p>Explicit rendering provides full control over the widget lifecycle.</p>
<pre tabindex="0"><code class="language-js">// Render a widget&#10;const widgetId = turnstile.render(&quot;#container&quot;, {&#10;	sitekey: &quot;&lt;YOUR-SITE-KEY&gt;&quot;,&#10;	callback: handleSuccess,&#10;});&#10;&#10;// Get the current token&#10;const token = turnstile.getResponse(widgetId);&#10;&#10;// Check if widget is expired&#10;const isExpired = turnstile.isExpired(widgetId);&#10;&#10;// Reset the widget (clears current state)&#10;turnstile.reset(widgetId);&#10;&#10;// Remove the widget completely&#10;turnstile.remove(widgetId);&#10;</code></pre>
<h3 id="execution-mode">Execution mode</h3>
<p>Control when challenges run with execution modes.</p>
<pre tabindex="0"><code class="language-js">// Render widget but don&#x27;t run challenge yet&#10;const widgetId = turnstile.render(&quot;#container&quot;, {&#10;	sitekey: &quot;&lt;YOUR-SITE-KEY&gt;&quot;,&#10;	execution: &quot;execute&quot;, // Don&#x27;t auto-execute&#10;});&#10;&#10;// Later, run the challenge when needed&#10;turnstile.execute(&quot;#container&quot;);&#10;</code></pre>
<hr />
<h2 id="performance-and-user-experience-optimization">Performance and user experience optimization</h2>
<p>Cloudflare recommends that you execute the Turnstile script as early upon the visitor's page entry as possible, so that the verification is complete and the interaction is available once the visitor attempts an action on the page.</p>
<hr />
<h2 id="configuration-options">Configuration options</h2>
<p>Both implicit and explicit rendering methods support the same configuration options. Refer to the table below for the most commonly used configurations.</p>
<table>
<thead>
<tr>
<th>Option</th>
<th>Description</th>
<th>Values</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>sitekey</code></td>
<td>Your widget's sitekey</td>
<td>Required string</td>
</tr>
<tr>
<td><code>theme</code></td>
<td>Visual theme</td>
<td><code>auto</code>, <code>light</code>, <code>dark</code></td>
</tr>
<tr>
<td><code>size</code></td>
<td>Widget size</td>
<td><code>normal</code>, <code>flexible</code>, <code>compact</code></td>
</tr>
<tr>
<td><code>callback</code></td>
<td>Success callback</td>
<td>Function</td>
</tr>
<tr>
<td><code>error-callback</code></td>
<td>Error callback</td>
<td>Function</td>
</tr>
<tr>
<td><code>execution</code></td>
<td>When to run the challenge</td>
<td><code>render</code>, <code>execute</code></td>
</tr>
<tr>
<td><code>appearance</code></td>
<td>When the widget is visible</td>
<td><code>always</code>, <code>execute</code>, <code>interaction-only</code></td>
</tr>
</tbody>
</table>
<p>For a complete list of configuration options, refer to <a href="/turnstile/get-started/client-side-rendering/widget-configurations/">Widget configurations</a>.</p>
<hr />
<h2 id="testing">Testing</h2>
<p>You can test your Turnstile widget on your webpage without triggering an actual Cloudflare Challenge by using a testing sitekey.</p>
<p>Refer to <a href="/turnstile/troubleshooting/testing/">Testing</a> for more information.</p>
<hr />
<h2 id="limitations">Limitations</h2>
<p>Turnstile is designed to function only on pages using <code>http://</code> or <code>https://</code> URI schemes. Other protocols, such as <code>file://</code>, are not supported for embedding the widget.</p>
<hr />
<h2 id="security-requirements">Security requirements</h2>
<ul>
<li>
<p>Server-side validation is mandatory. It is critical to enforce Turnstile tokens with the Siteverify API. The Turnstile token could be invalid, expired, or already redeemed. Not verifying the token will leave major vulnerabilities in your implementation. You must call Siteverify to complete your Turnstile configuration. Otherwise, it is incomplete and will result in zeroes for token validation when viewing your metrics in <a href="/turnstile/turnstile-analytics/">Turnstile Analytics</a>.</p>
</li>
<li>
<p>Tokens expire after 300 seconds (5 minutes). Each token can only be validated once. Expired or used tokens must be replaced with fresh challenges.</p>
</li>
</ul>

---
cp9:
  canonical: https://developers.cloudflare.com/zaraz/reference/triggers/
  description: Trigger types and matching rules for Zaraz actions.
  full_title: Triggers and rules · Cloudflare Zaraz docs
  head_html: <title>Triggers and rules · Cloudflare Zaraz docs</title><meta name="generator" content="Nift"><meta name="description" content="Trigger types and matching rules for Zaraz actions."><link rel="canonical" href="https://developers.cloudflare.com/zaraz/reference/triggers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/zaraz/reference/triggers/index.md"><meta property="og:title" content="Triggers and rules · Cloudflare Zaraz docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Trigger types and matching rules for Zaraz actions."><meta property="og:url" content="https://developers.cloudflare.com/zaraz/reference/triggers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Zaraz"><meta name="algolia_product_filter" content="Zaraz"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Zaraz"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/zaraz/reference/triggers/#page","headline":"Triggers and rules \u00b7 Cloudflare Zaraz docs","description":"Trigger types and matching rules for Zaraz actions.","url":"https://developers.cloudflare.com/zaraz/reference/triggers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /zaraz/reference/triggers/
  schema: 1
---
<p>Triggers define the conditions under which <a href="/zaraz/custom-actions/">a tool will start an action</a>. In most cases, your objective will be to create triggers that match specific website events that are relevant to your business. A trigger can be based on an event that happened on your website, like after selecting a button or loading a specific page.</p>
<p>These website events can be passed to Cloudflare Zaraz in a number of ways. You can use the <a href="/zaraz/web-api/track/">Track</a> method of the Web API or the <a href="/zaraz/advanced/datalayer-compatibility/"><code>dataLayer</code></a> call. Alternatively, if you do not want to write code to track events on your website, you can configure triggers to listen to browser-side website events, with different types of rules like click listeners or form submissions.</p>
<h2 id="rule-types">Rule types</h2>
<p>The exact composition of the trigger will change depending on the type of rule you choose.</p>
<h3 id="match-rule">Match rule</h3>
<p>Zaraz matches the variable you input in <strong>Variable name</strong> with the text under <strong>Match string</strong>. For a complete list of supported variables, refer to <a href="/zaraz/reference/properties-reference/">Properties reference</a>.</p>
<p><strong>Trigger example: Match <code>zaraz.track(&quot;purchase&quot;)</code></strong></p>
<table>
<thead>
<tr>
<th>Rule type</th>
<th>Variable name</th>
<th>Match operation</th>
<th>Match string</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Match rule</em></td>
<td><em>Event Name</em></td>
<td><em>Equals</em></td>
<td><code>purchase</code></td>
</tr>
</tbody>
</table>
<p>If you create a trigger with match rules using variables from Page Properties, Cookies, Device Properties, or Miscellaneous categories, you will often want to add a second rule that matches <code>Pageview</code>. Otherwise, your trigger will be valid for every other event happening on this page too. Refer to <a href="/zaraz/custom-actions/create-trigger/">Create a trigger</a> to learn how to add more than one condition to a trigger.</p>
<p><strong>Trigger example: All pages under <code>/blog</code></strong></p>
<table>
<thead>
<tr>
<th>Rule type</th>
<th>Variable name</th>
<th>Match operation</th>
<th>Match string</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Match rule</em></td>
<td><em>URL pathname</em></td>
<td><em>Starts with</em></td>
<td><code>/blog</code></td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>Rule type</th>
<th>Variable name</th>
<th>Match operation</th>
<th>Match string</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Match rule</em></td>
<td><em>Event Name</em></td>
<td><em>Equals</em></td>
<td><code>Pageview</code></td>
</tr>
</tbody>
</table>
<p><strong>Trigger example: All logged in users</strong></p>
<table>
<thead>
<tr>
<th>Rule type</th>
<th>Variable name</th>
<th>Match operation</th>
<th>Match string</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Match rule</em></td>
<td><em>Cookie: name:</em> <code>isLoggedIn</code></td>
<td><em>Equals</em></td>
<td><code>true</code></td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>Rule type</th>
<th>Variable name</th>
<th>Match operation</th>
<th>Match string</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Match rule</em></td>
<td><em>Event Name</em></td>
<td><em>Equals</em></td>
<td><code>Pageview</code></td>
</tr>
</tbody>
</table>
<p>Refer to <a href="/zaraz/reference/properties-reference/">Properties reference</a> for more information on the variables you can use when using Match rule.</p>
<h3 id="click-listener">Click listener</h3>
<p>Tracks clicks in a web page. You can set up click listeners using CSS selectors or XPath expressions. <strong>Wait for actions</strong> (in milliseconds) tells Zaraz to prevent the page from changing for the amount of time specified. This allows all requests triggered by the click listener to reach their destination.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17598.md")
</aside>
<p><strong>Trigger example for CSS selector:</strong></p>
<table>
<thead>
<tr>
<th>Rule type</th>
<th>Type</th>
<th>Selector</th>
<th>Wait for actions</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Click listener</em></td>
<td><em>CSS</em></td>
<td><code>#my-button</code></td>
<td><code>500</code></td>
</tr>
</tbody>
</table>
<p>To improve the performance of the web page, you can limit a click listener to a specific URL, by combining it with a Match rule. For example, to track button clicks on a specific page you can set up the following rules in a trigger:</p>
<table>
<thead>
<tr>
<th>Rule type</th>
<th>Type</th>
<th>Selector</th>
<th>Wait for actions</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Click listener</em></td>
<td><em>CSS</em></td>
<td><code>#myButton</code></td>
<td><code>500</code></td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>Rule type</th>
<th>Variable name</th>
<th>Match operation</th>
<th>Match string</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Match rule</em></td>
<td><em>URL pathname</em></td>
<td><em>Equals</em></td>
<td><code>/my-page-path</code></td>
</tr>
</tbody>
</table>
<p>If you need to track a link of an element using CSS selectors - for example, on a clickable button - you have to create a listener for the <code>href</code> attribute of the <code>&lt;a&gt;</code> tag:</p>
<table>
<thead>
<tr>
<th>Rule type</th>
<th>Type</th>
<th>Selector</th>
<th>Wait for actions</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Click listener</em></td>
<td><em>CSS</em></td>
<td><code>a[href$='/#my-css-selector']</code></td>
<td><code>500</code></td>
</tr>
</tbody>
</table>
<p>Refer to <a href="/zaraz/custom-actions/create-trigger/"><strong>Create a trigger</strong></a> to learn how to add more than one rule to a trigger.</p>
<hr />
<p><strong>Trigger example for XPath:</strong></p>
<table>
<thead>
<tr>
<th>Rule type</th>
<th>Type</th>
<th>Selector</th>
<th>Wait for actions</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Click listener</em></td>
<td><em>XPath</em></td>
<td><code>/html/body//*[contains(text(), 'Add To Cart')]</code></td>
<td><code>500</code></td>
</tr>
</tbody>
</table>
<h3 id="element-visibility">Element Visibility</h3>
<p>Triggers an action when a CSS selector becomes visible in the screen.</p>
<table>
<thead>
<tr>
<th>Rule type</th>
<th>CSS Selector</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Element Visibility</em></td>
<td><code>#my-id</code></td>
</tr>
</tbody>
</table>
<h3 id="scroll-depth">Scroll depth</h3>
<p>Triggers an action when the users scrolls a predetermined amount of pixels. This can be a fixed amount of pixels or a percentage of the screen.</p>
<p><strong>Example with pixels</strong></p>
<table>
<thead>
<tr>
<th>Rule type</th>
<th>CSS Selector</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Scroll Depth</em></td>
<td><code>100px</code></td>
</tr>
</tbody>
</table>
<hr />
<p><strong>Example with a percentage of the screen</strong></p>
<table>
<thead>
<tr>
<th>Rule type</th>
<th>CSS Selector</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Scroll Depth</em></td>
<td><code>45%</code></td>
</tr>
</tbody>
</table>
<h3 id="form-submission">Form submission</h3>
<p>Tracks form submissions using CSS selectors. Select the <strong>Validate</strong> toggle button to only fire the trigger when the form has no validation errors.</p>
<p><strong>Trigger example:</strong></p>
<table>
<thead>
<tr>
<th>Rule type</th>
<th>CSS Selector</th>
<th>Validate</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Form submission</em></td>
<td><code>#my-form</code></td>
<td>Toggle on or off</td>
</tr>
</tbody>
</table>
<p>To improve the performance of the web page, you can limit a Form submission trigger to a specific URL, by combining it with a Match rule. For example, to track a form on a specific page you can set up the following rules in a trigger:</p>
<table>
<thead>
<tr>
<th>Rule type</th>
<th>CSS Selector</th>
<th>Validate</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Form submission</em></td>
<td><code>#my-form</code></td>
<td>Toggle on or off</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>Rule type</th>
<th>Variable name</th>
<th>Match operation</th>
<th>Match string</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Match rule</em></td>
<td><em>URL pathname</em></td>
<td><em>Equals</em></td>
<td><code>/my-page-path</code></td>
</tr>
</tbody>
</table>
<p>Refer to <a href="/zaraz/custom-actions/create-trigger/"><strong>Create a trigger</strong></a> to learn how to add more than one condition to a trigger.</p>
<h3 id="timer">Timer</h3>
<p>Set up a timer that will fire the trigger after each <strong>Interval</strong>. Set your interval time in milliseconds. In <strong>Limit</strong> specify the number of times the interval will run, causing the trigger to fire. If you do not specify a limit, the timer will repeat for as long as the page is on display.</p>
<p><strong>Trigger example:</strong></p>
<table>
<thead>
<tr>
<th>Rule type</th>
<th>Interval</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Timer</em></td>
<td><code>5000</code></td>
<td><code>1</code></td>
</tr>
</tbody>
</table>
<p>The above Timer will fire once, after five seconds. To improve the performance of a web page, you can limit a Timer trigger to a specific URL, by combining it with a Match rule. For example, to set up a timer on a specific page you can set up the following rules in a trigger:</p>
<table>
<thead>
<tr>
<th>Rule type</th>
<th>Interval</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Timer</em></td>
<td><code>5000</code></td>
<td><code>1</code></td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>Rule type</th>
<th>Variable name</th>
<th>Match operation</th>
<th>Match string</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Match rule</em></td>
<td><em>URL pathname</em></td>
<td><em>Equals</em></td>
<td><code>/my-page-path</code></td>
</tr>
</tbody>
</table>
<p>Refer to <a href="/zaraz/custom-actions/create-trigger/"><strong>Create a trigger</strong></a> to learn how to add more than one condition to a trigger.</p>

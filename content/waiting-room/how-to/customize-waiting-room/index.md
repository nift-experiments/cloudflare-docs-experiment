---
cp9:
  canonical: https://developers.cloudflare.com/waiting-room/how-to/customize-waiting-room/
  description: Customize the waiting room page with HTML templates.
  full_title: Customize a waiting room · Cloudflare Waiting Room docs
  head_html: <title>Customize a waiting room · Cloudflare Waiting Room docs</title><meta name="generator" content="Nift"><meta name="description" content="Customize the waiting room page with HTML templates."><link rel="canonical" href="https://developers.cloudflare.com/waiting-room/how-to/customize-waiting-room/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waiting-room/how-to/customize-waiting-room/index.md"><meta property="og:title" content="Customize a waiting room · Cloudflare Waiting Room docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Customize the waiting room page with HTML templates."><meta property="og:url" content="https://developers.cloudflare.com/waiting-room/how-to/customize-waiting-room/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Waiting Room"><meta name="algolia_product_filter" content="Waiting Room"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Waiting Room"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waiting-room/how-to/customize-waiting-room/#page","headline":"Customize a waiting room \u00b7 Cloudflare Waiting Room docs","description":"Customize the waiting room page with HTML templates.","url":"https://developers.cloudflare.com/waiting-room/how-to/customize-waiting-room/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waiting-room/how-to/customize-waiting-room/
  schema: 1
---
<p>You can customize your waiting room from the dashboard or via API.</p>
<h2 id="customize-a-waiting-room-from-the-dashboard">Customize a waiting room from the dashboard</h2>
<p>To design and preview the appearance of a waiting room, select the <strong>Customization</strong> tab in the <strong>Create waiting room</strong> page.</p>
<p>Cloudflare offers options to customize the appearance of your waiting room:</p>
<ul>
<li><a href="#default-waiting-room">Default waiting room</a>: An unbranded waiting room that displays an estimated waiting time to visitors.
<ul>
<li>Select a language for your default waiting room page. You can choose from the following languages: English, Arabic, German, Spanish, French, Indonesian, Italian, Japanese, Korean, Dutch, Polish, Portuguese (Brazilian), Turkish and Chinese (Simplified and Traditional).</li>
</ul>
</li>
<li><a href="#custom-waiting-room">Custom waiting room</a>: Edit template text or create your own HTML code:
<ul>
<li>Customize both HTML or CSS content, including fonts, colors, static images, additional languages and more.</li>
<li>Edit content directly in the dashboard or import relevant files.</li>
</ul>
</li>
<li><a href="/waiting-room/how-to/json-response/">Return a JSON-friendly waiting room response</a>: Toggle to also enable a JSON response with a user's status in the waiting room.</li>
</ul>
<h3 id="default-waiting-room">Default waiting room</h3>
<p>To choose the default, unbranded waiting room:</p>
<ol>
<li>Select a waiting room.</li>
<li>Go to the <strong>Customization</strong> step.</li>
<li>Select <strong>Default waiting room</strong>.</li>
<li>Select the language for your waiting room default page.</li>
</ol>
<h3 id="custom-waiting-room">Custom waiting room</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15747.md")
</aside>
<p>To customize a waiting room:</p>
<ol>
<li>Select a waiting room.</li>
<li>Go to the <strong>Customization</strong> step.</li>
<li>Select <strong>Custom waiting room</strong>.</li>
</ol>
<p>You can edit the HTML code directly in the text box:</p>
<ul>
<li>Select <strong>Download default template</strong> to download a HTML file containing the default template content to your computer.</li>
<li>Select <strong>Download</strong> to download a HTML file containing the text box content to your computer.</li>
<li>Select <strong>Copy</strong> to copy the text from the text box to your clipboard, then paste it into an editor of your choice.</li>
</ul>
<p>The template text contains <a href="#display-wait-time">code to display the wait time</a>. If you want to display the estimated wait time to visitors, do not delete this content.</p>
<h4 id="upload-an-html-file">Upload an HTML file</h4>
<ol>
<li>Select <strong>Import</strong> to upload a HTML file from your computer.</li>
<li>Select the file in the dialog and select <strong>Open</strong>. The HTML file size limit is 1,048,576 bytes (1 MB).</li>
</ol>
<p>Make further edits in the text box. Include the <a href="#display-wait-time">code to display the wait time</a> to display the estimated queue time on the waiting room page or create your own custom page using <a href="#available-variables">available variables</a>.</p>
<h4 id="display-wait-time">Display wait time</h4>
<p>The following content in the <code>&lt;main&gt;</code> section of the template HTML code displays the wait time:</p>
<pre tabindex="0"><code class="language-html">&lt;h2 id=&quot;time-remaining&quot;&gt;&#10;  &lt;noscript&gt;&#10;    {{#waitTimeKnown}}Your estimated wait time is {{waitTimeFormatted}}...{{/waitTimeKnown}}&#10;    {{^waitTimeKnown}}{{#queueIsFull}}The estimated wait time is greater than a day. You will&#10;    automatically be placed in the queue once space is available.{{/queueIsFull}}&#10;    {{^queueIsFull}}Your estimated wait time is unavailable.{{/queueIsFull}}{{/waitTimeKnown}}&#10;  &lt;/noscript&gt;&#10;&lt;/h2&gt;&#10;</code></pre>
<p>The following script within the <code>&lt;body&gt;</code> section after <code>&lt;main&gt;</code> fetches the wait time:</p>
<pre tabindex="0"><code class="language-html">&lt;script type=&quot;text/javascript&quot;&gt;&#10;  var remainingEl = document.getElementById(&#x27;time-remaining&#x27;);&#10;  var waitTime = {{waitTime}};&#10;  var waitTimeKnown = {{waitTimeKnown}};&#10;&#10;  var remainingString = &#x27;Your estimated wait time is &#x27;;&#10;&#10;  if (!waitTimeKnown) {&#10;    remainingString += &#x27;unavailable.&#x27;&#10;  } else {&#10;    if (waitTime === 1) {&#10;      remainingString += waitTime + &#x27; minute...&#x27;;&#10;    } else {&#10;      remainingString += waitTime + &#x27; minutes...&#x27;;&#10;    }&#10;  }&#10;&#10;  remainingEl.innerText = remainingString;&#10;&lt;/script&gt;&#10;</code></pre>
<h4 id="turnstile-variable">Turnstile variable</h4>
<p>If you are using Turnstile for your customized waiting room, you will need to ensure the <code>turnstile</code> variable is added. The default queuing page template and any newly created custom templates already include this variable. If you have an existing custom HTML template and wish to enable the Turnstile integration, you will need to add <code>{{{turnstile}}}</code> somewhere in the template to let Waiting Room know where the widget should be placed. Waiting Room uses Mustache templates, so including raw HTML within your template without escaping requires three curly braces instead of two.</p>
<pre tabindex="0"><code class="language-html">&lt;!DOCTYPE html&gt;&#10;&lt;html&gt;&#10;  &lt;head&gt;&#10;    &lt;title&gt;Waiting Room&lt;/title&gt;&#10;  &lt;/head&gt;&#10;  &lt;body&gt;&#10;    &lt;h1&gt;You are currently in the queue.&lt;/h1&gt;&#10;    {{#waitTimeKnown}}&#10;      &lt;h2&gt;Your estimated wait time is {{waitTimeFormatted}}.&lt;/h2&gt;&#10;    {{/waitTimeKnown}}&#10;    {{^waitTimeKnown}}&#10;      &lt;h2&gt;Your estimated wait time is unknown.&lt;/h2&gt;&#10;    {{/waitTimeKnown}}&#10;    {{#turnstile}}&#10;      &lt;!-- for a managed (and potentially interactive) challenge, you may want to instruct the user to complete the challenge --&gt;&#10;      &lt;p&gt;Please complete this challenge so we know you&#x27;re a human:&lt;/p&gt;&#10;      {{{turnstile}}} &lt;!-- include the turnstile widget --&gt;&#10;    {{/turnstile}}&#10;  &lt;/body&gt;&#10;&lt;/html&gt;&#10;</code></pre>
<p>When using Infinite Queue (especially with managed challenges which may be interactive), you may want to let users know that they will not be in the queue until they complete the challenge.</p>
<h4 id="available-variables">Available variables</h4>
<p>When you create a waiting room with custom HTML, you can have access to several variables to customize your response. For a full list of variables, refer to the <code>json_response_enabled</code> parameter in the <a href="/api/resources/waiting_rooms/methods/create/">Cloudflare API docs</a>.</p>
<h4 id="multiple-language-support">Multiple-language support</h4>
<p>Customizable waiting rooms can display text in any language supported by the UTF-8 character set. To display estimated wait time, you can use numeric variables like <code>waitTime</code> and <code>waitTimeHours</code> within your waiting room template, regardless of user language. However, at the time, the following variables are only available in English: <code>waitTimeFormatted</code>, <code>timeUntilEventStartFormatted</code>, and <code>timeUntilEventEndFormatted</code>.</p>
<p>If you would like to display different languages within your custom waiting room depending on path or subdomain, you can add JavaScript code to your custom HTML to do so. Below you can find a couple of starter templates that you can use as an example to start from:</p>
<ul>
<li>
<p>To display a different language based on path, download this <a href="/waiting-room/static/index.path.html.txt">template</a>. The template displays the content in English if the path contains <code>en</code> or as a default, Japanese if the path contains <code>jp</code>, French if the path contains <code>fr</code>, and Spanish if the path contains <code>es</code>.</p>
</li>
<li>
<p>To display a different language based on subdomain, download this <a href="/waiting-room/static/index.subdomain.html.txt">template</a>. The template displays the content in English as a default or if the subdomain contains <code>en</code>, Japanese if the subdomain contains <code>jp</code>, French if the subdomain contains <code>fr</code>, and Spanish if the subdomain contains <code>es</code>.</p>
</li>
</ul>
<p>Download either of these templates and customize them however you would like. Update the path or subdomain to reflect your site’s language selection structure. You may edit these templates to include other languages by adding translations to the <code>translations</code> object for each of the locales.</p>
<h4 id="resource-hosting">Resource hosting</h4>
<p>If you are using images or other resources for your customized waiting room, <strong>do not</strong> host those assets on the hostname covered by your waiting room. Otherwise, any requests for these assets will not be able to pass through the waiting room.</p>
<h3 id="preview-waiting-room">Preview waiting room</h3>
<p>To preview the appearance of a waiting room:</p>
<ol>
<li>In your application, go to <strong>Traffic</strong> &gt; <strong>Waiting Room</strong>.</li>
<li>Either <a href="/waiting-room/how-to/create-waiting-room/">create a waiting room</a> or <a href="/waiting-room/how-to/edit-delete-waiting-room/">edit an existing one</a>.</li>
<li>Go to the <strong>Review</strong> step.</li>
<li>Select <strong>Preview waiting room</strong>:</li>
</ol>
<ul>
<li>Choose <strong>Queueing</strong> to display the waiting room appearance when it is enabled on the dashboard and <strong>Queue-all</strong> is not enabled.</li>
<li>Choose <strong>Queue-All</strong> to display the waiting room appearance when it is enabled on the dashboard and <strong>Queue-all</strong> is enabled. When <strong>Queue-all</strong> is enabled for a waiting room, the estimated wait time is not displayed.</li>
</ul>
<h3 id="troubleshooting">Troubleshooting</h3>
<p>If you notice something unexpected when previewing your waiting room, review your custom code for proper syntax. Often, you might forget to close each tag with its appropriate closing tag (the tag name with a <code>/</code>).</p>
<h2 id="customize-a-waiting-room-via-api">Customize a waiting room via API</h2>
<p>You can use the Waiting Room API to customize the web page served to visitors when they are placed in a virtual waiting room.</p>
<p>In the following <code>PATCH</code> request, the <code>custom_page_html</code> field contains the HTML code for the <a href="/waiting-room/how-to/customize-waiting-room/">customized waiting room</a>:</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/waiting_rooms/{waiting_room_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;webshop-waiting-room&quot;,&#10;  &quot;host&quot;: &quot;example.com&quot;,&#10;  &quot;new_users_per_minute&quot;: 200,&#10;  &quot;total_active_users&quot;: 300,&#10;  &quot;custom_page_html&quot;: &quot;&lt;p&gt;Include custom HTML here&lt;/p&gt;&quot;&#10;}&#x27;</code></pre>
<p>Response:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: [&#10;    {&#10;      &quot;id&quot;: &quot;1111111111111111111111&quot;,&#10;      &quot;name&quot;: &quot;webshop-waiting-room&quot;,&#10;      &quot;description&quot;: &quot;Waiting room for webshop&quot;,&#10;      &quot;host&quot;: &quot;example.com&quot;,&#10;      &quot;path&quot;: &quot;/shop&quot;,&#10;      &quot;suspended&quot;: false,&#10;      &quot;queue_all&quot;: false,&#10;      &quot;new_users_per_minute&quot;: 200,&#10;      &quot;total_active_users&quot;: 300,&#10;      &quot;session_duration&quot;: 1,&#10;      &quot;disable_session_renewal&quot;: false,&#10;      &quot;json_response_enabled&quot;: false,&#10;      &quot;queueing_method&quot;: &quot;FIFO&quot;,&#10;      &quot;cookie_attributes&quot;: {&#10;        &quot;samesite&quot;: &quot;auto&quot;,&#10;        &quot;secure&quot;: &quot;auto&quot;&#10;      },&#10;      &quot;custom_page_html&quot;: &quot;&lt;p&gt;Include custom HTML here&lt;/p&gt;&quot;,&#10;      &quot;created_on&quot;: &quot;2014-01-01T05:20:00.12345Z&quot;,&#10;      &quot;modified_on&quot;: &quot;2014-01-01T05:20:00.12345Z&quot;&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<h3 id="preview-the-html-code-for-a-customized-waiting-room">Preview the HTML code for a customized waiting room</h3>
<p>Before making an API request to configure a waiting room web page with customized HTML, you can preview your custom HTML by uploading it to a preview endpoint:</p>
<pre tabindex="0"><code class="language-txt">POST https://api.cloudflare.com/client/v4/zones/{zone_id}/waiting_rooms/preview&#10;</code></pre>
<p>In the request body, include the customized HTML content in the <code>custom_html</code> field:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;custom_html&quot;: &quot;&lt;p&gt;Include custom HTML here&lt;/p&gt;&quot;&#10;}&#10;</code></pre>
<p>Note that you pass HTML content to the preview endpoint in the <code>custom_html</code> field, but when you are using the API to configure a waiting room, you pass the HTML content in the <code>custom_page_html</code> field.</p>
<p>Example request:</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/waiting_rooms/preview \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;custom_html&quot;: &quot;&lt;p&gt;Include custom HTML here&lt;/p&gt;&quot;&#10;}&#x27;</code></pre>
<p>The preview endpoint returns a temporary URL in the response body where you can preview your custom page:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;result&quot;: {&#10;    &quot;preview_url&quot;: &quot;https://waitingrooms.dev/preview/111111111111&quot;&#10;  },&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>You do not have to have a Cloudflare account to access the preview link, so you can validate the waiting room webpage on multiple devices.</p>
<h3 id="preview-the-default-or-current-waiting-room-web-page">Preview the default or current waiting room web page</h3>
<p>After <a href="/api/resources/waiting_rooms/subresources/page/methods/preview/">generating a preview URL</a>, use the following endpoint to generate a link to preview the currently configured web page for a waiting room, or the default page if no custom page is configured.</p>
<pre tabindex="0"><code class="language-txt">GET https://waitingrooms.dev/preview/{preview_id}&#10;</code></pre>
<p>The link in the response displays the content of the <code>custom_page_html</code> field, rendered with <a href="https://mustache.github.io">mustache</a>.</p>
<p>Use the optional <code>force_queue</code> query parameter to preview the waiting room web page when all traffic is force-queued.</p>

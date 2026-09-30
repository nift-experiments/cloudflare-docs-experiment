<p>You can add AI Search easily into your website using the <a href="https://search.ai.cloudflare.com/">Cloudflare AI Search UI snippet library</a>, which provides production-ready, customizable web components.</p>
<p>The library is open source at <a href="https://github.com/cloudflare/ai-search-snippet">github.com/cloudflare/ai-search-snippet</a>.</p>
<h2 id="available-components">Available components</h2>
<p>The snippet library provides four web components. Each component connects to your AI Search instance using the <code>api-url</code> attribute, which should point to your public endpoint URL.</p>
<table>
<thead>
<tr>
<th>Component</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&lt;search-bar-snippet&gt;</code></td>
<td>An inline search bar that displays results in a dropdown</td>
</tr>
<tr>
<td><code>&lt;search-modal-snippet&gt;</code></td>
<td>A search modal that opens with <code>Cmd/Ctrl+K</code> keyboard shortcut</td>
</tr>
<tr>
<td><code>&lt;chat-bubble-snippet&gt;</code></td>
<td>A floating chat bubble in the corner of the page</td>
</tr>
<tr>
<td><code>&lt;chat-page-snippet&gt;</code></td>
<td>A full-page chat interface with conversation history</td>
</tr>
</tbody>
</table>
<p>For advanced styling and configuration, visit <a href="https://search.ai.cloudflare.com/">search.ai.cloudflare.com</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>UI snippets connect to your AI Search instance through a public endpoint. You need to enable this endpoint before using the snippets.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3100.md")
</div>
<h2 id="use-with-html">Use with HTML</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3101.md")
</div>
<h3 id="full-html-example">Full HTML example</h3>
<p>The following example shows a complete HTML page with a search bar. When a user types in the search bar, results appear in a dropdown below.</p>
<pre><code class="language-html">&lt;!doctype html&gt;&#10;&lt;html&gt;&#10;	&lt;head&gt;&#10;		&lt;script&#10;			type=&quot;module&quot;&#10;			src=&quot;https://&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com/assets/v0.0.25/search-snippet.es.js&quot;&#10;		&gt;&lt;/script&gt;&#10;	&lt;/head&gt;&#10;	&lt;body&gt;&#10;		&lt;search-bar-snippet&#10;			api-url=&quot;https://&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com/&quot;&#10;			placeholder=&quot;Search...&quot;&#10;			max-results=&quot;10&quot;&#10;		&gt;&lt;/search-bar-snippet&gt;&#10;	&lt;/body&gt;&#10;&lt;/html&gt;&#10;</code></pre>
<h2 id="use-with-a-framework">Use with a framework</h2>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3106.md")
</div></div>
<h2 id="configure-a-component">Configure a component</h2>
<p>Each component accepts attributes that control its behavior. Common attributes include:</p>
<table>
<thead>
<tr>
<th>Attribute</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>api-url</code></td>
<td>Required. Your instance's public endpoint URL.</td>
</tr>
<tr>
<td><code>placeholder</code></td>
<td>Placeholder text for the input.</td>
</tr>
<tr>
<td><code>max-results</code></td>
<td>Maximum number of results to request.</td>
</tr>
<tr>
<td><code>theme</code></td>
<td><code>light</code>, <code>dark</code>, or <code>auto</code> (default) to follow the system theme.</td>
</tr>
<tr>
<td><code>hide-branding</code></td>
<td>Hide the Cloudflare branding.</td>
</tr>
<tr>
<td><code>translations</code></td>
<td>Override the user-facing strings to localize the component.</td>
</tr>
</tbody>
</table>
<p>The chat components (<code>&lt;chat-bubble-snippet&gt;</code> and <code>&lt;chat-page-snippet&gt;</code>) also accept <code>chat-query-rewrite</code> to rewrite follow-up messages into standalone queries.</p>
<p>For the complete list of attributes and a live editor that generates the HTML, React, or Vue code for you, use the <a href="https://search.ai.cloudflare.com/">snippet playground</a>.</p>
<h2 id="customize-the-appearance">Customize the appearance</h2>
<p>Style the components with CSS custom properties, all prefixed with <code>--search-snippet-</code>. Set them on the component or a parent element:</p>
<pre><code class="language-css">search-bar-snippet {&#10;	&#45;-search-snippet-primary-color: #f6821f;&#10;	&#45;-search-snippet-border-radius: 12px;&#10;}&#10;</code></pre>
<p>The <a href="https://search.ai.cloudflare.com/">playground</a> lists every available variable and previews your changes live.</p>
<h2 id="configure-cors-for-local-testing">Configure CORS for local testing</h2>
<p>When testing locally (for example, <code>http://localhost:3000</code>), you need to allow your local origin in the public endpoint settings.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3107.md")
</div>
<p>When you deploy, replace <code>*</code> with your production origin so that other sites cannot embed your search components. Allowed origins are a browser control, not an access control, so this does not stop a direct request from <code>curl</code> or a script. To restrict who can query the endpoint, refer to <a href="/ai-search/configuration/retrieval/public-endpoint/cloudflare-access/">Cloudflare Access</a>.</p>

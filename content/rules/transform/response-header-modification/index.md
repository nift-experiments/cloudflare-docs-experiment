<p>Use Response Header Transform Rules to manipulate the headers of HTTP responses sent to website visitors.</p>
<pre><code class="language-mermaid">flowchart LR&#10;accTitle: Header modifications diagram&#10;accDescr: Header transform rules can change the headers sent to your origin server (request header modifications) or sent your website visitors (response header modifications).&#10;&#10;A[Visitor]&#10;B((Cloudflare))&#10;C[(Origin server)]&#10;&#10;A -.-&gt; B -. &quot;Includes request&lt;br&gt; header modifications&quot; .-&gt; C&#10;C -.-&gt; B == &quot;Includes response&lt;br&gt; header modifications&quot; ==&gt; A&#10;&#10;style A stroke-width: 2px&#10;style B stroke: orange,fill: orange,color: black&#10;linkStyle 0,1,2 stroke-width: 1px&#10;linkStyle 3 stroke-width: 3px&#10;</code></pre>
<br />
<p>To modify HTTP headers in the <strong>request</strong> sent to your origin server, refer to <a href="/rules/transform/request-header-modification/">Request Header Transform Rules</a>.</p>
<p>Through Response Header Transform Rules you can:</p>
<ul>
<li>Set the value of an HTTP response header to a literal string value, overwriting its previous value or adding a new header to the response if it does not exist.</li>
<li>Set the value of an HTTP response header according to an expression, overwriting its previous value or adding a new header to the response if it does not exist.</li>
<li>Add a new HTTP response header with a literal string value without removing any existing headers with the same name.</li>
<li>Add a new HTTP response header according to an expression without removing any existing headers with the same name.</li>
<li>Remove an HTTP header from the response.</li>
</ul>
<p>You can create a response header transform rule <a href="/rules/transform/response-header-modification/create-dashboard/">in the dashboard</a>, <a href="/rules/transform/response-header-modification/create-api/">via API</a>, or <a href="/terraform/additional-configurations/transform-rules/#create-a-response-header-transform-rule">using Terraform</a>.</p>
<p>For more complex response header modifications, consider using <a href="/rules/snippets/">Snippets</a>.</p>
<h2 id="important-remarks">Important remarks</h2>
<ul>
<li>
<p>The response header values are calculated using the field values from the corresponding HTTP request. For example, the field <code>ip.src.country</code> (used in expressions) will return the country of the website visitor, not the country of the origin server where the response was sent from.</p>
</li>
<li>
<p>You cannot add, modify, or remove HTTP response headers whose name starts with <code>cf-</code> or <code>x-cf-</code>.</p>
</li>
<li>
<p>You cannot modify the value of certain headers such as <code>server</code>, <code>eh-cache-tag</code>, or <code>eh-cdn-cache-control</code>.</p>
</li>
<li>
<p>Currently you cannot reference <a href="/waf/tools/lists/custom-lists/#ip-lists">IP lists</a> in expressions of Response Header Transform Rules.</p>
</li>
<li>
<p>The HTTP response header removal operation will remove all response headers with the provided name.</p>
</li>
<li>
<p>If you change the value of an existing HTTP response header using an expression that evaluates to an empty string (<code>&quot;&quot;</code>) or an undefined value, the HTTP response header is <strong>removed</strong>.</p>
</li>
<li>
<p>Currently, there is a limited number of HTTP response headers that you cannot change. Cloudflare may remove restrictions for some of these HTTP response headers when presented with valid use cases. <a href="https://community.cloudflare.com">Create a post in the community</a> for consideration.</p>
</li>
<li>
<p>Response header transform rules will also apply to default Cloudflare error pages and <a href="/rules/custom-errors/">Custom Errors</a>.</p>
</li>
<li>
<p>Modifying <code>cache-control</code>, <code>CDN-Cache-Control</code>, or <code>Cloudflare-CDN-Cache-Control</code> headers using response header transform rules will not change the way Cloudflare caches an object, because Cloudflare evaluates caching behavior before applying response header modifications. To control Cloudflare cache behavior, create a <a href="/cache/how-to/cache-rules/">cache rule</a>.</p>
</li>
<li>
<p>To add a <code>set-cookie</code> header to the response, use one of the <em>Add static</em>/<em>Add dynamic</em> operations instead of <em>Set static</em>/<em>Set dynamic</em>. <em>Add</em> operations append a new header without removing existing headers of the same name, while <em>Set</em> operations replace all existing headers of that name. Using a <em>Set</em> operation for <code>set-cookie</code> will remove any <code>set-cookie</code> headers already in the response, including those added by other Cloudflare products such as Bot Management.</p>
</li>
<li>
<p>Response header transform rules run in order, and later rules can overwrite changes done by previous rules.</p>
</li>
<li>
<p>The values of request and response fields are immutable within each <a href="/ruleset-engine/about/phases/">phase</a>, such as the <code>http_response_headers_transform</code> phase where response header transform rules are defined. This means that later response header transform rules will still use the original field values when evaluating their filter expressions, not the values changed by previous rules. Refer to <a href="/ruleset-engine/about/rules/#field-values-during-rule-evaluation">Field values during rule evaluation</a> for more information.</p>
</li>
</ul>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>When troubleshooting Response Header Transform Rules, use <a href="/rules/trace-request/">Cloudflare Trace</a> to determine if a rule is triggering for a specific URL.</p>

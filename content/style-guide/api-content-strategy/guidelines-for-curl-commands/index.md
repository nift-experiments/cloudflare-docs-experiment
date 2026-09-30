<p>We follow several formatting conventions for cURL commands.</p>
<h2 id="components">Components</h2>
<p>To automatically incorporate our conventions into your examples, use:</p>
<ul>
<li><a href="/style-guide/build-the-page/components/api-request/"><code>APIRequest</code></a>: For examples hitting endpoints in the Cloudflare API schema.</li>
<li><a href="/style-guide/build-the-page/components/curl/"><code>CURL</code></a>: For other cURL commands.</li>
</ul>
<h2 id="parameter-names">Parameter names</h2>
<p>Use long parameter names for clarity:</p>
<ul>
<li><code>--header</code> (instead of <code>-H</code>)</li>
<li><code>--request</code> (when needed, instead of <code>-X</code>)</li>
<li><code>--data</code> (instead of <code>-d</code>)</li>
</ul>
<p>You do not need to use the <code>--url</code> parameter since it is the main cURL parameter. Also, the URL does not need to be enclosed in double quotes (<code>&quot;&quot;</code>), except if it contains a <code>?</code> character (that is, when it includes a query string).</p>
<h2 id="indentation">Indentation</h2>
<p>Use two spaces to indent request or response bodies (the additional data included in the request/response).</p>
<p>For requests with body content, start indenting when you get to the body part (the line after <code>--data</code> in the examples in this page). This means that the URL, any headers, and the line containing the <code>--data</code> parameter should not be indented.</p>
<p>Requests without a body should not be indented also, to make them consistent with requests containing a body.</p>
<h2 id="do-not-use-jq-as-part-of-curl-examples">Do not use jq as part of cURL examples</h2>
<p><a href="https://jqlang.github.io/jq/">jq</a> is a separate tool that not everyone will have installed. cURL examples should not include response formatting through jq as part of the example.</p>
<p>If you must suggest the use of this tool, you can add a link to the <a href="/fundamentals/api/how-to/make-api-calls/">Make API calls</a> page in Fundamentals, which mentions this tool. Do not repeat the existing content about jq near the cURL example.</p>
<h2 id="request-guidelines">Request guidelines</h2>
<h3 id="preliminary-notes">Preliminary notes</h3>
<ul>
<li>Make sure not to use typographical or smart quotes in a cURL command, or the command will fail.</li>
<li>Placeholders in the URL should follow the same format as in the API documentation: <code>$ZONE_ID</code></li>
<li>Placeholders in the request body (that is, the data included in a <code>POST</code>/<code>PUT</code>/<code>PATCH</code> request) should use <a href="/style-guide/style-and-grammar/formatting/code-conventions-and-format/#angle-brackets---and--">angle brackets</a>: <code>&lt;RULE_ID&gt;</code></li>
</ul>
<p>The same placeholder name should correspond to the same value – use different placeholder names for different ID values. You can use the same request placeholders in the response, if they should match the values in the request.</p>
<h3 id="authentication-http-headers">Authentication HTTP headers</h3>
<p>If using Email + API Key authentication, include the following arguments in the cURL command to add the two required HTTP headers to the request:</p>
<pre><code class="language-txt">&#45;-header &quot;X-Auth-Email: $CLOUDFLARE_EMAIL&quot; \&#10;&#45;-header &quot;X-Auth-Key: $CLOUDFLARE_API_KEY&quot; \&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14612.md")
</aside>
<p>If using API Token (the preferred authentication method), include the following arguments in the cURL command to add the required HTTP header to the request:</p>
<pre><code class="language-txt">&#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;</code></pre>
<h3 id="request-without-body-content-get-delete">Request without body content (<code>GET</code>, <code>DELETE</code>)</h3>
<p>For <code>GET</code> requests, do not include the <code>--request GET</code> command-line argument, since it is the default where the request does not include a body and it is not recommended for <code>GET</code>/<code>POST</code> requests:</p>
<h4 id="get-request-template"><code>GET</code> request template</h4>
<pre><code class="language-txt">curl {full_url_with_placeholders} \&#10;&#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/zones/$ZONE_ID/firewall/rules \&#10;&#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<h4 id="delete-request-template"><code>DELETE</code> request template</h4>
<pre><code class="language-txt">curl --request DELETE \&#10;{full_url_with_placeholders} \&#10;&#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>Requests without a body do not need syntax highlight, but we use <code>bash</code> syntax highlighting to highlight the several delimited strings.</p>
<h3 id="request-with-json-body-content-post-put-patch">Request with JSON body content (<code>POST</code>, <code>PUT</code>, <code>PATCH</code>)</h3>
<p>Make sure to include a <code>Content-Type</code> header if the request includes a body. For requests with JSON content, the header should be <code>Content-Type: application/json</code>.</p>
<p>This header should appear after the authentication headers.</p>
<p>For <code>POST</code> requests with a body, do not include the <code>--request POST</code> command-line argument, since it is the default when the request includes a body.</p>
<h4 id="post-request-template"><code>POST</code> request template</h4>
<pre><code class="language-txt">curl {full_url_with_placeholders} \&#10;&#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;({|[)&#10;  (...JSON content, pretty printed, using 2-space indents...)&#10;(}|])&#x27;&#10;</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/zones/$ZONE_ID/firewall/rules \&#10;&#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;[&#10;  {&#10;    &quot;filter&quot;: {&#10;      &quot;id&quot;: &quot;&lt;FILTER_ID&gt;&quot;&#10;    },&#10;    &quot;action&quot;: &quot;allow&quot;,&#10;    &quot;description&quot;: &quot;Do not challenge login from office&quot;&#10;  }&#10;]&#x27;&#10;</code></pre>
<h4 id="put-patch-request-template"><code>PUT</code>/<code>PATCH</code> request template</h4>
<pre><code class="language-txt">curl --request (PUT/PATCH) \&#10;{full_url_with_placeholders} \&#10;&#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;({|[)&#10;  (...JSON content, pretty printed, using 2-space indents...)&#10;(}|])&#x27;&#10;</code></pre>
<p>Enclose the JSON payload ( the <code>--data</code> command-line argument) in single quotes (<code>'</code>) instead of double quotes because it requires less escaping (strings in JSON must be delimited using double quotes).</p>
<h4 id="escaping-a-single-quote-in-the-body">Escaping a single quote in the body</h4>
<p>The recommended way of escaping a single quote inside the body is the following (assuming the user will run the command in a bash-like terminal):</p>
<ul>
<li>Replace the single quote <code>'</code> with <code>'\''</code></li>
</ul>
<p>Which means &quot;close string, add escaped single quote, begin string again&quot;.</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/api/v4/zones/$ZONE_ID/page_shield/policies \&#10;&#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;value&quot;: &quot;script-src myapp.example.com cdnjs.cloudflare.com https://www.google-analytics.com/analytics.js &#x27;\&#x27;&#x27;self&#x27;\&#x27;&#x27;&quot;&#10;}&#x27;&#10;</code></pre>
<h4 id="post-requests-without-a-body"><code>POST</code> requests without a body</h4>
<p>If you have a <code>POST</code> request without a body, you must add the <code>--request POST</code> argument explicitly to the cURL command.</p>
<pre><code class="language-txt">curl --request POST \&#10;{full_url_with_placeholders} \&#10;&#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<h3 id="additional-information">Additional information</h3>
<p>Code blocks with example requests that include a JSON body should use <code>bash</code> syntax, similarly to example requests without a body.</p>
<h3 id="full-request-example">Full request example</h3>
<pre><code class="language-bash">curl https://api.cloudflare.com/api/v4/zones/$ZONE_ID/page_shield/policies \&#10;&#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;description&quot;: &quot;My first policy in log mode&quot;,&#10;  &quot;action&quot;: &quot;log&quot;,&#10;  &quot;expression&quot;: &quot;http.host eq \&quot;myapp.example.com\&quot;&quot;,&#10;  &quot;enabled&quot;: &quot;true&quot;,&#10;  &quot;value&quot;: &quot;script-src myapp.example.com cdnjs.cloudflare.com https://www.google-analytics.com/analytics.js &#x27;\&#x27;&#x27;self&#x27;\&#x27;&#x27;&quot;&#10;}&#x27;&#10;</code></pre>
<h2 id="response-guidelines">Response guidelines</h2>
<p>Include the complete response (including any empty error and message arrays, if present) using <code>json</code> syntax highlighting.</p>
<p>A response starts either with an object (<code>{ ... }</code>) or a list (<code>[ ... ]</code>). The initial character should appear on its own line, as well as the last character.</p>
<pre><code class="language-txt">({|[)&#10;  (...JSON content, pretty printed, using 2-space indents...)&#10;(}|])&#10;</code></pre>
<ul>
<li>If there are IDs that were obtained using a previous command, or if their exact value is not relevant in the current context, use a placeholder (for example, <code>&lt;RULE_ID&gt;</code>) instead of the ID. The same placeholder name should correspond to the same value. Use different placeholder names for different ID values.</li>
<li>Response excerpts or snippets containing the most relevant parts of the response body should mention that they do not correspond to the entire response.</li>
</ul>
<h3 id="full-response-example">Full response example</h3>
<pre><code class="language-json">{&#10;  &quot;result&quot;: {&#10;    &quot;id&quot;: &quot;&lt;RULE_ID&gt;&quot;,&#10;    &quot;paused&quot;: false,&#10;    &quot;description&quot;: &quot;do not challenge login from office&quot;,&#10;    &quot;action&quot;: &quot;allow&quot;,&#10;    &quot;priority&quot;: null,&#10;    &quot;filter&quot;: {&#10;      &quot;id&quot;: &quot;&lt;FILTER_ID&gt;&quot;,&#10;      &quot;expression&quot;: &quot;ip.src in {2400:cb00::/32 2803:f800::/32 2c0f:f248::/32 2a06:98c0::/29} and (http.request.uri.path ~ \&quot;^.*/wp-login.php$\&quot; or http.request.uri.path ~ \&quot;^.*/xmlrpc.php$\&quot;)&quot;,&#10;      &quot;paused&quot;: false,&#10;      &quot;description&quot;: &quot;Login from office&quot;&#10;    }&#10;  },&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: []&#10;}&#10;</code></pre>

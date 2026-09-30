<p>Many organizations qualify traffic based on the presence of specific HTTP request headers. Use the Rules language <a href="/ruleset-engine/rules-language/fields/reference/?field-category=Headers&amp;search-term=http.request">HTTP request header fields</a> to target requests with specific headers.</p>
<h2 id="example-1-require-presence-of-http-header">Example 1: Require presence of HTTP header</h2>
<p>This example custom rule uses the <a href="/ruleset-engine/rules-language/fields/reference/http.request.headers.names/"><code>http.request.headers.names</code></a> field to look for the presence of an <code>X-CSRF-Token</code> header. The <a href="/ruleset-engine/rules-language/functions/#lower"><code>lower()</code></a> transformation function converts the header name to lowercase so that the expression is case-insensitive.</p>
<p>When the <code>X-CSRF-Token</code> header is missing, Cloudflare blocks the request.</p>
<ul>
<li>
<p><strong>When incoming requests match</strong>:</p>
<p>Use the expression editor:<br/>
<code>not any(lower(http.request.headers.names[*])[*] eq &quot;x-csrf-token&quot;) and (http.request.full_uri eq &quot;https://www.example.com/somepath&quot;)</code></p>
</li>
<li>
<p><strong>Then take action</strong>: <em>Block</em></p>
</li>
</ul>
<h2 id="example-2-require-http-header-with-a-specific-value">Example 2: Require HTTP header with a specific value</h2>
<p>This example custom rule uses the <a href="/ruleset-engine/rules-language/fields/reference/http.request.headers/"><code>http.request.headers</code></a> field to look for the presence of the <code>X-Example-Header</code> header and to get its value (if any). When the <code>X-Example-Header</code> header is missing or it does not have the value <code>example-value</code>, Cloudflare blocks the request.</p>
<ul>
<li>
<p><strong>When incoming requests match</strong>:</p>
<p>Use the expression editor:<br/>
<code>not any(http.request.headers[&quot;x-example-header&quot;][*] eq &quot;example-value&quot;) and (http.request.uri.path eq &quot;/somepath&quot;)</code></p>
</li>
<li>
<p><strong>Then take action</strong>: <em>Block</em></p>
</li>
</ul>
<p>The keys in the <code>http.request.headers</code> field, corresponding to HTTP header names, are in lowercase.</p>
<p>In this example the header name is case-insensitive, but the header value is case-sensitive.</p>

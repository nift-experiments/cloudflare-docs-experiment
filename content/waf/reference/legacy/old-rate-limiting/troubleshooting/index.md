<p>A few common rate limiting configuration issues prevent proper request matches:</p>
<ul>
<li><strong>Including HTTP or HTTPS protocol schemes in rule patterns</strong> (such as <code>https://example.com/*</code>). To restrict rules to match only HTTP or HTTPS traffic, use the schemes array in the request match. For example, <code>&quot;schemes&quot;: [ &quot;HTTPS&quot; ]</code>.</li>
<li><strong>Forgetting a trailing slash character (<code>/</code>)</strong>. Cloudflare Rate Limiting only treats requests for the homepage (such as <code>example.com</code> and <code>example.com/</code>) as equivalent, but not any other path (such as <code>example.com/path/</code> and <code>example.com/path</code>). To match request paths both with and without the trailing slash, use a wildcard match (for example, <code>example.com/path*</code>).</li>
<li><strong>Including a query string or anchor</strong> (such as <code>example.com/path?foo=bar</code> or <code>example.com/path#section1</code>). A rule like <code>example.com/path</code> will match requests for <code>example.com/path?foo=bar</code>.</li>
<li><strong>Overriding a rate limit with <a href="/waf/tools/ip-access-rules/">IP Access rules</a></strong>.</li>
<li><strong>Including a port number</strong> (such as <code>example.com:8443/api/</code>). Rate Limiting does not consider port numbers within rules. Remove the port number from the URL so that the rate limit rule triggers as expected.</li>
</ul>
<h2 id="common-api-errors">Common API errors</h2>
<p>The following common errors may prevent configuring rate limiting rules via the <a href="/api/resources/rate_limits/methods/create/">Cloudflare API</a>:</p>
<ul>
<li><code>Decoding is not yet implemented</code> – Indicates that your request is missing the <code>Content-Type: application/json</code> header. Add the header to your API request to fix the issue.</li>
<li><code>Ratelimit.api.not_entitled</code> – Enterprise customers must contact their account team before adding rules.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15691.md")
</aside>

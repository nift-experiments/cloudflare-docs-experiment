<p>The following sections describe the settings of redirect rules to configure static and dynamic URL redirects.</p>
<h2 id="wildcard-url-redirect">Wildcard URL Redirect</h2>
<p>Performs a URL redirect using <a href="/ruleset-engine/rules-language/operators/#wildcard-matching">wildcard patterns</a> to match multiple requests. This method simplifies defining source and target URL patterns without needing complex expressions.</p>
<p>A wildcard URL redirect has the following configuration parameters:</p>
<ul>
<li>
<p><strong>Request URL</strong>: Enter the <a href="/ruleset-engine/rules-language/operators/#wildcard-matching">wildcard pattern</a> using the asterisk (<code>*</code>) character to match multiple requests. For example, <code>https://*.example.com/files/*</code>.</p>
</li>
<li>
<p><strong>Target URL</strong>: Enter the target URL, which can be static (for example, <code>https://example.com</code>) or dynamic (for example, <code>https://example.com/${1}/files/${2}</code>). Use <a href="/ruleset-engine/rules-language/functions/#wildcard_replace">wildcard replacement</a> like <code>${1}</code>, <code>${2}</code>, etc., to define dynamic targets.</p>
</li>
<li>
<p><strong>Status code</strong>: The HTTP status code of the redirect response (<em>301 - Permanent Redirect</em> by default). Must be one of the following:</p>
</li>
<li>
<p><strong>301 - Permanent Redirect</strong>: The page has permanently moved to a new address. For <code>POST</code> requests, the client or browser might switch the HTTP method to <code>GET</code> when following the redirect.</p>
</li>
<li>
<p><strong>302 - Temporary Redirect</strong>: The page has temporarily moved to a new address. For <code>POST</code> requests, the client or browser might switch the HTTP method to <code>GET</code> when following the redirect.</p>
</li>
<li>
<p><strong>307 - Advanced: Temporary, HTTP method preserved</strong>: The page has temporarily moved to a new address. The client or browser must preserve the original HTTP method (for example, <code>POST</code>) when following the redirect.</p>
</li>
<li>
<p><strong>308 - Advanced: Permanent, HTTP method preserved</strong>: The page has permanently moved to a new address. The client or browser must preserve the original HTTP method (for example, <code>POST</code>) when following the redirect.</p>
</li>
<li>
<p><strong>Preserve query string</strong>: Whether to preserve the query string when redirecting (disabled by default).</p>
</li>
</ul>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13187.md")
</div></details>
<h2 id="static-url-redirect">Static URL redirect</h2>
<p>Performs a static URL redirect with a given HTTP status code and optionally preserves the query string.</p>
<p>A static URL redirect has the following configuration parameters:</p>
<ul>
<li>
<p><strong>URL</strong>: A literal string that will be used in the <code>Location</code> HTTP header returned in the redirect response.</p>
</li>
<li>
<p><strong>Status code</strong>: The HTTP status code of the redirect response (<em>301 - Permanent Redirect</em> by default). Must be one of the following:</p>
</li>
<li>
<p><strong>301 - Permanent Redirect</strong>: The page has permanently moved to a new address. For <code>POST</code> requests, the client or browser might switch the HTTP method to <code>GET</code> when following the redirect.</p>
</li>
<li>
<p><strong>302 - Temporary Redirect</strong>: The page has temporarily moved to a new address. For <code>POST</code> requests, the client or browser might switch the HTTP method to <code>GET</code> when following the redirect.</p>
</li>
<li>
<p><strong>307 - Advanced: Temporary, HTTP method preserved</strong>: The page has temporarily moved to a new address. The client or browser must preserve the original HTTP method (for example, <code>POST</code>) when following the redirect.</p>
</li>
<li>
<p><strong>308 - Advanced: Permanent, HTTP method preserved</strong>: The page has permanently moved to a new address. The client or browser must preserve the original HTTP method (for example, <code>POST</code>) when following the redirect.</p>
</li>
<li>
<p><strong>Preserve query string</strong>: Whether to preserve the query string when redirecting (disabled by default).</p>
</li>
</ul>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13188.md")
</div></details>
<h2 id="dynamic-url-redirect">Dynamic URL redirect</h2>
<p>Performs a dynamic URL redirect, where the target URL is determined by an expression. You can configure the redirect HTTP status code and whether to preserve the query string when redirecting.</p>
<p>A dynamic URL redirect has the following configuration parameters:</p>
<ul>
<li>
<p><strong>Expression</strong>: An <a href="/ruleset-engine/rules-language/expressions/">expression</a> that defines the target URL of the redirect. The result of evaluating this expression will be used in the <code>Location</code> HTTP header returned in the redirect response. Refer to the <a href="/ruleset-engine/rules-language/fields/reference/">fields</a> and <a href="/ruleset-engine/rules-language/functions/">functions</a> you can use in expressions.</p>
</li>
<li>
<p><strong>Status code</strong>: The HTTP status code of the redirect response (<em>301 - Permanent Redirect</em> by default). Must be one of the following:</p>
</li>
<li>
<p><strong>301 - Permanent Redirect</strong>: The page has permanently moved to a new address. For <code>POST</code> requests, the client or browser might switch the HTTP method to <code>GET</code> when following the redirect.</p>
</li>
<li>
<p><strong>302 - Temporary Redirect</strong>: The page has temporarily moved to a new address. For <code>POST</code> requests, the client or browser might switch the HTTP method to <code>GET</code> when following the redirect.</p>
</li>
<li>
<p><strong>307 - Advanced: Temporary, HTTP method preserved</strong>: The page has temporarily moved to a new address. The client or browser must preserve the original HTTP method (for example, <code>POST</code>) when following the redirect.</p>
</li>
<li>
<p><strong>308 - Advanced: Permanent, HTTP method preserved</strong>: The page has permanently moved to a new address. The client or browser must preserve the original HTTP method (for example, <code>POST</code>) when following the redirect.</p>
</li>
<li>
<p><strong>Preserve query string</strong>: Whether to preserve the query string when redirecting (disabled by default).</p>
</li>
</ul>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13189.md")
</div></details>

<p>A URL redirect has a source URL, a target URL, a status code, and some additional parameters that affect its URL matching behavior and runtime behavior.</p>
<h2 id="source-url">Source URL</h2>
<p>API field: <code>source_url</code> <span class="nb-type">String</span></p>
<p>The URL string that the incoming request URL must match for the redirect to be applied. This property is mandatory. The maximum length of the source URL is 32 KB.</p>
<p>The value must be a valid URL, but the URL scheme is not required (for example, <code>https</code>); when the scheme is omitted, the redirect applies to both <code>http</code> and <code>https</code> URL schemes.</p>
<p>A Bulk Redirect List cannot contain several URL redirects with the exact same source URL.
The exact behavior of the <a href="/rules/url-forwarding/bulk-redirects/how-it-works/#url-matching-algorithm">URL matching algorithm</a>, which matches an incoming request with the redirect's source URL, depends on the values of the <a href="#include-subdomains"><strong>Include subdomains</strong></a> and <a href="#subpath-matching"><strong>Subpath matching</strong></a> parameters.</p>
<p>For more information on the supported URL components, refer to <a href="/rules/url-forwarding/bulk-redirects/reference/url-components/">Supported URL components in Bulk Redirects</a>.</p>
<h2 id="target-url">Target URL</h2>
<p>API field: <code>target_url</code> <span class="nb-type">String</span></p>
<p>The URL where the client will be redirected to when there is a match for the URL redirect. This property is mandatory. The maximum length of the target URL is 32 KB.</p>
<p>The value must be a valid URL. The final target URL depends on the values of the <a href="#preserve-query-string"><strong>Preserve query string</strong></a> and <a href="#preserve-path-suffix"><strong>Preserve path suffix</strong></a> parameters.</p>
<p>For more information on the supported URL components, refer to <a href="/rules/url-forwarding/bulk-redirects/reference/url-components/">Supported URL components in Bulk Redirects</a>.</p>
<h2 id="subpath-matching">Subpath matching</h2>
<p>API field: <code>subpath_matching</code> <span class="nb-type">Boolean</span> <span class="nb-metainfo">default: false</span></p>
<p>If <code>true</code>, the current redirect will apply the subpath matching algorithm to the request URL when determining if there is a match for the current URL redirect.</p>
<p>For example, a URL redirect from <code>/my-folder/</code> to <code>/other-folder/</code> with <strong>Subpath matching</strong> enabled will also redirect a request from <code>/my-folder/item</code> to <code>/other-folder/item</code>. However, the redirect will only include the <code>item</code> part when <a href="#preserve-path-suffix"><strong>Preserve path suffix</strong></a> is <code>true</code>.</p>
<p>For more information, refer to <a href="/rules/url-forwarding/bulk-redirects/how-it-works/#matching-the-source-url-of-redirects">Matching the source URL of redirects</a>.</p>
<h2 id="include-subdomains">Include subdomains</h2>
<p>API field: <code>include_subdomains</code> <span class="nb-type">Boolean</span> <span class="nb-metainfo">default: false</span></p>
<p>If <code>true</code>, the source URL hostname will also apply to any subdomains — the redirect will match for all subdomains to the left of the domain portion of the source URL, as well as the specified domain.</p>
<p>For example, a redirect with source URL defined as <code>http://example.com/about</code> will also apply to requests with source URL <code>http://a.example.com/about</code> or <code>http://a.b.example.com/about</code>.</p>
<p>For more information, refer to <a href="/rules/url-forwarding/bulk-redirects/how-it-works/#matching-the-source-url-of-redirects">Matching the source URL of redirects</a>.</p>
<h2 id="preserve-query-string">Preserve query string</h2>
<p>API field: <code>preserve_query_string</code> <span class="nb-type">Boolean</span> <span class="nb-metainfo">default: false</span></p>
<p>If <code>true</code>, the redirect URL will keep the query string of the original request.</p>
<p>For example, a URL redirect from <code>/my-folder/</code> to <code>/other-folder/</code> with <strong>Preserve query string</strong> enabled will redirect a request from <code>/my-folder/?name=value</code> to <code>/other-folder/?name=value</code>. If <strong>Preserve query string</strong> is disabled, the request will be redirected from <code>/my-folder/?name=value</code> to <code>/other-folder/</code>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13232.md")
</aside>
<h2 id="preserve-path-suffix">Preserve path suffix</h2>
<p>API field: <code>preserve_path_suffix</code> <span class="nb-type">Boolean</span> <span class="nb-metainfo">default: true</span></p>
<p>Applicable only when <a href="#subpath-matching"><strong>Subpath matching</strong></a> is enabled. If <code>true</code>, defines that the redirect URL will include the remaining (non-matched) path elements of the source URL, if any.</p>
<p>For example, when both <strong>Subpath matching</strong> and <strong>Preserve path suffix</strong> are enabled, a URL redirect from <code>/my-folder/</code> to <code>/another-folder/</code> will redirect an incoming request from <code>/my-folder/foo</code> to <code>/another-folder/foo</code>. If <strong>Preserve path suffix</strong> is disabled, the same request would still match the URL redirect, but it would redirect from <code>/my-folder/foo</code> to <code>/another-folder/</code>.</p>
<h2 id="status-code">Status code</h2>
<p>API field: <code>status_code</code> <span class="nb-type">Integer</span> <span class="nb-metainfo">default: 301</span><br/>
API values: <code>301</code>, <code>302</code>, <code>307</code>, or <code>308</code>.</p>
<p>The HTTP status code returned to the client when redirecting:</p>
<ul>
<li><strong>301 - Permanent Redirect</strong>: The page has permanently moved to a new address. For <code>POST</code> requests, the client or browser might switch the HTTP method to <code>GET</code> when following the redirect.</li>
<li><strong>302 - Temporary Redirect</strong>: The page has temporarily moved to a new address. For <code>POST</code> requests, the client or browser might switch the HTTP method to <code>GET</code> when following the redirect.</li>
<li><strong>307 - Advanced: Temporary, HTTP method preserved</strong>: The page has temporarily moved to a new address. The client or browser must preserve the original HTTP method (for example, <code>POST</code>) when following the redirect.</li>
<li><strong>308 - Advanced: Permanent, HTTP method preserved</strong>: The page has permanently moved to a new address. The client or browser must preserve the original HTTP method (for example, <code>POST</code>) when following the redirect.</li>
</ul>

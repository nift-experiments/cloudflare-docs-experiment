<p>You can check whether or not APO is working by verifying APO headers are present. When APO is working, three headers are present: <code>CF-Cache-Status</code>, <code>cf-apo-via</code>, <code>cf-edge-cache</code>.</p>
<ol>
<li>Visit <a href="https://www.uptrends.com/tools/http-response-header-check">Uptrends.com</a>.</li>
<li>In the text field, enter the URL for your WordPress homepage including the <code>https://www.</code>.</li>
<li>Select <strong>Start test</strong>. The <strong>Response Headers</strong> table displays.</li>
<li>Locate the three header responses and their description. APO is working correctly when the headers exactly match the headers below.</li>
</ol>
<ul>
<li><code>CF-Cache-Status</code> | <code>HIT</code>
<ul>
<li>The <code>cf-cache-status</code> header displays if the asset is served from the cache or was considered dynamic and served from the origin.</li>
</ul>
</li>
<li><code>cf-apo-via</code> | <code>tcache</code>
<ul>
<li>The <code>cf-apo-via</code> header returns the APO status for the given request.</li>
</ul>
</li>
<li><code>cf-edge-cache</code> | <code>cache, platform=wordpress</code>
<ul>
<li>The <code>cf-edge-cache</code> headers confirms the WordPress plugin is installed and enabled.</li>
</ul>
</li>
</ul>
<p>In a terminal, use the following cURL. Include the <code>'accept: text/html'</code> header so the request is treated as a browser-like HTML request. This makes the test result deterministic. APO can also cache requests that omit the header, depending on the URL path. For more information, refer to <a href="/automatic-platform-optimization/troubleshooting/faq/">FAQ on <code>cf-cache-status</code> results</a>.</p>
<pre><code class="language-sh">curl -svo /dev/null -A &quot;CF&quot; &#x27;https://example.com/&#x27; -H &#x27;accept: text/html&#x27; 2&gt;&amp;1 | grep &#x27;cf-cache-status\|cf-edge\|cf-apo-via&#x27;&#10;</code></pre>
<pre><code class="language-sh">&lt; cf-cache-status: HIT&#10;&lt; cf-apo-via: cache&#10;&lt; cf-edge-cache: cache,platform=wordpress&#10;</code></pre>
<p>As always, <code>cf-cache-status</code> displays if the asset hit the cache or was considered dynamic and served from the origin.</p>
<ul>
<li><code>cf-apo-via</code> | <code>tcache</code>
<ul>
<li>The <code>cf-apo-via</code> header returns the APO status for the given request.</li>
</ul>
</li>
<li><code>cf-edge-cache</code> | <code>cache, platform=wordpress</code>
<ul>
<li>The <code>cf-edge-cache</code> headers confirms the WordPress plugin is installed and enabled.</li>
</ul>
</li>
</ul>
<h2 id="verify-the-apo-integration-and-wordpress-integration-work">Verify the APO integration and WordPress integration work</h2>
<p>Open your WordPress site and publish a change. When the integration is working, the page is cached with <code>cf-cache-status: HIT</code> and <code>cf-apo-via: tcache</code>.</p>

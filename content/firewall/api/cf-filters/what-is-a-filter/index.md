<p>A filter is a way of saying:</p>
<pre><code class="language-txt">if (traffic matches certain criteria) then...&#10;</code></pre>
<p>A filter contains an expression that would return <code>true</code> or <code>false</code> when evaluated against traffic passing through Cloudflare.</p>
<p>Filter expressions are human and machine readable, and you can compose complex logic to precisely match the traffic that you are interested in detecting and acting upon.</p>
<p>A filter object typically looks like the following:</p>
<pre><code class="language-json">{&#10;  &quot;id&quot;: &quot;&lt;FILTER_ID&gt;&quot;,&#10;  &quot;expression&quot;: &quot;(http.request.uri.path ~ \&quot;^.*wp-login.php$\&quot; or http.request.uri.path ~ \&quot;^.*xmlrpc.php$\&quot;) and ip.src ne 93.184.216.34&quot;,&#10;  &quot;description&quot;: &quot;WordPress login paths via the login page or mobile RPC endpoint&quot;&#10;}&#10;</code></pre>
<p>The expression specified in this example filter is:</p>
<pre><code class="language-txt">(http.request.uri.path ~ &quot;^.*wp-login.php$&quot; or http.request.uri.path ~ &quot;^.*xmlrpc.php$&quot;) and ip.src ne 93.184.216.34&#10;</code></pre>
<p>This filter expression has a <code>(this or that) and not this</code> structure designed to:</p>
<ul>
<li>Capture two WordPress paths that may be subject to brute force password attacks, and</li>
<li>Exclude traffic that comes from the IP address <code>93.184.216.34</code>.</li>
</ul>
<p>Imagine that this is an IP for your office. This expression demonstrates a filter that might be used (in a firewall rule) to block access to the WordPress login when accessed outside the office network.</p>
<p>For more information on rule expressions, refer to <a href="/ruleset-engine/rules-language/expressions/">Expressions</a> in the Rules language documentation.</p>

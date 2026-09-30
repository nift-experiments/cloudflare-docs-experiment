<p>In some cases, Microsoft Exchange Autodiscover service requests can be &quot;noisy&quot;, triggering large numbers of <code>HTTP 404</code> (<code>Not found</code>) errors.</p>
<p>This example <a href="/waf/custom-rules/create-dashboard/">custom rule</a> blocks requests for <code>autodiscover.xml</code> and <code>autodiscover.src</code>:</p>
<ul>
<li>
<p><strong>When incoming requests match</strong>:</p>
<p>Use the expression editor:<br/>
<code>(ends_with(http.request.uri.path, &quot;/autodiscover.xml&quot;) or ends_with(http.request.uri.path, &quot;/autodiscover.src&quot;))</code></p>
</li>
<li>
<p><strong>Then take action</strong>: <em>Block</em></p>
</li>
</ul>
<p>Alternatively, customers on a Business or Enterprise plan can use the <code>matches</code> <a href="/ruleset-engine/rules-language/operators/#comparison-operators">comparison operator</a> for the same purpose. For this example, the expression would be the following:</p>
<pre><code class="language-txt">(http.request.uri.path matches &quot;/autodiscover.(xml|src)$&quot;)&#10;</code></pre>

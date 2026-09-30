<p>In the Cloudflare dashboard, there are two options for editing <a href="/ruleset-engine/rules-language/expressions/">expressions</a>:</p>
<ul>
<li><a href="/ruleset-engine/rules-language/expressions/edit-expressions/#expression-builder">Expression Builder</a>: Allows you to create expressions using drop-down lists, emphasizing a visual approach to defining an expression.</li>
<li><a href="/ruleset-engine/rules-language/expressions/edit-expressions/#expression-editor">Expression Editor</a>: A text-only interface that supports advanced features, such as grouping symbols and functions for transforming and validating values.</li>
</ul>
<h2 id="use-a-list-in-the-expression-builder">Use a list in the Expression Builder</h2>
<p>To use a list in the Expression Builder:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15710.md")
</div>
<h2 id="use-a-list-in-the-expression-editor">Use a list in the Expression Editor</h2>
<p>To use a list in the Expression Editor, specify the <code>in</code> operator and use <code>$&lt;list_name&gt;</code> to specify the name of the list.</p>
<p>Examples:</p>
<ul>
<li>Expression matching requests from IP addresses that are in an IP list named <code>office_network</code>:</li>
</ul>
<pre><code class="language-txt">ip.src in $office_network&#10;</code></pre>
<ul>
<li>Expression matching requests with a source IP address different from IP addresses in the <code>office_network</code> IP list:</li>
</ul>
<pre><code class="language-txt">not ip.src in $office_network&#10;</code></pre>
<ul>
<li>Expression matching requests from IP addresses in the Cloudflare Open Proxies <a href="/waf/tools/lists/managed-lists/#managed-ip-lists">Managed IP List</a>:</li>
</ul>
<pre><code class="language-txt">ip.src in $cf.open_proxies&#10;</code></pre>

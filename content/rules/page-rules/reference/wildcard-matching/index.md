<p>You can use the asterisk (<code>*</code>) in any URL segment to match certain patterns. For example, <code>example.com/t*st</code> would match:</p>
<ul>
<li><code>example.com/test</code></li>
<li><code>example.com/toast</code></li>
<li><code>example.com/trust</code></li>
</ul>
<p><code>example.com/foo/* </code>does not match <code>example.com/foo</code>, but <code>example.com/foo*</code> does match.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13097.md")
</aside>
<h2 id="helpful-tips">Helpful tips</h2>
<ul>
<li>To match both <code>http</code> and <code>https</code>, write <code>example.com</code>. Writing <code>*example.com</code> is unnecessary.</li>
<li>To match every page on a domain, write <code>example.com/*</code>. Writing <code>example.com</code> will not work.</li>
<li>To match every page on a domain and its subdomains, write <code>*example.com/*</code>. Writing <code>example.com</code> will not work.</li>
<li>A wildcard (<code>*</code>) in a page rule URL will match even if no characters are present and may include any part of the URL, including the query string.</li>
</ul>
<h2 id="reference-wildcard-matches">Reference wildcard matches</h2>
<p>You can reference a matched wildcard later using the <code>$&lt;X&gt;</code> syntax, where <code>&lt;X&gt;</code> indicates the index of a glob pattern. For example, <code>$1</code> represents the first wildcard match and <code>$2</code> represents the second wildcard match.</p>
<p>The <code>$&lt;X&gt;</code> syntax is especially useful with the <em>Forwarding URL</em> setting. For example, you could forward <code>http://*.example.com/*</code> to <code>http://example.com/images/$1/$2.jpg</code>.</p>
<p>This rule would match <code>http://cloud.example.com/flare.jpg</code>, which would be forwarded to <code>http://example.com/images/cloud/flare.jpg</code>.</p>
<p>To add a <code>$</code> character in the forwarding URL, escape it by adding a backslash <code>\</code> in front like <code>\$</code>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13096.md")
</aside>

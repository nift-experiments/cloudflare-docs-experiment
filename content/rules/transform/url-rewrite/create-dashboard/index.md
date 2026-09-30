<p>Refer to the <a href="/rules/transform/examples/?operation=Rewrite+URL">Rules examples gallery</a> for examples of rule definitions.</p>
<p>To create a rule:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13129.md")
</div>
<h2 id="wildcard-pattern-parameters">Wildcard pattern parameters</h2>
<p>The Cloudflare dashboard offers a simplified user interface for creating URL rewrites based on wildcard matching and replacement. When you select <strong>Wildcard pattern</strong>, you will have the following parameters available:</p>
<ul>
<li>
<p><strong>Request URL</strong>: Enter the <a href="/ruleset-engine/rules-language/operators/#wildcard-matching">wildcard pattern</a> using the asterisk (<code>*</code>) character to match multiple requests. For example, <code>http*://*.example.com/*</code>.</p>
</li>
<li>
<p><strong>Then rewrite the path and/or query</strong>: Define the <a href="/rules/transform/url-rewrite/reference/parameters/">URL rewrite settings</a> including:</p>
<ul>
<li><strong>Path</strong> &gt; <strong>Target path</strong>: Enter the URI path to match, which can include wildcards (for example, <code>/oldpath/*</code>).</li>
<li><strong>Path</strong> &gt; <strong>Rewrite to</strong>: Enter the new URI path. You can use <a href="/ruleset-engine/rules-language/functions/#wildcard_replace">wildcard replacement</a> such as <code>${1}</code> and <code>${2}</code> to define a dynamic target path (for example, <code>/newpath/${1}</code>). Leave this field empty to remove the URI path.</li>
<li><strong>Query</strong> &gt; <strong>Target query</strong>: Enter the query string to match, which can include wildcards (for example, <code>?sort=*</code>).</li>
<li><strong>Query</strong> &gt; <strong>Rewrite to</strong>: Enter the new query string. You can use <a href="/ruleset-engine/rules-language/functions/#wildcard_replace">wildcard replacement</a> such as <code>${1}</code> and <code>${2}</code> to define a dynamic query string (for example, <code>?order=${1}</code>). Leave this field empty to remove the query string.</li>
</ul>
</li>
</ul>
<p>Refer to <a href="/rules/transform/url-rewrite/reference/parameters/#wildcard-matching-and-replacement">URL rewrite parameters</a> for the equivalent rule configuration when using the API.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/13127.md")
</aside>

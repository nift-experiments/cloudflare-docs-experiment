<p class="article-summary">Create a URL rewrite rule (part of Transform Rules) to normalize encoded forward slashes (`%2F`) in the request path to standard slashes (`/`).</p>
<p>Different web servers and applications handle encoded forward slashes (<code>%2F</code>) in URLs differently. Cloudflare follows <a href="https://datatracker.ietf.org/doc/html/rfc3986">RFC 3986</a>, which specifies that <code>%2F</code> <strong>should not</strong> be automatically normalized to <code>/</code> because <code>/</code> is a reserved character in URLs, and decoding it might change the intended meaning of the path.</p>
<p>However, many origin servers <strong>do</strong> automatically decode <code>%2F</code> into <code>/</code> when processing requests. If your origin server behaves this way, you may want to apply the same normalization at Cloudflare’s edge to ensure consistency in request handling, rule evaluation, and logging.</p>
<h2 id="how-to-normalize-2f">How to normalize <code>%2F</code></h2>
<p>To normalize encoded forward slashes (<code>%2F</code>) to standard slashes (<code>/</code>) in the request path before <a href="/ruleset-engine/reference/phases-list/">subsequent</a> rule evaluation, create a new URL rewrite rule and define a dynamic URL path rewrite using <a href="/ruleset-engine/rules-language/functions/#url_decode"><code>url_decode()</code></a> function:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13174.md")
</div>
<p>This transformation ensures that <code>%2F</code> is always treated as <code>/</code> in the request path. This is particularly useful when setting up rules that depend on URL path matching, as it prevents discrepancies caused by differing normalization behaviors.</p>

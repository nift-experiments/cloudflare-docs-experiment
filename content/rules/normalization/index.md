<p>Cloudflare provides a URL normalization feature to modify the URLs of incoming requests so that they conform to a consistent formatting standard. This is important because the same resource can be requested using different URL formats (for example, <code>/hello</code> and <code>/%68ello</code> refer to the same path), and without normalization, security rules and other features might not match all variations of a URL.</p>
<p>When you enable URL normalization, all incoming URLs are normalized before they pass to subsequent global network features that accept a URL input, such as WAF custom rules, Workers, and Access. Rule expressions that filter traffic based on URLs will therefore trigger correctly, regardless of the format of the incoming URL. When URL normalization is disabled, Cloudflare forwards the URL to origin in its original form.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/12972.md")
</aside>
<p>URL normalization does not perform any <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/12973.md")
</div>, and therefore it will not change the address displayed in the visitor's browser. The normalization operation, when enabled, occurs on the global network and affects Cloudflare features executed later and (optionally) the URL received at the origin server.
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12971.md")
</aside>
<hr />
<h2 id="availability">Availability</h2>
<p>URL normalization is available in all Cloudflare plans.</p>
<h2 id="get-started">Get started</h2>
<p>Learn more about <a href="/rules/normalization/how-it-works/">URL normalization</a> and how to <a href="/rules/normalization/manage/">configure URL normalization</a> in the Cloudflare dashboard.</p>

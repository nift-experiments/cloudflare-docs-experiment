<p class="article-summary">Create a response header transform rule (part of Transform Rules) to set an `X-Bot-Score` HTTP header in the response to a static value (`Cloudflare`).</p>
<p>The following response header transform rule sets a header named <code>X-Source</code> to a static value (<code>Cloudflare</code>) in the HTTP response:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13162.md")
</div>
<p>This rule would overwrite any existing <code>X-Source</code> headers already present in the HTTP response.</p>

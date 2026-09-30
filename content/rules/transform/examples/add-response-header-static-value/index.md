<p class="article-summary">Create a response header transform rule to add a `set-cookie` HTTP header to the response with a static value (`cookiename=value`).</p>
<p>The following response header transform rule adds a header named <code>set-cookie</code> with a static value (<code>cookiename=value</code>) to the HTTP response:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13175.md")
</div>
<p>This rule would keep any existing <code>set-cookie</code> headers already present in the HTTP response.</p>

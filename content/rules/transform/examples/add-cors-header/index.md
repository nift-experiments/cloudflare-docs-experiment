<p class="article-summary">Create a response header transform rule to add an `Access-Control-Allow-Origin` CORS HTTP header to the response with a static wildcard value.</p>
<p>The following response header transform rule adds a header named <code>Access-Control-Allow-Origin</code> with a static wildcard value (<code>*</code>) to the HTTP response:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13179.md")
</div>
<p>You can also use an expression similar to the following to apply the CORS header to several specific hostnames:</p>
<pre><code class="language-txt">(http.host in {&quot;&lt;YOUR_HOSTNAME_1&gt;&quot; &quot;&lt;YOUR_HOSTNAME_2&gt;&quot;})&#10;</code></pre>

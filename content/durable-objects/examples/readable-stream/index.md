<p class="article-summary">Stream ReadableStream from Durable Objects.</p>
<p>This example demonstrates:</p>
<ul>
<li>A Worker receives a request, and forwards it to a Durable Object <code>my-id</code>.</li>
<li>The Durable Object streams an incrementing number every second, until it receives <code>AbortSignal</code>.</li>
<li>The Worker reads and logs the values from the stream.</li>
<li>The Worker then cancels the stream after 5 values.</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8211.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8210.md")
</aside>

<p class="article-summary">Draw a watermark from KV on an image from R2</p>
<p>Enable <a href="/workers/cache/">Workers Cache</a> so repeat requests for the same watermarked image are served from cache without re-running the Worker or re-transforming the image:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9454.md")
</div>
<p>Then set <code>Cache-Control</code> headers on your response to control the cache lifetime:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/9455.md")
</div>

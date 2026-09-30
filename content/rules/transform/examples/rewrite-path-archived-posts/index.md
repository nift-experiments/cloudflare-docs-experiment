<p class="article-summary">Create a URL rewrite rule (part of Transform Rules) to rewrite any requests for `/news/2012/...` URI paths to `/archive/news/2012/...`.</p>
<p>To rewrite all requests to <code>/news/2012/...</code> to <code>/archive/news/2012/...</code> you must add a reference to the content of the original URL. Create a new URL rewrite rule and define a dynamic URL path rewrite using <a href="/rules/transform/url-rewrite/create-dashboard/#wildcard-pattern-parameters">wildcard pattern parameters</a>:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13169.md")
</div>
<p>Make sure to replace <code>&lt;YOUR_HOSTNAME&gt;</code> with your actual hostname and adjust the example paths according to your setup.</p>

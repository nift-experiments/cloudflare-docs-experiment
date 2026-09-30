<p class="article-summary">Create a transform rule to rewrite the request path from `/blog` to `/blog?sort-by=date`.</p>
<p>To rewrite a request to the <code>/blog</code> path to <code>/blog?sort-by=date</code>, create a URL rewrite rule with the following settings:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13166.md")
</div>
<p>Additionally, set the path rewrite action of the same rule to <em>Preserve</em> so that the URL path does not change.</p>

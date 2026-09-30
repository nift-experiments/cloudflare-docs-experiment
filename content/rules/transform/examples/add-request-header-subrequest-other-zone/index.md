<p class="article-summary">Create a request header transform rule to add an HTTP header when the Workers subrequest comes from a different zone.</p>
<p>The following request header transform rule adds an HTTP header to Workers subrequests coming from a different zone:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13176.md")
</div>
<p>The <a href="/ruleset-engine/rules-language/fields/reference/cf.worker.upstream_zone/"><code>cf.worker.upstream_zone</code></a> field used in the rule expression is set to empty if the current request is not a Workers subrequest.</p>

<p class="article-summary">Create a URL rewrite rule (part of Transform Rules) to remove `/files/` from URI paths before routing request to your object storage bucket.</p>
<p>To remove <code>/files/</code> from URI paths before routing request to your object storage bucket, create a new URL rewrite rule and define a dynamic URL path rewrite using <a href="/rules/transform/url-rewrite/create-dashboard/#wildcard-pattern-parameters">wildcard pattern parameters</a>:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13168.md")
</div>
<p>Make sure to replace <code>&lt;YOUR_HOSTNAME&gt;</code> with your actual hostname and adjust the example paths according to your setup.
Then, use <a href="/rules/cloud-connector/">Cloud Connector</a> to route traffic to an object storage bucket.</p>

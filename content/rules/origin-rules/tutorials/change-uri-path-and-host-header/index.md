<p>This tutorial will instruct you how to modify both the URI path and the <code>Host</code> header of incoming requests using <a href="/rules/transform/">Transform Rules</a> and Origin Rules.</p>
<p>Your website visitors will be routed from <code>https://&lt;YOUR_SOURCE_HOSTNAME&gt;/uploads/*</code> to <code>https://&lt;YOUR_TARGET_HOSTNAME&gt;/*</code>.</p>
<p>In this tutorial you will do the following:</p>
<ol>
<li>Create a URL rewrite to remove <code>/uploads</code> from the path.</li>
<li>Create an origin rule to modify the <code>Host</code> header to desired hostname.</li>
</ol>
<p>By following these steps, you can effectively manage both URI paths and <code>Host</code> headers to route traffic appropriately and optimize request handling.</p>
<h2 id="1-create-a-url-rewrite"><ol>
<li>Create a URL rewrite</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13078.md")
</div>
<h2 id="2-create-an-origin-rule"><ol start="2">
<li>Create an origin rule</li>
</ol></h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13075.md")
</aside>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13082.md")
</div>
<h2 id="final-remarks">Final remarks</h2>
<p>After completing this tutorial, incoming traffic for <code>https://&lt;YOUR_SOURCE_HOSTNAME&gt;/uploads/*</code> will be routed to <code>https://&lt;YOUR_TARGET_HOSTNAME&gt;/*</code>.</p>
<p>Ensure the filters for the <a href="/rules/transform/url-rewrite/">URL rewrite</a> and the <a href="/rules/origin-rules/">origin rule</a> (or <a href="/rules/cloud-connector/">Cloud Connector</a> rule) are precise to avoid unintended rule executions.</p>
<p>Remember that rules are evaluated <a href="/ruleset-engine/reference/phases-list/">in sequence</a>, so Transform Rules (including URL rewrites) run before Origin Rules or Cloud Connector.</p>

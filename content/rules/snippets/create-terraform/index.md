<p>You can create Snippets using the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest">Terraform Cloudflare provider</a>.</p>
<p>To get started with Terraform for Cloudflare configuration, refer to <a href="/terraform/installing/">Get started</a>.</p>
<h2 id="example-configuration">Example configuration</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12787.md")
</aside>
<p>The following example Terraform configuration creates a snippet and an associated snippet rule that defines when the snippet code will run. The snippet code is loaded from the <code>file1.js</code> file in your machine.</p>
<pre><code class="language-tf">resource &quot;cloudflare_snippet&quot; &quot;my_snippet&quot; {&#10;	zone_id  = &quot;&lt;ZONE_ID&gt;&quot;&#10;	name = &quot;my_test_snippet_1&quot;&#10;	main_module = &quot;file1.js&quot;&#10;	files {&#10;		name = &quot;file1.js&quot;&#10;		content = file(&quot;file1.js&quot;)&#10;	}&#10;}&#10;&#10;resource &quot;cloudflare_snippet_rules&quot; &quot;cookie_snippet_rule&quot; {&#10;	zone_id  = &quot;&lt;ZONE_ID&gt;&quot;&#10;	rules {&#10;		enabled = true&#10;		expression = &quot;http.cookie eq \&quot;a=b\&quot;&quot;&#10;		description = &quot;Trigger snippet on specific cookie&quot;&#10;		snippet_name = &quot;my_test_snippet_1&quot;&#10;	}&#10;	depends_on = [cloudflare_snippet.my_snippet]&#10;}&#10;</code></pre>
<p>The name of a snippet can only contain the characters <code>a-z</code>, <code>0-9</code>, and <code>_</code> (underscore). The name must be unique in the context of the zone. You cannot change the snippet name after creating the snippet.</p>
<p>All <code>snippet_name</code> values in the <code>cloudflare_snippet_rules</code> resource must match the names of existing snippets.</p>
<h2 id="more-resources">More resources</h2>
<p>Refer to the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform Cloudflare provider documentation</a> for more information on the <code>cloudflare_snippet</code> and <code>cloudflare_snippet_rules</code> resources.</p>

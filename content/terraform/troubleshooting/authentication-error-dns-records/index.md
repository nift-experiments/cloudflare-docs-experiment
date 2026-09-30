<p>When creating DNS records using Terraform, the API returns the following error:</p>
<p><code>Error: failed to create DNS record: HTTP status 403: Authentication error (10000)</code></p>
<p>This is caused by an error in your code syntax, when you are not using index <code>[0]</code> for the zones. Find an example below and a more detailed thread on <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/913">GitHub</a>.</p>
<p>Instead of this:</p>
<pre><code class="language-txt">zone_id = data.cloudflare_zones.example_com.id&#10;</code></pre>
<p>Use this:</p>
<pre><code class="language-txt">zone_id = data.cloudflare_zones.example_com.zones[0].id`&#10;</code></pre>

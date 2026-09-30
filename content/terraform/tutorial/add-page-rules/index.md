<p>In the <a href="/terraform/tutorial/configure-https-settings/">Configure HTTPS settings</a> tutorial, you configured zone settings that apply to all incoming requests for <code>example.com</code>. In this tutorial, you will add an exception to these settings using <a href="/rules/page-rules/">Page Rules</a>.</p>
<p>Specifically, you will increase the security level for a URL known to be expensive to render and cannot be cached: <code>https://www.example.com/expensive-db-call</code>. Additionally, you will add a redirect from the previous URL used to host this page.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14762.md")
</aside>
<h2 id="1-create-page-rules-configuration"><ol>
<li>Create Page Rules configuration</li>
</ol></h2>
<p>Create a new branch and append the configuration.</p>
<pre><code class="language-bash">git checkout -b step5-pagerule&#10;</code></pre>
<p>Page Rules let you override zone settings for specific URL patterns. Add two Page Rules to your <code>main.tf</code>:</p>
<pre><code class="language-hcl">&#35; Increase security for expensive database operations&#10;resource &quot;cloudflare_page_rule&quot; &quot;expensive_endpoint_security&quot; {&#10;  zone_id  = var.zone_id&#10;  target   = &quot;${var.domain}/expensive-db-call&quot;&#10;  priority = 1&#10;&#10;  actions = {&#10;    security_level = &quot;under_attack&quot;&#10;  }&#10;}&#10;&#10;&#35; Redirect old URLs to new location&#10;resource &quot;cloudflare_page_rule&quot; &quot;legacy_redirect&quot; {&#10;  zone_id  = var.zone_id&#10;  target   = &quot;${var.domain}/old-location.php&quot;&#10;  priority = 2&#10;&#10;  actions = {&#10;    forwarding_url = {&#10;      url         = &quot;https://www.${var.domain}/expensive-db-call&quot;&#10;      status_code = 301&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>The first rule increases security to &quot;Under Attack&quot; mode for your database endpoint. The second rule redirects old URLs with a 301 permanent redirect.</p>
<h2 id="2-preview-and-apply-the-changes"><ol start="2">
<li>Preview and apply the changes:</li>
</ol></h2>
<pre><code class="language-sh">terraform plan&#10;terraform apply&#10;</code></pre>
<h2 id="3-verify-changes"><ol start="3">
<li>Verify changes:</li>
</ol></h2>
<p>Test the redirect functionality:</p>
<pre><code class="language-bash">curl -I https://example.com/old-location.php&#10;</code></pre>
<p>Expected output:</p>
<pre><code class="language-bash">HTTP/1.1 301 Moved Permanently&#10;Location: https://example.com/expensive-db-call&#10;</code></pre>
<p>Test the increased security (Under Attack mode returns a challenge page):</p>
<pre><code class="language-bash">curl -I https://example.com/expensive-db-call&#10;</code></pre>
<p>Expected output:</p>
<pre><code class="language-bash">HTTP/1.1 503 Service Temporarily Unavailable&#10;</code></pre>
<p>The 503 response indicates the Under Attack mode is active, presenting visitors with a challenge page before allowing access to protect against DDoS attacks.</p>
<h2 id="4-commit-and-merge-the-changes"><ol start="4">
<li>Commit and merge the changes:</li>
</ol></h2>
<pre><code class="language-bash">git add main.tf&#10;git commit -m &quot;Step 5 - Add two Page Rules&quot;&#10;git push&#10;</code></pre>
<p>The call works as expected. In the first case, the Cloudflare global network responds with a <code>301</code> redirecting the browser to the new location. In the second case, the Cloudflare global network initially responds with a <code>503</code>, which is consistent with the Under Attack mode.</p>

<p>After setting up basic DNS records, you can configure zone settings using Terraform. This tutorial shows how to enable <a href="/ssl/edge-certificates/additional-options/tls-13/">TLS 1.3</a>, <a href="/ssl/edge-certificates/additional-options/automatic-https-rewrites/">Automatic HTTPS Rewrites</a>, and <a href="/ssl/origin-configuration/ssl-modes/full-strict/">Strict SSL mode</a> using the updated v5 provider.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Completed tutorials <a href="/terraform/tutorial/initialize-terraform/">1</a> and <a href="/terraform/tutorial/track-history/">2</a></li>
<li>Valid SSL certificate on your origin server (use the <a href="/ssl/origin-configuration/origin-ca/">Cloudflare Origin CA</a> to generate one for strict SSL mode)</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14761.md")
</aside>
<h2 id="1-create-zone-setting-configuration"><ol>
<li>Create zone setting configuration</li>
</ol></h2>
<p>Create a new branch and add zone settings:</p>
<pre><code class="language-bash">git checkout -b step3-zone-settings&#10;</code></pre>
<p>Add the following to your <code>main.tf</code> file:</p>
<pre><code class="language-hcl">&#35; Enable TLS 1.3&#10;resource &quot;cloudflare_zone_setting&quot; &quot;tls_1_3&quot; {&#10;  zone_id    = var.zone_id&#10;  setting_id = &quot;tls_1_3&quot;&#10;  value      = &quot;on&quot;&#10;}&#10;&#10;&#35; Enable automatic HTTPS rewrites&#10;resource &quot;cloudflare_zone_setting&quot; &quot;automatic_https_rewrites&quot; {&#10;  zone_id    = var.zone_id&#10;  setting_id = &quot;automatic_https_rewrites&quot;&#10;  value      = &quot;on&quot;&#10;}&#10;&#10;&#35; Set SSL mode to strict&#10;resource &quot;cloudflare_zone_setting&quot; &quot;ssl&quot; {&#10;  zone_id    = var.zone_id&#10;  setting_id = &quot;ssl&quot;&#10;  value      = &quot;strict&quot;&#10;}&#10;</code></pre>
<h2 id="2-preview-and-apply-the-changes"><ol start="2">
<li>Preview and apply the changes</li>
</ol></h2>
<p>Review the proposed changes:</p>
<pre><code class="language-sh">terraform plan&#10;</code></pre>
<p>Expected output</p>
<pre><code class="language-sh">Plan: 3 to add, 0 to change, 0 to destroy.&#10;&#10;Terraform will perform the following actions:&#10;&#10;  &#35; cloudflare_zone_setting.automatic_https_rewrites will be created&#10;  &#43; resource &quot;cloudflare_zone_setting&quot; &quot;automatic_https_rewrites&quot; {&#10;      &#43; setting_id = &quot;automatic_https_rewrites&quot;&#10;      &#43; value      = &quot;on&quot;&#10;      &#43; zone_id    = &quot;your-zone-id&quot;&#10;    }&#10;&#10;  &#35; cloudflare_zone_setting.ssl will be created&#10;  &#43; resource &quot;cloudflare_zone_setting&quot; &quot;ssl&quot; {&#10;      &#43; setting_id = &quot;ssl&quot;&#10;      &#43; value      = &quot;strict&quot;&#10;      &#43; zone_id    = &quot;your-zone-id&quot;&#10;    }&#10;&#10;  &#35; cloudflare_zone_setting.tls_1_3 will be created&#10;  &#43; resource &quot;cloudflare_zone_setting&quot; &quot;tls_1_3&quot; {&#10;      &#43; setting_id = &quot;tls_1_3&quot;&#10;      &#43; value      = &quot;on&quot;&#10;      &#43; zone_id    = &quot;your-zone-id&quot;&#10;    }&#10;</code></pre>
<p>Commit and merge the changes:</p>
<pre><code class="language-bash">git add main.tf&#10;git commit -m &quot;Step 3 - Enable TLS 1.3, automatic HTTPS rewrites, and strict SSL&quot;&#10;git checkout main&#10;git merge step3-zone-settings&#10;git push&#10;</code></pre>
<p>Before applying the changes, try to connect with TLS 1.3. Technically, you should not be able to with default settings. To follow along with this test, you will need to <a href="https://everything.curl.dev/source/build/tls/boringssl#build-boringssl">compile <code>curl</code> against BoringSSL</a>.</p>
<pre><code class="language-sh">curl -v --tlsv1.3 https://www.example.com 2&gt;&amp;1 | grep &quot;SSL connection\|error&quot;&#10;</code></pre>
<p>As shown above, you should receive an error because TLS 1.3 is not yet enabled on your zone. Enable it by running <code>terraform apply</code> and try again.</p>
<p>Apply the configuration:</p>
<pre><code class="language-sh">terraform apply&#10;</code></pre>
<p>Type <code>yes</code> when prompted.</p>
<h2 id="3-verify-the-settings"><ol start="3">
<li>Verify the settings</li>
</ol></h2>
<p>Try the same command as before. The command will now succeed.</p>
<pre><code class="language-sh">curl -v --tlsv1.3 https://www.example.com 2&gt;&amp;1 | grep &quot;SSL connection\|error&quot;&#10;</code></pre>

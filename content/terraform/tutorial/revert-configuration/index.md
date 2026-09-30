<p>Sometimes, you may have to roll back configuration changes. For example, you might want to run performance tests on a new configuration or maybe you mistyped an IP address and brought your entire site down.</p>
<p>To revert your configuration, check out the desired branch and ask Terraform to move your Cloudflare settings back in time. If you accidentally brought your site down, consider establishing a good strategy for peer reviewing pull requests rather than merging directly to <code>master</code> as done in the tutorials for brevity.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14757.md")
</aside>
<h2 id="1-review-your-configuration-history"><ol>
<li>Review your configuration history</li>
</ol></h2>
<p>Before determining how far back to revert, review your Git history:</p>
<pre><code class="language-sh">git log --oneline&#10;</code></pre>
<pre><code class="language-sh">f1a2b3c Step 5 - Add two Page Rules&#10;d4e5f6g Step 4 - Create load balancer (LB) monitor, LB pool, and LB&#10;a7b8c9d Step 3 - Enable TLS 1.3, automatic HTTPS rewrites, and strict SSL&#10;e1f2g3h Step 2 - Initial Terraform v5 configuration&#10;</code></pre>
<p>Another benefit of storing your Cloudflare configuration in Git is that you can see who made the change. You can also see who reviewed and approved the change if you peer-review pull requests.</p>
<pre><code class="language-sh">git log&#10;</code></pre>
<p>Check when the last change was made:</p>
<pre><code class="language-sh">git show&#10;</code></pre>
<p>This shows the most recent commit and what files changed.</p>
<h2 id="2-scenario-revert-the-page-rules"><ol start="2">
<li>Scenario: Revert the Page Rules</li>
</ol></h2>
<p>Assume that shortly after you deployed the Page Rules when following the <a href="/terraform/tutorial/add-page-rules/">Add exceptions with Page Rules</a> tutorial, you are told the URL is no longer needed, and the security setting and redirect should be dropped.</p>
<p>While you can always edit the config file directly and delete those entries, you can use Git to do that for you.</p>
<h3 id="revert-using-git">Revert using Git</h3>
<p>Use Git to create a revert commit that undoes the Page Rules changes:</p>
<pre><code class="language-sh">git revert HEAD&#10;</code></pre>
<p>Git will open your default editor with a commit message. Save and close to accept the default message, or customize it:</p>
<pre><code class="language-sh">Revert &quot;Add Page Rules for security and redirects&quot;&#10;&#10;This reverts commit f1a2b3c4d5e6f7a8b9c0d1e2f3g4h5i6j7k8l9m0.&#10;</code></pre>
<h2 id="3-preview-the-changes"><ol start="3">
<li>Preview the changes</li>
</ol></h2>
<p>Check what Terraform will do with the reverted configuration:</p>
<pre><code class="language-sh">terraform plan&#10;</code></pre>
<p>Expected output:</p>
<pre><code class="language-sh">Plan: 0 to add, 0 to change, 2 to destroy.&#10;&#10;Terraform will perform the following actions:&#10;&#10;  &#35; cloudflare_page_rule.expensive_endpoint_security will be destroyed&#10;  &#35; cloudflare_page_rule.legacy_redirect will be destroyed&#10;</code></pre>
<p>As expected, Terraform will remove the two Page Rules that were added in tutorial 5.</p>
<h2 id="4-apply-the-changes"><ol start="4">
<li>Apply the changes</li>
</ol></h2>
<p>Apply the changes to remove the Page Rules from your Cloudflare zone:</p>
<pre><code class="language-sh">terraform apply --auto-approve&#10;</code></pre>
<pre><code class="language-sh">cloudflare_page_rule.expensive_endpoint_security: Destroying...&#10;cloudflare_page_rule.legacy_redirect: Destroying...&#10;cloudflare_page_rule.expensive_endpoint_security: Destruction complete after 1s&#10;cloudflare_page_rule.legacy_redirect: Destruction complete after 1s&#10;&#10;Apply complete! Resources: 0 added, 0 changed, 2 destroyed.&#10;</code></pre>
<p>Two resources were destroyed, as expected, and you have rolled back to the previous version.</p>
<h2 id="5-verify-the-revert"><ol start="5">
<li>Verify the revert</li>
</ol></h2>
<p>Test that the Page Rules are no longer active:</p>
<pre><code class="language-bash">&#35; This should now return 404 (no redirect)&#10;curl -I https://www.example.com/old-location.php&#10;&#10;&#35; This should return normal response (no Under Attack mode)&#10;curl -I https://www.example.com/expensive-db-call&#10;</code></pre>
<p>Your configuration has been successfully reverted. The Page Rules are removed, and your zone settings are back to the previous state. Git's version control ensures you can always recover or revert changes safely.</p>

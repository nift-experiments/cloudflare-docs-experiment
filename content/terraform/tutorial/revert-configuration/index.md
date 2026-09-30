---
cp9:
  canonical: https://developers.cloudflare.com/terraform/tutorial/revert-configuration/
  description: Sometimes, you may have to roll back configuration changes. To revert your configuration, check out the desired branch and ask Terraform to move your Cloudflare settings back in time.
  full_title: Revert configuration · Cloudflare Terraform docs
  head_html: <title>Revert configuration · Cloudflare Terraform docs</title><meta name="generator" content="Nift"><meta name="description" content="Sometimes, you may have to roll back configuration changes. To revert your configuration, check out the desired branch and ask Terraform to move your Cloudflare settings back in time."><link rel="canonical" href="https://developers.cloudflare.com/terraform/tutorial/revert-configuration/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/terraform/tutorial/revert-configuration/index.md"><meta property="og:title" content="Revert configuration · Cloudflare Terraform docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Sometimes, you may have to roll back configuration changes. To revert your configuration, check out the desired branch and ask Terraform to move your Cloudflare settings back in time."><meta property="og:url" content="https://developers.cloudflare.com/terraform/tutorial/revert-configuration/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Terraform"><meta name="algolia_product_filter" content="Terraform"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Terraform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/terraform/tutorial/revert-configuration/#page","headline":"Revert configuration \u00b7 Cloudflare Terraform docs","description":"Sometimes, you may have to roll back configuration changes. To revert your configuration, check out the desired branch and ask Terraform to move your Cloudflare settings back in time.","url":"https://developers.cloudflare.com/terraform/tutorial/revert-configuration/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /terraform/tutorial/revert-configuration/
  schema: 1
---
<p>Sometimes, you may have to roll back configuration changes. For example, you might want to run performance tests on a new configuration or maybe you mistyped an IP address and brought your entire site down.</p>
<p>To revert your configuration, check out the desired branch and ask Terraform to move your Cloudflare settings back in time. If you accidentally brought your site down, consider establishing a good strategy for peer reviewing pull requests rather than merging directly to <code>master</code> as done in the tutorials for brevity.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14757.md")
</aside>
<h2 id="1-review-your-configuration-history"><ol>
<li>Review your configuration history</li>
</ol></h2>
<p>Before determining how far back to revert, review your Git history:</p>
<pre tabindex="0"><code class="language-sh">git log --oneline&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">f1a2b3c Step 5 - Add two Page Rules&#10;d4e5f6g Step 4 - Create load balancer (LB) monitor, LB pool, and LB&#10;a7b8c9d Step 3 - Enable TLS 1.3, automatic HTTPS rewrites, and strict SSL&#10;e1f2g3h Step 2 - Initial Terraform v5 configuration&#10;</code></pre>
<p>Another benefit of storing your Cloudflare configuration in Git is that you can see who made the change. You can also see who reviewed and approved the change if you peer-review pull requests.</p>
<pre tabindex="0"><code class="language-sh">git log&#10;</code></pre>
<p>Check when the last change was made:</p>
<pre tabindex="0"><code class="language-sh">git show&#10;</code></pre>
<p>This shows the most recent commit and what files changed.</p>
<h2 id="2-scenario-revert-the-page-rules"><ol start="2">
<li>Scenario: Revert the Page Rules</li>
</ol></h2>
<p>Assume that shortly after you deployed the Page Rules when following the <a href="/terraform/tutorial/add-page-rules/">Add exceptions with Page Rules</a> tutorial, you are told the URL is no longer needed, and the security setting and redirect should be dropped.</p>
<p>While you can always edit the config file directly and delete those entries, you can use Git to do that for you.</p>
<h3 id="revert-using-git">Revert using Git</h3>
<p>Use Git to create a revert commit that undoes the Page Rules changes:</p>
<pre tabindex="0"><code class="language-sh">git revert HEAD&#10;</code></pre>
<p>Git will open your default editor with a commit message. Save and close to accept the default message, or customize it:</p>
<pre tabindex="0"><code class="language-sh">Revert &quot;Add Page Rules for security and redirects&quot;&#10;&#10;This reverts commit f1a2b3c4d5e6f7a8b9c0d1e2f3g4h5i6j7k8l9m0.&#10;</code></pre>
<h2 id="3-preview-the-changes"><ol start="3">
<li>Preview the changes</li>
</ol></h2>
<p>Check what Terraform will do with the reverted configuration:</p>
<pre tabindex="0"><code class="language-sh">terraform plan&#10;</code></pre>
<p>Expected output:</p>
<pre tabindex="0"><code class="language-sh">Plan: 0 to add, 0 to change, 2 to destroy.&#10;&#10;Terraform will perform the following actions:&#10;&#10;  &#35; cloudflare_page_rule.expensive_endpoint_security will be destroyed&#10;  &#35; cloudflare_page_rule.legacy_redirect will be destroyed&#10;</code></pre>
<p>As expected, Terraform will remove the two Page Rules that were added in tutorial 5.</p>
<h2 id="4-apply-the-changes"><ol start="4">
<li>Apply the changes</li>
</ol></h2>
<p>Apply the changes to remove the Page Rules from your Cloudflare zone:</p>
<pre tabindex="0"><code class="language-sh">terraform apply --auto-approve&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">cloudflare_page_rule.expensive_endpoint_security: Destroying...&#10;cloudflare_page_rule.legacy_redirect: Destroying...&#10;cloudflare_page_rule.expensive_endpoint_security: Destruction complete after 1s&#10;cloudflare_page_rule.legacy_redirect: Destruction complete after 1s&#10;&#10;Apply complete! Resources: 0 added, 0 changed, 2 destroyed.&#10;</code></pre>
<p>Two resources were destroyed, as expected, and you have rolled back to the previous version.</p>
<h2 id="5-verify-the-revert"><ol start="5">
<li>Verify the revert</li>
</ol></h2>
<p>Test that the Page Rules are no longer active:</p>
<pre tabindex="0"><code class="language-bash">&#35; This should now return 404 (no redirect)&#10;curl -I https://www.example.com/old-location.php&#10;&#10;&#35; This should return normal response (no Under Attack mode)&#10;curl -I https://www.example.com/expensive-db-call&#10;</code></pre>
<p>Your configuration has been successfully reverted. The Page Rules are removed, and your zone settings are back to the previous state. Git's version control ensures you can always recover or revert changes safely.</p>

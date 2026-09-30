<p>In the <a href="/terraform/tutorial/initialize-terraform/">Initialize Terraform</a> tutorial, you created and applied basic Cloudflare configuration. Now you'll store this configuration in version control for tracking, peer review, and rollback capabilities.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14756.md")
</aside>
<h2 id="1-use-environment-variables-for-authentication"><ol>
<li>Use environment variables for authentication</li>
</ol></h2>
<p>Remove credentials from your Terraform files before committing to version control. The Cloudflare provider v5 reads authentication from environment variables automatically.
Update your <code>main.tf</code> file to remove the hardcoded API token:</p>
<pre><code class="language-hcl">terraform {&#10;  required_providers {&#10;    cloudflare = {&#10;      source  = &quot;cloudflare/cloudflare&quot;&#10;      version = &quot;~&gt; 5&quot;&#10;    }&#10;  }&#10;}&#10;&#10;provider &quot;cloudflare&quot; {&#10;  &#35; API token will be read from CLOUDFLARE_API_TOKEN environment variable&#10;}&#10;&#10;variable &quot;zone_id&quot; {&#10;  description = &quot;Cloudflare Zone ID&quot;&#10;  type        = string&#10;  sensitive   = true&#10;}&#10;&#10;variable &quot;account_id&quot; {&#10;  description = &quot;Cloudflare Account ID&quot;&#10;  type        = string&#10;  sensitive   = true&#10;}&#10;&#10;variable &quot;domain&quot; {&#10;  description = &quot;Domain name&quot;&#10;  type        = string&#10;  default     = &quot;example.com&quot;&#10;}&#10;&#10;resource &quot;cloudflare_dns_record&quot; &quot;www&quot; {&#10;  zone_id = var.zone_id&#10;  name    = &quot;www&quot;&#10;  content = &quot;203.0.113.10&quot;&#10;  type    = &quot;A&quot;&#10;  ttl     = 1&#10;  proxied = true&#10;  comment = &quot;Domain verification record&quot;&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14755.md")
</aside>
<p>Update your <code>terraform.tfvars</code> file:</p>
<pre><code class="language-hcl">zone_id    = &quot;your-zone-id-here&quot;&#10;account_id = &quot;your-account-id-here&quot;&#10;domain     = &quot;your-domain.com&quot;&#10;</code></pre>
<p>Ensure your API token is set as an environment variable:</p>
<pre><code class="language-sh">export CLOUDFLARE_API_TOKEN=&quot;your-api-token-here&quot;&#10;</code></pre>
<p>Verify authentication works:</p>
<pre><code class="language-sh">terraform plan&#10;</code></pre>
<p>You may see changes detected as Terraform compares your new variable-based configuration with the existing resources. This is normal when migrating from hardcoded values to variables:</p>
<pre><code class="language-sh">&#35; cloudflare_dns_record.www will be updated in-place&#10;~ resource &quot;cloudflare_dns_record&quot; &quot;www&quot; {&#10;    ~ name     = &quot;www.your-domain.com&quot; -&gt; &quot;www&quot;&#10;    ~ zone_id  = (sensitive value)&#10;    &#35; (other attributes may show changes)&#10;}&#10;&#10;Plan: 0 to add, 1 to change, 0 to destroy.&#10;</code></pre>
<h2 id="2-store-configuration-in-github"><ol start="2">
<li>Store configuration in GitHub</li>
</ol></h2>
<p>Create a <code>.gitignore</code> file with these contents:</p>
<pre><code class="language-text">.terraform/&#10;&#42;.tfstate*&#10;.terraform.lock.hcl&#10;terraform.tfvars&#10;</code></pre>
<p>Initialize Git and commit your configuration:</p>
<pre><code class="language-sh">git init&#10;git add main.tf .gitignore&#10;git commit -m &quot;Step 2 - Initial Terraform v5 configuration&quot;&#10;</code></pre>
<p>Create a GitHub repository (via web interface or GitHub CLI) and push:</p>
<pre><code class="language-sh">git branch -M main&#10;git remote add origin https://github.com/YOUR_USERNAME/cf-config.git&#10;git push -u origin main&#10;</code></pre>
<p>Your Terraform configuration is now version controlled and ready for team collaboration. The sensitive data (API tokens, zone IDs) remains secure and separate from your code.</p>

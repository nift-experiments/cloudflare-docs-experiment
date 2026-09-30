<p>Manage Turnstile widgets as code using Terraform for version control and automated deployments.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you begin, you must have:</p>
<ul>
<li><a href="https://terraform.io/">Terraform</a> installed</li>
<li>A Cloudflare API token with <code>Account:Turnstile:Edit permissions</code></li>
<li>(Optional) A <code>cf-terraforming</code> tool for importing existing widgets</li>
</ul>
<h2 id="setup">Setup</h2>
<h3 id="1-configure-provider"><ol>
<li>Configure provider</li>
</ol></h3>
<p>Create a <code>main.tf</code> file.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15042.md")
</aside>
<pre><code class="language-tf">terraform {&#10;  required_providers {&#10;    cloudflare = {&#10;      source  = &quot;cloudflare/cloudflare&quot;&#10;      version = &quot;~&gt; 4.0&quot;&#10;    }&#10;  }&#10;}&#10;&#10;provider &quot;cloudflare&quot; {&#10;  api_token = var.cloudflare_api_token&#10;}&#10;&#10;variable &quot;cloudflare_api_token&quot; {&#10;  description = &quot;Cloudflare API Token&quot;&#10;  type        = string&#10;  sensitive   = true&#10;}&#10;&#10;variable &quot;account_id&quot; {&#10;  description = &quot;Cloudflare Account ID&quot;&#10;  type        = string&#10;}&#10;</code></pre>
<h3 id="2-define-widgets"><ol start="2">
<li>Define widgets</li>
</ol></h3>
<pre><code class="language-tf">resource &quot;cloudflare_turnstile_widget&quot; &quot;login_form&quot; {&#10;  account_id = var.account_id&#10;  name       = &quot;Login Form Widget&quot;&#10;  domains    = [&quot;example.com&quot;, &quot;www.example.com&quot;]&#10;  mode       = &quot;managed&quot;&#10;  region     = &quot;world&quot;&#10;}&#10;&#10;resource &quot;cloudflare_turnstile_widget&quot; &quot;api_protection&quot; {&#10;  account_id = var.account_id&#10;  name       = &quot;API Protection&quot;&#10;  domains    = [&quot;api.example.com&quot;]&#10;  mode       = &quot;invisible&quot;&#10;  region     = &quot;world&quot;&#10;}&#10;&#10;&#35; Output the sitekeys for use in your application&#10;output &quot;login_sitekey&quot; {&#10;  value = cloudflare_turnstile_widget.login_form.sitekey&#10;}&#10;&#10;output &quot;api_sitekey&quot; {&#10;  value = cloudflare_turnstile_widget.api_protection.sitekey&#10;}&#10;</code></pre>
<h3 id="3-environment-variables"><ol start="3">
<li>Environment variables</li>
</ol></h3>
<p>Create a <code>.env</code> file or set environment variables.</p>
<pre><code class="language-shell">export TF_VAR_cloudflare_api_token=&quot;your-api-token&quot;&#10;export TF_VAR_account_id=&quot;your-account-id&quot;&#10;</code></pre>
<hr />
<h2 id="terraform-commands">Terraform commands</h2>
<h3 id="initialize-and-plan">Initialize and plan</h3>
<pre><code class="language-shell">terraform init&#10;</code></pre>
<pre><code class="language-shell">terraform plan&#10;</code></pre>
<pre><code class="language-shell">terraform apply&#10;</code></pre>
<h3 id="manage-changes">Manage changes</h3>
<pre><code class="language-shell">terraform plan&#10;</code></pre>
<pre><code class="language-shell">terraform apply&#10;</code></pre>
<pre><code class="language-shell">terraform destroy&#10;</code></pre>
<hr />
<h2 id="advanced-terraform-configuration">Advanced Terraform configuration</h2>
<h3 id="multiple-environments">Multiple environments</h3>
<pre><code class="language-tf">locals {&#10;  environments = {&#10;    dev = {&#10;      domains = [&quot;dev.example.com&quot;]&#10;      mode    = &quot;managed&quot;&#10;    }&#10;    staging = {&#10;      domains = [&quot;staging.example.com&quot;]&#10;      mode    = &quot;non_interactive&quot;&#10;    }&#10;    prod = {&#10;      domains = [&quot;example.com&quot;, &quot;www.example.com&quot;]&#10;      mode    = &quot;invisible&quot;&#10;    }&#10;  }&#10;}&#10;&#10;resource &quot;cloudflare_turnstile_widget&quot; &quot;app_widget&quot; {&#10;  for_each = local.environments&#10;  &#10;  account_id = var.account_id&#10;  name       = &quot;App Widget - ${each.key}&quot;&#10;  domains    = each.value.domains&#10;  mode       = each.value.mode&#10;  region     = &quot;world&quot;&#10;}&#10;</code></pre>
<h3 id="widget-with-enterprise-features">Widget with Enterprise features</h3>
<pre><code class="language-tf">resource &quot;cloudflare_turnstile_widget&quot; &quot;enterprise_widget&quot; {&#10;  account_id     = var.account_id&#10;  name          = &quot;Enterprise Form&quot;&#10;  domains       = [&quot;enterprise.example.com&quot;]&#10;  mode          = &quot;managed&quot;&#10;  region        = &quot;world&quot;&#10;  offlabel      = true  # Remove Cloudflare branding&#10;  bot_fight_mode = true # Enable bot fight mode&#10;}&#10;</code></pre>
<hr />
<h2 id="import-existing-widgets">Import existing widgets</h2>
<p>Use <a href="/terraform/advanced-topics/import-cloudflare-resources/#cf-terraforming"><code>cf-terraforming</code></a> to import existing widgets.</p>
<pre><code class="language-shell">go install github.com/cloudflare/cf-terraforming/cmd/cf-terraforming@latest&#10;</code></pre>
<pre><code class="language-shell">cf-terraforming generate \&#10;  &#45;-resource-type cloudflare_turnstile_widget \&#10;  &#45;-account $ACCOUNT_ID&#10;</code></pre>
<pre><code class="language-shell">terraform import cloudflare_turnstile_widget.existing_widget \&#10;  $ACCOUNT_ID/$WIDGET_SITEKEY&#10;</code></pre>

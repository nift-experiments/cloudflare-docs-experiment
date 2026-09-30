<p>To start using Zero Trust features, create a Zero Trust organization in your Cloudflare account.</p>
<h2 id="sign-up-for-zero-trust">Sign up for Zero Trust</h2>
<p>To create a Zero Trust organization:</p>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, select <strong>Zero Trust</strong>.</p>
</li>
<li>
<p>On the onboarding screen, choose a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
</li>
</ol>
@markup("md", "content/.markup/bodies/10041.md")
</div>. The team name is a unique, internal identifier for your Zero Trust organization. Users will enter this team name when they enroll their device manually, and it will be the subdomain for your App Launcher (as relevant). Your business name is the typical entry.
<p>You can find your team name in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> by going to <strong>Zero Trust</strong> &gt; <strong>Settings</strong>.</p>
<ol start="3">
<li>Complete your onboarding by selecting a subscription plan and entering your payment details. If you chose the <strong>Zero Trust Free plan</strong>, this step is still needed but you will not be charged.</li>
</ol>
<p>When you create your organization, Cloudflare automatically adds the <a href="/cloudflare-one/integrations/identity-providers/cloudflare/">Cloudflare identity provider</a> as your default login method, so your users can sign in with their Cloudflare account credentials right away. You can add a <a href="/cloudflare-one/integrations/identity-providers/one-time-pin/">one-time PIN</a> or connect a <a href="/cloudflare-one/integrations/identity-providers/">third-party identity provider</a> at any time.</p>
<h2 id="optional-manage-zero-trust-in-terraform">(Optional) Manage Zero Trust in Terraform</h2>
<p>You can use the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest">Cloudflare Terraform provider</a> to manage your Zero Trust organization alongside your other IT infrastructure. To get started with Terraform, refer to our <a href="/terraform/tutorial/">Terraform tutorial series</a>.</p>
<p>To add Zero Trust to your Terraform configuration:</p>
<ol>
<li>
<p><a href="#sign-up-for-zero-trust">Sign up for Zero Trust</a> on the Cloudflare dashboard.</p>
</li>
<li>
<p>Add the following permission to your <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/api_token"><code>cloudflare_api_token</code></a>:</p>
<ul>
<li><code>Access: Organizations, Identity Providers, and Groups Write</code></li>
</ul>
</li>
<li>
<p>Add the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zero_trust_organization"><code>cloudflare_zero_trust_organization</code></a> resource:</p>
</li>
</ol>
<pre><code class="language-terraform">resource &quot;cloudflare_zero_trust_organization&quot; &quot;&lt;your-team-name&gt;&quot; {&#10;	account_id                         = var.cloudflare_account_id&#10;	name                               = &quot;Acme Corporation&quot;&#10;	auth_domain                        = &quot;&lt;your-team-name&gt;.cloudflareaccess.com&quot;&#10;}&#10;</code></pre>
<p>Replace <code>&lt;your-team-name&gt;</code> with the Zero Trust organization name selected during <a href="#sign-up-for-zero-trust">onboarding</a>. You can also view your team name in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> under <strong>Zero Trust</strong> &gt; <strong>Settings</strong> &gt; <strong>Team name and domain</strong>.</p>
<p>You can now update Zero Trust organization settings using Terraform.</p>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/10040.md")
</aside>

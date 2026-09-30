<p>This guide covers how to use the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Cloudflare Terraform provider</a> to quickly publish and secure a private application. In the following example, we will add a new published application to an existing Cloudflare Tunnel, configure how <code>cloudflared</code> proxies traffic to the application, and secure the application with Cloudflare Access.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li><a href="/learning-paths/clientless-access/initial-setup/add-site/">Add your domain to Cloudflare</a></li>
<li><a href="/learning-paths/clientless-access/initial-setup/configure-idp/">Configure an IdP integration</a></li>
<li><a href="/learning-paths/clientless-access/connect-private-applications/create-tunnel/#create-a-tunnel">Create a Cloudflare Tunnel</a> via the Zero Trust dashboard</li>
<li>Install the <a href="https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli">Terraform client</a></li>
<li><a href="/fundamentals/api/get-started/create-token/">Create an API token</a> (refer to the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/terraform/#3-create-a-cloudflare-api-token">minimum required permissions</a>)</li>
</ul>
<h2 id="1-create-a-terraform-configuration-directory"><ol>
<li>Create a Terraform configuration directory</li>
</ol></h2>
<p>Terraform functions through a working directory that contains configuration files. You can store your configuration in multiple files or just one — Terraform will evaluate all of the configuration files in the directory as if they were in a single document.</p>
<ol>
<li>Create a folder for your Terraform configuration:</li>
</ol>
<pre><code class="language-sh">mkdir cloudflare-tf&#10;</code></pre>
<ol start="2">
<li>Change into the directory:</li>
</ol>
<pre><code class="language-sh">cd cloudflare-tf&#10;</code></pre>
<h2 id="2-declare-providers-and-variables"><ol start="2">
<li>Declare providers and variables</li>
</ol></h2>
<p>Create a <code>.tf</code> file and copy-paste the following example. Fill in your API token, account and zone information, and Tunnel ID.</p>
<details class="nb-details"><summary>Find the Tunnel ID</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9664.md")
</div></details>
<pre><code class="language-txt">terraform {&#10;  required_providers {&#10;    cloudflare = {&#10;      source = &quot;cloudflare/cloudflare&quot;&#10;      version = &quot;~&gt; 4.0&quot;&#10;    }&#10;  }&#10;}&#10;&#10;provider &quot;cloudflare&quot; {&#10;  api_token = &quot;&lt;API-TOKEN&gt;&quot;&#10;}&#10;&#10;variable &quot;account_id&quot; {&#10;  default = &quot;&lt;ACCOUNT-ID&gt;&quot;&#10;}&#10;&#10;variable &quot;zone_id&quot; {&#10;  default = &quot;&lt;ZONE-ID&gt;&quot;&#10;}&#10;&#10;variable &quot;zone_name&quot; {&#10;  default = &quot;mycompany.com&quot;&#10;}&#10;&#10;variable &quot;tunnel_id&quot; {&#10;  default = &quot;&lt;TUNNEL-ID&gt;&quot;&#10;}&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/9663.md")
</aside>
<h2 id="3-configure-cloudflare-resources"><ol start="3">
<li>Configure Cloudflare resources</li>
</ol></h2>
<p>Add the following resources to your Terraform configuration.</p>
<h3 id="add-published-application-to-cloudflare-tunnel">Add published application to Cloudflare Tunnel</h3>
<p>Using the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/tunnel_config"><code>cloudflare_tunnel_config</code></a> resource, create an ingress rule that maps your application to a public DNS record. This example makes <code>localhost:8080</code> available on <code>app.mycompany.com</code>, sets the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/origin-parameters/#connecttimeout">Connect Timeout</a>, and enables <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/origin-parameters/#access">Access JWT validation</a>.</p>
<pre><code class="language-txt">resource &quot;cloudflare_tunnel_config&quot; &quot;example_config&quot; {&#10;  account_id = var.cloudflare_account_id&#10;  tunnel_id  = var.tunnel_id&#10;&#10;  config {&#10;    ingress_rule {&#10;      hostname = &quot;app.${var.zone_name}&quot;&#10;      service  = &quot;http://localhost:8080&quot;&#10;      origin_request {&#10;        connect_timeout = &quot;2m0s&quot;&#10;        access {&#10;          required  = true&#10;          team_name = &quot;myteam&quot;&#10;          aud_tag   = [cloudflare_access_application.example_app.aud]&#10;        }&#10;      }&#10;    }&#10;    ingress_rule {&#10;      &#35; Respond with a `404` status code when the request does not match any of the previous hostnames.&#10;      service  = &quot;http_status:404&quot;&#10;    }&#10;  }&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9662.md")
</aside>
<h3 id="create-an-access-application">Create an Access application</h3>
<p>Using the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_application"><code>cloudflare_access_application</code></a> resource, add the application to Cloudflare Access.</p>
<pre><code class="language-txt">resource &quot;cloudflare_access_application&quot; &quot;example_app&quot; {&#10;  zone_id                   = var.zone_id&#10;  name                      = &quot;Example application&quot;&#10;  domain                    = &quot;app.${var.zone_name}&quot;&#10;  type                      = &quot;self_hosted&quot;&#10;  session_duration          = &quot;24h&quot;&#10;  auto_redirect_to_identity = false&#10;}&#10;</code></pre>
<h3 id="create-an-access-policy">Create an Access policy</h3>
<p>Using the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_application"><code>cloudflare_access_policy</code></a> resource, create a policy to secure the application. The following policy will only allow access to users who authenticate through your identity provider.</p>
<pre><code class="language-txt">resource &quot;cloudflare_access_policy&quot; &quot;example_policy&quot; {&#10;  application_id    = cloudflare_access_application.example_app.id&#10;  zone_id           = var.zone_id&#10;  name              = &quot;Example policy&quot;&#10;  precedence        = &quot;1&quot;&#10;  decision          = &quot;allow&quot;&#10;&#10;  include {&#10;    login_method = [&quot;&lt;IDP-UUID&gt;&quot;]&#10;  }&#10;&#10;}&#10;</code></pre>
<h2 id="4-deploy-terraform"><ol start="4">
<li>Deploy Terraform</li>
</ol></h2>
<p>To deploy the configuration files:</p>
<ol>
<li>Initialize your configuration directory:</li>
</ol>
<pre><code class="language-sh">terraform init&#10;</code></pre>
<ol start="2">
<li>Preview everything that will be created:</li>
</ol>
<pre><code class="language-sh">terraform plan&#10;</code></pre>
<ol start="3">
<li>Apply the configuration:</li>
</ol>
<pre><code class="language-sh">terraform apply&#10;</code></pre>
<p>Users can now access the private application by going to the public URL and authenticating with Cloudflare Access.</p>
<p>You can view your new tunnel in the Cloudflare dashboard under <strong>Networking</strong> &gt; <strong>Tunnels</strong>.</p>
<div class="nb-dash-button"></div>
<p>Your Access application and policy are under <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong><a href="https://dash.cloudflare.com/?to=/:account/one/access/apps">Applications</a></strong>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9661.md")
</aside>

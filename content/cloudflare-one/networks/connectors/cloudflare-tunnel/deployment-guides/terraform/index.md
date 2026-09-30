---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/terraform/
  description: Learn how to deploy a Cloudflare Tunnel using Terraform and our lightweight server-side daemon, cloudflared.
  full_title: Deploy Tunnels with Terraform · Cloudflare One docs
  head_html: <title>Deploy Tunnels with Terraform · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to deploy a Cloudflare Tunnel using Terraform and our lightweight server-side daemon, cloudflared."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/terraform/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/terraform/index.md"><meta property="og:title" content="Deploy Tunnels with Terraform · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to deploy a Cloudflare Tunnel using Terraform and our lightweight server-side daemon, cloudflared."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/terraform/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="GCP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/terraform/#page","headline":"Deploy Tunnels with Terraform \u00b7 Cloudflare One docs","description":"Learn how to deploy a Cloudflare Tunnel using Terraform and our lightweight server-side daemon, cloudflared.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/terraform/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["GCP"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/terraform/
  schema: 1
---
<p><a href="https://www.terraform.io/">Terraform</a> is an infrastructure as code software tool that allows you to deploy services from different providers using a standardized configuration syntax. When creating a Terraform configuration file, you define the final state of the configuration rather than the step-by-step procedure. This allows you to easily deploy, modify, and manage your Tunnels alongside your other infrastructure.</p>
<p>In this guide, you will use Terraform to deploy:</p>
<ul>
<li>A Google Cloud Project (GCP) virtual machine that runs an HTTP test server</li>
<li>A Cloudflare Tunnel that makes the server available over the Internet</li>
<li>A Cloudflare Access policy that defines who can connect to the server</li>
</ul>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/5320.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<p>To complete the following procedure, you will need:</p>
<ul>
<li><a href="https://cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project">A Google Cloud Project</a></li>
<li><a href="/fundamentals/manage-domains/add-site/">A zone on Cloudflare</a></li>
<li>Enabled <a href="/cloudflare-one/integrations/identity-providers/one-time-pin/">one-time PIN login</a> or integrated an <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a></li>
</ul>
<h2 id="1-install-terraform"><ol>
<li>Install Terraform</li>
</ol></h2>
<p>Refer to the <a href="https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli">Terraform installation guide</a> for your operating system.</p>
<h2 id="2-install-the-gcloud-cli"><ol start="2">
<li>Install the gcloud CLI</li>
</ol></h2>
<ol>
<li>
<p><a href="https://cloud.google.com/sdk/docs/install">Install the gcloud CLI</a> so that Terraform can interact with your GCP account.</p>
</li>
<li>
<p>Authenticate with the CLI by running:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-sh">gcloud auth application-default login&#10;</code></pre>
<h2 id="3-create-a-cloudflare-api-token"><ol start="3">
<li>Create a Cloudflare API token</li>
</ol></h2>
<p><a href="/fundamentals/api/get-started/create-token/">Create an API token</a> so that Terraform can interact with your Cloudflare account. At minimum, your token should include the following permissions:</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Item</th>
<th>Permission</th>
</tr>
</thead>
<tbody>
<tr>
<td>Account</td>
<td>Cloudflare Tunnel</td>
<td>Edit</td>
</tr>
<tr>
<td>Account</td>
<td>Access: Apps and Policies</td>
<td>Edit</td>
</tr>
<tr>
<td>Zone</td>
<td>DNS</td>
<td>Edit</td>
</tr>
</tbody>
</table>
<h2 id="4-create-a-configuration-directory"><ol start="4">
<li>Create a configuration directory</li>
</ol></h2>
<p>Terraform functions through a working directory that contains configuration files. You can store your configuration in multiple files or just one — Terraform will evaluate all of the configuration files in the directory as if they were in a single document.</p>
<ol>
<li>Create a folder for your Terraform configuration:</li>
</ol>
<pre tabindex="0"><code class="language-sh">mkdir cloudflare-tf&#10;</code></pre>
<ol start="2">
<li>Change into the directory:</li>
</ol>
<pre tabindex="0"><code class="language-sh">cd cloudflare-tf&#10;</code></pre>
<h2 id="5-create-terraform-configuration-files"><ol start="5">
<li>Create Terraform configuration files</li>
</ol></h2>
<h3 id="define-input-variables">Define input variables</h3>
<p>The following variables will be passed into your GCP and Cloudflare configuration.</p>
<ol>
<li>In your configuration directory, create a <code>.tf</code> file:</li>
</ol>
<pre tabindex="0"><code class="language-sh">touch variables.tf&#10;</code></pre>
<ol start="2">
<li>Open the file in a text editor and copy and paste the following:</li>
</ol>
<pre tabindex="0"><code class="language-tf">&#35; GCP variables&#10;variable &quot;gcp_project_id&quot; {&#10;  description = &quot;Google Cloud Platform (GCP) project ID&quot;&#10;  type        = string&#10;}&#10;&#10;variable &quot;zone&quot; {&#10;  description = &quot;Geographical zone for the GCP VM instance&quot;&#10;  type        = string&#10;}&#10;&#10;variable &quot;machine_type&quot; {&#10;  description = &quot;Machine type for the GCP VM instance&quot;&#10;  type        = string&#10;}&#10;&#10;&#35; Cloudflare variables&#10;variable &quot;cloudflare_zone&quot; {&#10;  description = &quot;Domain used to expose the GCP VM instance to the Internet&quot;&#10;  type        = string&#10;}&#10;&#10;variable &quot;cloudflare_zone_id&quot; {&#10;  description = &quot;Zone ID for your domain&quot;&#10;  type        = string&#10;}&#10;&#10;variable &quot;cloudflare_account_id&quot; {&#10;  description = &quot;Account ID for your Cloudflare account&quot;&#10;  type        = string&#10;  sensitive   = true&#10;}&#10;&#10;variable &quot;cloudflare_email&quot; {&#10;  description = &quot;Email address for your Cloudflare account&quot;&#10;  type        = string&#10;  sensitive   = true&#10;}&#10;&#10;variable &quot;cloudflare_token&quot; {&#10;  description = &quot;Cloudflare API token&quot;&#10;  type        = string&#10;  sensitive   = true&#10;}&#10;</code></pre>
<h3 id="assign-values-to-the-variables">Assign values to the variables</h3>
<ol>
<li>In your configuration directory, create a <code>.tfvars</code> file:</li>
</ol>
<pre tabindex="0"><code class="language-sh">touch terraform.tfvars&#10;</code></pre>
<p>Terraform will automatically use these variables if the file is named <code>terraform.tfvars</code>, otherwise the variable file will need to be manually passed in.</p>
<ol start="2">
<li>Add the following variables to <code>terraform.tfvars</code>. Be sure to modify the example with your own values.</li>
</ol>
<pre tabindex="0"><code class="language-tfvars">cloudflare_zone           = &quot;example.com&quot;&#10;cloudflare_zone_id        = &quot;023e105f4ecef8ad9ca31a8372d0c353&quot;&#10;cloudflare_account_id     = &quot;372e67954025e0ba6aaa6d586b9e0b59&quot;&#10;cloudflare_email          = &quot;user@example.com&quot;&#10;cloudflare_token          = &quot;y3AalHS_E7Vabk3c3lX950F90_Xl7YtjSlzyFn_X&quot;&#10;gcp_project_id            = &quot;testvm-123&quot;&#10;zone                      = &quot;us-central1-a&quot;&#10;machine_type              = &quot;e2-medium&quot;&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5319.md")
</aside>
<h3 id="configure-terraform-providers">Configure Terraform providers</h3>
<p>You will need to declare the <a href="https://registry.terraform.io/browse/providers">providers</a> used to provision the infrastructure.</p>
<ol>
<li>In your configuration directory, create a <code>.tf</code> file:</li>
</ol>
<pre tabindex="0"><code class="language-sh">touch providers.tf&#10;</code></pre>
<ol start="2">
<li>Add the following providers to <code>providers.tf</code>. The <code>random</code> provider is used to generate a tunnel secret.</li>
</ol>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5323.md")
</div></div>
<h3 id="configure-cloudflare-resources">Configure Cloudflare resources</h3>
<p>The following configuration will modify settings in your Cloudflare account.</p>
<ol>
<li>In your configuration directory, create a <code>.tf</code> file:</li>
</ol>
<pre tabindex="0"><code class="language-sh">touch Cloudflare-config.tf&#10;</code></pre>
<ol start="2">
<li>Add the following resources to <code>Cloudflare-config.tf</code>:</li>
</ol>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5326.md")
</div></div>
<p>To learn more about these resources, refer to the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Cloudflare provider documentation</a>.</p>
<h3 id="configure-gcp-resources">Configure GCP resources</h3>
<p>The following configuration defines the specifications for the GCP virtual machine and configures a startup script to run upon boot.</p>
<ol>
<li>In your configuration directory, create a <code>.tf</code> file:</li>
</ol>
<pre tabindex="0"><code class="language-sh">touch GCP-config.tf&#10;</code></pre>
<ol start="2">
<li>Add the following content to <code>GCP-config.tf</code>:</li>
</ol>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5329.md")
</div></div>
<h3 id="create-a-startup-script">Create a startup script</h3>
<p>The following script will install <code>cloudflared</code> and run the tunnel as a service. This example also installs a lightweight HTTP application that you can use to test connectivity.</p>
<ol>
<li>In your configuration directory, create a Terraform template file:</li>
</ol>
<pre tabindex="0"><code class="language-sh">touch install-tunnel.tftpl&#10;</code></pre>
<ol start="2">
<li>Open the file in a text editor and copy and paste the following bash script:</li>
</ol>
<pre tabindex="0"><code class="language-bash">&#35; Script to install Cloudflare Tunnel and Docker resources&#10;&#10;&#35; Docker configuration&#10;cd /tmp&#10;sudo apt-get install software-properties-common&#10;&#35; Retrieving the docker repository for this OS&#10;curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -&#10;sudo add-apt-repository &quot;deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable&quot;&#10;&#35; The OS is updated and docker is installed&#10;sudo apt update -y &amp;&amp; sudo apt upgrade -y&#10;sudo apt install docker docker-compose -y&#10;&#35; Add the HTTPBin application and run it on localhost:8080.&#10;cat &gt; /tmp/docker-compose.yml &lt;&lt; &quot;EOF&quot;&#10;version: &#x27;3&#x27;&#10;services:&#10;  httpbin:&#10;    image: kennethreitz/httpbin&#10;    restart: always&#10;    container_name: httpbin&#10;    ports:&#10;      &#45; 8080:80&#10;&#10;  cloudflared:&#10;    image: cloudflare/cloudflared:latest&#10;    restart: always&#10;    container_name: cloudflared&#10;    command: tunnel run --token ${tunnel_token}&#10;EOF&#10;cd /tmp&#10;sudo docker-compose up -d&#10;</code></pre>
<h2 id="6-deploy-terraform"><ol start="6">
<li>Deploy Terraform</li>
</ol></h2>
<p>To deploy the configuration files:</p>
<ol>
<li>Initialize your configuration directory:</li>
</ol>
<pre tabindex="0"><code class="language-sh">terraform init&#10;</code></pre>
<ol start="2">
<li>Preview everything that will be created:</li>
</ol>
<pre tabindex="0"><code class="language-sh">terraform plan&#10;</code></pre>
<ol start="3">
<li>Apply the configuration:</li>
</ol>
<pre tabindex="0"><code class="language-sh">terraform apply&#10;</code></pre>
<p>It may take several minutes for the GCP instance and tunnel to come online. You can view your new tunnel in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> under <strong>Networking</strong> &gt; <strong>Tunnels</strong>, and your Access application and policy under <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>. The new DNS records are available on the <a href="/dns/manage-dns-records/how-to/create-dns-records/"><strong>DNS Records</strong> page</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="remove-terraform-resources">Remove Terraform resources</h3>
@markup("md", "content/.markup/bodies/5318.md")
</aside>
<h2 id="7-test-the-connection"><ol start="7">
<li>Test the connection</li>
</ol></h2>
<ol>
<li>
<p>In <strong>Networking</strong> &gt; <strong>Tunnels</strong>, verify that your tunnel is active.</p>
</li>
<li>
<p>In <strong>Access controls</strong> &gt; <strong>Applications</strong>, verify that your Cloudflare email is allowed by the Access policy.</p>
</li>
<li>
<p>From any device, open a browser and go to <code>http_app.&lt;CLOUDFLARE_ZONE&gt;</code> (for example, <code>http_app.example.com</code>).</p>
<p>You will see the Access login page if you have not recently logged in.</p>
</li>
<li>
<p>Log in with your Cloudflare email.</p>
<p>You should see the <a href="https://httpbin.org/">HTTPBin</a> homepage.</p>
</li>
</ol>

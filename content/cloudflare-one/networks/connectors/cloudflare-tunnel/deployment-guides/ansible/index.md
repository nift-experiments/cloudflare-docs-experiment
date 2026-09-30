<p>Ansible is a software tool that enables at scale management of infrastructure. Ansible is agentless — all it needs to function is the ability to SSH to the target and Python installed on the target.</p>
<p>Ansible works alongside Terraform to streamline the Cloudflare Tunnel setup process. In this guide, you will use Terraform to deploy an SSH server on Google Cloud and create a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/create-local-tunnel/">locally-managed tunnel</a> that makes the server available over the Internet. Terraform will automatically run an Ansible playbook that installs and configures <code>cloudflared</code> on the server.</p>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/5343.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<p>To complete the steps in this guide, you will need:</p>
<ul>
<li><a href="https://cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project">A Google Cloud Project</a> and <a href="https://cloud.google.com/sdk/docs/install">GCP CLI installed and authenticated</a>.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/terraform/">Basic knowledge of Terraform</a> and <a href="https://developer.hashicorp.com/terraform/tutorials/certification-associate-tutorials/install-cli">Terraform installed</a>.</li>
<li><a href="/fundamentals/manage-domains/add-site/">A zone on Cloudflare</a>.</li>
<li><a href="/fundamentals/api/get-started/create-token/">A Cloudflare API token</a> with <code>Cloudflare Tunnel</code> and <code>DNS</code> permissions.</li>
</ul>
<h2 id="1-install-ansible"><ol>
<li>Install Ansible</li>
</ol></h2>
<p>Refer to the <a href="https://docs.ansible.com/ansible/latest/installation_guide/index.html">Ansible installation instructions</a>.</p>
<h2 id="2-optional-create-an-ssh-key-pair"><ol start="2">
<li>(Optional) Create an SSH key pair</li>
</ol></h2>
<p>Terraform and Ansible require an unencrypted SSH key to connect to the GCP server. If you do not already have a key, you can generate one as follows:</p>
<ol>
<li>Open a terminal and type the following command:</li>
</ol>
<pre><code class="language-sh">ssh-keygen -t rsa -f ~/.ssh/gcp_ssh -C &lt;username in GCP&gt;&#10;</code></pre>
<ol start="2">
<li>When prompted for a passphrase, press the <code>Enter</code> key twice to leave it blank. Terraform cannot decode encrypted private keys.</li>
</ol>
<p>Two files will be generated: <code>gcp_ssh</code> which contains the private key, and <code>gcp_ssh.pub</code> which contains the public key.</p>
<h2 id="3-create-a-configuration-directory"><ol start="3">
<li>Create a configuration directory</li>
</ol></h2>
<ol>
<li>Create a folder for your Terraform and Ansible configuration files:</li>
</ol>
<pre><code class="language-sh">mkdir ansible-tunnel&#10;</code></pre>
<ol start="2">
<li>Change to the new directory:</li>
</ol>
<pre><code class="language-sh">cd ansible-tunnel&#10;</code></pre>
<h2 id="4-create-terraform-configuration-files"><ol start="4">
<li>Create Terraform configuration files</li>
</ol></h2>
<h3 id="define-input-variables">Define input variables</h3>
<p>The following variables will be passed into your GCP and Cloudflare configuration.</p>
<ol>
<li>In your configuration directory, create a <code>.tf</code> file:</li>
</ol>
<pre><code class="language-sh">touch variables.tf&#10;</code></pre>
<ol start="2">
<li>Open the file in a text editor and copy and paste the following:</li>
</ol>
<pre><code class="language-tf">&#35; GCP variables&#10;variable &quot;gcp_project_id&quot; {&#10;  description = &quot;Google Cloud Platform (GCP) project ID&quot;&#10;  type        = string&#10;}&#10;&#10;variable &quot;zone&quot; {&#10;  description = &quot;Geographical zone for the GCP VM instance&quot;&#10;  type        = string&#10;}&#10;&#10;variable &quot;machine_type&quot; {&#10;  description = &quot;Machine type for the GCP VM instance&quot;&#10;  type        = string&#10;}&#10;&#10;&#35; Cloudflare variables&#10;variable &quot;cloudflare_zone&quot; {&#10;  description = &quot;Domain used to expose the GCP VM instance to the Internet&quot;&#10;  type        = string&#10;}&#10;&#10;variable &quot;cloudflare_zone_id&quot; {&#10;  description = &quot;Zone ID for your domain&quot;&#10;  type        = string&#10;}&#10;&#10;variable &quot;cloudflare_account_id&quot; {&#10;  description = &quot;Account ID for your Cloudflare account&quot;&#10;  type        = string&#10;  sensitive   = true&#10;}&#10;&#10;variable &quot;cloudflare_email&quot; {&#10;  description = &quot;Email address for your Cloudflare account&quot;&#10;  type        = string&#10;  sensitive   = true&#10;}&#10;&#10;variable &quot;cloudflare_token&quot; {&#10;  description = &quot;Cloudflare API token&quot;&#10;  type        = string&#10;  sensitive   = true&#10;}&#10;</code></pre>
<h3 id="assign-values-to-the-variables">Assign values to the variables</h3>
<ol>
<li>In your configuration directory, create a <code>.tfvars</code> file:</li>
</ol>
<pre><code class="language-sh">touch terraform.tfvars&#10;</code></pre>
<p>Terraform will automatically use these variables if the file is named <code>terraform.tfvars</code>, otherwise the variable file will need to be manually passed in.</p>
<ol start="2">
<li>Add the following variables to <code>terraform.tfvars</code>. Be sure to modify the example with your own values.</li>
</ol>
<pre><code class="language-tfvars">cloudflare_zone           = &quot;example.com&quot;&#10;cloudflare_zone_id        = &quot;023e105f4ecef8ad9ca31a8372d0c353&quot;&#10;cloudflare_account_id     = &quot;372e67954025e0ba6aaa6d586b9e0b59&quot;&#10;cloudflare_email          = &quot;user@example.com&quot;&#10;cloudflare_token          = &quot;y3AalHS_E7Vabk3c3lX950F90_Xl7YtjSlzyFn_X&quot;&#10;gcp_project_id            = &quot;testvm-123&quot;&#10;zone                      = &quot;us-central1-a&quot;&#10;machine_type              = &quot;e2-medium&quot;&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5342.md")
</aside>
<h3 id="configure-terraform-providers">Configure Terraform providers</h3>
<p>You will need to declare the <a href="https://registry.terraform.io/browse/providers">providers</a> used to provision the infrastructure.</p>
<ol>
<li>In your configuration directory, create a <code>.tf</code> file:</li>
</ol>
<pre><code class="language-sh">touch providers.tf&#10;</code></pre>
<ol start="2">
<li>Add the following providers to <code>providers.tf</code>. The <code>random</code> provider is used to generate a tunnel secret.</li>
</ol>
<pre><code class="language-tf">terraform {&#10;	required_providers {&#10;		cloudflare = {&#10;			source = &quot;cloudflare/cloudflare&quot;&#10;			version = &quot;&gt;= 5.8.2&quot;&#10;		}&#10;		google = {&#10;			source = &quot;hashicorp/google&quot;&#10;		}&#10;	}&#10;	required_version = &quot;&gt;= 1.2&quot;&#10;}&#10;&#10;&#35; Providers&#10;provider &quot;cloudflare&quot; {&#10;	api_token    = var.cloudflare_token&#10;}&#10;provider &quot;google&quot; {&#10;	project    = var.gcp_project_id&#10;}&#10;provider &quot;random&quot; {&#10;}&#10;</code></pre>
<h3 id="configure-cloudflare-resources">Configure Cloudflare resources</h3>
<p>The following configuration will modify settings in your Cloudflare account.</p>
<ol>
<li>In your configuration directory, create a <code>.tf</code> file:</li>
</ol>
<pre><code class="language-sh">touch Cloudflare-config.tf&#10;</code></pre>
<ol start="2">
<li>Add the following resources to <code>Cloudflare-config.tf</code>:</li>
</ol>
<pre><code class="language-tf">&#10;&#35; Creates a new remotely-managed tunnel for the GCP VM.&#10;resource &quot;cloudflare_zero_trust_tunnel_cloudflared&quot; &quot;gcp_tunnel&quot; {&#10;	account_id    = var.cloudflare_account_id&#10;	name          = &quot;Ansible GCP tunnel&quot;&#10;	config_src    = &quot;cloudflare&quot;&#10;}&#10;&#10;&#35; Reads the token used to run the tunnel on the server.&#10;data &quot;cloudflare_zero_trust_tunnel_cloudflared_token&quot; &quot;gcp_tunnel_token&quot; {&#10;	account_id 	= var.cloudflare_account_id&#10;	tunnel_id 	= cloudflare_zero_trust_tunnel_cloudflared.gcp_tunnel.id&#10;}&#10;&#10;&#35; Creates the CNAME record that routes http_app.${var.cloudflare_zone} to the tunnel.&#10;resource &quot;cloudflare_dns_record&quot; &quot;http_app&quot; {&#10;	zone_id = var.cloudflare_zone_id&#10;	name    = &quot;http_app&quot;&#10;	content = &quot;${cloudflare_zero_trust_tunnel_cloudflared.gcp_tunnel.id}.cfargotunnel.com&quot;&#10;	type    = &quot;CNAME&quot;&#10;	ttl     = 1&#10;	proxied = true&#10;}&#10;&#10;&#35; Configures tunnel with a published application for clientless access.&#10;resource &quot;cloudflare_zero_trust_tunnel_cloudflared_config&quot; &quot;gcp_tunnel_config&quot; {&#10;	tunnel_id  = cloudflare_zero_trust_tunnel_cloudflared.gcp_tunnel.id&#10;	account_id = var.cloudflare_account_id&#10;	config     = {&#10;		ingress 	= [&#10;			{&#10;				hostname = &quot;http_app.${var.cloudflare_zone}&quot;&#10;				service  = &quot;http://localhost:80&quot;&#10;			},&#10;			{&#10;				service  = &quot;http_status:404&quot;&#10;			}&#10;		]&#10;	}&#10;}&#10;</code></pre>
<h3 id="configure-gcp-resources">Configure GCP resources</h3>
<p>The following configuration defines the specifications for the GCP virtual machine and installs Python3 on the machine. Python3 allows Ansible to configure the GCP instance instead of having to run a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/terraform/#create-a-startup-script">startup script</a> on boot.</p>
<ol>
<li>In your configuration directory, create a <code>.tf</code> file:</li>
</ol>
<pre><code class="language-sh">touch GCP-config.tf&#10;</code></pre>
<ol start="2">
<li>Open the file in a text editor and copy and paste the following example. Be sure to insert your own GCP username and SSH key pair.</li>
</ol>
<pre><code class="language-txt">&#35; Selects the OS for the GCP VM.&#10;data &quot;google_compute_image&quot; &quot;image&quot; {&#10;family  = &quot;ubuntu-2204-lts&quot;&#10;project = &quot;ubuntu-os-cloud&quot;&#10;}&#10;&#10;&#35; Sets up a GCP VM instance.&#10;resource &quot;google_compute_instance&quot; &quot;http_server&quot; {&#10;name         = &quot;ansible-inst&quot;&#10;machine_type = var.machine_type&#10;zone         = var.zone&#10;tags         = []&#10;boot_disk {&#10;    initialize_params {&#10;    image = data.google_compute_image.image.self_link&#10;    }&#10;}&#10;network_interface {&#10;    network = &quot;default&quot;&#10;    access_config {&#10;    // Ephemeral IP&#10;    }&#10;}&#10;scheduling {&#10;    preemptible = true&#10;    automatic_restart = false&#10;}&#10;&#10;// Installs Python3 on the VM.&#10;provisioner &quot;remote-exec&quot; {&#10;    inline = [&#10;    &quot;sudo apt update&quot;, &quot;sudo apt install python3 -y&quot;,  &quot;echo Done!&quot;&#10;    ]&#10;    connection {&#10;    host = self.network_interface.0.access_config.0.nat_ip&#10;    user = &quot;&lt;username in GCP&gt;&quot;&#10;    type = &quot;ssh&quot;&#10;    private_key= file(&quot;&lt;path to private key&gt;&quot;)&#10;    }&#10;}&#10;provisioner &quot;local-exec&quot; {&#10;    // If specifying an SSH key and user, add `--private-key &lt;path to private key&gt; -u var.name`&#10;    command = &quot;ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -u &lt;username in GCP&gt; --private-key &lt;path to private key&gt; -i ${self.network_interface.0.access_config.0.nat_ip}, playbook.yml&quot;&#10;}&#10;&#10;metadata = {&#10;    cf-email     = var.cloudflare_email&#10;    cf-zone      = var.cloudflare_zone&#10;    ssh-keys     = &quot;&lt;username in GCP&gt;:${file(&quot;&lt;path to public key&gt;&quot;)}&quot;&#10;}&#10;depends_on = [&#10;    local_file.tf_ansible_vars_file&#10;]&#10;}&#10;</code></pre>
<h3 id="export-variables-to-ansible">Export variables to Ansible</h3>
<p>The following Terraform resource exports the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/remote-tunnel-permissions/">tunnel token</a> and other variables to <code>tf_ansible_vars_file.yml</code>. Ansible will use the tunnel token to configure and run <code>cloudflared</code> on the server.</p>
<ol>
<li>In your configuration directory, create a new <code>tf</code> file:</li>
</ol>
<pre><code class="language-sh">touch export.tf&#10;</code></pre>
<ol start="2">
<li>Copy and paste the following content into <code>export.tf</code>:</li>
</ol>
<pre><code class="language-tf">resource &quot;local_file&quot; &quot;tf_ansible_vars_file&quot; {&#10;	content = &lt;&lt;-DOC&#10;		&#35; Ansible vars_file containing variable values from Terraform.&#10;		tunnel_id: ${cloudflare_zero_trust_tunnel_cloudflared.gcp_tunnel.id}&#10;		tunnel_name: ${cloudflare_zero_trust_tunnel_cloudflared.gcp_tunnel.name}&#10;		tunnel_token: ${data.cloudflare_zero_trust_tunnel_cloudflared_token.gcp_tunnel_token.token}&#10;		DOC&#10;&#10;	filename = &quot;./tf_ansible_vars_file.yml&quot;&#10;}&#10;</code></pre>
<h2 id="5-create-the-ansible-playbook"><ol start="5">
<li>Create the Ansible playbook</li>
</ol></h2>
<p>Ansible playbooks are YAML files that declare the configuration Ansible will deploy.</p>
<ol>
<li>Create a new <code>.yml</code> file:</li>
</ol>
<pre><code class="language-sh">touch playbook.yml&#10;</code></pre>
<ol start="2">
<li>Open the file in a text editor and copy and paste the following content:</li>
</ol>
<pre><code class="language-yml">&#45;--&#10;&#45; hosts: all&#10;  become: yes&#10;  &#35; Import tunnel variables into the VM.&#10;  vars_files:&#10;    &#45; ./tf_ansible_vars_file.yml&#10;  &#35; Execute the following commands on the VM.&#10;  tasks:&#10;    &#45; name: Download the cloudflared Linux package.&#10;      shell: wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb&#10;    &#45; name: Depackage cloudflared.&#10;      shell: sudo dpkg -i cloudflared-linux-amd64.deb&#10;    &#45; name: Install the tunnel as a systemd service.&#10;      shell: &quot;cloudflared service install {{ tunnel_token }}&quot;&#10;    &#45; name: Start the tunnel.&#10;      systemd:&#10;        name: cloudflared&#10;        state: started&#10;        enabled: true&#10;        masked: no&#10;    &#45; name: Deploy an example Apache web server on port 80.&#10;      shell: apt update &amp;&amp; apt -y install apache2&#10;    &#45; name: Edit the default Apache index file.&#10;      copy:&#10;        dest: /var/www/html/index.html&#10;        content: |&#10;          &lt;!DOCTYPE html&gt;&#10;          &lt;html&gt;&#10;          &lt;body&gt;&#10;            &lt;h1&gt;Hello Cloudflare!&lt;/h1&gt;&#10;            &lt;p&gt;This page was created for a Cloudflare demo.&lt;/p&gt;&#10;          &lt;/body&gt;&#10;          &lt;/html&gt;&#10;</code></pre>
<p><a href="https://docs.ansible.com/ansible/latest/reference_appendices/playbooks_keywords.html#play">Keywords</a> define how Ansible will execute the configuration. In the example above, the <code>vars_files</code> keyword specifies where variable definitions are stored, and the <code>tasks</code> keyword specifies the actions Ansible will perform.</p>
<p><a href="https://docs.ansible.com/ansible/2.9/user_guide/modules.html">Modules</a> specify what tasks to complete. In this example, the <code>copy</code> module creates a file and populates it with content.</p>
<h2 id="6-deploy-the-configuration"><ol start="6">
<li>Deploy the configuration</li>
</ol></h2>
<p>Once you have created the configuration files, you can deploy them through Terraform. The Ansible deployment happens within the Terraform deployment when the <code>ansible-playbook</code> command is run.</p>
<ol>
<li>Initialize your configuration directory:</li>
</ol>
<pre><code class="language-sh">terraform init&#10;</code></pre>
<ol start="2">
<li>(Optional) Preview everything that will be created:</li>
</ol>
<pre><code class="language-sh">terraform plan&#10;</code></pre>
<ol start="3">
<li>Deploy the configuration:</li>
</ol>
<pre><code class="language-sh">terraform apply&#10;</code></pre>
<p>It may take several minutes for the GCP instance and tunnel to come online. You can view your new tunnel in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> under <strong>Zero Trust</strong> &gt; <strong>Networks</strong> &gt; <strong>Connectors</strong> &gt; <strong>Cloudflare Tunnels</strong>.</p>
<h2 id="7-test-the-connection"><ol start="7">
<li>Test the connection</li>
</ol></h2>
<p>To test, open a browser and go to <code>http://http_app.&lt;CLOUDFLARE_ZONE&gt;.com</code> (for example, <code>http_app.example.com</code>). You should see the <strong>Hello Cloudflare!</strong> test page.</p>

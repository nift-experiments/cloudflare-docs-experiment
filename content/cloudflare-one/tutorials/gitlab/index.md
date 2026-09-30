<p>You can use Cloudflare Access to add Zero Trust rules to a self-hosted instance of GitLab. Combined with Cloudflare Tunnel, users can connect through HTTP and SSH and authenticate with your team's identity provider.</p>
<p><strong>This walkthrough covers how to:</strong></p>
<ul>
<li>Deploy an instance of GitLab</li>
<li>Lock down all inbound connections to that instance and use Cloudflare Tunnel to set outbound connections to Cloudflare</li>
<li>Build policies with Cloudflare Access to control who can reach GitLab</li>
<li>Connect over HTTP and SSH through Cloudflare</li>
</ul>
<p><strong>Time to complete:</strong></p>
<p>1 hour</p>
<hr />
<h2 id="deploying-gitlab">Deploying GitLab</h2>
<p>This section walks through deploying GitLab in DigitalOcean. If you have already deployed GitLab, you can skip this section.</p>
<p>Create a Droplet that has 16 GB of RAM and 6 CPUs. This should make it possible to support 500 users, based on <a href="https://docs.gitlab.com/ee/install/requirements.html">GitLab's resource recommendations</a>.</p>
<p><img src="/assets/upstream/images/cloudflare-one/zero-trust-security/gitlab/create-droplet.png" alt="Create Droplet" /></p>
<p>GitLab will provide an external IP that is exposed to the Internet (for now). You will need to connect to the deployed server using this external IP for the initial configuration. You can secure connections to the IP by <a href="https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2">adding SSH keys</a> to your DigitalOcean account.</p>
<p>This example uses a macOS machine to configure the Droplet. Copy the IP address assigned to the machine from DigitalOcean.</p>
<p><img src="/assets/upstream/images/cloudflare-one/zero-trust-security/gitlab/show-ip.png" alt="Machine IP" /></p>
<p>Open Terminal and run the following command, replacing the IP address with the IP assigned by DigitalOcean.</p>
<pre><code class="language-sh">ssh root@134.209.124.123&#10;</code></pre>
<p>Next, install GitLab. This example uses the <a href="https://about.gitlab.com/install/#ubuntu">Ubuntu package</a> and the steps in the GitLab documentation, with a few exceptions called out below.</p>
<p>Run the following commands to begin.</p>
<pre><code class="language-sh">sudo apt-get update&#10;&#10;sudo apt-get install -y curl openssh-server ca-certificates&#10;curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.deb.sh | sudo bash&#10;</code></pre>
<p>The commands above download the GitLab software to this machine. You must now install it. This is the first place this tutorial will diverge from the operations in the GitLab documentation. The next step in the GitLab-provided tutorial sets an external hostname. Instead, you can just install the software.</p>
<pre><code class="language-sh">sudo apt-get install gitlab-ee&#10;</code></pre>
<p>After a minute or so, GitLab will be installed.</p>
<p><img src="/assets/upstream/images/cloudflare-one/zero-trust-security/gitlab/install-gitlab.png" alt="Install GitLab" /></p>
<p>However, the application is not running yet. You can check to see what ports are listening to confirm by using <code>ss</code>.</p>
<pre><code class="language-sh">sudo ss -lntup&#10;</code></pre>
<p>The result should be only the services currently active on the machine:</p>
<pre><code class="language-bash">sudo ss -lntup&#10;</code></pre>
<pre><code class="language-bash">Netid   State    Recv-Q   Send-Q     Local Address:Port     Peer Address:Port   Process&#10;udp     UNCONN   0        0                      *:9094                *:*&#10;tcp     LISTEN   0        128              0.0.0.0:22            0.0.0.0:*       users:((&quot;sshd&quot;,pid=29,fd=3))&#10;tcp     LISTEN   0        128                 [::]:22               [::]:*       users:((&quot;sshd&quot;,pid=29,fd=4))&#10;</code></pre>
<p>To start GitLab, run the software's reconfigure command.</p>
<pre><code class="language-sh">sudo gitlab-ctl reconfigure&#10;</code></pre>
<p>GitLab will launch its component services. Once complete, confirm that GitLab is running and listening on both ports 22 and 80.</p>
<p><img src="/assets/upstream/images/cloudflare-one/zero-trust-security/gitlab/gitlab-services.png" alt="GitLab Services" /></p>
<pre><code class="language-bash">sudo ss -lntup&#10;</code></pre>
<pre><code class="language-bash">Netid   State    Recv-Q   Send-Q     Local Address:Port     Peer Address:Port   Process&#10;udp     UNCONN   0        0                      *:9094                *:*&#10;tcp     LISTEN   0        4096           127.0.0.1:9236          0.0.0.0:*&#10;tcp     LISTEN   0        4096           127.0.0.1:8150          0.0.0.0:*&#10;tcp     LISTEN   0        128              0.0.0.0:22            0.0.0.0:*       users:((&quot;sshd&quot;,pid=29,fd=3))&#10;tcp     LISTEN   0        4096           127.0.0.1:8151          0.0.0.0:*&#10;tcp     LISTEN   0        4096           127.0.0.1:3000          0.0.0.0:*&#10;tcp     LISTEN   0        4096           127.0.0.1:8153          0.0.0.0:*&#10;tcp     LISTEN   0        4096           127.0.0.1:8154          0.0.0.0:*&#10;tcp     LISTEN   0        4096           127.0.0.1:8155          0.0.0.0:*&#10;tcp     LISTEN   0        511              0.0.0.0:8060          0.0.0.0:*       users:((&quot;nginx&quot;,pid=324,fd=8))&#10;tcp     LISTEN   0        4096           127.0.0.1:9121          0.0.0.0:*&#10;tcp     LISTEN   0        4096           127.0.0.1:9090          0.0.0.0:*&#10;tcp     LISTEN   0        4096           127.0.0.1:9187          0.0.0.0:*&#10;tcp     LISTEN   0        4096           127.0.0.1:9093          0.0.0.0:*&#10;tcp     LISTEN   0        4096           127.0.0.1:9229          0.0.0.0:*&#10;tcp     LISTEN   0        1024           127.0.0.1:8080          0.0.0.0:*&#10;tcp     LISTEN   0        511              0.0.0.0:80            0.0.0.0:*       users:((&quot;nginx&quot;,pid=324,fd=7))&#10;tcp     LISTEN   0        4096           127.0.0.1:9168          0.0.0.0:*&#10;tcp     LISTEN   0        4096           127.0.0.1:8082          0.0.0.0:*&#10;tcp     LISTEN   0        128                 [::]:22               [::]:*       users:((&quot;sshd&quot;,pid=29,fd=4))&#10;tcp     LISTEN   0        4096                   *:9094                *:*&#10;</code></pre>
<p>Users connect to GitLab over SSH (port 22 here) and HTTP for the web app (port 80). In the next step, you will make it possible for users to try both through Cloudflare Access. I'll leave this running and head over to the Cloudflare dashboard.</p>
<h2 id="securing-gitlab-with-zero-trust-rules">Securing GitLab with Zero Trust rules</h2>
<h3 id="building-zero-trust-policies">Building Zero Trust policies</h3>
<p>You can use Cloudflare Access to build Zero Trust rules to determine who can connect to both the web application of GitLab (HTTP) and who can connect over SSH.</p>
<p>When a user makes a request to a site protected by Access, that request hits Cloudflare's network first. Access can then check if the user is allowed to reach the application. When integrated with Cloudflare Tunnel, the Zero Trust architecture looks like this:</p>
<p><img src="/assets/upstream/images/cloudflare-one/zero-trust-security/gitlab/teams-diagram.png" alt="GitLab Services" /></p>
<p>To determine who can reach the application, Cloudflare Access relies on integration with identity providers like Okta, Microsoft Entra ID, or Google to issue the identity cards that get checked at the door. While a VPN allows users free range on a private network unless someone builds an active rule to stop them, Access enforces that identity check on every request (and at any granularity configured).</p>
<p>For GitLab, start by building two policies. Users will connect to GitLab in a couple of methods: in the web app and over SSH. Create policies to secure a subdomain for each. First, the web app.</p>
<p>Before you build the rule, you'll need to follow <a href="/cloudflare-one/setup/">these instructions</a> to set up Cloudflare Access in your account.</p>
<p>Once enabled, go to the <strong>Applications</strong> page in Zero Trust. Select <strong>Create new application</strong>.</p>
<p>Select <strong>Self-hosted and private</strong>.</p>
<p><img src="/assets/upstream/images/cloudflare-one/zero-trust-security/gitlab/policy.png" alt="Self Hosted" /></p>
<p>You will be prompted to add a subdomain that will represent the resource. This must be a subdomain of a domain in your Cloudflare account. You will need separate subdomains for the web application and SSH flows.</p>
<p>This example uses <code>gitlab.widgetcorp.tech</code> for the web application and <code>gitlab-ssh.widgetcorp.tech</code> for SSH connectivity.</p>
<p>You can decide which identity providers will be allowed to authenticate. By default, all configured providers are allowed. Add rules to determine who can reach the site.</p>
<p>Select <strong>Create</strong> to publish the application. Repeat these steps for the second application, <code>gitlab-ssh.widgetcorp.tech</code>.</p>
<h2 id="cloudflare-tunnel">Cloudflare Tunnel</h2>
<p>Cloudflare Tunnel creates a secure, outbound-only, connection between this machine and Cloudflare's network. With an outbound-only model, you can prevent any direct access to this machine and lock down any externally exposed points of ingress. And with that, no open firewall ports.</p>
<p>Cloudflare Tunnel is made possible through a lightweight daemon from Cloudflare called <code>cloudflared</code>. Download and install <code>cloudflared</code> on the DigitalOcean machine by following the instructions listed on the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/">Downloads</a> page.</p>
<p>Once installed, authenticate the instance of <code>cloudflared</code> with the following command.</p>
<pre><code class="language-sh">cloudflared login&#10;</code></pre>
<p>The command will print a URL that you must visit to login with your Cloudflare account.</p>
<p>Choose a website that you have added into your account.</p>
<p>Once you select one of the sites in your account, Cloudflare will download a certificate file to authenticate this instance of <code>cloudflared</code>. You can now use <code>cloudflared</code> to control Cloudflare Tunnel connections in your Cloudflare account.</p>
<p><img src="/assets/upstream/images/cloudflare-one/secure-origin-connections/share-new-site/cert-download.png" alt="Download Cert" /></p>
<h3 id="connecting-to-cloudflare">Connecting to Cloudflare</h3>
<p>You can now connect GitLab to Cloudflare using Cloudflare Tunnel.</p>
<ol>
<li>Create a new Tunnel by running the following command.</li>
</ol>
<pre><code class="language-sh">cloudflared tunnel create gitlab&#10;</code></pre>
<p><code>cloudflared</code> will generate a unique ID for this Tunnel, for example <code>6ff42ae2-765d-4adf-8112-31c55c1551ef</code>. You can use this Tunnel both for SSH and HTTP traffic.</p>
<ol start="2">
<li>You will need to configure Cloudflare Tunnel to proxy traffic to both destinations. The configuration below will take traffic bound for the DNS record that will be created for the web app and the DNS record to represent SSH traffic to the right port.</li>
</ol>
<p>You use the text editor of your choice to edit the configuration file. The example relies on <code>Vi</code>.</p>
<pre><code class="language-sh">vim ~/.cloudflared/config.yml&#10;</code></pre>
<ol start="3">
<li>Configure the Tunnel to serve traffic.</li>
</ol>
<pre><code class="language-yml">tunnel: 6ff42ae2-765d-4adf-8112-31c55c1551ef&#10;credentials-file: /root/.cloudflared/6ff42ae2-765d-4adf-8112-31c55c1551ef.json&#10;&#10;ingress:&#10;  &#45; hostname: gitlab.widgetcorp.tech&#10;    service: http://localhost:80&#10;  &#45; hostname: gitlab-ssh.widgetcorp.tech&#10;    service: ssh://localhost:22&#10;  &#35; Catch-all rule, which just responds with 404 if traffic doesn&#x27;t match any of&#10;  &#35; the earlier rules&#10;  &#45; service: http_status:404&#10;</code></pre>
<p><img src="/assets/upstream/images/cloudflare-one/zero-trust-security/gitlab/config-file.png" alt="Self Hosted" /></p>
<ol start="4">
<li>You can test that the configuration file is set correctly with the following command:</li>
</ol>
<pre><code class="language-sh">cloudflared tunnel ingress validate&#10;</code></pre>
<p><code>cloudflared</code> should indicate the Tunnel is okay. You can now begin running the Tunnel.</p>
<pre><code class="language-sh">cloudflared tunnel run&#10;</code></pre>
<p><img src="/assets/upstream/images/cloudflare-one/zero-trust-security/gitlab/tunnel-run.png" alt="Tunnel Run" /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4299.md")
</aside>
<h3 id="configure-dns-records">Configure DNS records</h3>
<p>You can now create DNS records for GitLab in the Cloudflare dashboard. Remember, you will still need two records - one for the web application and one for SSH traffic.</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and go to the <strong>DNS Records</strong> page for your domain.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Add record</strong>. Choose <code>CNAME</code> as the record type.</li>
<li>In the <strong>Name</strong> field, input <code>gitlab</code>.</li>
<li>In the <strong>Target</strong> field, input the ID of the Tunnel created followed by <code>cfargotunnel.com</code>. In this example, that value is:</li>
</ol>
<pre><code class="language-txt">6ff42ae2-765d-4adf-8112-31c55c1551ef.cfargotunnel.com&#10;</code></pre>
<ol start="5">
<li>Select <strong>Save</strong>.</li>
<li>Repeat the process again by creating a second <code>CNAME</code> record, with the same <strong>Target</strong>, but input <code>gitlab-ssh</code> for the <strong>Name</strong>. Both records should then appear, pointing to the same Tunnel. The ingress rules defined in the configuration file above will direct traffic to the appropriate port.</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/zero-trust-security/gitlab/view-dns.png" alt="View DNS" /></p>
<h3 id="connecting-to-the-web-application">Connecting to the web application</h3>
<p>You can now test the end-to-end configuration for the web application. Visit the subdomain created for the web application. Cloudflare Access will prompt you to authenticate. Login with your provider.</p>
<p>Once authenticated, you should see the GitLab web application.</p>
<p><img src="/assets/upstream/images/cloudflare-one/zero-trust-security/gitlab/gitlab-web.png" alt="GitLab Web" /></p>
<p>Register your own account and create a Blank project to test SSH in the next step.</p>
<p><img src="/assets/upstream/images/cloudflare-one/zero-trust-security/gitlab/blank-project.png" alt="Blank Project" /></p>
<p>GitLab will create a new project and repository.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4298.md")
</aside>
<h3 id="configuring-ssh">Configuring SSH</h3>
<p>To push and pull code over SSH, you will need to install <code>cloudflared</code> on the client machine as well. This example uses a macOS laptop. On macOS, you can install <code>cloudflared</code> with the following command.</p>
<pre><code class="language-sh">brew install cloudflared&#10;</code></pre>
<p>While you need to install <code>cloudflared</code>, you do not need to wrap your SSH commands in any unique way. Instead, you will need to make a one-time change to your SSH configuration file.</p>
<pre><code class="language-sh">vim /Users/samrhea/.ssh/config&#10;</code></pre>
<p>Input the following values; replacing <code>gitlab-ssh.widgetcorp.tech</code> with the hostname you created.</p>
<pre><code class="language-txt">Host gitlab-ssh.widgetcorp.tech&#10;  ProxyCommand /usr/local/bin/cloudflared access ssh --hostname %h&#10;</code></pre>
<p>You can now test the SSH flow by attempting to clone the project created earlier.</p>
<pre><code class="language-sh">git clone git@gitlab-ssh.widgetcorp.tech:samrhea/demo&#10;</code></pre>
<p><code>cloudflared</code> will prompt you to login with my identity provider and, once successful, issue a token to your device to allow you to authenticate.</p>
<p><img src="/assets/upstream/images/cloudflare-one/zero-trust-security/gitlab/git-clone.png" alt="GitLab Clone" /></p>
<h3 id="lock-down-exposed-ports">Lock down exposed ports</h3>
<p>You can now configure your DigitalOcean firewall with a single rule, block any inbound traffic, to prevent direct access.</p>
<p><img src="/assets/upstream/images/cloudflare-one/zero-trust-security/gitlab/disable-ingress.png" alt="Set Rules" /></p>
<p>Cloudflare Tunnel will continue to run outbound-only connections and I can avoid this machine getting caught up in a crypto mining operation, or something worse.</p>
<h2 id="view-logs">View logs</h2>
<p>You can also view logs of the events that are allowed and blocked. Open the <code>Access</code> page of the <code>Logs</code> section in Zero Trust.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If you are using Git Large File Storage (LFS), note that Git LFS is not automatically supported by <code>cloudflared</code>. To access repositories protected by Cloudflare Access, you need to authenticate manually by running:</p>
<pre><code class="language-sh">cloudflared access login &lt;your-git-access-url&gt;&#10;</code></pre>
<p>Replace <code>&lt;your-git-access-url&gt;</code> with the Cloudflare Access-protected URL.</p>

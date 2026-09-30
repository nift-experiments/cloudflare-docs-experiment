<p>You can build Zero Trust rules to secure connections to MongoDB deployments using Cloudflare Access and Cloudflare Tunnel. Cloudflare Tunnel requires a lightweight daemon, <code>cloudflared</code>, running alongside the deployment and as on the client side.</p>
<p>In this tutorial, a client running <code>cloudflared</code> connects over SSH to a MongoDB deployment running on Kubernetes. The deployment example is structured to connect <a href="https://www.mongodb.com/products/compass">Compass</a> to the MongoDB instance. The MongoDB Kubernetes deployment runs both the MongoDB database service and <code>cloudflared</code> as a ingress service that operates like a jump host.</p>
<p><strong>This tutorial covers how to:</strong></p>
<ul>
<li>Create a Cloudflare Access rule to secure a MongoDB deployment</li>
<li>Configure a StatefulSet and service definition for the deployment</li>
<li>Configure an Cloudflare Tunnel connection to Cloudflare's edge</li>
<li>Create an SSH configuration file for the client</li>
</ul>
<p><strong>Time to complete:</strong></p>
<p>50 minutes</p>
<hr />
<h2 id="configure-cloudflare-access">Configure Cloudflare Access</h2>
<p>You can build a rule in Cloudflare Access to control who can connect to your MongoDB deployment. Cloudflare Access rules are built around a hostname; even though this deployment will be accessible over SSH, the resource will be represented in Cloudflare as a hostname. For example, if you have the website <code>app.com</code> in your Cloudflare account, you can build a rule to secure <code>mongodb.app.com</code>.</p>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</p>
</li>
<li>
<p>Select <strong>Create new application</strong>.</p>
</li>
<li>
<p>Select <strong>Self-hosted and private</strong>.</p>
</li>
<li>
<p>Select <strong>Add public hostname</strong> and enter the subdomain where users will connect to your deployment (for example, <code>mongodb.app.com</code>).</p>
</li>
<li>
<p>Add <a href="/cloudflare-one/access-controls/policies/">Access policies</a> to control who can reach the deployment. You can build a policy that allows anyone in your organization to connect or you can build more granular policies based on signals like identity provider groups, <a href="/cloudflare-one/tutorials/okta-u2f/">multifactor method</a>, or <a href="/cloudflare-one/access-controls/policies/groups/">country</a>.</p>
</li>
<li>
<p>Follow the remaining <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted application creation steps</a> to publish the application.</p>
</li>
</ol>
<h2 id="configure-the-kubernetes-deployment">Configure the Kubernetes deployment</h2>
<p>To be accessible over SSH, the Kubernetes deployment should manage both the MongoDB standalone service and an SSH proxy service. The configuration below will deploy 1 replica of the database service, available at port 27017, as well as an SSH proxy available at port 22.</p>
<details class="nb-details"><summary>StatefulSet Configuration</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4294.md")
</div></details>
<p>The corresponding service definition should also specify the ports and target ports for the containers (in this case, the database service and the SSH proxy service).</p>
<details class="nb-details"><summary>Service Definition</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4295.md")
</div></details>
<p>The MongoDB pod and the SSH jump host will share a Unix socket over an empty directory volume. The <code>entrypoint.sh</code> file run by the jump host, example below, will start an OpenSSH server.</p>
<pre><code class="language-bash">&#35;!/bin/sh&#10;export TZ=America/Chicago&#10;ln -snf /usr/share/zoneinfo/$TZ /etc/localtime &amp;&amp; echo $TZ &gt; /etc/timezone&#10;apt-get update -y &amp;&amp; apt-get install -y openssh-server&#10;mkdir /root/.ssh&#10;cp /config/ssh/authorized_keys /root/.ssh/authorized_keys&#10;chmod 400 /root/.ssh/authorized_keys&#10;service ssh start&#10;while true;&#10;do sleep 30;&#10;done;&#10;</code></pre>
<h2 id="configure-cloudflare-tunnel">Configure Cloudflare Tunnel</h2>
<p>Next, you can use <code>cloudflared</code> to connect to Cloudflare's Edge using Cloudflare Tunnel. Start by <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/create-local-tunnel/">downloading and installing</a> the Cloudflare Tunnel daemon, <code>cloudflared</code>.</p>
<p>Once installed, run the following command to authenticate the instance of <code>cloudflared</code> into your Cloudflare account.</p>
<pre><code class="language-sh">cloudflared login&#10;</code></pre>
<p>The command will launch a browser window and prompt you to login with your Cloudflare account. Choose a website that you have added into your account.</p>
<p>Once you select one of the sites in your account, Cloudflare will download a certificate file, called <code>cert.pem</code> to authenticate this instance of <code>cloudflared</code>. The <code>cert.pem</code> file uses a certificate to authenticate your instance of <code>cloudflared</code> and includes an API key for your account to perform actions like DNS record changes.</p>
<p>You can now use <code>cloudflared</code> to control Cloudflare Tunnel connections in your Cloudflare account.</p>
<p><img src="/assets/upstream/images/cloudflare-one/secure-origin-connections/share-new-site/cert-download.png" alt="Download Certificate" /></p>
<h3 id="create-a-tunnel">Create a Tunnel</h3>
<p>You can now <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/create-local-tunnel/">create a Tunnel</a> that will connect <code>cloudflared</code> to Cloudflare's edge. You'll configure the details of that Tunnel in the next step.</p>
<p>Run the following command to create a Tunnel. You can replace <code>mongodb</code> with any name that you choose. This command requires the <code>cert.pem</code> file.</p>
<p><code>cloudflared tunnel create mongodb</code></p>
<p>Cloudflare will create the Tunnel with that name and generate an ID and credentials file for that Tunnel.</p>
<p><img src="/assets/upstream/images/cloudflare-one/secure-origin-connections/share-new-site/create.png" alt="New Tunnel" /></p>
<h3 id="delete-the-cert-pem-file">Delete the <code>cert.pem</code> file</h3>
<p>The credentials file is separate from the <code>cert.pem</code> file. Unlike the <code>cert.pem</code> file, the credentials file consists of a token that authenticates only the Named Tunnel you just created. Formatted as <code>JSON</code>, the file cannot make changes to your Cloudflare account or create additional Tunnels.</p>
<p>If you are done creating Tunnels, you can delete the <code>cert.pem</code> file, leave only the credentials file, and continue to manage DNS records directly in the Cloudflare dashboard or API. For additional information on the different functions of the two files, refer to the list of <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/tunnel-useful-terms/#certpem">useful terms</a>.</p>
<p>Store the <code>JSON</code> file as a Kubernetes secret.</p>
<h3 id="configure-cloudflare-tunnel-1">Configure Cloudflare Tunnel</h3>
<p>The previous setps used <code>cloudflared</code> to generate a credentials file for your Cloudflare account. When run as a service alongside the MongoDB Kubernetes deployment you will need to use a Docker image of <code>cloudflared</code>. Cloudflare makes an <a href="https://hub.docker.com/r/cloudflare/cloudflared">official image available</a> in DockerHub.</p>
<p>The configuration below will run a single replica of <code>cloudflared</code> as an ingress point alongside the MongoDB and SSH proxy services. <code>cloudflared</code> will proxy traffic to the SSH proxy service. The <code>cloudflared</code> instance will run as its own deployment in a different namespace and, if network policy allows, ingress to any service in the Kubernetes node.</p>
<details class="nb-details"><summary>�CODE35� Configuration</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4296.md")
</div></details>
<h2 id="connect-from-a-client">Connect from a client</h2>
<p>Once deployed, you can run <code>cloudflared</code> on the client side to connect to the MongoDB deployment. Add the following lines to your SSH configuration file, replacing the examples with your hostname and details. The <code>--destination</code> value should match the URL of the SSH Proxy service configured previously.</p>
<pre><code class="language-bash">Host mongodb&#10;  ProxyCommand /usr/local/bin/cloudflared access ssh --hostname mongodb.widgetcorp.tech --destination ssh-proxy.mongodb.svc.cluster.local:22&#10;  LocalForward 27000 /socket/mongodb-27017.sock&#10;  User root&#10;  IdentityFile /Users/username/.ssh/id_rsa&#10;</code></pre>
<p>This is a one-time step. When you next attempt to make an SSH connection to the deployment, <code>cloudflared</code> will launch a browser window and prompt you to authenticate. Once authenticated, you will be connected if you have a valid session. Once the tunnel is established, all requests to <code>localhost:27000</code> on your machine will be forwarded to <code>/socket/mongodb-27017.sock</code> on the SSH proxy container.</p>
<p>You can then set MongoDB Compass to connect to <code>localhost:27000</code>.</p>

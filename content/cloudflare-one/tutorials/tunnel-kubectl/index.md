<p>This tutorial explains how to use Cloudflare Tunnels with Kubernetes client-go credential plugins for authentication. By following these steps, you can securely access your Kubernetes cluster through a Cloudflare Tunnel using the <code>kubectl</code> command-line tool.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A Cloudflare account</li>
<li>The Cloudflare Tunnel client (<code>cloudflared</code>) installed on your machine</li>
<li>Access to a Kubernetes cluster</li>
<li><code>kubectl</code> installed on your machine</li>
</ul>
<h2 id="1-set-up-a-cloudflare-tunnel"><ol>
<li>Set up a Cloudflare Tunnel</li>
</ol></h2>
<ol>
<li>Authenticate <code>cloudflared</code> with your Cloudflare account:</li>
</ol>
<pre><code class="language-sh">cloudflared tunnel login&#10;</code></pre>
<ol start="2">
<li>Create a new tunnel:</li>
</ol>
<pre><code class="language-sh">cloudflared tunnel create k8s-tunnel&#10;</code></pre>
<ol start="3">
<li>Configure your tunnel by creating a configuration file named <code>config.yml</code>:</li>
</ol>
<pre><code class="language-yaml">tunnel: &lt;TUNNEL_ID&gt;&#10;credentials-file: /path/to/credentials.json&#10;ingress:&#10;  &#45; hostname: k8s.example.com&#10;    service: tcp://kubernetes.default.svc.cluster.local:443&#10;  &#45; service: http_status:404&#10;</code></pre>
<p>Replace <code>&lt;TUNNEL_ID&gt;</code> with your tunnel ID and adjust the hostname as needed.</p>
<ol start="4">
<li>Start the tunnel:</li>
</ol>
<pre><code class="language-sh">cloudflared tunnel run k8s-tunnel&#10;</code></pre>
<h2 id="2-configure-the-kubernetes-api-server"><ol start="2">
<li>Configure the Kubernetes API server</li>
</ol></h2>
<p>Ensure your Kubernetes API server is configured to accept authentication from Cloudflare Tunnels. This may involve setting up an authentication webhook or configuring the API server to trust the Cloudflare Tunnel's client certificates.</p>
<h2 id="3-set-up-client-go-credential-plugin"><ol start="3">
<li>Set up client-go credential plugin</li>
</ol></h2>
<ol>
<li>Create a script named <code>cloudflare-k8s-auth.sh</code> with the following content:</li>
</ol>
<pre><code class="language-bash">&#35;!/bin/bash&#10;&#10;echo &#x27;{&#10;  &quot;apiVersion&quot;: &quot;client.authentication.k8s.io/v1beta1&quot;,&#10;  &quot;kind&quot;: &quot;ExecCredential&quot;,&#10;  &quot;status&quot;: {&#10;    &quot;token&quot;: &quot;&#x27;&quot;$(cloudflared access token -app=https://k8s.example.com)&quot;&#x27;&quot;&#10;  }&#10;}&#x27;&#10;</code></pre>
<p>Make the script executable:</p>
<pre><code class="language-sh">chmod +x cloudflare-k8s-auth.sh&#10;</code></pre>
<ol start="2">
<li>Update your <code>~/.kube/config</code> file to use the credential plugin:</li>
</ol>
<pre><code class="language-yaml">apiVersion: v1&#10;kind: Config&#10;clusters:&#10;  &#45; cluster:&#10;      server: https://k8s.example.com&#10;    name: cloudflare-k8s&#10;users:&#10;  &#45; name: cloudflare-user&#10;    user:&#10;      exec:&#10;        apiVersion: client.authentication.k8s.io/v1beta1&#10;        command: /path/to/cloudflare-k8s-auth.sh&#10;        interactiveMode: Never&#10;contexts:&#10;  &#45; context:&#10;      cluster: cloudflare-k8s&#10;      user: cloudflare-user&#10;    name: cloudflare-k8s-context&#10;current-context: cloudflare-k8s-context&#10;</code></pre>
<h2 id="4-use-kubectl-with-cloudflare-tunnel"><ol start="4">
<li>Use kubectl with Cloudflare Tunnel</li>
</ol></h2>
<p>Now you can use <code>kubectl</code> commands as usual. The client-go credential plugin will automatically handle authentication through the Cloudflare Tunnel:</p>
<pre><code class="language-sh">kubectl get pods&#10;</code></pre>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If you encounter issues:</p>
<ul>
<li>Ensure <code>cloudflared</code> is running and the tunnel is active</li>
<li>Check that your <code>~/.kube/config</code> file is correctly configured</li>
<li>Verify that the Kubernetes API server is properly set up to accept authentication from Cloudflare Tunnels</li>
<li>Review the Cloudflare Tunnel logs for any error messages</li>
</ul>
<p>For more information, refer to the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnels documentation</a> and the <a href="https://kubernetes.io/docs/reference/access-authn-authz/authentication/#client-go-credential-plugins">Kubernetes client-go credential plugins documentation</a>.</p>

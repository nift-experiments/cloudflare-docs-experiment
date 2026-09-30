---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/tutorials/tunnel-kubectl/
  description: This tutorial explains how to use Cloudflare Tunnels with Kubernetes client-go credential plugins for authentication. By following these steps, you can securely access your Kubernetes cluster through a Cloudflare Tunnel.
  full_title: Use Cloudflare Tunnels with Kubernetes client-go credential plugins · Cloudflare One docs
  head_html: <title>Use Cloudflare Tunnels with Kubernetes client-go credential plugins · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="This tutorial explains how to use Cloudflare Tunnels with Kubernetes client-go credential plugins for authentication. By following these steps, you can securely access your Kubernetes cluster through a Cloudflare Tunnel."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/tutorials/tunnel-kubectl/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/tutorials/tunnel-kubectl/index.md"><meta property="og:title" content="Use Cloudflare Tunnels with Kubernetes client-go credential plugins · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This tutorial explains how to use Cloudflare Tunnels with Kubernetes client-go credential plugins for authentication. By following these steps, you can securely access your Kubernetes cluster through a Cloudflare Tunnel."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/tutorials/tunnel-kubectl/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Kubernetes"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/tutorials/tunnel-kubectl/#page","headline":"Use Cloudflare Tunnels with Kubernetes client-go credential plugins \u00b7 Cloudflare One docs","description":"This tutorial explains how to use Cloudflare Tunnels with Kubernetes client-go credential plugins for authentication. By following these steps, you can securely access your Kubernetes cluster through a Cloudflare Tunnel.","url":"https://developers.cloudflare.com/cloudflare-one/tutorials/tunnel-kubectl/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Kubernetes"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/tutorials/tunnel-kubectl/
  schema: 1
---
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
<pre tabindex="0"><code class="language-sh">cloudflared tunnel login&#10;</code></pre>
<ol start="2">
<li>Create a new tunnel:</li>
</ol>
<pre tabindex="0"><code class="language-sh">cloudflared tunnel create k8s-tunnel&#10;</code></pre>
<ol start="3">
<li>Configure your tunnel by creating a configuration file named <code>config.yml</code>:</li>
</ol>
<pre tabindex="0"><code class="language-yaml">tunnel: &lt;TUNNEL_ID&gt;&#10;credentials-file: /path/to/credentials.json&#10;ingress:&#10;  &#45; hostname: k8s.example.com&#10;    service: tcp://kubernetes.default.svc.cluster.local:443&#10;  &#45; service: http_status:404&#10;</code></pre>
<p>Replace <code>&lt;TUNNEL_ID&gt;</code> with your tunnel ID and adjust the hostname as needed.</p>
<ol start="4">
<li>Start the tunnel:</li>
</ol>
<pre tabindex="0"><code class="language-sh">cloudflared tunnel run k8s-tunnel&#10;</code></pre>
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
<pre tabindex="0"><code class="language-bash">&#35;!/bin/bash&#10;&#10;echo &#x27;{&#10;  &quot;apiVersion&quot;: &quot;client.authentication.k8s.io/v1beta1&quot;,&#10;  &quot;kind&quot;: &quot;ExecCredential&quot;,&#10;  &quot;status&quot;: {&#10;    &quot;token&quot;: &quot;&#x27;&quot;$(cloudflared access token -app=https://k8s.example.com)&quot;&#x27;&quot;&#10;  }&#10;}&#x27;&#10;</code></pre>
<p>Make the script executable:</p>
<pre tabindex="0"><code class="language-sh">chmod +x cloudflare-k8s-auth.sh&#10;</code></pre>
<ol start="2">
<li>Update your <code>~/.kube/config</code> file to use the credential plugin:</li>
</ol>
<pre tabindex="0"><code class="language-yaml">apiVersion: v1&#10;kind: Config&#10;clusters:&#10;  &#45; cluster:&#10;      server: https://k8s.example.com&#10;    name: cloudflare-k8s&#10;users:&#10;  &#45; name: cloudflare-user&#10;    user:&#10;      exec:&#10;        apiVersion: client.authentication.k8s.io/v1beta1&#10;        command: /path/to/cloudflare-k8s-auth.sh&#10;        interactiveMode: Never&#10;contexts:&#10;  &#45; context:&#10;      cluster: cloudflare-k8s&#10;      user: cloudflare-user&#10;    name: cloudflare-k8s-context&#10;current-context: cloudflare-k8s-context&#10;</code></pre>
<h2 id="4-use-kubectl-with-cloudflare-tunnel"><ol start="4">
<li>Use kubectl with Cloudflare Tunnel</li>
</ol></h2>
<p>Now you can use <code>kubectl</code> commands as usual. The client-go credential plugin will automatically handle authentication through the Cloudflare Tunnel:</p>
<pre tabindex="0"><code class="language-sh">kubectl get pods&#10;</code></pre>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If you encounter issues:</p>
<ul>
<li>Ensure <code>cloudflared</code> is running and the tunnel is active</li>
<li>Check that your <code>~/.kube/config</code> file is correctly configured</li>
<li>Verify that the Kubernetes API server is properly set up to accept authentication from Cloudflare Tunnels</li>
<li>Review the Cloudflare Tunnel logs for any error messages</li>
</ul>
<p>For more information, refer to the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnels documentation</a> and the <a href="https://kubernetes.io/docs/reference/access-authn-authz/authentication/#client-go-credential-plugins">Kubernetes client-go credential plugins documentation</a>.</p>

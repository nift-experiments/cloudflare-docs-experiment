---
cp9:
  canonical: https://developers.cloudflare.com/containers/guides/ssh/
  description: Connect to running container instances with SSH.
  full_title: SSH · Cloudflare Containers docs
  head_html: <title>SSH · Cloudflare Containers docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect to running container instances with SSH."><link rel="canonical" href="https://developers.cloudflare.com/containers/guides/ssh/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/containers/guides/ssh/index.md"><meta property="og:title" content="SSH · Cloudflare Containers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect to running container instances with SSH."><meta property="og:url" content="https://developers.cloudflare.com/containers/guides/ssh/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Containers"><meta name="algolia_product_filter" content="Containers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Containers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/containers/guides/ssh/#page","headline":"SSH \u00b7 Cloudflare Containers docs","description":"Connect to running container instances with SSH.","url":"https://developers.cloudflare.com/containers/guides/ssh/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /containers/guides/ssh/
  schema: 1
---
<p>Anyone with write access to a Container can SSH into it with Wrangler as long as a matching public key is listed in <code>authorized_keys</code>.</p>
<p>SSH does not expose a publicly accessible port on the Container. The only way to connect is through Wrangler with <a href="/workers/wrangler/commands/containers/#containers-ssh"><code>wrangler containers ssh</code></a>, which authenticates against your Cloudflare account.</p>
<h2 id="configure-ssh">Configure SSH</h2>
<p>SSH can be configured in your <a href="/workers/wrangler/configuration/#containers">Container's configuration</a> with the <code>ssh</code> and <code>authorized_keys</code> properties. Only the <code>ssh-ed25519</code> key type is supported.</p>
<p>The <code>ssh.enabled</code> property only controls whether you can SSH into a Container through Wrangler. It defaults to <code>true</code>. Set it to <code>false</code> to disable SSH access completely.</p>
<h2 id="connect-with-wrangler">Connect with Wrangler</h2>
<p>To SSH into a Container with Wrangler, add an <code>ssh-ed25519</code> public key to <code>authorized_keys</code> in your Container configuration. The following example shows a basic configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/7091.md")
</div>
<p>For more information on configuring SSH, refer to <a href="/workers/wrangler/configuration/#ssh">SSH configuration</a>.</p>
<p>Find the instance ID for your Container by running <a href="/workers/wrangler/commands/containers/#containers-instances"><code>wrangler containers instances</code></a> or in the <a href="https://dash.cloudflare.com/?to=/:account/workers/containers">Cloudflare dashboard</a>.
The instance you want to SSH into must be running.
SSH will not start a stopped Container, and an active SSH connection alone will not keep a Container alive.</p>
<p>Once SSH is configured and the Container is running, open the SSH connection with:</p>
<pre tabindex="0"><code class="language-bash">wrangler containers ssh &lt;INSTANCE_ID&gt;&#10;</code></pre>
<h2 id="use-as-ssh-proxy">Use as SSH proxy</h2>
<p>You can use <code>wrangler containers ssh</code> as an OpenSSH <code>ProxyCommand</code>. This lets your local SSH client connect through Wrangler.</p>
<pre tabindex="0"><code class="language-sh">ssh -o ProxyCommand=&quot;wrangler containers ssh %h&quot; cloudchamber@&lt;INSTANCE_ID&gt;&#10;</code></pre>
<p>When used this way, Wrangler pipes standard input and output to the SSH server in the running Container. You can also pass <code>--stdio</code> to force this mode.</p>
<h2 id="process-visibility">Process visibility</h2>
<p>Without the <a href="/workers/configuration/compatibility-flags/#use-an-isolated-pid-namespace-for-containers"><code>containers_pid_namespace</code></a> compatibility flag, all processes inside the VM are visible when you connect to your Container through SSH. This flag is turned on by default for Workers with a <a href="/workers/configuration/compatibility-dates/">compatibility date</a> of <code>2026-04-01</code> or later.</p>

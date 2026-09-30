---
cp9:
  canonical: https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/tunnel-useful-commands/
  description: Common cloudflared commands for managing tunnels.
  full_title: Useful commands · Cloudflare Docs
  head_html: <title>Useful commands · Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="Common cloudflared commands for managing tunnels."><link rel="canonical" href="https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/tunnel-useful-commands/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/tunnel-useful-commands/index.md"><meta property="og:title" content="Useful commands · Cloudflare Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Common cloudflared commands for managing tunnels."><meta property="og:url" content="https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/tunnel-useful-commands/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Tunnel"><meta name="algolia_product_filter" content="Cloudflare Tunnel"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Tunnel"><meta name="pcx_tags" content="CLI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/tunnel-useful-commands/#page","headline":"Useful commands \u00b7 Cloudflare Docs","description":"Common cloudflared commands for managing tunnels.","url":"https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/tunnel-useful-commands/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["CLI"]}</script>
  markdown: true
  noindex: false
  route: /tunnel/features/locally-managed-tunnels/tunnel-useful-commands/
  schema: 1
---
<p>This page lists the most commonly used commands for managing local tunnels.</p>
<p>To view all CLI commands, refer to the CLI help text in your terminal. For example, to view all options for the <code>cloudflared tunnel</code> subcommand, type <code>cloudflared tunnel help</code>.</p>
<h2 id="manage-cloudflared">Manage <code>cloudflared</code></h2>
<table>
<thead>
<tr>
<th>Command</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cloudflared update</code></td>
<td>Looks for a new version on the official download server. If a new version exists, it updates the agent binary and quits. Otherwise, no action is performed. This command only works if <code>cloudflared</code> was installed from GitHub binaries or from source. For more information, refer to the <a href="/tunnel/guides/update-cloudflared/">update instructions</a>.</td>
</tr>
<tr>
<td><code>cloudflared version</code></td>
<td>Prints the <code>cloudflared</code> version number and build date.</td>
</tr>
<tr>
<td><code>cloudflared help</code></td>
<td>Shows a list of all top-level commands for <code>cloudflared</code>.</td>
</tr>
</tbody>
</table>
<h2 id="manage-tunnels">Manage tunnels</h2>
<table>
<thead>
<tr>
<th>Command</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cloudflared tunnel login</code></td>
<td>Prompts a browser window where you can authenticate your tunnel to your Cloudflare account.</td>
</tr>
<tr>
<td><code>cloudflared tunnel list</code></td>
<td>Displays all active tunnels, their creation time, and associated connections. Use the <code>-d</code> flag to include deleted tunnels.</td>
</tr>
<tr>
<td><code>cloudflared tunnel create &lt;NAME or UUID&gt;</code></td>
<td>Creates a tunnel, registers it with the Cloudflare edge and generates a credential file to run this tunnel.</td>
</tr>
<tr>
<td><code>cloudflared tunnel --config path/config.yaml run &lt;NAME or UUID&gt;</code></td>
<td>Runs a tunnel, creating highly available connections between your server and the Cloudflare edge. You can provide name or UUID of the tunnel to run either as the last command line argument or in the configuration file using <code>tunnel: &lt;NAME&gt;</code>.</td>
</tr>
<tr>
<td><code>cloudflared tunnel info &lt;NAME or UUID&gt;</code></td>
<td>Displays details about the active connectors for a given tunnel identified by name of UUID.</td>
</tr>
<tr>
<td><code>cloudflared tunnel cleanup &lt;NAME or UUID&gt;</code></td>
<td>Deletes connections for tunnels with the given UUIDs or names. This is useful if you get an error trying to delete or run a tunnel after <code>cloudflared</code> is not shut down gracefully (for example, if a <code>kill</code> command is issued).</td>
</tr>
<tr>
<td><code>cloudflared tunnel cleanup --connector-id &lt;CONNECTOR-ID&gt; &lt;NAME or UUID&gt;</code></td>
<td>Disconnects and deletes a <a href="/tunnel/configuration/#replicas-and-high-availability"><code>cloudflared</code> replica</a> with the given connector ID. You can view all replicas for a tunnel by running <code>cloudflared tunnel info &lt;NAME or UUID&gt;</code>.</td>
</tr>
<tr>
<td><code>cloudflared tunnel delete &lt;NAME or UUID&gt;</code></td>
<td>Deletes tunnels with the given name or UUID. A tunnel cannot be deleted if it has active connections. To delete the tunnel unconditionally, use the <code>-f</code> flag.</td>
</tr>
<tr>
<td><code>cloudflared tail &lt;UUID&gt;</code></td>
<td>Start a session to livestream logs from a specific tunnel. For more information, refer to <a href="/tunnel/observability/#logs">Tunnel logs</a>.</td>
</tr>
</tbody>
</table>
<h2 id="manage-published-applications">Manage published applications</h2>
<table>
<thead>
<tr>
<th>Command</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cloudflared tunnel route dns</code></td>
<td>Creates a DNS CNAME record hostname that points to the tunnel.</td>
</tr>
<tr>
<td><code>cloudflared tunnel route lb &lt;NAME or UUID&gt; &lt;hostname&gt; &lt;load balancer pool&gt;</code></td>
<td>Adds a tunnel as an endpoint in a <a href="/tunnel/concepts/routing/#add-a-tunnel-to-a-load-balancer-pool">load balancer pool</a>. A new load balancer and pool will be created if necessary. <ul> <li> <code>&lt;hostname&gt;</code>: the public-facing hostname of the load balancer, for example <code>lb.example.com</code> </li> <li> <code>&lt;load balancer pool&gt;</code>: the name of the <a href="/load-balancing/pools/create-pool/#create-a-pool">pool</a> that will contain the tunnel endpoint </li> </ul> To load balance traffic to a <a href="/tunnel/features/locally-managed-tunnels/configuration-file/#file-structure-for-published-applications">published application</a>, you will also need to specify the application hostname in the <a href="/load-balancing/additional-options/override-http-host-headers/">endpoint host header</a> using the dashboard or API.</td>
</tr>
</tbody>
</table>

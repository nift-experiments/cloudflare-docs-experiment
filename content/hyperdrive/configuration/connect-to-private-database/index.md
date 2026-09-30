<p>Hyperdrive can securely connect to your private databases using <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> and <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9059.md")
</aside>
<h2 id="how-it-works">How it works</h2>
<p>When your database is isolated within a private network (such as a <a href="https://www.cloudflare.com/learning/cloud/what-is-a-virtual-private-cloud">virtual private cloud</a> or an on-premise network), you must enable a secure connection from your network to Cloudflare.</p>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> is used to establish the secure tunnel connection.</li>
<li><a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a> is used to restrict access to your tunnel such that only specific Hyperdrive configurations can access it.</li>
</ul>
<p>A request from the Cloudflare Worker to the origin database goes through Hyperdrive, Cloudflare Access, and the Cloudflare Tunnel established by <code>cloudflared</code>. <code>cloudflared</code> must be running in the private network in which your database is accessible.</p>
<p>The Cloudflare Tunnel will establish an outbound bidirectional connection from your private network to Cloudflare. Cloudflare Access will secure your Cloudflare Tunnel to be only accessible by your Hyperdrive configuration.</p>
<p><img src="/assets/upstream/images/hyperdrive/configuration/hyperdrive-private-database-architecture.png" alt="A request from the Cloudflare Worker to the origin database goes through Hyperdrive, Cloudflare Access and the Cloudflare Tunnel established by cloudflared." /></p>
<h2 id="before-you-start">Before you start</h2>
<p>All of the tutorials assume you have already completed the <a href="/workers/get-started/guide/">Get started guide</a>, which gets you set up with a Cloudflare Workers account, <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare">C3</a>, and <a href="/workers/wrangler/install-and-update/">Wrangler</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/9058.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A database in your private network, <a href="/hyperdrive/examples/connect-to-postgres/">configured to use TLS/SSL</a>.</li>
<li>A hostname on your Cloudflare account, which will be used to route requests to your database.</li>
</ul>
<h2 id="1-create-a-tunnel-in-your-private-network"><ol>
<li>Create a tunnel in your private network</li>
</ol></h2>
<h3 id="1-1-create-a-tunnel">1.1. Create a tunnel</h3>
<p>First, create a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> in your private network to establish a secure connection between your network and Cloudflare. Your network must be configured such that the tunnel has permissions to egress to the Cloudflare network and access the database within your network.</p>
<ol>
<li>Log in to the Cloudflare dashboard and go to <strong>Networking</strong> &gt; <strong>Tunnels</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select <strong>Create a tunnel</strong>.</p>
</li>
<li>
<p>Enter a name for your tunnel. We suggest choosing a name that reflects the type of resources you want to connect through this tunnel (for example, <code>enterprise-VPC-01</code>).</p>
</li>
<li>
<p>Select <strong>Create Tunnel</strong>.</p>
</li>
<li>
<p>Choose your operating system, then copy the installation command and run it in a terminal on your origin server.</p>
</li>
<li>
<p>Wait for the tunnel to connect. Once the connection is established, select <strong>Continue</strong>.</p>
</li>
</ol>
<h3 id="1-2-connect-your-database-using-a-public-hostname">1.2. Connect your database using a public hostname</h3>
<p>Your tunnel must be configured to use a public hostname on Cloudflare so that Hyperdrive can route requests to it. If you don't have a hostname on Cloudflare yet, you will need to <a href="/registrar/get-started/register-domain/">register a new hostname</a> or <a href="/dns/zone-setups/">add a zone</a> to Cloudflare to proceed.</p>
<ol>
<li>
<p>In the <strong>Published application routes</strong> tab, choose a <strong>Domain</strong> and specify any subdomain or path information. This will be used in your Hyperdrive configuration to route to this tunnel.</p>
</li>
<li>
<p>In the <strong>Service</strong> section, specify <strong>Type</strong> <code>TCP</code> and the URL and configured port of your database, such as <code>localhost:5432</code> or <code>my-database-host.database-provider.com:5432</code>. This address will be used by the tunnel to route requests to your database.</p>
</li>
<li>
<p>Select <strong>Save tunnel</strong>.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9057.md")
</aside>
<h2 id="2-create-and-configure-hyperdrive-to-connect-to-the-cloudflare-tunnel"><ol start="2">
<li>Create and configure Hyperdrive to connect to the Cloudflare Tunnel</li>
</ol></h2>
<p>To restrict access to the Cloudflare Tunnel to Hyperdrive, a <a href="/cloudflare-one/access-controls/applications/http-apps/">Cloudflare Access application</a> must be configured with a <a href="/cloudflare-one/traffic-policies/">Policy</a> that requires requests to contain a valid <a href="/cloudflare-one/access-controls/policies/#service-auth">Service Auth token</a>.</p>
<p>The Cloudflare dashboard can automatically create and configure the underlying <a href="/cloudflare-one/access-controls/applications/http-apps/">Cloudflare Access application</a>, <a href="/cloudflare-one/access-controls/policies/#service-auth">Service Auth token</a>, and <a href="/cloudflare-one/traffic-policies/">Policy</a> on your behalf. Alternatively, you can manually create the Access application and configure the Policies.</p>
<details class="nb-details"><summary>Automatic creation</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9061.md")
</div></details>
<details class="nb-details"><summary>Manual creation</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9067.md")
</div></details>
<h2 id="3-query-your-hyperdrive-configuration-from-a-worker-optional"><ol start="3">
<li>Query your Hyperdrive configuration from a Worker (optional)</li>
</ol></h2>
<p>To test your Hyperdrive configuration to the database using Cloudflare Tunnel and Access, use the Hyperdrive configuration ID in your Worker and deploy it.</p>
<h3 id="3-1-create-a-hyperdrive-binding">3.1. Create a Hyperdrive binding</h3>
<p>You must create a binding in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> for your Worker to connect to your Hyperdrive configuration. <a href="/workers/runtime-apis/bindings/">Bindings</a> allow your Workers to access resources, like Hyperdrive, on the Cloudflare developer platform.</p>
<p>To bind your Hyperdrive configuration to your Worker, add the following to the end of your Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9068.md")
</div>
<p>Specifically:</p>
<ul>
<li>The value (string) you set for the <code>binding</code> (binding name) will be used to reference this database in your Worker. In this tutorial, name your binding <code>HYPERDRIVE</code>.</li>
<li>The binding must be <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#variables">a valid JavaScript variable name</a>. For example, <code>binding = &quot;hyperdrive&quot;</code> or <code>binding = &quot;productionDB&quot;</code> would both be valid names for the binding.</li>
<li>Your binding is available in your Worker at <code>env.&lt;BINDING_NAME&gt;</code>.</li>
</ul>
<p>If you wish to use a local database during development, you can add a <code>localConnectionString</code> to your  Hyperdrive configuration with the connection string of your database:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9069.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9054.md")
</aside>
<h3 id="3-2-query-your-database">3.2. Query your database</h3>
<p>Validate that you can connect to your database from Workers and make queries.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9074.md")
</div></div>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If you encounter issues when setting up your Hyperdrive configuration with tunnels to a private database, consider these common solutions, in addition to <a href="/hyperdrive/observability/troubleshooting/">general troubleshooting steps</a> for Hyperdrive:</p>
<ul>
<li>Ensure your database is configured to use TLS (SSL). Hyperdrive requires TLS (SSL) to connect.</li>
</ul>

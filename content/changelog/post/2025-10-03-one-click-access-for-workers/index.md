<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 3, 2025</time><h2 id="post-title">One-click Cloudflare Access for Workers</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now enable <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a> for your <a href="/workers/configuration/routing/workers-dev/"><code>workers.dev</code></a> and <a href="/workers/versions-and-deployments/preview-urls/">Preview URLs</a> in a single click.</p>
<p><img src="/assets/upstream/images/workers/changelog/workers-access.png" alt="Screenshot of the Enable/Disable Cloudflare Access button on the workers.dev route settings page" /></p>
<p>Access allows you to limit access to your Workers to specific users or groups. You can limit access to yourself, your teammates, your organization, or anyone else you specify in your <a href="/cloudflare-one/access-controls/policies/">Access policy</a>.</p>
<p>To enable Cloudflare Access:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In <strong>Overview</strong>, select your Worker.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Domains &amp; Routes</strong>.</li>
<li>For <code>workers.dev</code> or Preview URLs, click <strong>Enable Cloudflare Access</strong>.</li>
<li>Optionally, to configure the Access application, click <strong>Manage Cloudflare Access</strong>. There, you can change the email addresses you want to authorize. View <a href="/cloudflare-one/access-controls/policies/#selectors">Access policies</a> to learn about configuring alternate rules.</li>
</ol>
<p>To fully secure your application, it is important that you validate the JWT that Cloudflare Access adds to the <code>Cf-Access-Jwt-Assertion</code> header on the incoming request.</p>
<p>The following code will validate the JWT using the <a href="https://www.npmjs.com/package/jose">jose NPM package</a>:</p>
<pre><code class="language-javascript">import { jwtVerify, createRemoteJWKSet } from &quot;jose&quot;;&#10;&#10;export default {&#10;	async fetch(request, env, ctx) {&#10;		// Verify the POLICY_AUD environment variable is set&#10;		if (!env.POLICY_AUD) {&#10;			return new Response(&quot;Missing required audience&quot;, {&#10;				status: 403,&#10;				headers: { &quot;Content-Type&quot;: &quot;text/plain&quot; },&#10;			});&#10;		}&#10;&#10;		// Get the JWT from the request headers&#10;		const token = request.headers.get(&quot;cf-access-jwt-assertion&quot;);&#10;&#10;		// Check if token exists&#10;		if (!token) {&#10;			return new Response(&quot;Missing required CF Access JWT&quot;, {&#10;				status: 403,&#10;				headers: { &quot;Content-Type&quot;: &quot;text/plain&quot; },&#10;			});&#10;		}&#10;&#10;		try {&#10;			// Create JWKS from your team domain&#10;			const JWKS = createRemoteJWKSet(&#10;				new URL(`${env.TEAM_DOMAIN}/cdn-cgi/access/certs`),&#10;			);&#10;&#10;			// Verify the JWT&#10;			const { payload } = await jwtVerify(token, JWKS, {&#10;				issuer: env.TEAM_DOMAIN,&#10;				audience: env.POLICY_AUD,&#10;			});&#10;&#10;			// Token is valid, proceed with your application logic&#10;			return new Response(`Hello ${payload.email || &quot;authenticated user&quot;}!`, {&#10;				headers: { &quot;Content-Type&quot;: &quot;text/plain&quot; },&#10;			});&#10;		} catch (error) {&#10;			// Token verification failed&#10;			return new Response(`Invalid token: ${error.message}`, {&#10;				status: 403,&#10;				headers: { &quot;Content-Type&quot;: &quot;text/plain&quot; },&#10;			});&#10;		}&#10;	},&#10;};&#10;</code></pre>
<h4 id="required-environment-variables">Required environment variables</h4>
<p>Add these <a href="/workers/configuration/environment-variables/">environment variables</a> to your Worker:</p>
<ul>
<li><code>POLICY_AUD</code>: Your application's AUD tag</li>
<li><code>TEAM_DOMAIN</code>: <code>https://&lt;your-team-name&gt;.cloudflareaccess.com</code></li>
</ul>
<p>Both of these appear in the modal that appears when you enable Cloudflare Access.</p>
<p>You can set these variables by adding them to your Worker's <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>, or via the Cloudflare dashboard under <strong>Workers &amp; Pages</strong> &gt; <strong>your-worker</strong> &gt; <strong>Settings</strong> &gt; <strong>Environment Variables</strong>.</p>
</div></article></div>

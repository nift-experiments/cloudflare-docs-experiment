<p>This tutorial will walk you through extending the single-sign-on (SSO) capabilities of <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a> with our serverless computing platform, <a href="/workers/">Cloudflare Workers</a>. Specifically, this guide will demonstrate how to modify requests sent to your secured origin to include additional information from the Cloudflare Access authentication event.</p>
<p><strong>Time to complete:</strong> 45 minutes</p>
<h2 id="authentication-flow">Authentication flow</h2>
<p><a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a> is an authentication proxy in charge of validating a user's identity before they connect to your application. As shown in the diagram below, Access inserts a <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/">JWT</a> into the request, which can then be <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/#validate-jwts">verified</a> by the origin server.</p>
<p><img src="/assets/upstream/images/cloudflare-one/applications/access-standard-flow.png" alt="Standard authentication flow for a request to an Access application" /></p>
<p>You can extend this functionality by using a Cloudflare Worker to insert additional HTTP headers into the request. In this example, we will add the <a href="/cloudflare-one/reusable-components/posture-checks/#enforce-device-posture">device posture attributes</a> <code>firewall_activated</code> and <code>disk_encrypted</code>, but you can include any attributes that Cloudflare Access collects from the authentication event.</p>
<p><img src="/assets/upstream/images/cloudflare-one/applications/access-extended-flow-serverless.png" alt="Extended authentication flow uses a Worker to pass additional request headers to the origin" /></p>
<h2 id="benefits">Benefits</h2>
<p>This approach allows you to:</p>
<ul>
<li><strong>Enhance security:</strong> By incorporating additional information from the authentication event, you can implement more robust security measures. For example, you can use device posture data to enforce access based on device compliance.</li>
<li><strong>Improve user experience:</strong> You can personalize the user experience by tailoring content or functionality based on user attributes. For example, you can display different content based on the user's role or location.</li>
<li><strong>Simplify development:</strong> By using Cloudflare Workers, you can easily extend your Cloudflare Access configuration without modifying your origin application code.</li>
</ul>
<h2 id="before-you-begin">Before you begin</h2>
<ul>
<li>Add a <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted application</a> to Cloudflare Access.</li>
<li>Enable the <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/disk-encryption/">Disk encryption</a> and <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/firewall/">Firewall</a> device posture checks.</li>
<li>Install <a href="/workers/wrangler/install-and-update/">Wrangler</a> on your local machine.</li>
</ul>
<h2 id="1-create-the-worker"><ol>
<li>Create the Worker</li>
</ol></h2>
<ol>
<li>Create a new Workers project:</li>
</ol>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- device-posture-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- device-posture-worker" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare device-posture-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare device-posture-worker" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest device-posture-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest device-posture-worker" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>JavaScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<ol start="2">
<li>Change to the project directory:</li>
</ol>
<pre><code class="language-sh">$ cd device-posture-worker&#10;</code></pre>
<ol start="3">
<li>Copy-paste the following code into <code>src/index.js</code>. Be sure to replace <code>&lt;your-team-name&gt;</code> with your Zero Trust <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ol>
@markup("md", "content/.markup/bodies/4300.md")
</div>.
<pre><code class="language-js">import { parse } from &quot;cookie&quot;;&#10;export default {&#10;	async fetch(request, env, ctx) {&#10;		// The name of the cookie&#10;		const COOKIE_NAME = &quot;CF_Authorization&quot;;&#10;		const CF_GET_IDENTITY =&#10;			&quot;https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/get-identity&quot;;&#10;		const cookie = parse(request.headers.get(&quot;Cookie&quot;) || &quot;&quot;);&#10;		if (cookie[COOKIE_NAME] != null) {&#10;			try {&#10;				let id = await (await fetch(CF_GET_IDENTITY, request)).json();&#10;				let diskEncryptionStatus = false;&#10;				let firewallStatus = false;&#10;&#10;				for (const checkId in id.devicePosture) {&#10;					const check = id.devicePosture[checkId];&#10;					if (check.type === &quot;disk_encryption&quot;) {&#10;						console.log(check.type);&#10;						diskEncryptionStatus = check.success;&#10;					}&#10;					if (check.type === &quot;firewall&quot;) {&#10;						console.log(check.type);&#10;						firewallStatus = check.success;&#10;						break;&#10;					}&#10;				}&#10;				//clone request (immutable otherwise) and insert posture values in new header set&#10;				let newRequest = await new Request(request);&#10;				newRequest.headers.set(&#10;					&quot;Cf-Access-Firewall-Activated&quot;,&#10;					firewallStatus,&#10;				);&#10;				newRequest.headers.set(&quot;Cf-Access-Disk-Encrypted&quot;, firewallStatus);&#10;&#10;				//sent modified request to origin&#10;				return await fetch(newRequest);&#10;			} catch (e) {&#10;				console.log(e);&#10;				return await fetch(request);&#10;			}&#10;		}&#10;		return await fetch(request);&#10;	},&#10;};&#10;</code></pre>
<h2 id="2-view-the-user-s-identity"><ol start="2">
<li>View the user's identity</li>
</ol></h2>
<p>The script in <code>index.js</code> uses the <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/#user-identity"><code>get-identity</code></a> endpoint to fetch a user's complete identity from a Cloudflare Access authentication event. To view a list of available data fields, log in to your Access application and append <code>/cdn-cgi/access/get-identity</code> to the URL. For example, if <code>www.example.com</code> is behind Access, go to <code>https://www.example.com/cdn-cgi/access/get-identity</code>.</p>
<p>Below is an example of a user identity that includes the <code>disk_encryption</code> and <code>firewall</code> posture checks. The Worker inserts the posture check results into the request headers <strong>Cf-Access-Firewall-Activated</strong> and <strong>Cf-Access-Disk-Encrypted</strong>.</p>
<pre><code class="language-json">{&#10;  &quot;id&quot;: &quot;P51Tuu01fWHMBjIBvrCK1lK-eUDWs2aQMv03WDqT5oY&quot;,&#10;  &quot;name&quot;: &quot;John Doe&quot;,&#10;  &quot;email&quot;: &quot;john.doe@cloudflare.com&quot;,&#10;  &quot;amr&quot;: [&#10;    &quot;pwd&quot;&#10;  ],&#10;  &quot;oidc_fields&quot;: {&#10;    &quot;principalName&quot;: &quot;XXXXXX_cloudflare.com#EXT#@XXXXXXcloudflare.onmicrosoft.com&quot;&#10;  },&#10;  &quot;groups&quot;: [&#10;    {&#10;      &quot;id&quot;: &quot;fdaedb59-e9be-4ab7-8001-3e069da54185&quot;,&#10;      &quot;name&quot;: &quot;XXXXX&quot;&#10;    }&#10;  ],&#10;  &quot;idp&quot;: {&#10;    &quot;id&quot;: &quot;b9f4d68e-dac1-48b0-b728-ae05a5f0d4b2&quot;,&#10;    &quot;type&quot;: &quot;azureAD&quot;&#10;  },&#10;  &quot;geo&quot;: {&#10;    &quot;country&quot;: &quot;FR&quot;&#10;  },&#10;  &quot;user_uuid&quot;: &quot;ce40d564-c72f-475f-a9b8-f395f19ad986&quot;,&#10;  &quot;account_id&quot;: &quot;121287a0c6e6260ec930655e6b39a3a8&quot;,&#10;  &quot;iat&quot;: 1724056537,&#10;  &quot;devicePosture&quot;: {&#10;    &quot;f6f9391e-6776-4878-9c60-0cc807dc7dc8&quot;: {&#10;      &quot;id&quot;: &quot;f6f9391e-6776-4878-9c60-0cc807dc7dc8&quot;,&#10;      &quot;schedule&quot;: &quot;5m&quot;,&#10;      &quot;timestamp&quot;: &quot;2024-08-19T08:31:59.274Z&quot;,&#10;      &quot;description&quot;: &quot;&quot;,&#10;      &quot;type&quot;: &quot;disk_encryption&quot;,&#10;      &quot;check&quot;: {&#10;        &quot;drives&quot;: {&#10;          &quot;C&quot;: {&#10;            &quot;encrypted&quot;: true&#10;          }&#10;        }&#10;      },&#10;      &quot;success&quot;: false,&#10;      &quot;rule_name&quot;: &quot;Disk Encryption - Windows&quot;,&#10;      &quot;input&quot;: {&#10;        &quot;requireAll&quot;: true,&#10;        &quot;checkDisks&quot;: []&#10;    },&#10;    &quot;a0a8e83d-be75-4aa6-bfa0-5791da6e9186&quot;: {&#10;      &quot;id&quot;: &quot;a0a8e83d-be75-4aa6-bfa0-5791da6e9186&quot;,&#10;      &quot;schedule&quot;: &quot;5m&quot;,&#10;      &quot;timestamp&quot;: &quot;2024-08-19T08:31:59.274Z&quot;,&#10;      &quot;description&quot;: &quot;&quot;,&#10;      &quot;type&quot;: &quot;firewall&quot;,&#10;      &quot;check&quot;: {&#10;        &quot;firewall&quot;: false&#10;      },&#10;      &quot;success&quot;: false,&#10;      &quot;rule_name&quot;: &quot;Local Firewall Check - Windows&quot;,&#10;      &quot;input&quot;: {&#10;        &quot;enabled&quot;: true&#10;      }&#10;    }&#10;    ...&#10;  }&#10;</code></pre>
<h2 id="3-route-the-worker-to-your-application"><ol start="3">
<li>Route the Worker to your application</li>
</ol></h2>
<p>In the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>, <a href="/workers/configuration/routing/routes/">set up a route</a> that maps the Worker to your Access application domain:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/4301.md")
</div>
<h2 id="4-deploy-the-worker"><ol start="4">
<li>Deploy the Worker</li>
</ol></h2>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>The Worker will now insert the <strong>Cf-Access-Firewall-Activated</strong> and <strong>Cf-Access-Disk-Encrypted</strong> headers into requests that pass your application's Access policies.</p>
<pre><code class="language-json">{&#10;	&quot;headers&quot;: {&#10;		&quot;Accept&quot;: &quot;text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7&quot;,&#10;		&quot;Accept-Encoding&quot;: &quot;gzip&quot;,&#10;		&quot;Accept-Language&quot;: &quot;en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-GB;q=0.6&quot;,&#10;		&quot;Cf-Access-Authenticated-User-Email&quot;: &quot;John.Doe@cloudflare.com&quot;,&#10;		&quot;Cf-Access-Disk-Encrypted&quot;: &quot;false&quot;,&#10;		&quot;Cf-Access-Firewall-Activated&quot;: &quot;false&quot;,&#10;		&quot;User-Agent&quot;: &quot;Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36&quot;&#10;	}&#10;}&#10;</code></pre>
<p>You can verify that these headers are received by the origin server.</p>

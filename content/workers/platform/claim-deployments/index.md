---
cp9:
  canonical: https://developers.cloudflare.com/workers/platform/claim-deployments/
  description: Deploy Workers before authentication, then claim the temporary account to keep its deployments and resources.
  full_title: Claim deployments (temporary accounts) · Cloudflare Workers docs
  head_html: <title>Claim deployments (temporary accounts) · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy Workers before authentication, then claim the temporary account to keep its deployments and resources."><link rel="canonical" href="https://developers.cloudflare.com/workers/platform/claim-deployments/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/platform/claim-deployments/index.md"><meta property="og:title" content="Claim deployments (temporary accounts) · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy Workers before authentication, then claim the temporary account to keep its deployments and resources."><meta property="og:url" content="https://developers.cloudflare.com/workers/platform/claim-deployments/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/platform/claim-deployments/#page","headline":"Claim deployments (temporary accounts) \u00b7 Cloudflare Workers docs","description":"Deploy Workers before authentication, then claim the temporary account to keep its deployments and resources.","url":"https://developers.cloudflare.com/workers/platform/claim-deployments/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/platform/claim-deployments/
  schema: 1
---
<p>Temporary preview accounts let you deploy and test <a href="/workers/">Workers</a> before you authenticate with Cloudflare. You can then claim the account to keep its deployments and supported resources.</p>
<p><a href="https://www.cloudflare.com/drop/">Cloudflare Drop</a> demonstrates this preview-and-claim lifecycle for static sites. Platforms can use the REST API to offer a similar experience for generated applications.</p>
<p>For design context, refer to <a href="https://blog.cloudflare.com/temporary-accounts/">Temporary Cloudflare Accounts for AI agents</a>.</p>
<p><img src="/assets/upstream/images/workers/claim-deployments-flow.png" alt="Diagram showing an AI agent deploying, verifying, and redeploying a Worker in a temporary account, then a user authenticating and claiming the account to keep its resources" /></p>
<h2 id="choose-an-integration">Choose an integration</h2>
<p>Choose an integration based on who controls account provisioning:</p>
<table>
<thead>
<tr>
<th>Integration</th>
<th>Use when</th>
<th>Provisioning behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/workers/wrangler/">Wrangler</a> with <code>wrangler deploy --temporary</code></td>
<td>An AI agent or tool runs Wrangler</td>
<td>Wrangler creates or reuses the account and prints the claim URL</td>
</tr>
<tr>
<td>REST API at <code>api.cloudflare.com/client/v4/provisioning/previews</code></td>
<td>Your platform backend controls the deployment experience</td>
<td>Your backend receives temporary credentials and the claim URL</td>
</tr>
</tbody>
</table>
<p>For production and continuous integration and continuous deployment (CI/CD), use a permanent Cloudflare account. Authenticate with <a href="/workers/wrangler/commands/general/#login"><code>wrangler login</code></a> or a <a href="/fundamentals/api/get-started/create-token/">Cloudflare API token</a>.</p>
<h2 id="deploy-with-wrangler">Deploy with Wrangler</h2>
<p>Use Wrangler when an AI agent or tool runs deployment commands. Wrangler manages the proof-of-work challenge, credentials, and claim URL.</p>
<p>Wrangler 4.102.0 or later prints guidance to rerun unauthenticated deployments with <code>--temporary</code>.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16232.md")
</div>
<h2 id="integrate-with-the-rest-api">Integrate with the REST API</h2>
<p>Use the REST API when your platform backend controls deployments. The backend provisions an account before the user authenticates, then deploys supported resources.</p>
<p>Make all provisioning and deployment calls from your backend. The provisioning response contains sensitive credentials and a claim URL.</p>
<p>The following diagram shows how the platform keeps temporary credentials in its backend while the user previews and claims the deployment:</p>
<pre tabindex="0"><code class="language-mermaid">flowchart LR&#10;    accTitle: Platform preview and claim architecture&#10;    accDescr: A user accepts Cloudflare&#x27;s policies and requests a preview in the platform UI. The trusted platform backend creates a temporary account, keeps account.apiToken private, deploys the Worker, and returns only the preview and claim URLs to the UI. The claim URL is a bearer credential shown only to the intended user. The user claims the account in the Cloudflare dashboard. Future platform deployments require a separate OAuth flow.&#10;&#10;    USER((User))&#10;&#10;    subgraph PLATFORM[&quot;Platform&quot;]&#10;        direction TB&#10;        UI[&quot;Platform UI&lt;br/&gt;No temporary API token&quot;]&#10;        BACKEND[&quot;Trusted platform backend&lt;br/&gt;Stores account.apiToken&quot;]&#10;        UI --&gt;|&quot;2. Request preview&quot;| BACKEND&#10;        BACKEND --&gt;|&quot;10. Preview URL and bearer claim URL only&quot;| UI&#10;    end&#10;&#10;    subgraph CLOUDFLARE[&quot;Cloudflare&quot;]&#10;        direction TB&#10;        API[&quot;Cloudflare API&quot;]&#10;        DASHBOARD[&quot;Cloudflare dashboard&lt;br/&gt;Claims the account&quot;]&#10;    end&#10;&#10;    USER --&gt;|&quot;1. Accept policies and generate application&quot;| UI&#10;    BACKEND --&gt;|&quot;3. Request challenge&quot;| API&#10;    API --&gt;|&quot;4. Challenge parameters&quot;| BACKEND&#10;    BACKEND --&gt;|&quot;5. Solve challenge locally&quot;| BACKEND&#10;    BACKEND --&gt;|&quot;6. Create temporary account with solution&quot;| API&#10;    API --&gt;|&quot;7. Account ID, API token, and claim URL&quot;| BACKEND&#10;    BACKEND --&gt;|&quot;8. Deploy Worker and request subdomain&quot;| API&#10;    API --&gt;|&quot;9. workers.dev subdomain&quot;| BACKEND&#10;    UI --&gt;|&quot;11. Show live preview and intended-user-only claim link&quot;| USER&#10;    USER --&gt;|&quot;12. Sign in and complete claim&quot;| DASHBOARD&#10;    DASHBOARD -.-&gt;|&quot;Optional after claim&quot;| OAUTH[&quot;Separate OAuth flow&lt;br/&gt;for future platform deployments&quot;]&#10;</code></pre>
<h3 id="request-a-challenge">Request a challenge</h3>
<p>Request a proof-of-work challenge before creating the temporary account:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/provisioning/previews/challenge&quot; \&#10;  &#45;X POST \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{}&#x27;&#10;</code></pre>
<p>The response includes the challenge token, seed, and difficulty parameters:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;result&quot;: {&#10;		&quot;challengeToken&quot;: &quot;&lt;CHALLENGE_TOKEN&gt;&quot;,&#10;		&quot;seed&quot;: &quot;&lt;BASE64URL_32_BYTE_SEED&gt;&quot;,&#10;		&quot;k&quot;: 8000,&#10;		&quot;g&quot;: 2000&#10;	},&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h3 id="solve-the-proof-of-work">Solve the proof of work</h3>
<p>Solve the challenge by computing a sequential SHA-256 checkpoint chain:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16233.md")
</div>
<p>Before solving a challenge, require <code>k</code> and <code>g</code> to be positive integers. Reject the challenge if <code>seed</code> does not decode to 32 bytes or if <code>k * g</code> exceeds <code>64,000,000</code>.</p>
<p>The following Node.js example applies these bounds and returns the object required by the create request:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16234.md")
</div>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="production-execution">Production execution</h3>
@markup("md", "content/.markup/bodies/16231.md")
</aside>
<h3 id="create-a-temporary-account">Create a temporary account</h3>
<p>Require the user to accept Cloudflare's <a href="https://www.cloudflare.com/terms/">Terms of Service</a> and <a href="https://www.cloudflare.com/privacypolicy/">Privacy Policy</a> before account creation. Set <code>acceptTermsOfService</code> to <code>&quot;yes&quot;</code> only after the user accepts both.</p>
<p>Then send the proof-of-work solution with the required policy fields:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/provisioning/previews&quot; \&#10;  &#45;X POST \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;termsOfService&quot;: &quot;https://www.cloudflare.com/terms/&quot;,&#10;    &quot;privacyPolicy&quot;: &quot;https://www.cloudflare.com/privacypolicy/&quot;,&#10;    &quot;acceptTermsOfService&quot;: &quot;yes&quot;,&#10;    &quot;challengeToken&quot;: &quot;&lt;CHALLENGE_TOKEN&gt;&quot;,&#10;    &quot;solution&quot;: {&#10;      &quot;checkpoints&quot;: &quot;&lt;BASE64_CHECKPOINTS&gt;&quot;&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>The response includes temporary credentials and a claim URL:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;result&quot;: {&#10;		&quot;account&quot;: {&#10;			&quot;id&quot;: &quot;&lt;TEMPORARY_ACCOUNT_ID&gt;&quot;,&#10;			&quot;name&quot;: &quot;&lt;TEMPORARY_ACCOUNT_NAME&gt;&quot;,&#10;			&quot;type&quot;: &quot;standard&quot;,&#10;			&quot;apiToken&quot;: &quot;&lt;TEMPORARY_ACCOUNT_API_TOKEN&gt;&quot;,&#10;			&quot;tokenId&quot;: &quot;&lt;TEMPORARY_TOKEN_ID&gt;&quot;,&#10;			&quot;expiresAt&quot;: &quot;&lt;ACCOUNT_EXPIRES_AT&gt;&quot;&#10;		},&#10;		&quot;claim&quot;: {&#10;			&quot;token&quot;: &quot;&lt;CLAIM_TOKEN&gt;&quot;,&#10;			&quot;url&quot;: &quot;https://dash.cloudflare.com/claim-preview?claimToken=&lt;CLAIM_TOKEN&gt;&quot;,&#10;			&quot;expiresAt&quot;: &quot;&lt;CLAIM_EXPIRES_AT&gt;&quot;&#10;		}&#10;	},&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>Before using the response, confirm that <code>success</code> is <code>true</code>. Verify that <code>account.id</code>, <code>account.apiToken</code>, <code>account.expiresAt</code>, <code>claim.url</code>, and <code>claim.expiresAt</code> are present.</p>
<h3 id="deploy-supported-resources">Deploy supported resources</h3>
<p>Use <code>account.id</code> and <code>account.apiToken</code> with supported Cloudflare API endpoints. Use temporary values only with supported resource operations.</p>
<p>Temporary account tokens do not grant every permanent-account API permission. Unsupported operations return an authorization error.</p>
<p>The following examples upload and deploy a Worker with the <a href="/api/resources/workers/subresources/scripts/methods/update/">Workers Script Upload API</a>, then retrieve the account's <code>workers.dev</code> subdomain.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16237.md")
</div></div>
<p>Provide the deployment URL and <code>claim.url</code> to the intended user.</p>
<h2 id="claim-the-account">Claim the account</h2>
<p>The intended user must complete the claim within 60 minutes. Opening the claim URL before the deadline is not enough.</p>
<p>They open the URL, sign in to Cloudflare or create an account, then complete the dashboard prompts.</p>
<p>If the user does not complete the claim, Cloudflare deletes the account and its resources.</p>
<p>With Wrangler, rerun <code>wrangler deploy --temporary</code> if the temporary credentials or claim URL expire. Wrangler provisions a new account and prints a new claim URL.</p>
<p>For REST integrations, request a new challenge and account if <code>account.expiresAt</code> or <code>claim.expiresAt</code> passes before the claim.</p>
<p>After the claim, the Worker and supported resources remain in the claimed account.</p>
<p>To continue with Wrangler, run <a href="/workers/wrangler/commands/general/#login"><code>wrangler login</code></a>, then deploy without <code>--temporary</code>. Claiming does not grant the platform permanent access to the account.</p>
<p>For later deployments, connect the claimed account through your normal authenticated flow, such as a <a href="/fundamentals/oauth/create-an-oauth-client/">Cloudflare OAuth client</a>.</p>
<h2 id="supported-resources">Supported resources</h2>
<p>The following table summarizes supported capabilities and limits. Temporary credentials do not grant every operation for these resources.</p>
<table>
<thead>
<tr>
<th>Supported product or resource</th>
<th>Supported capability or limit</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/workers/">Workers</a></td>
<td>Deployments on <code>workers.dev</code></td>
</tr>
<tr>
<td><a href="/workers/static-assets/">Workers Static Assets</a></td>
<td>Up to 1,000 files, with each asset up to 5 MiB</td>
</tr>
<tr>
<td><a href="/kv/">Workers KV</a></td>
<td>Create, list, rename, and delete namespaces; put, get, list, and delete keys; bulk put, get, and delete</td>
</tr>
<tr>
<td><a href="/d1/">D1</a></td>
<td>One database, with up to 100 MB per database and 100 MB total</td>
</tr>
<tr>
<td><a href="/durable-objects/">Durable Objects</a></td>
<td>Deploy Workers with Durable Object bindings and migrations</td>
</tr>
<tr>
<td><a href="/hyperdrive/">Hyperdrive</a></td>
<td>Up to two database configurations and 10 connections</td>
</tr>
<tr>
<td><a href="/queues/">Queues</a></td>
<td>Up to 10 queues</td>
</tr>
<tr>
<td><a href="/workers/wrangler/commands/certificates/">mTLS and CA certificates</a></td>
<td><code>wrangler cert</code> upload, list, and delete operations</td>
</tr>
</tbody>
</table>
<h2 id="security-and-limits">Security and limits</h2>
<h3 id="protect-temporary-values">Protect temporary values</h3>
<ul>
<li><code>account.apiToken</code> authorizes supported resource operations. Never expose it in browser responses or client-side code.</li>
<li>Treat <code>claim.url</code> like a bearer credential. Anyone with the URL can claim ownership of the temporary account.</li>
<li>Store both values only in backend storage or server-side session storage scoped to the intended user. Deliver <code>claim.url</code> only to that user.</li>
<li>Exclude both values from logs, analytics, and support telemetry. Delete stored copies when they are no longer needed and no later than either returned expiration time.</li>
</ul>
<h3 id="limits">Limits</h3>
<ul>
<li>Cloudflare requires a proof-of-work check before creating an account. Wrangler handles the check, while REST integrations must submit a solution.</li>
<li>Cloudflare rate limits temporary account creation. Wait before retrying, or authenticate with a permanent account.</li>
<li><code>--temporary</code> supports unauthenticated use only. Existing OAuth, API token, or global API key credentials cause an error.</li>
<li><code>--temporary</code> is not a global flag. Only commands that support temporary credentials include it.</li>
<li>Temporary account provisioning is available only through the default public API endpoint. It is unavailable through the FedRAMP High API endpoint.</li>
<li>Cloudflare may reject requests that fail additional abuse-prevention checks.</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<div class="nb-card nb-link-card"><h3 id="card-wrangler-deploy-workers-wrangler-commands-workers-deploy"><a href="/workers/wrangler/commands/workers/#deploy">wrangler deploy</a></h3><p>Review the full command reference for deploying Workers.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-prompting-workers-get-started-prompting"><a href="/workers/get-started/prompting/">Prompting</a></h3><p>Build Workers apps with AI prompts and MCP servers.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-deploy-an-existing-project-workers-framework-guides-automatic-configuration"><a href="/workers/framework-guides/automatic-configuration/">Deploy an existing project</a></h3><p>Learn how the Wrangler CLI automatically detects and configures projects for Workers.</p></div>

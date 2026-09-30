<h1 id="changelog">Changelog</h1>

<h2 id="manage-and-deploy-your-ai-provider-keys-through-bring-your-own-key-byok-with-ai-gateway-now-powered-by-cloudflare-secrets-store"><a href="/changelog/post/2025-08-25-secrets-store-ai-gateway/">Manage and deploy your AI provider keys through Bring Your Own Key (BYOK) with AI Gateway, now powered by Cloudflare Secrets Store</a></h2>
<p><em>2025-08-25T11:00:00+00:00</em></p>
<p>Cloudflare Secrets Store is now integrated with AI Gateway, allowing you to store, manage, and deploy your AI provider keys in a secure and seamless configuration through <a href="https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/">Bring Your Own Key</a>. Instead of passing your AI provider keys directly in every request header, you can centrally manage each key with Secrets Store and deploy in your gateway configuration using only a reference, rather than passing the value in plain text.</p>
<p>You can now create a secret directly from your AI Gateway <a href="http://dash.cloudflare.com/?to=/:account/ai-gateway">in the dashboard</a> by navigating into your gateway -&gt; <strong>Provider Keys</strong> -&gt; <strong>Add</strong>.</p>
<p><img src="/assets/upstream/images/ssl/add-secret-ai-gateway.png" alt="Import repo or choose template" /></p>
<p>You can also create your secret with the newly available <strong>ai_gateway</strong> scope via <a href="https://developers.cloudflare.com/workers/wrangler/commands/">wrangler</a>, the <a href="http://dash.cloudflare.com/?to=/:account/secrets-store">Secrets Store dashboard</a>, or the <a href="https://developers.cloudflare.com/api/resources/secrets_store/">API</a>.</p>
<p>Then, pass the key in the request header using its Secrets Store reference:</p>
<pre><code class="language-bash">curl -X POST https://gateway.ai.cloudflare.com/v1/&lt;ACCOUNT_ID&gt;/my-gateway/anthropic/v1/messages \&#10; &#45;-header &#x27;cf-aig-authorization: ANTHROPIC_KEY_1 \&#10; &#45;-header &#x27;anthropic-version: 2023-06-01&#x27; \&#10; &#45;-header &#x27;Content-Type: application/json&#x27; \&#10; &#45;-data  &#x27;{&quot;model&quot;: &quot;claude-3-opus-20240229&quot;, &quot;messages&quot;: [{&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;What is Cloudflare?&quot;}]}&#x27;&#10;</code></pre>
<p>Or, using Javascript:</p>
<pre><code>import Anthropic from &#x27;@anthropic-ai/sdk&#x27;;&#10;&#10;&#10;const anthropic = new Anthropic({&#10; apiKey: &quot;ANTHROPIC_KEY_1&quot;,&#10; baseURL: &quot;https://gateway.ai.cloudflare.com/v1/&lt;ACCOUNT_ID&gt;/my-gateway/anthropic&quot;,&#10;});&#10;&#10;&#10;const message = await anthropic.messages.create({&#10; model: &#x27;claude-3-opus-20240229&#x27;,&#10; messages: [{role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot;}],&#10; max_tokens: 1024&#10;});&#10;</code></pre>
<p>For more information, check out the <a href="https://blog.cloudflare.com/ai-gateway-aug-2025-refresh">blog</a>!</p>


<h2 id="deploy-to-cloudflare-buttons-now-support-worker-environment-variables-secrets-and-secrets-store-secrets"><a href="/changelog/post/2025-07-01-workers-deploy-button-supports-environment-variables-and-secrets/">Deploy to Cloudflare buttons now support Worker environment variables, secrets, and Secrets Store secrets</a></h2>
<p><em>2025-07-29T01:00:00+00:00</em></p>
<p>Any template which uses <a href="/workers/configuration/environment-variables/">Worker environment variables</a>, <a href="/workers/configuration/secrets/">secrets</a>, or <a href="/secrets-store/">Secrets Store secrets</a> can now be deployed using a <a href="/workers/platform/deploy-buttons/">Deploy to Cloudflare button</a>.</p>
<p>Define environment variables and secrets store bindings in your Wrangler configuration file as normal:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17781.md")</div>
<p>Add secrets to a <code>.dev.vars.example</code> or <code>.env.example</code> file:</p>
<pre><code class="language-ini">COOKIE_SIGNING_KEY=my-secret # comment&#10;</code></pre>
<p>And optionally, you can add a description for these bindings in your template's <code>package.json</code> to help users understand how to configure each value:</p>
<pre><code class="language-json">{&#10;	&quot;name&quot;: &quot;my-worker&quot;,&#10;	&quot;private&quot;: true,&#10;	&quot;cloudflare&quot;: {&#10;		&quot;bindings&quot;: {&#10;			&quot;API_KEY&quot;: {&#10;				&quot;description&quot;: &quot;Select your company&#x27;s API key for connecting to the example service.&quot;&#10;			},&#10;			&quot;COOKIE_SIGNING_KEY&quot;: {&#10;				&quot;description&quot;: &quot;Generate a random string using `openssl rand -hex 32`.&quot;&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>These secrets and environment variables will be presented to users in the dashboard as they deploy this template, allowing them to configure each value. Additional information about creating templates and Deploy to Cloudflare buttons can be found in <a href="/workers/platform/deploy-buttons/">our documentation</a>.</p>


<h2 id="increased-limits-for-cloudflare-for-saas-and-secrets-store-free-and-pay-as-you-go-plans"><a href="/changelog/post/2025-05-19-paygo-updates/">Increased limits for Cloudflare for SaaS and Secrets Store free and Pay-as-you-go plans</a></h2>
<p><em>2025-05-27T11:00:00+00:00</em></p>
<p>With upgraded limits to <a href="https://www.cloudflare.com/plans/">all free and paid plans</a>, you can now scale more easily with <a href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a> and <a href="https://developers.cloudflare.com/secrets-store/">Secrets Store</a>.</p>
<p><a href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a> allows you to extend the benefits of Cloudflare to your customers via their own custom or vanity domains. Now, the <a href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/plans/">limit for custom hostnames</a> on a Cloudflare for SaaS Pay-as-you-go plan has been <strong>raised from 5,000 custom hostnames to 50,000 custom hostnames.</strong></p>
<p>With custom origin server -- previously an enterprise-only feature -- you can route traffic from one or more custom hostnames somewhere other than your default proxy fallback. <a href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/custom-origin/">Custom origin server</a> is now available to Cloudflare for SaaS customers on Free, Pro, and Business plans.</p>
<p>You can enable custom origin server on a per-custom hostname basis <a href="https://developers.cloudflare.com/api/resources/custom_hostnames/methods/edit/">via the API</a> or the UI:</p>
<p><img src="/assets/upstream/images/ssl/custom-origin-server.png" alt="Import repo or choose template" /></p>
<p>Currently <a href="https://blog.cloudflare.com/secrets-store-beta/">in beta with a Workers integration</a>, <a href="https://developers.cloudflare.com/secrets-store/">Cloudflare Secrets Store</a> allows you to store, manage, and deploy account level secrets from a secure, centralized platform your <a href="https://developers.cloudflare.com/workers/">Cloudflare Workers</a>. Now, you can create and deploy <strong>100 secrets per account</strong>. Try it out <a href="http://dash.cloudflare.com/?to=/:account/secrets-store">in the dashboard</a>, with <a href="https://developers.cloudflare.com/secrets-store/integrations/workers/">Wrangler</a>, or <a href="https://developers.cloudflare.com/api/resources/secrets_store/">via the API</a> today.</p>


<h2 id="cloudflare-secrets-store-now-available-in-beta"><a href="/changelog/post/2025-04-09-secrets-store-beta/">Cloudflare Secrets Store now available in Beta</a></h2>
<p><em>2025-04-09</em></p>
<p>Cloudflare Secrets Store is available today in Beta. You can now store, manage, and deploy account level secrets from a secure, centralized platform to your Workers.</p>
<p><img src="/assets/upstream/images/ssl/secrets-store-landing-page.png" alt="Import repo or choose template" /></p>
<p>To spin up your Cloudflare Secrets Store, simply click the new Secrets Store tab <a href="http://dash.cloudflare.com/?to=/:account/secrets-store">in the dashboard</a> or use this Wrangler command:</p>
<pre><code class="language-sh">wrangler secrets-store store create &lt;name&gt; --remote&#10;</code></pre>
<p>The following are supported in the Secrets Store beta:</p>
<ul>
<li>Secrets Store UI &amp; API: create your store &amp; create, duplicate, update, scope, and delete a secret</li>
<li>Workers UI: bind a new or existing account level secret to a Worker and deploy in code</li>
<li>Wrangler: create your store &amp; create, duplicate, update, scope, and delete a secret</li>
<li>Account Management UI &amp; API: assign Secrets Store permissions roles &amp; view audit logs for actions taken in Secrets Store core platform</li>
</ul>
<p>For instructions on how to get started, visit our <a href="/secrets-store/">developer documentation</a>.</p>




<p>Protect your gateway with <a href="/cloudflare-one/access-controls/applications/http-apps/">Cloudflare Access</a> so users authenticate with your identity provider before they can send requests. Putting AI Gateway behind Access gives you identity-aware control over your AI traffic: you decide who can reach the gateway, tie each request to a verified user, and govern usage per user without building your own authentication layer or passing user IDs from the client application.</p>
<p>To put AI Gateway behind Access, you must first <a href="/ai-gateway/configuration/custom-domains/">set a custom domain</a> on your gateway and have <a href="/cloudflare-one/access-controls/applications/http-apps/">Cloudflare Access</a> enabled on your account.</p>
<h2 id="how-it-works">How it works</h2>
<p>When a request to a custom domain includes a valid Cloudflare Access JWT, AI Gateway accepts the Access JWT as the request credential. The client does not need to send an AI Gateway token for that request.</p>
<p>AI Gateway also adds the verified Access user ID to request metadata as <a href="/ai-gateway/observability/custom-metadata/#reserved-metadata"><code>cf.user_id</code></a>. This value is the Access JWT <code>sub</code> claim, not the user's email address. You can then filter logs, analytics, and spend by the authenticated user.</p>
<p>Before AI Gateway forwards the request to the upstream provider, it removes Cloudflare-only credentials such as the Access JWT and AI Gateway authorization headers.</p>
<p>Once a custom domain is protected by Access, every request to that domain must pass an Access policy. Requests that only include an AI Gateway token, without a valid Access token, are blocked by Access before they reach the gateway. Update existing integrations to authenticate through Access, or keep sending gateway-token traffic to the default <code>gateway.ai.cloudflare.com</code> endpoint, which is not protected by Access.</p>
<h2 id="set-up-access-on-a-gateway">Set up Access on a gateway</h2>
<ol>
<li><a href="/ai-gateway/configuration/custom-domains/">Set up a custom domain</a> for the gateway you want to protect.</li>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>AI</strong> &gt; <strong>AI Gateway</strong>.</li>
<li>Select the gateway you configured with a custom domain.</li>
<li>Go to the <strong>Access</strong> tab and set up Cloudflare Access on the gateway.</li>
<li>Add Access policies that define which users can call the gateway.</li>
</ol>
<p>Setting up Access from the <strong>Access</strong> tab configures the Access application for you, so coding agents and other non-browser clients can authenticate by sending the Access token as a bearer token.</p>
<p>After setup, users can make requests to the custom domain after authenticating through Access. Requests with a valid Access user subject include <code>cf.user_id</code> in AI Gateway metadata.</p>
<h2 id="make-a-request">Make a request</h2>
<p>After the user authenticates to Access, send requests to the custom domain without the account ID or gateway ID in the path:</p>
<pre><code class="language-bash">curl -X POST &quot;https://ai.example.com/openai/v1/chat/completions&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;gpt-4.1-mini&quot;,&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<p>If you call the custom domain from a non-browser client, include the Access token using the header or cookie format supported by Cloudflare Access. For example, <a href="/cloudflare-one/access-controls/authenticate-agents/#make-requests-with-cloudflared-access-curl"><code>cloudflared access curl</code></a> can send the Access token for command-line requests.</p>
<p>For coding agents, refer to the per-agent setup under <a href="/ai-gateway/integrations/coding-agents/">Coding agents</a> — for example, <a href="/ai-gateway/integrations/coding-agents/claude-code/#use-with-cloudflare-access">Claude Code</a> and <a href="/ai-gateway/integrations/coding-agents/openai-codex/#use-with-cloudflare-access">OpenAI Codex</a>.</p>
<h2 id="limitations">Limitations</h2>
<ul>
<li><code>cf.user_id</code> is only added when AI Gateway receives a valid Access JWT with a non-empty user subject.</li>
<li>Service-token requests do not include <code>cf.user_id</code> because they do not represent an individual Access user.</li>
<li>You may not supply metadata keys that begin with <code>cf.</code>. These keys are reserved and are not saved.</li>
</ul>

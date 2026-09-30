<h2 id="introduction">Introduction</h2>
<p>Bring your own keys (BYOK) is a feature in Cloudflare AI Gateway that allows you to securely store your AI provider API keys directly in the Cloudflare dashboard. Instead of including API keys in every request to your AI models, you can configure them once in the dashboard, and reference them in your gateway configuration.</p>
<p>The keys are stored securely with <a href="/secrets-store/">Secrets Store</a> and allows for:</p>
<ul>
<li>Secure storage and limit exposure</li>
<li>Easier key rotation</li>
<li>Rate limit, budget limit and other restrictions with <a href="/ai-gateway/features/dynamic-routing/">Dynamic Routes</a></li>
</ul>
<h2 id="setting-up-byok">Setting up BYOK</h2>
<h3 id="prerequisites">Prerequisites</h3>
<ul>
<li>Ensure your gateway is <a href="/ai-gateway/configuration/authentication/">authenticated</a>.</li>
<li>Ensure you have appropriate <a href="/secrets-store/access-control/">permissions</a> to create and deploy secrets on Secrets Store.</li>
</ul>
<h3 id="configure-api-keys">Configure API keys</h3>
<p>You can configure BYOK from the dashboard or by using the API.</p>
<h4 id="dashboard">Dashboard</h4>
<p>When you add a provider key from the dashboard, AI Gateway creates and names the Secrets Store secret automatically.</p>
<ol>
<li>Log into the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and select your account.</li>
<li>Go to <strong>AI</strong> &gt; <strong>AI Gateway</strong>.</li>
<li>Select your gateway or create a new one.</li>
<li>Go to the <strong>Provider Keys</strong> section.</li>
<li>Click <strong>Add API Key</strong>.</li>
<li>Select your AI provider from the dropdown.</li>
<li>Enter your API key and optionally provide a description.</li>
<li>Click <strong>Save</strong>.</li>
</ol>
<h4 id="api">API</h4>
<p>If you use the API to configure BYOK, create the Secrets Store secret before you create the provider configuration. Name the secret with this format:</p>
<pre><code class="language-txt">{gateway_id}_{provider_slug}_{alias}&#10;</code></pre>
<p>For example, for gateway <code>my-gateway</code>, provider <code>anthropic</code>, and alias <code>default</code>, create the Secrets Store secret as:</p>
<pre><code class="language-txt">my-gateway_anthropic_default&#10;</code></pre>
<p>Then create the provider configuration with the same <code>provider_slug</code> and <code>alias</code> values.</p>
<p>The <code>secret_id</code> returned by Secrets Store is not used by AI Gateway for runtime lookup, so API-created secrets must follow the naming convention.</p>
<h3 id="update-your-applications">Update your applications</h3>
<p>Once you've configured your API keys in the dashboard:</p>
<ol>
<li><strong>Remove API keys from your code</strong>: Delete any hardcoded API keys or environment variables.</li>
<li><strong>Update request headers</strong>: Remove provider authorization headers from your requests. Note that you still need to pass <code>cf-aig-authorization</code>.</li>
<li><strong>Test your integration</strong>: Verify that requests work without including API keys.</li>
</ol>
<h2 id="example">Example</h2>
<p>With BYOK enabled, your workflow changes from:</p>
<ol>
<li><strong>Traditional approach</strong>: Include API key in every request header</li>
</ol>
<pre><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/chat/completions \&#10;  &#45;H &#x27;cf-aig-authorization: Bearer {CF_AIG_TOKEN}&#x27; \&#10;  &#45;H &quot;Authorization: Bearer YOUR_OPENAI_API_KEY&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&quot;model&quot;: &quot;gpt-4&quot;, &quot;messages&quot;: [...]}&#x27;&#10;</code></pre>
<ol start="2">
<li><strong>BYOK approach</strong>: Configure key once in dashboard, make requests without exposing keys</li>
</ol>
<pre><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/chat/completions \&#10;  &#45;H &#x27;cf-aig-authorization: Bearer {CF_AIG_TOKEN}&#x27; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&quot;model&quot;: &quot;gpt-4&quot;, &quot;messages&quot;: [...]}&#x27;&#10;</code></pre>
<h2 id="managing-api-keys">Managing API keys</h2>
<h3 id="viewing-configured-keys">Viewing configured keys</h3>
<p>In the AI Gateway dashboard, you can:</p>
<ul>
<li>View all configured API keys by provider</li>
<li>See when each key was last used</li>
<li>Check the status of each key (active, expired, invalid)</li>
</ul>
<h3 id="rotating-keys">Rotating keys</h3>
<p>To rotate an API key:</p>
<ol>
<li>Generate a new API key from your AI provider</li>
<li>In the Cloudflare dashboard, edit the existing key entry</li>
<li>Replace the old key with the new one</li>
<li>Save the changes</li>
</ol>
<p>Your applications will immediately start using the new key without any code changes or downtime.</p>
<h3 id="revoking-access">Revoking access</h3>
<p>To remove an API key:</p>
<ol>
<li>In the AI Gateway dashboard, find the key you want to remove</li>
<li>Click the <strong>Delete</strong> button</li>
<li>Confirm the deletion</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="impact-of-key-deletion">Impact of key deletion</h3>
@markup("md", "content/.markup/bodies/2887.md")
</aside>
<h2 id="multiple-keys-per-provider">Multiple keys per provider</h2>
<p>AI Gateway supports storing multiple API keys for the same provider. This allows you to:</p>
<ul>
<li>Use different keys for different use cases (for example, development vs production)</li>
<li>Gradually migrate between keys during rotation</li>
</ul>
<h3 id="key-aliases">Key aliases</h3>
<p>Each API key can be assigned an alias to identify it. When you add a key, you can specify a custom alias, or the system will use <code>default</code> as the alias.</p>
<p>When making requests, AI Gateway uses the key with the <code>default</code> alias by default. To use a different key, include the <code>cf-aig-byok-alias</code> header with the alias of the key you want to use.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2886.md")
</aside>
<h3 id="example-using-a-specific-key-alias">Example: Using a specific key alias</h3>
<p>If you have multiple OpenAI keys configured with different aliases (for example, <code>default</code>, <code>production</code>, and <code>testing</code>), you can specify which one to use:</p>
<pre><code class="language-bash">&#35; Uses the key with alias &quot;default&quot; (no header needed)&#10;curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/chat/completions \&#10;  &#45;H &#x27;cf-aig-authorization: Bearer {CF_AIG_TOKEN}&#x27; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&quot;model&quot;: &quot;gpt-4&quot;, &quot;messages&quot;: [...]}&#x27;&#10;</code></pre>
<pre><code class="language-bash">&#35; Uses the key with alias &quot;production&quot;&#10;curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/chat/completions \&#10;  &#45;H &#x27;cf-aig-authorization: Bearer {CF_AIG_TOKEN}&#x27; \&#10;  &#45;H &#x27;cf-aig-byok-alias: production&#x27; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&quot;model&quot;: &quot;gpt-4&quot;, &quot;messages&quot;: [...]}&#x27;&#10;</code></pre>
<pre><code class="language-bash">&#35; Uses the key with alias &quot;testing&quot;&#10;curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/chat/completions \&#10;  &#45;H &#x27;cf-aig-authorization: Bearer {CF_AIG_TOKEN}&#x27; \&#10;  &#45;H &#x27;cf-aig-byok-alias: testing&#x27; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&quot;model&quot;: &quot;gpt-4&quot;, &quot;messages&quot;: [...]}&#x27;&#10;</code></pre>

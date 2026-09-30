<p>This page covers common issues when using AI Gateway. For provider-specific troubleshooting, refer to the relevant provider documentation.</p>
<h2 id="authentication-errors">Authentication errors</h2>
<h3 id="401-or-unauthenticated-errors">401 or unauthenticated errors</h3>
<p>If you receive authentication errors from your AI provider, AI Gateway did not pass valid credentials upstream. Check the following:</p>
<ol>
<li>
<p><strong>Verify header placement</strong>: Make sure your Cloudflare token is in <code>cf-aig-authorization</code>, not <code>Authorization</code>. The <code>Authorization</code> header is reserved for provider credentials.</p>
</li>
<li>
<p><strong>Check your configuration based on endpoint type</strong>:</p>
<ul>
<li><strong>Provider-specific endpoints</strong>: Confirm your request URL includes the provider path (for example, <code>/google-vertex-ai/</code> or <code>/openai/</code>). AI Gateway uses this to identify the provider and apply the correct stored credentials.</li>
<li><strong>Unified <code>/compat/chat/completions</code> endpoint</strong>: Confirm your <code>model</code> name starts with the provider prefix (for example, <code>google-vertex-ai/google/gemini-2.5-flash</code> or <code>openai/gpt-4o</code>). AI Gateway uses this prefix to route the request and select the correct stored credentials.</li>
</ul>
</li>
<li>
<p><strong>Verify BYOK key selection</strong>: If you have multiple keys configured for a provider, ensure either:</p>
<ul>
<li>You are using the key with alias <code>default</code>, or</li>
<li>You include the <code>cf-aig-byok-alias</code> header with the correct alias name</li>
</ul>
</li>
<li>
<p><strong>Verify BYOK configuration</strong>: If using BYOK, confirm in the dashboard that your credentials were saved correctly.</p>
</li>
</ol>
<p>For provider-specific authentication issues:</p>
<ul>
<li><a href="/ai-gateway/usage/providers/vertex/#troubleshooting">Google Vertex AI troubleshooting</a></li>
</ul>
<h2 id="dlp-issues">DLP issues</h2>
<p>For troubleshooting Data Loss Prevention issues such as DLP not triggering or unexpected blocking, refer to <a href="/ai-gateway/features/dlp/set-up-dlp/#troubleshooting">DLP troubleshooting</a>.</p>
<h2 id="request-failures">Request failures</h2>
<h3 id="requests-timing-out">Requests timing out</h3>
<ul>
<li>Check if the upstream provider is experiencing issues</li>
<li>Consider implementing <a href="/ai-gateway/features/dynamic-routing/">dynamic routing</a> with fallbacks for transient failures</li>
<li>Review your <a href="/ai-gateway/features/rate-limiting/">rate limiting</a> configuration</li>
</ul>
<h3 id="requests-returning-errors-from-the-provider">Requests returning errors from the provider</h3>
<ul>
<li>Verify your API key or credentials are valid with the provider directly</li>
<li>Check the provider's status page for outages</li>
<li>Review <a href="/ai-gateway/observability/logging/">AI Gateway logs</a> for detailed error information</li>
</ul>
<h2 id="caching-issues">Caching issues</h2>
<h3 id="requests-not-being-cached">Requests not being cached</h3>
<ul>
<li>Verify <a href="/ai-gateway/features/caching/">caching is enabled</a> for your gateway</li>
<li>Check that the request method and content type are cacheable</li>
<li>Streaming responses are not cached by default</li>
</ul>
<h3 id="unexpected-cache-hits-or-misses">Unexpected cache hits or misses</h3>
<ul>
<li>Review your cache TTL settings</li>
<li>Check if you have request headers that are <a href="/ai-gateway/features/caching/#skip-cache-cf-aig-skip-cache">bypassing the cache</a> or setting a <a href="/ai-gateway/features/caching/#custom-cache-key-cf-aig-cache-key">custom cache key</a>.</li>
</ul>

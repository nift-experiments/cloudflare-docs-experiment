<p><a href="https://cloud.google.com/vertex-ai">Google Vertex AI</a> enables developers to easily build and deploy enterprise ready generative AI experiences.</p>
<p>Below is a quick guide on how to set your Google Cloud Account:</p>
<ol>
<li>
<p>Google Cloud Platform (GCP) Account</p>
<ul>
<li>Sign up for a <a href="https://cloud.google.com/vertex-ai">GCP account</a>. New users may be eligible for credits (valid for 90 days).</li>
</ul>
</li>
<li>
<p>Enable the Vertex AI API</p>
<ul>
<li>Go to <a href="https://console.cloud.google.com/marketplace/product/google/aiplatform.googleapis.com">Enable Vertex AI API</a> and activate the API for your project.</li>
</ul>
</li>
<li>
<p>Apply for access to desired models.</p>
</li>
</ol>
<h2 id="endpoint">Endpoint</h2>
<pre><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/google-vertex-ai&#10;</code></pre>
<h2 id="prerequisites">Prerequisites</h2>
<p>When making requests to Google Vertex AI, you will need:</p>
<ul>
<li>AI Gateway account tag</li>
<li>AI Gateway gateway name</li>
<li>Google Vertex AI credentials (service account JSON or access token)</li>
<li>Google Vertex AI Project Name</li>
<li>Google Vertex AI Region (for example, <code>us-central1</code>)</li>
<li>Google Vertex AI model</li>
</ul>
<h2 id="url-structure">URL structure</h2>
<p>Your new base URL will use the data above in this structure: <code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/google-vertex-ai/v1/projects/{project_name}/locations/{region}</code>.</p>
<p>Then you can append the endpoint you want to hit, for example: <code>/publishers/google/models/{model}:{generative_ai_rest_resource}</code></p>
<p>So your final URL will come together as: <code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/google-vertex-ai/v1/projects/{project_name}/locations/{region}/publishers/google/models/gemini-2.5-flash:generateContent</code></p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="use-a-specific-region">Use a specific region</h3>
@markup("md", "content/.markup/bodies/2954.md")
</aside>
<h2 id="authenticating-with-vertex-ai">Authenticating with Vertex AI</h2>
<p>Authenticating with Vertex AI normally requires generating short-term credentials using the <a href="https://cloud.google.com/vertex-ai/docs/authentication">Google Cloud SDKs</a> with a complicated setup, but AI Gateway simplifies this for you with multiple options.</p>
<h3 id="authentication-methods-comparison">Authentication methods comparison</h3>
<table>
<thead>
<tr>
<th>Method</th>
<th><code>cf-aig-authorization</code> header</th>
<th><code>Authorization</code> header</th>
<th>Region handling</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>BYOK (Recommended)</strong></td>
<td><code>Bearer {CF_AIG_TOKEN}</code></td>
<td>Not needed</td>
<td>Select in dashboard dropdown</td>
</tr>
<tr>
<td><strong>Service account JSON in header</strong></td>
<td><code>Bearer {CF_AIG_TOKEN}</code></td>
<td>Base64-encoded JSON with <code>region</code> key</td>
<td>Include <code>region</code> key in JSON</td>
</tr>
<tr>
<td><strong>Direct access token</strong></td>
<td><code>Bearer {CF_AIG_TOKEN}</code></td>
<td><code>Bearer {gcloud_access_token}</code></td>
<td>Included in URL path</td>
</tr>
</tbody>
</table>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="do-not-confuse-the-headers">Do not confuse the headers</h3>
@markup("md", "content/.markup/bodies/2953.md")
</aside>
<h3 id="option-1-byok-recommended">Option 1: BYOK (Recommended)</h3>
<p>The recommended approach is to store your Google service account credentials using AI Gateway's <a href="/ai-gateway/configuration/bring-your-own-keys/">Bring Your Own Keys (BYOK)</a> feature. This keeps your credentials secure and out of your application code.</p>
<ol>
<li><a href="https://cloud.google.com/iam/docs/keys-create-delete">Create a service account key</a> in the Google Cloud Console. Ensure that the service account has the required permissions for the Vertex AI endpoints and models you plan to use.</li>
<li>In the Cloudflare dashboard, go to <strong>AI</strong> &gt; <strong>AI Gateway</strong> &gt; your gateway &gt; <strong>Provider Keys</strong>.</li>
<li>Select <strong>Add API Key</strong> and choose <strong>Google Vertex AI</strong> as the provider.</li>
<li>Paste your service account JSON and select your region from the dropdown. AI Gateway automatically applies this selected region to your stored credentials, so you do not need to manually add a <code>region</code> field to the JSON.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>With BYOK configured, you only need to include the <code>cf-aig-authorization</code> header in your requests. AI Gateway handles the Vertex AI authentication automatically.</p>
<pre><code class="language-bash">curl &quot;https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/google-vertex-ai/v1/projects/{project_name}/locations/{region}/publishers/google/models/gemini-2.5-flash:generateContent&quot; \&#10;    &#45;H &#x27;cf-aig-authorization: Bearer {CF_AIG_TOKEN}&#x27; \&#10;    &#45;H &#x27;Content-Type: application/json&#x27; \&#10;    &#45;d &#x27;{&#10;        &quot;contents&quot;: [&#10;          {&#10;            &quot;role&quot;: &quot;user&quot;,&#10;            &quot;parts&quot;: [&#10;              {&#10;                &quot;text&quot;: &quot;Tell me more about Cloudflare&quot;&#10;              }&#10;            ]&#10;          }&#10;        ]&#10;      }&#x27;&#10;</code></pre>
<h3 id="option-2-service-account-json-in-header">Option 2: Service Account JSON in Header</h3>
<p>You can pass a Google service account JSON directly in the <code>Authorization</code> header on each request with a base64-encoded version of the JSON. This option is useful for testing or when you cannot use BYOK.</p>
<p><a href="https://cloud.google.com/iam/docs/keys-create-delete">Create a service account key</a> in the Google Cloud Console. Ensure that the service account has the required permissions for the Vertex AI endpoints and models you plan to use.</p>
<p>AI Gateway uses your service account JSON to generate short-term access tokens which are cached and used for consecutive requests, and are automatically refreshed when they expire.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2952.md")
</aside>
<h4 id="example-service-account-json-structure">Example service account JSON structure</h4>
<pre><code class="language-json">{&#10;	&quot;type&quot;: &quot;service_account&quot;,&#10;	&quot;project_id&quot;: &quot;your-project-id&quot;,&#10;	&quot;private_key_id&quot;: &quot;your-private-key-id&quot;,&#10;	&quot;private_key&quot;: &quot;-----BEGIN PRIVATE KEY-----\nYOUR_PRIVATE_KEY\n-----END PRIVATE KEY-----\n&quot;,&#10;	&quot;client_email&quot;: &quot;your-service-account@your-project.iam.gserviceaccount.com&quot;,&#10;	&quot;client_id&quot;: &quot;your-client-id&quot;,&#10;	&quot;auth_uri&quot;: &quot;https://accounts.google.com/o/oauth2/auth&quot;,&#10;	&quot;token_uri&quot;: &quot;https://oauth2.googleapis.com/token&quot;,&#10;	&quot;auth_provider_x509_cert_url&quot;: &quot;https://www.googleapis.com/oauth2/v1/certs&quot;,&#10;	&quot;client_x509_cert_url&quot;: &quot;https://www.googleapis.com/robot/v1/metadata/x509/your-service-account%40your-project.iam.gserviceaccount.com&quot;,&#10;	&quot;region&quot;: &quot;us-central1&quot;&#10;}&#10;</code></pre>
<h3 id="option-3-direct-access-token">Option 3: Direct Access Token</h3>
<p>If you are already using the Google Cloud SDKs and generating a short-term access token (for example, with <code>gcloud auth print-access-token</code>), you can directly pass this as a Bearer token in the <code>Authorization</code> header of the request.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2951.md")
</aside>
<pre><code class="language-bash">curl &quot;https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/google-vertex-ai/v1/projects/{project_name}/locations/{region}/publishers/google/models/gemini-2.5-flash:generateContent&quot; \&#10;    &#45;H &#x27;cf-aig-authorization: Bearer {CF_AIG_TOKEN}&#x27; \&#10;    &#45;H &quot;Authorization: Bearer ya29.c.b0Aaekm1K...&quot; \&#10;    &#45;H &#x27;Content-Type: application/json&#x27; \&#10;    &#45;d &#x27;{&#10;        &quot;contents&quot;: [&#10;          {&#10;            &quot;role&quot;: &quot;user&quot;,&#10;            &quot;parts&quot;: [&#10;              {&#10;                &quot;text&quot;: &quot;Tell me more about Cloudflare&quot;&#10;              }&#10;            ]&#10;          }&#10;        ]&#10;      }&#x27;&#10;</code></pre>
<h2 id="using-unified-chat-completions-api">Using Unified Chat Completions API</h2>
<p>AI Gateway provides a <a href="/ai-gateway/usage/chat-completion/">Unified API</a> that works across providers. For Google Vertex AI, you can use the standard chat completions format. Note that the model field includes the provider prefix, so your model string will look like <code>google-vertex-ai/google/gemini-2.5-pro</code>.</p>
<h3 id="endpoint-1">Endpoint</h3>
<pre><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat/chat/completions&#10;</code></pre>
<h3 id="example-with-byok">Example with BYOK</h3>
<p>With BYOK configured, you only need to include the <code>cf-aig-authorization</code> header:</p>
<pre><code class="language-bash">curl &quot;https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat/chat/completions&quot; \&#10;    &#45;H &#x27;cf-aig-authorization: Bearer {CF_AIG_TOKEN}&#x27; \&#10;    &#45;H &#x27;Content-Type: application/json&#x27; \&#10;    &#45;d &#x27;{&#10;        &quot;model&quot;: &quot;google-vertex-ai/google/gemini-2.5-pro&quot;,&#10;        &quot;messages&quot;: [&#10;          {&#10;            &quot;role&quot;: &quot;user&quot;,&#10;            &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;          }&#10;        ]&#10;      }&#x27;&#10;</code></pre>
<h3 id="example-with-openai-sdk">Example with OpenAI SDK</h3>
<p>If not using BYOK, pass the base64-encoded service account JSON (with <code>region</code> key included) as the API key:</p>
<pre><code class="language-javascript">import OpenAI from &quot;openai&quot;;&#10;&#10;// Service account JSON must include &quot;region&quot; key when not using BYOK&#10;const serviceAccountJson = JSON.stringify({&#10;	type: &quot;service_account&quot;,&#10;	project_id: &quot;your-project-id&quot;,&#10;	// ... other fields from your downloaded JSON&#10;	region: &quot;us-central1&quot;, // Required: add this to your service account JSON&#10;});&#10;&#10;const client = new OpenAI({&#10;	apiKey: Buffer.from(serviceAccountJson).toString(&quot;base64&quot;),&#10;	baseURL:&#10;		&quot;https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat&quot;,&#10;	defaultHeaders: {&#10;		&quot;cf-aig-authorization&quot;: `Bearer {cf_aig_token}`,&#10;	},&#10;});&#10;&#10;const response = await client.chat.completions.create({&#10;	model: &quot;google-vertex-ai/google/gemini-2.5-pro&quot;,&#10;	messages: [&#10;		{&#10;			role: &quot;user&quot;,&#10;			content: &quot;What is Cloudflare?&quot;,&#10;		},&#10;	],&#10;});&#10;&#10;console.log(response.choices[0].message.content);&#10;</code></pre>
<h3 id="example-with-curl">Example with cURL</h3>
<pre><code class="language-bash">&#35; First, base64-encode your service account JSON (must include &quot;region&quot; key)&#10;SERVICE_ACCOUNT_BASE64=$(base64 &lt; service-account.json | tr -d &#x27;\n&#x27;)&#10;&#10;curl &quot;https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat/chat/completions&quot; \&#10;    &#45;H &#x27;cf-aig-authorization: Bearer {CF_AIG_TOKEN}&#x27; \&#10;    &#45;H &quot;Authorization: Bearer $SERVICE_ACCOUNT_BASE64&quot; \&#10;    &#45;H &#x27;Content-Type: application/json&#x27; \&#10;    &#45;d &#x27;{&#10;        &quot;model&quot;: &quot;google-vertex-ai/google/gemini-2.5-pro&quot;,&#10;        &quot;messages&quot;: [&#10;          {&#10;            &quot;role&quot;: &quot;user&quot;,&#10;            &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;          }&#10;        ]&#10;      }&#x27;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2950.md")
</aside>
<h2 id="using-provider-specific-endpoint">Using Provider-Specific Endpoint</h2>
<p>You can also use the provider-specific endpoint to access the full Vertex AI API.</p>
<h3 id="curl-with-byok">cURL with BYOK</h3>
<p>With BYOK configured, you only need the <code>cf-aig-authorization</code> header:</p>
<pre><code class="language-bash">curl &quot;https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/google-vertex-ai/v1/projects/{project_name}/locations/{region}/publishers/google/models/gemini-2.5-flash:generateContent&quot; \&#10;    &#45;H &#x27;cf-aig-authorization: Bearer {CF_AIG_TOKEN}&#x27; \&#10;    &#45;H &#x27;Content-Type: application/json&#x27; \&#10;    &#45;d &#x27;{&#10;        &quot;contents&quot;: [&#10;          {&#10;            &quot;role&quot;: &quot;user&quot;,&#10;            &quot;parts&quot;: [&#10;              {&#10;                &quot;text&quot;: &quot;Tell me more about Cloudflare&quot;&#10;              }&#10;            ]&#10;          }&#10;        ]&#10;      }&#x27;&#10;</code></pre>
<h3 id="curl-with-service-account-json">cURL with Service Account JSON</h3>
<p>If not using BYOK, pass the base64-encoded service account JSON (with <code>region</code> key included) in the Authorization header:</p>
<pre><code class="language-bash">&#35; First, base64-encode your service account JSON (must include &quot;region&quot; key) as a single line&#10;SERVICE_ACCOUNT_BASE64=$(base64 &lt; service-account.json | tr -d &#x27;\n&#x27;)&#10;&#10;curl &quot;https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/google-vertex-ai/v1/projects/{project_name}/locations/{region}/publishers/google/models/gemini-2.5-flash:generateContent&quot; \&#10;    &#45;H &#x27;cf-aig-authorization: Bearer {CF_AIG_TOKEN}&#x27; \&#10;    &#45;H &quot;Authorization: Bearer $SERVICE_ACCOUNT_BASE64&quot; \&#10;    &#45;H &#x27;Content-Type: application/json&#x27; \&#10;    &#45;d &#x27;{&#10;        &quot;contents&quot;: [&#10;          {&#10;            &quot;role&quot;: &quot;user&quot;,&#10;            &quot;parts&quot;: [&#10;              {&#10;                &quot;text&quot;: &quot;Tell me more about Cloudflare&quot;&#10;              }&#10;            ]&#10;          }&#10;        ]&#10;      }&#x27;&#10;</code></pre>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>For general AI Gateway troubleshooting, refer to <a href="/ai-gateway/reference/troubleshooting/">Troubleshooting</a>.</p>
<h3 id="401-unauthenticated-errors">401 Unauthenticated errors</h3>
<p>If you receive a <code>CREDENTIALS_MISSING</code> or <code>UNAUTHENTICATED</code> error from Google, check the following Vertex AI-specific issues:</p>
<ol>
<li>
<p><strong>Check your region</strong>: Use a specific regional endpoint (like <code>us-central1</code>) in your URL, not <code>global</code>. The <code>global</code> endpoint has limited model support.</p>
</li>
<li>
<p><strong>Verify BYOK configuration</strong>: If using BYOK, confirm in the dashboard that:</p>
<ul>
<li>Your service account JSON was saved correctly</li>
<li>A region was selected from the dropdown</li>
</ul>
</li>
<li>
<p><strong>Check service account permissions</strong>: Ensure your service account has the <code>Vertex AI User</code> role or equivalent permissions in Google Cloud.</p>
</li>
<li>
<p><strong>Verify the region key</strong> (non-BYOK only): If passing service account JSON directly in the <code>Authorization</code> header, make sure the JSON includes the <code>region</code> key.</p>
</li>
</ol>

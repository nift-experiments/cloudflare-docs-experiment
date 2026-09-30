---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/tutorials/ai-wrapper-tenant-control/
  description: This tutorial explains how to use Cloudflare AI Gateway and Zero Trust to create a functional and secure website wrapper for an AI agent.
  full_title: Create and secure an AI agent wrapper using AI Gateway and Zero Trust · Cloudflare One docs
  head_html: <title>Create and secure an AI agent wrapper using AI Gateway and Zero Trust · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="This tutorial explains how to use Cloudflare AI Gateway and Zero Trust to create a functional and secure website wrapper for an AI agent."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/tutorials/ai-wrapper-tenant-control/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/tutorials/ai-wrapper-tenant-control/index.md"><meta property="og:title" content="Create and secure an AI agent wrapper using AI Gateway and Zero Trust · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This tutorial explains how to use Cloudflare AI Gateway and Zero Trust to create a functional and secure website wrapper for an AI agent."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/tutorials/ai-wrapper-tenant-control/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/tutorials/ai-wrapper-tenant-control/#page","headline":"Create and secure an AI agent wrapper using AI Gateway and Zero Trust \u00b7 Cloudflare One docs","description":"This tutorial explains how to use Cloudflare AI Gateway and Zero Trust to create a functional and secure website wrapper for an AI agent.","url":"https://developers.cloudflare.com/cloudflare-one/tutorials/ai-wrapper-tenant-control/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/tutorials/ai-wrapper-tenant-control/
  schema: 1
---
<p>This tutorial explains how to use <a href="/ai-gateway/">Cloudflare AI Gateway</a> and Zero Trust to create a functional and secure website wrapper for an AI agent. Cloudflare Zero Trust administrators can protect access to the wrapper with <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a>. Additionally, you can enforce <a href="/cloudflare-one/traffic-policies/">Gateway policies</a> to control how your users interact with AI agents, including executing AI agents in an isolated browser with <a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a>, enforcing <a href="/cloudflare-one/data-loss-prevention/">Data Loss Prevention</a> profiles to prevent your users from sharing sensitive data, and scanning content to avoid answers from AI agents that violate internal corporate guidelines. Creating an AI agent wrapper is also an effective way to enforce tenant control if you have an enterprise plan for a specific AI provider, such as ChatGPT Enterprise.</p>
<p>This tutorial uses ChatGPT as an example AI agent.</p>
<h2 id="before-you-begin">Before you begin</h2>
<p>Make sure you have:</p>
<ul>
<li>A <a href="/cloudflare-one/setup/">Cloudflare Zero Trust organization</a>.</li>
<li>An API key for your desired AI provider, such as an <a href="https://platform.openai.com/api-keys">OpenAI API key</a> for ChatGPT.</li>
</ul>
<h2 id="1-create-an-ai-gateway"><ol>
<li>Create an AI gateway</li>
</ol></h2>
<p>First, create an AI gateway to control your AI app.</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to the <strong>AI Gateway</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create Gateway</strong>.</li>
<li>Name your gateway.</li>
<li>Select <strong>Create</strong>.</li>
<li>Configure your desired options for the gateway.</li>
<li><a href="/ai-gateway/get-started/#connect-application">Connect your AI provider</a> to proxy queries to your AI agent of choice using your AI gateway.</li>
<li>(Optional) Turn on <a href="/ai-gateway/configuration/authentication/">Authenticated Gateway</a>. The Authenticated Gateway feature ensures your AI gateway can only be called securely by enforcing a token in the form of a request header <code>cf-aig-authorization</code>.
<ol>
<li>Go to <strong>AI</strong> &gt; <strong>AI Gateway</strong>.</li>
<li>Select your AI gateway, then go to <strong>Settings</strong>.</li>
<li>Turn on <strong>Authenticated Gateway</strong>, then choose <strong>Confirm</strong>.</li>
<li>Select <strong>Create authentication token</strong>, then select <strong>Create an AI Gateway authentication token</strong>.</li>
<li>Configure your token and copy the token value. When creating your Worker, you will need to pass this token when calling your AI gateway.</li>
</ol>
</li>
</ol>
<p>For more information, refer to <a href="/ai-gateway/get-started/">Getting started with AI Gateway</a>.</p>
<h2 id="2-optional-use-guardrails-to-block-unsafe-or-inappropriate-content"><ol start="2">
<li>(Optional) Use Guardrails to block unsafe or inappropriate content</li>
</ol></h2>
<p><a href="/ai-gateway/features/guardrails/">Guardrails</a> is an built-in AI Gateway security feature that allows Cloudflare to identify unsafe or inappropriate content in prompts and responses based on selected categories.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>AI Gateway</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your AI gateway.</li>
<li>Go to <strong>Guardrails</strong>.</li>
<li>Turn on Guardrails.</li>
<li>Select <strong>Change</strong> to configure the categories you would like to filter for both prompts and responses.</li>
</ol>
<h2 id="3-build-a-worker-to-serve-the-wrapper"><ol start="3">
<li>Build a Worker to serve the wrapper</li>
</ol></h2>
<h3 id="1-create-the-worker"><ol>
<li>Create the Worker</li>
</ol></h3>
<p>In order to build the Worker, you will need to choose if you want to build it locally using <a href="/workers/wrangler/install-and-update/">Wrangler</a> or remotely using the <a href="https://dash.cloudflare.com/">dashboard</a>.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4328.md")
</div></div>
<h3 id="2-build-the-worker"><ol start="2">
<li>Build the Worker</li>
</ol></h3>
<p>The following is an example starter Worker that serves a simple front-end to allow a user to interact with an AI provider behind AI Gateway. This example uses OpenAI as its AI provider:</p>
<pre tabindex="0"><code class="language-javascript">export default {&#10;	async fetch(request, env) {&#10;		if (request.url.endsWith(&quot;/api/chat&quot;)) {&#10;			if (request.method === &quot;POST&quot;) {&#10;				try {&#10;					const { messages } = await request.json();&#10;&#10;					const response = await fetch(&#10;						&quot;https://gateway.ai.cloudflare.com/v1/$ACCOUNT_ID/$GATEWAY_ID/openai/chat/completions&quot;,&#10;						{&#10;							method: &quot;POST&quot;,&#10;							headers: {&#10;								&quot;Content-Type&quot;: &quot;application/json&quot;,&#10;								Authorization: `Bearer ${env.OPENAI_API_KEY}`,&#10;							},&#10;							body: JSON.stringify({&#10;								model: &quot;gpt-4o-mini&quot;,&#10;								messages: messages,&#10;							}),&#10;						},&#10;					);&#10;&#10;					if (!response.ok) {&#10;						throw new Error(`AI Gateway Error: ${response.status}`);&#10;					}&#10;&#10;					const result = await response.json();&#10;					return new Response(&#10;						JSON.stringify({&#10;							response: result.choices[0].message.content,&#10;						}),&#10;						{&#10;							headers: { &quot;Content-Type&quot;: &quot;application/json&quot; },&#10;						},&#10;					);&#10;				} catch (error) {&#10;					return new Response(JSON.stringify({ error: error.message }), {&#10;						status: 500,&#10;						headers: { &quot;Content-Type&quot;: &quot;application/json&quot; },&#10;					});&#10;				}&#10;			}&#10;			return new Response(&quot;Method not allowed&quot;, { status: 405 });&#10;		}&#10;&#10;		return new Response(HTML, {&#10;			headers: { &quot;Content-Type&quot;: &quot;text/html&quot; },&#10;		});&#10;	},&#10;};&#10;&#10;const HTML = `&lt;!DOCTYPE html&gt;&#10;  &lt;html lang=&quot;en&quot; data-theme=&quot;dark&quot;&gt;&#10;  &lt;head&gt;&#10;      &lt;meta charset=&quot;UTF-8&quot;&gt;&#10;      &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;&#10;      &lt;title&gt;ChatGPT Wrapper&lt;/title&gt;&#10;      &lt;style&gt;&#10;          :root {&#10;              &#45;-background-color: #1a1a1a;&#10;              &#45;-chat-background: #2d2d2d;&#10;              &#45;-text-color: #ffffff;&#10;              &#45;-input-border: #404040;&#10;              &#45;-message-ai-background: #404040;&#10;              &#45;-message-ai-text: #ffffff;&#10;          }&#10;&#10;          body {&#10;              font-family: system-ui, sans-serif;&#10;              margin: 0;&#10;              padding: 20px;&#10;              background: var(--background-color);&#10;              display: flex;&#10;              flex-direction: column;&#10;              align-items: center;&#10;              gap: 20px;&#10;              color: var(--text-color);&#10;          }&#10;&#10;          .chat-container {&#10;              width: 100%;&#10;              max-width: 800px;&#10;              background: var(--chat-background);&#10;              border-radius: 10px;&#10;              box-shadow: 0 2px 10px rgba(0,0,0,0.1);&#10;              height: 80vh;&#10;              display: flex;&#10;              flex-direction: column;&#10;          }&#10;&#10;          .chat-header {&#10;              padding: 15px 20px;&#10;              border-bottom: 1px solid var(--input-border);&#10;              background: var(--chat-background);&#10;              border-radius: 10px 10px 0 0;&#10;              text-align: center;&#10;          }&#10;&#10;          .chat-messages {&#10;              flex-grow: 1;&#10;              overflow-y: auto;&#10;              padding: 20px;&#10;          }&#10;&#10;          .message {&#10;              margin-bottom: 20px;&#10;              padding: 10px 15px;&#10;              border-radius: 10px;&#10;              max-width: 80%;&#10;          }&#10;&#10;          .user-message {&#10;              background: #007AFF;&#10;              color: white;&#10;              margin-left: auto;&#10;          }&#10;&#10;          .ai-message {&#10;              background: var(--message-ai-background);&#10;              color: var(--message-ai-text);&#10;          }&#10;&#10;          .input-container {&#10;              padding: 20px;&#10;              border-top: 1px solid var(--input-border);&#10;              display: flex;&#10;              gap: 10px;&#10;          }&#10;&#10;          input {&#10;              flex-grow: 1;&#10;              padding: 10px;&#10;              border: 1px solid var(--input-border);&#10;              border-radius: 5px;&#10;              font-size: 16px;&#10;              background: var(--chat-background);&#10;              color: var(--text-color);&#10;          }&#10;&#10;          button {&#10;              padding: 10px 20px;&#10;              background: #007AFF;&#10;              color: white;&#10;              border: none;&#10;              border-radius: 5px;&#10;              cursor: pointer;&#10;              font-size: 16px;&#10;          }&#10;&#10;          button:disabled {&#10;              background: #ccc;&#10;          }&#10;&#10;          .error {&#10;              color: red;&#10;              padding: 10px;&#10;              text-align: center;&#10;          }&#10;      &lt;/style&gt;&#10;  &lt;/head&gt;&#10;  &lt;body&gt;&#10;      &lt;div class=&quot;chat-container&quot;&gt;&#10;          &lt;div class=&quot;chat-header&quot;&gt;&#10;              &lt;h2&gt;AI Assistant&lt;/h2&gt;&#10;          &lt;/div&gt;&#10;          &lt;div class=&quot;chat-messages&quot; id=&quot;messages&quot;&gt;&lt;/div&gt;&#10;          &lt;div class=&quot;input-container&quot;&gt;&#10;              &lt;input type=&quot;text&quot; id=&quot;userInput&quot; placeholder=&quot;Type your message...&quot; /&gt;&#10;              &lt;button onclick=&quot;sendMessage()&quot; id=&quot;sendButton&quot;&gt;Send&lt;/button&gt;&#10;          &lt;/div&gt;&#10;      &lt;/div&gt;&#10;&#10;      &lt;script&gt;&#10;          let messages = [];&#10;          const messagesDiv = document.getElementById(&#x27;messages&#x27;);&#10;          const userInput = document.getElementById(&#x27;userInput&#x27;);&#10;          const sendButton = document.getElementById(&#x27;sendButton&#x27;);&#10;&#10;          userInput.addEventListener(&#x27;keypress&#x27;, (e) =&gt; {&#10;              if (e.key === &#x27;Enter&#x27;) sendMessage();&#10;          });&#10;&#10;          async function sendMessage() {&#10;              const content = userInput.value.trim();&#10;              if (!content) return;&#10;&#10;              userInput.disabled = true;&#10;              sendButton.disabled = true;&#10;&#10;              messages.push({ role: &#x27;user&#x27;, content });&#10;              appendMessage(&#x27;user&#x27;, content);&#10;              userInput.value = &#x27;&#x27;;&#10;&#10;              try {&#10;                  const response = await fetch(&#x27;/api/chat&#x27;, {&#10;                      method: &#x27;POST&#x27;,&#10;                      headers: { &#x27;Content-Type&#x27;: &#x27;application/json&#x27; },&#10;                      body: JSON.stringify({&#10;                          messages&#10;                      })&#10;                  });&#10;&#10;                  if (!response.ok) {&#10;                      throw new Error(&#x27;API request failed&#x27;);&#10;                  }&#10;&#10;                  const result = await response.json();&#10;                  const aiMessage = result.response;&#10;&#10;                  messages.push({ role: &#x27;assistant&#x27;, content: aiMessage });&#10;                  appendMessage(&#x27;ai&#x27;, aiMessage);&#10;              } catch (error) {&#10;                  appendMessage(&#x27;ai&#x27;, &#x27;Sorry, there was an error processing your request.&#x27;);&#10;                  console.error(&#x27;Error:&#x27;, error);&#10;              }&#10;&#10;              userInput.disabled = false;&#10;              sendButton.disabled = false;&#10;              userInput.focus();&#10;          }&#10;&#10;          function appendMessage(role, content) {&#10;              const messageDiv = document.createElement(&#x27;div&#x27;);&#10;              messageDiv.className = &#x27;message &#x27; + role + &#x27;-message&#x27;;&#10;              messageDiv.textContent = content;&#10;              messagesDiv.appendChild(messageDiv);&#10;              messagesDiv.scrollTop = messagesDiv.scrollHeight;&#10;          }&#10;      &lt;/script&gt;&#10;  &lt;/body&gt;&#10;  &lt;/html&gt;`;&#10;</code></pre>
<p>Note that the account ID and gateway ID need to be replaced in the AI Gateway endpoint. You can add these as <a href="/workers/configuration/environment-variables/">environment variables</a> or <a href="/workers/configuration/secrets/">secrets</a> in Workers. If you chose to use Authenticated Gateway when creating your AI gateway, make sure to also add your token as a secret and pass its value to the AI gateway in the <code>cf-aig-authorization</code> header.</p>
<h3 id="3-publish-the-worker"><ol start="3">
<li>Publish the Worker</li>
</ol></h3>
<p>Once the Worker code is complete, you need to make the Worker addressable using a hostname controllable by Cloudflare Access.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4331.md")
</div></div>
<h2 id="4-secure-the-wrapper-with-access"><ol start="4">
<li>Secure the wrapper with Access</li>
</ol></h2>
<p>To secure the AI agent wrapper to ensure that only trusted users can access it:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong>.</li>
<li>Select <strong>Self-hosted and private</strong>.</li>
<li>Select <strong>Add public hostname</strong> and enter the custom domain you set for your Worker.</li>
<li><a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">Configure your Access application</a> for your Worker.</li>
<li>Add <a href="/cloudflare-one/access-controls/policies/policy-management/">Access policies</a> to control who can connect to your application.</li>
</ol>
<p>Now your AI wrapper can only be accessed by your users that successfully match your Access policies.</p>
<h2 id="5-block-access-to-public-ai-agents-with-gateway"><ol start="5">
<li>Block access to public AI agents with Gateway</li>
</ol></h2>
<p>You can now block access to all unauthorized public AI agents with a Gateway <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policy</a>.</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong> &gt; <strong>HTTP</strong>.</li>
<li>Select <strong>Add a policy</strong>.</li>
<li>Add the following policy:</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Content Categories</td>
<td>in</td>
<td><em>Artificial Intelligence</em></td>
<td>Block</td>
</tr>
</tbody>
</table>
<ol start="4">
<li>Select <strong>Create policy</strong>.</li>
</ol>
<p>This ensures that public AI agents are not accessible using a managed endpoint.</p>
<p>Alternatively, you can prevent users from using public AI agents by displaying a <a href="/cloudflare-one/reusable-components/custom-pages/gateway-block-page/#customize-the-block-page">custom block message</a>, <a href="/cloudflare-one/reusable-components/custom-pages/gateway-block-page/#redirect-to-a-block-page">redirect</a>, or a <a href="/cloudflare-one/traffic-policies/http-policies/#cloudflare-one-client-block-notifications">user notification</a> directing users to the AI agent wrapper.</p>
<h2 id="6-enforce-data-loss-prevention-and-clientless-browser-isolation"><ol start="6">
<li>Enforce Data Loss Prevention and Clientless Browser Isolation</li>
</ol></h2>
<p>Now that you have full control over access to your AI agent wrapper, you can enforce extra security methods such as Data Loss Prevention (DLP) and Clientless Web Isolation to protect and control data shared with the AI agent.</p>
<h3 id="apply-data-loss-prevention-profiles">Apply Data Loss Prevention profiles</h3>
<p>You can use <a href="/cloudflare-one/data-loss-prevention/">Data Loss Prevention (DLP)</a> to prevent your users from sending sensitive data to the AI agent.</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>Profiles</strong>.</li>
<li>Ensure that the <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">DLP profiles</a> you want to enforce are properly configured.</li>
<li>Add an HTTP policy to enforce the DLP profile for the hostname for your wrapper. For example:</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Host</td>
<td>is</td>
<td><code>ai-wrapper.example.com</code></td>
<td>And</td>
<td>Block</td>
</tr>
<tr>
<td>DLP Profile</td>
<td>in</td>
<td><em>AI DLP profile</em></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<ol start="4">
<li>Select <strong>Create policy</strong>.</li>
</ol>
<p>For more information on creating DLP policies, refer to <a href="/cloudflare-one/data-loss-prevention/dlp-policies/">Scan HTTP traffic</a>.</p>
<h3 id="execute-in-a-clientless-isolated-browser">Execute in a clientless isolated browser</h3>
<p>Because you published your wrapper as a self-hosted Access application, you can execute it in an <a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/">isolated session</a> for your users by creating an <a href="/cloudflare-one/access-controls/policies/">Access policy</a> and configuring it for your application.</p>
<ol>
<li>
<p>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Browser isolation</strong> &gt; <strong>Browser isolation settings</strong>.</p>
</li>
<li>
<p>Turn on <strong>Allow users to open a remote browser without the device client</strong>.</p>
</li>
<li>
<p>Go to <strong>Access controls</strong> &gt; <strong>Policies</strong>.</p>
</li>
<li>
<p>Select <strong>Add a policy</strong>.</p>
</li>
<li>
<p>Set the <strong>Action</strong> to <em>Allow</em>.</p>
</li>
<li>
<p>In <strong>Add rules</strong>, add identity rules to define who the application should be isolated for.</p>
</li>
<li>
<p>In <strong>Additional settings (optional)</strong>, turn on <strong>Isolate application</strong>.</p>
</li>
</ol>
<p>Once the Access policy has been created, you can attach it to your wrapper.</p>
<ol>
<li>Go to <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Choose your wrapper application, then select <strong>Configure</strong>.</li>
<li>In <strong>Policies</strong>, select <strong>Select existing policies</strong>.</li>
<li>Choose the Access policy you previously created.</li>
<li>Select <strong>Confirm</strong>, then select <strong>Save</strong>.</li>
</ol>
<p>Because Clientless Web Isolation traffic applies your Gateway HTTP policies, your configured DLP profiles will apply to isolated sessions.</p>
<p>For more information on isolating an Access application, refer to <a href="/cloudflare-one/access-controls/policies/isolate-application/">Isolate self-hosted application</a>.</p>
<h2 id="additional-benefits">Additional benefits</h2>
<p>Organizations that adopt Cloudflare to secure access to AI agents will benefit from improved visibility and configurability.</p>
<h3 id="visibility">Visibility</h3>
<p>Zero Trust will log all <a href="/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/">Access events</a> and <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/#http-logs">DLP detections</a>. In addition, AI Gateway provides <a href="/ai-gateway/observability/logging/">visibility</a> into user prompts, model response, token usage, and costs.</p>
<p>Logs can be exported to external providers with <a href="/logs/logpush/">Logpush</a>.</p>
<h3 id="configurability">Configurability</h3>
<p>You can configure your wrapper to use a <a href="/ai-gateway/usage/providers/">different AI provider</a> or give your users the option to choose between multiple AI providers, including AI models running directly on Cloudflare's global network with <a href="/workers-ai/">Workers AI</a>. With this, you can control costs related to AI usage or adopt newer models without impacting your users or the access controls already put in place.</p>

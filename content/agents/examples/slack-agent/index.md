---
cp9:
  canonical: https://developers.cloudflare.com/agents/examples/slack-agent/
  description: Build and deploy an AI-powered Slack bot on Cloudflare Workers using the Agents SDK.
  full_title: Slack agent · Cloudflare Agents docs
  head_html: <title>Slack agent · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Build and deploy an AI-powered Slack bot on Cloudflare Workers using the Agents SDK."><link rel="canonical" href="https://developers.cloudflare.com/agents/examples/slack-agent/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/examples/slack-agent/index.md"><meta property="og:title" content="Slack agent · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build and deploy an AI-powered Slack bot on Cloudflare Workers using the Agents SDK."><meta property="og:url" content="https://developers.cloudflare.com/agents/examples/slack-agent/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/examples/slack-agent/#page","headline":"Slack agent \u00b7 Cloudflare Agents docs","description":"Build and deploy an AI-powered Slack bot on Cloudflare Workers using the Agents SDK.","url":"https://developers.cloudflare.com/agents/examples/slack-agent/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/examples/slack-agent/
  schema: 1
---
<h2 id="deploy-your-first-slack-agent">Deploy your first Slack Agent</h2>
<p>This guide will show you how to build and deploy an AI-powered Slack bot on Cloudflare Workers that can:</p>
<ul>
<li>Respond to direct messages</li>
<li>Reply when mentioned in channels</li>
<li>Maintain conversation context in threads</li>
<li>Use AI to generate intelligent responses</li>
</ul>
<p>Your Slack Agent will be a multi-tenant application, meaning a single deployment can serve multiple Slack workspaces. Each workspace gets its own isolated agent instance with dedicated storage, powered by the <a href="/agents/">Agents SDK</a>.</p>
<p>You can view the full code for this example <a href="https://github.com/cloudflare/awesome-agents/tree/69963298b359ddd66331e8b3b378bb9ae666629f/agents/slack">here</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you begin, you will need:</p>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a></li>
<li><a href="https://nodejs.org/">Node.js</a> installed (v18 or later)</li>
<li>A <a href="https://slack.com/create">Slack workspace</a> where you have permission to install apps</li>
<li>An <a href="https://platform.openai.com/api-keys">OpenAI API key</a> (or another LLM provider)</li>
</ul>
<h2 id="1-create-a-slack-app"><ol>
<li>Create a Slack App</li>
</ol></h2>
<p>First, create a new Slack App that your agent will use to interact with Slack:</p>
<ol>
<li>Go to <a href="https://api.slack.com/apps">api.slack.com/apps</a> and select <strong>Create New App</strong>.</li>
<li>Select <strong>From scratch</strong>.</li>
<li>Give your app a name (for example, &quot;My AI Assistant&quot;) and select your workspace.</li>
<li>Select <strong>Create App</strong>.</li>
</ol>
<h3 id="configure-oauth-permissions">Configure OAuth &amp; Permissions</h3>
<p>In your Slack App settings, go to <strong>OAuth &amp; Permissions</strong> and add the following <strong>Bot Token Scopes</strong>:</p>
<ul>
<li><code>chat:write</code> — Send messages as the bot</li>
<li><code>chat:write.public</code> — Send messages to channels without joining</li>
<li><code>channels:history</code> — View messages in public channels</li>
<li><code>app_mentions:read</code> — Receive mentions</li>
<li><code>im:write</code> — Send direct messages</li>
<li><code>im:history</code> — View direct message history</li>
</ul>
<h3 id="enable-event-subscriptions">Enable Event Subscriptions</h3>
<p>You will later configure the Event Subscriptions URL after deploying your agent. But for now, go to <strong>Event Subscriptions</strong> in your Slack App settings and prepare to enable it.</p>
<p>Subscribe to the following bot events:</p>
<ul>
<li><code>app_mention</code> — When the bot is @mentioned</li>
<li><code>message.im</code> — Direct messages to the bot</li>
</ul>
<p>Do not enable it yet. You will enable it after deployment.</p>
<h3 id="get-your-slack-credentials">Get your Slack credentials</h3>
<p>From your Slack App settings, collect these values:</p>
<ol>
<li><strong>Basic Information</strong> &gt; <strong>App Credentials</strong>:
<ul>
<li><strong>Client ID</strong></li>
<li><strong>Client Secret</strong></li>
<li><strong>Signing Secret</strong></li>
</ul>
</li>
</ol>
<p>Keep these handy — you will need them in the next step.</p>
<h2 id="2-create-your-slack-agent-project"><ol start="2">
<li>Create your Slack Agent project</li>
</ol></h2>
<ol>
<li>Create a new project for your Slack Agent:</li>
</ol>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- my-slack-agent</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- my-slack-agent" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare my-slack-agent</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare my-slack-agent" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest my-slack-agent</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest my-slack-agent" aria-label="Copy to clipboard">Copy</button></div></div>
<ol start="2">
<li>Navigate into your project:</li>
</ol>
<pre tabindex="0"><code class="language-sh">cd my-slack-agent&#10;</code></pre>
<ol start="3">
<li>Install the required dependencies:</li>
</ol>
<pre tabindex="0"><code class="language-sh">npm install agents openai&#10;</code></pre>
<h2 id="3-set-up-your-environment-variables"><ol start="3">
<li>Set up your environment variables</li>
</ol></h2>
<ol>
<li>Create a <code>.env</code> file in your project root for local development secrets:</li>
</ol>
<pre tabindex="0"><code class="language-sh">touch .env&#10;</code></pre>
<ol start="2">
<li>Add your credentials to <code>.env</code>:</li>
</ol>
<pre tabindex="0"><code class="language-sh">SLACK_CLIENT_ID=&quot;your-slack-client-id&quot;&#10;SLACK_CLIENT_SECRET=&quot;your-slack-client-secret&quot;&#10;SLACK_SIGNING_SECRET=&quot;your-slack-signing-secret&quot;&#10;OPENAI_API_KEY=&quot;your-openai-api-key&quot;&#10;OPENAI_BASE_URL=&quot;https://gateway.ai.cloudflare.com/v1/YOUR_ACCOUNT_ID/YOUR_GATEWAY/openai&quot;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1905.md")
</aside>
<ol start="3">
<li>Update your <code>wrangler.jsonc</code> to configure your Agent:</li>
</ol>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1906.md")
</div>
<h2 id="4-create-your-slack-agent"><ol start="4">
<li>Create your Slack Agent</li>
</ol></h2>
<ol>
<li>
<p>First, create the base <code>SlackAgent</code> class at <code>src/slack.ts</code>. This class handles OAuth, request verification, and event routing. You can view the <a href="https://github.com/cloudflare/awesome-agents/blob/69963298b359ddd66331e8b3b378bb9ae666629f/agents/slack/src/slack.ts">full implementation on GitHub</a>.</p>
</li>
<li>
<p>Now create your agent implementation at <code>src/index.ts</code>:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-ts">import { env } from &quot;cloudflare:workers&quot;;&#10;import { SlackAgent } from &quot;./slack&quot;;&#10;import { OpenAI } from &quot;openai&quot;;&#10;&#10;const openai = new OpenAI({&#10;	apiKey: env.OPENAI_API_KEY,&#10;	baseURL: env.OPENAI_BASE_URL,&#10;});&#10;&#10;type SlackMsg = {&#10;	user?: string;&#10;	text?: string;&#10;	ts: string;&#10;	thread_ts?: string;&#10;	subtype?: string;&#10;	bot_id?: string;&#10;};&#10;&#10;function normalizeForLLM(msgs: SlackMsg[], selfUserId: string) {&#10;	return msgs.map((m) =&gt; {&#10;		const role = m.user &amp;&amp; m.user !== selfUserId ? &quot;user&quot; : &quot;assistant&quot;;&#10;		const text = (m.text ?? &quot;&quot;).replace(/&lt;@([A-Z0-9]+)&gt;/g, &quot;@$1&quot;);&#10;		return { role, content: text };&#10;	});&#10;}&#10;&#10;export class MyAgent extends SlackAgent {&#10;	async generateAIReply(conversation: SlackMsg[]) {&#10;		const selfId = await this.ensureAppUserId();&#10;		const messages = normalizeForLLM(conversation, selfId);&#10;&#10;		const system = `You are a helpful AI assistant in Slack.&#10;Be brief, specific, and actionable. If you&#x27;re unsure, ask a single clarifying question.`;&#10;&#10;		const input = [{ role: &quot;system&quot;, content: system }, ...messages];&#10;&#10;		const response = await openai.chat.completions.create({&#10;			model: &quot;gpt-4o-mini&quot;,&#10;			messages: input,&#10;		});&#10;&#10;		const msg = response.choices[0].message.content;&#10;		if (!msg) throw new Error(&quot;No message from AI&quot;);&#10;&#10;		return msg;&#10;	}&#10;&#10;	async onSlackEvent(event: { type: string } &amp; Record&lt;string, unknown&gt;) {&#10;		// Ignore bot messages and subtypes (edits, joins, etc.)&#10;		if (event.bot_id || event.subtype) return;&#10;&#10;		// Handle direct messages&#10;		if (event.type === &quot;message&quot;) {&#10;			const e = event as unknown as SlackMsg &amp; { channel: string };&#10;			const isDM = (e.channel || &quot;&quot;).startsWith(&quot;D&quot;);&#10;			const mentioned = (e.text || &quot;&quot;).includes(&#10;				`&lt;@${await this.ensureAppUserId()}&gt;`,&#10;			);&#10;&#10;			if (!isDM &amp;&amp; !mentioned) return;&#10;&#10;			const conversation = await this.fetchConversation(e.channel);&#10;			const content = await this.generateAIReply(conversation);&#10;			await this.sendMessage(content, { channel: e.channel });&#10;			return;&#10;		}&#10;&#10;		// Handle @mentions in channels&#10;		if (event.type === &quot;app_mention&quot;) {&#10;			const e = event as unknown as SlackMsg &amp; {&#10;				channel: string;&#10;				text?: string;&#10;			};&#10;			const thread = await this.fetchThread(e.channel, e.thread_ts || e.ts);&#10;			const content = await this.generateAIReply(thread);&#10;			await this.sendMessage(content, {&#10;				channel: e.channel,&#10;				thread_ts: e.thread_ts || e.ts,&#10;			});&#10;			return;&#10;		}&#10;	}&#10;}&#10;&#10;export default MyAgent.listen({&#10;	clientId: env.SLACK_CLIENT_ID,&#10;	clientSecret: env.SLACK_CLIENT_SECRET,&#10;	slackSigningSecret: env.SLACK_SIGNING_SECRET,&#10;	scopes: [&#10;		&quot;chat:write&quot;,&#10;		&quot;chat:write.public&quot;,&#10;		&quot;channels:history&quot;,&#10;		&quot;app_mentions:read&quot;,&#10;		&quot;im:write&quot;,&#10;		&quot;im:history&quot;,&#10;	],&#10;});&#10;</code></pre>
<h2 id="5-test-locally"><ol start="5">
<li>Test locally</li>
</ol></h2>
<p>Start your development server:</p>
<pre tabindex="0"><code class="language-sh">npm run dev&#10;</code></pre>
<p>Your agent is now running at <code>http://localhost:8787</code>.</p>
<h3 id="configure-slack-event-subscriptions">Configure Slack Event Subscriptions</h3>
<p>Now that your agent is running locally, you need to expose it to Slack. Use <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/trycloudflare/">Cloudflare Tunnel</a> to create a secure tunnel:</p>
<pre tabindex="0"><code class="language-sh">npx cloudflared tunnel --url http://localhost:8787&#10;</code></pre>
<p>This will output a public URL like <code>https://random-subdomain.trycloudflare.com</code>.</p>
<p>Go back to your Slack App settings:</p>
<ol>
<li>
<p>Go to <strong>Event Subscriptions</strong>.</p>
</li>
<li>
<p>Toggle <strong>Enable Events</strong> to <strong>On</strong>.</p>
</li>
<li>
<p>Enter your Request URL: <code>https://random-subdomain.trycloudflare.com/slack</code>.</p>
</li>
<li>
<p>Slack will send a verification request — if your agent is running correctly, it should show <strong>Verified</strong>.</p>
</li>
<li>
<p>Under <strong>Subscribe to bot events</strong>, add:</p>
<ul>
<li><code>app_mention</code></li>
<li><code>message.im</code></li>
</ul>
</li>
<li>
<p>Select <strong>Save Changes</strong>.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1904.md")
</aside>
<h3 id="install-your-app-to-slack">Install your app to Slack</h3>
<p>Visit <code>http://localhost:8787/install</code> in your browser. This will redirect you to Slack's authorization page. Select <strong>Allow</strong> to install the app to your workspace.</p>
<p>After authorization, you should see &quot;Successfully registered!&quot; in your browser.</p>
<h3 id="test-your-agent">Test your agent</h3>
<p>Open Slack. Then:</p>
<ol>
<li>Send a DM to your bot — it should respond with an AI-generated message.</li>
<li>Mention your bot in a channel (e.g., <code>@My AI Assistant hello</code>) — it should reply in a thread.</li>
</ol>
<p>If everything works, you're ready to deploy to production!</p>
<h2 id="6-deploy-to-production"><ol start="6">
<li>Deploy to production</li>
</ol></h2>
<ol>
<li>Before deploying, add your secrets to Cloudflare:</li>
</ol>
<pre tabindex="0"><code class="language-sh">npx wrangler secret put SLACK_CLIENT_ID&#10;npx wrangler secret put SLACK_CLIENT_SECRET&#10;npx wrangler secret put SLACK_SIGNING_SECRET&#10;npx wrangler secret put OPENAI_API_KEY&#10;npx wrangler secret put OPENAI_BASE_URL&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1903.md")
</aside>
<ol start="2">
<li>Deploy your agent:</li>
</ol>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>After deploying, you will get a production URL like:</p>
<pre tabindex="0"><code>https://my-slack-agent.your-account.workers.dev&#10;</code></pre>
<h3 id="update-slack-event-subscriptions">Update Slack Event Subscriptions</h3>
<p>Go back to your Slack App settings:</p>
<ol>
<li>Go to <strong>Event Subscriptions</strong>.</li>
<li>Update the Request URL to your production URL: <code>https://my-slack-agent.your-account.workers.dev/slack</code>.</li>
<li>Select <strong>Save Changes</strong>.</li>
</ol>
<h3 id="distribute-your-app">Distribute your app</h3>
<p>Now that your agent is deployed, you can share it with others:</p>
<ul>
<li><strong>Single workspace</strong>: Install it via <code>https://my-slack-agent.your-account.workers.dev/install</code>.</li>
<li><strong>Public distribution</strong>: Submit your app to the <a href="https://api.slack.com/start/distributing">Slack App Directory</a>.</li>
</ul>
<p>Each workspace that installs your app will get its own isolated agent instance with dedicated storage.</p>
<h2 id="how-it-works">How it works</h2>
<h3 id="multi-tenancy-with-durable-objects">Multi-tenancy with Durable Objects</h3>
<p>Your Slack Agent uses <a href="/durable-objects/">Durable Objects</a> to provide isolated, stateful instances for each Slack workspace:</p>
<ul>
<li>Each workspace's <code>team_id</code> is used as the Durable Object ID.</li>
<li>Each agent instance stores its own Slack access token in KV storage.</li>
<li>Conversations are fetched on-demand from Slack's API.</li>
<li>All agent logic runs in an isolated, consistent environment.</li>
</ul>
<h3 id="oauth-flow">OAuth flow</h3>
<p>The agent handles Slack's OAuth 2.0 flow:</p>
<ol>
<li>User visits <code>/install</code> &gt; redirected to Slack authorization.</li>
<li>User selects <strong>Allow</strong> &gt; Slack redirects to <code>/accept</code> with an authorization code.</li>
<li>Agent exchanges code for access token.</li>
<li>Agent stores token in the workspace's Durable Object.</li>
</ol>
<h3 id="event-handling">Event handling</h3>
<p>When Slack sends an event:</p>
<ol>
<li>Request arrives at <code>/slack</code> endpoint.</li>
<li>Agent verifies the request signature using HMAC-SHA256.</li>
<li>Agent routes the event to the correct workspace's Durable Object.</li>
<li><code>onSlackEvent</code> method processes the event and generates a response.</li>
</ol>
<h2 id="customizing-your-agent">Customizing your agent</h2>
<h3 id="change-the-ai-model">Change the AI model</h3>
<p>Update the model in <code>src/index.ts</code>:</p>
<pre tabindex="0"><code class="language-ts">const response = await openai.chat.completions.create({&#10;	model: &quot;gpt-4o&quot;, // or any other model&#10;	messages: input,&#10;});&#10;</code></pre>
<h3 id="add-conversation-memory">Add conversation memory</h3>
<p>Store conversation history in Durable Object storage:</p>
<pre tabindex="0"><code class="language-ts">async storeMessage(channel: string, message: SlackMsg) {&#10;  const history = await this.ctx.storage.kv.get(`history:${channel}`) || [];&#10;  history.push(message);&#10;  await this.ctx.storage.kv.put(`history:${channel}`, history);&#10;}&#10;</code></pre>
<h3 id="react-to-specific-keywords">React to specific keywords</h3>
<p>Add custom logic in <code>onSlackEvent</code>:</p>
<pre tabindex="0"><code class="language-ts">async onSlackEvent(event: { type: string } &amp; Record&lt;string, unknown&gt;) {&#10;  if (event.type === &quot;message&quot;) {&#10;    const e = event as unknown as SlackMsg &amp; { channel: string };&#10;&#10;    if (e.text?.includes(&quot;help&quot;)) {&#10;      await this.sendMessage(&quot;Here&#x27;s how I can help...&quot;, {&#10;        channel: e.channel&#10;      });&#10;      return;&#10;    }&#10;  }&#10;&#10;  // ... rest of your event handling&#10;}&#10;</code></pre>
<h3 id="use-different-llm-providers">Use different LLM providers</h3>
<p>Replace OpenAI with <a href="/workers-ai/">Workers AI</a>:</p>
<pre tabindex="0"><code class="language-ts">import { Ai } from &quot;@cloudflare/ai&quot;;&#10;&#10;export class MyAgent extends SlackAgent {&#10;	async generateAIReply(conversation: SlackMsg[]) {&#10;		const ai = new Ai(this.ctx.env.AI);&#10;		const response = await ai.run(&quot;@cf/meta/llama-3-8b-instruct&quot;, {&#10;			messages: normalizeForLLM(conversation, await this.ensureAppUserId()),&#10;		});&#10;		return response.response;&#10;	}&#10;}&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Add <a href="https://api.slack.com/interactivity">Slack Interactive Components</a> (buttons, modals)</li>
<li>Connect your Agent to an <a href="/agents/model-context-protocol/apis/client-api/">MCP server</a></li>
<li>Add rate limiting to prevent abuse</li>
<li>Implement conversation state management</li>
<li>Use <a href="/analytics/analytics-engine/">Workers Analytics Engine</a> to track usage</li>
<li>Add <a href="/agents/runtime/execution/schedule-tasks/">schedules</a> for scheduled tasks</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<div class="nb-card nb-link-card"><h3 id="card-agents-documentation-agents"><a href="/agents/">Agents documentation</a></h3><p>Complete Agents framework documentation.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-durable-objects-durable-objects"><a href="/durable-objects/">Durable Objects</a></h3><p>Learn about the underlying stateful infrastructure.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-slack-api-https-api-slack-com"><a href="https://api.slack.com/">Slack API</a></h3><p>Official Slack API documentation.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-openai-api-https-platform-openai-com-docs"><a href="https://platform.openai.com/docs/">OpenAI API</a></h3><p>Official OpenAI API documentation.</p></div>

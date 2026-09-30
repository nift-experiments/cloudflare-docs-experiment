<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 25, 2025</time><h2 id="post-title">Introducing the Agents SDK</h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>We've released the <a href="http://blog.cloudflare.com/build-ai-agents-on-cloudflare/">Agents SDK</a>, a package and set of tools that help you build and ship AI Agents.</p>
<p>You can get up and running with a <a href="https://github.com/cloudflare/agents-starter">chat-based AI Agent</a> (and deploy it to Workers) that uses the Agents SDK, tool calling, and state syncing with a React-based front-end by running the following command:</p>
<pre><code class="language-sh">npm create cloudflare@latest agents-starter -- --template=&quot;cloudflare/agents-starter&quot;&#10;&#35; open up README.md and follow the instructions&#10;</code></pre>
<p>You can also add an Agent to any existing Workers application by installing the <code>agents</code> package directly</p>
<pre><code class="language-sh">npm i agents&#10;</code></pre>
<p>... and then define your first Agent:</p>
<pre><code class="language-ts">import { Agent } from &quot;agents&quot;;&#10;&#10;export class YourAgent extends Agent&lt;Env&gt; {&#10;	// Build it out&#10;	// Access state on this.state or query the Agent&#x27;s database via this.sql&#10;	// Handle WebSocket events with onConnect and onMessage&#10;	// Run tasks on a schedule with this.schedule&#10;	// Call AI models&#10;	// ... and/or call other Agents.&#10;}&#10;</code></pre>
<p>Head over to the <a href="/agents/">Agents documentation</a> to learn more about the Agents SDK, the SDK APIs, as well as how to test and deploying agents to production.</p>
</div></article></div>

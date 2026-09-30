<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 15, 2026</time><h2 id="post-title">Agent Lee adds Write Operations and Generative UI</h2>
<div class="changelog-badges"><span>agents</span></div><div class="changelog-body"><h4 id="agent-lee-adds-write-operations-and-generative-ui">Agent Lee adds Write Operations and Generative UI</h4>
<p>We are excited to announce two major capability upgrades for <strong>Agent Lee</strong>, the AI co-pilot built directly into the Cloudflare dashboard. Agent Lee is designed to understand your specific account configuration, and with this release, it moves from a passive advisor to an active assistant that can help you manage your infrastructure and visualize your data through natural language.</p>
<h4 id="take-action-with-write-operations">Take action with Write Operations</h4>
<p>Agent Lee can now perform changes on your behalf across your Cloudflare account. Whether you need to update DNS records, modify SSL/TLS settings, or configure Workers routes, you can simply ask.</p>
<p>To ensure security and accuracy, every write operation requires <strong>explicit user approval</strong>. Before any change is committed, Agent Lee will present a summary of the proposed action in plain language. No action is taken until you select <strong>Confirm</strong>, and this approval requirement is enforced at the infrastructure level to prevent unauthorized changes.</p>
<p><strong>Example requests:</strong></p>
<ul>
<li><em>&quot;Add an A record for blog.example.com pointing to 192.0.2.10.&quot;</em></li>
<li><em>&quot;Enable Always Use HTTPS on my zone.&quot;</em></li>
<li><em>&quot;Set the SSL mode for example.com to Full (strict).&quot;</em></li>
</ul>
<h4 id="visualize-data-with-generative-ui">Visualize data with Generative UI</h4>
<p>Understanding your traffic and security trends is now as easy as asking a question. Agent Lee now features <strong>Generative UI</strong>, allowing it to render inline charts and structured data visualizations directly within the chat interface using your actual account telemetry.</p>
<p><strong>Example requests:</strong></p>
<ul>
<li><em>&quot;Show me a chart of my traffic over the last 7 days.&quot;</em></li>
<li><em>&quot;What does my error rate look like for the past 24 hours?&quot;</em></li>
<li><em>&quot;Graph my cache hit rate for example.com this week.&quot;</em></li>
</ul>
<hr />
<h4 id="availability">Availability</h4>
<p>These features are currently available in <strong>Beta</strong> for all users on the <strong>Free plan</strong>. To get started, log in to the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> and select <strong>Ask AI</strong> in the upper right corner.</p>
<p>To learn more about how to interact with your account using AI, refer to the <a href="/agent-lee/">Agent Lee documentation</a>.</p>
</div></article></div>

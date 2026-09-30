<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 16, 2026</time><h2 id="post-title">Email Sending now in public beta</h2>
<div class="changelog-badges"><span>email-service</span></div><div class="changelog-body"><p><strong><a href="/email-service/api/send-emails/">Email Sending</a></strong> is now in public beta. Send transactional emails directly from Workers (<code>env.EMAIL.send()</code>) or the REST API, with support for HTML, plain text, attachments, inline images, and custom headers. Email Sending joins <a href="https://blog.cloudflare.com/introducing-email-routing/">Email Routing</a> under the new <strong>Cloudflare Email Service</strong> — a single service for sending and receiving email on the Cloudflare developer platform.</p>
<p>Send an email from a Worker in a few lines of code:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17722.md")</div>
<p>Email Service also integrates with the <a href="/agents/">Agents SDK</a>, giving your agents a native <code>onEmail</code> hook to receive, process, and reply to emails. Combined with the new <a href="https://github.com/cloudflare/mcp-server-cloudflare">Email MCP server</a> and Wrangler CLI email commands, any agent can send email regardless of where it runs.</p>
<p>Start sending and receiving emails from Workers and agents today. Email Sending is available on the Workers paid plan. Refer to the <a href="/email-service/">Email Service documentation</a> to get started.</p>
</div></article></div>

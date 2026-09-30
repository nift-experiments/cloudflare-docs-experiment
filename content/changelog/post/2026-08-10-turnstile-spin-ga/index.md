<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 10, 2026</time><h2 id="post-title">Turnstile Spin is now generally available</h2>
<div class="changelog-badges"><span>turnstile</span></div><div class="changelog-body"><p><a href="/turnstile/spin/">Turnstile Spin</a> is now generally available with three setup paths for creating a Turnstile widget and wiring canonical server-side siteverify into your existing backend. Start in the dashboard, with Wrangler, or from your AI coding agent. All three paths create the same widget. You can complete the integration by hand or have your agent embed the widget, wire siteverify, and validate it.</p>
<h4 id="server-side-verification">Server-side verification</h4>
<p>Turnstile setup has two parts: embed the widget in your frontend, then call siteverify from your backend. Without the second part, the widget appears on the page but does not protect the request.</p>
<ul>
<li>The skill includes insertion snippets for Next.js (App Router and Pages Router), Astro, SvelteKit, Hugo, and vanilla HTML. For other frameworks, the agent proposes a generic pattern and asks you to confirm it first.</li>
<li>The Turnstile dashboard flags existing widgets with no matching siteverify traffic. Select <strong>Fix with Spin</strong> to copy a prompt that guides your agent through wiring siteverify into your backend.</li>
<li>Before finishing, the agent runs a real Turnstile token through your protected endpoint, checks that it passes, then replays the token to confirm the endpoint rejects it on the second try. If a check fails, the agent stops and shows you where.</li>
</ul>
<h4 id="run-spin">Run Spin</h4>
<p>You can run Spin three ways:</p>
<ul>
<li>In the <strong>Turnstile dashboard</strong>, select <strong>Set up with Spin</strong>, enter your domains, then select <strong>Set up</strong>. Spin creates the widget and returns the sitekey, secret, and a prompt for your agent.</li>
<li>From the <code>Wrangler CLI</code>, run <a href="/turnstile/spin/#set-up-from-the-wrangler-cli"><code>wrangler turnstile widget create</code></a>. Wrangler prints the sitekey and secret. You wire the frontend and siteverify by hand.</li>
<li>From your <strong>AI coding agent</strong>, paste the <a href="/turnstile/spin/#set-up-from-an-ai-coding-agent">Spin prompt</a> into Claude Code, Cursor, Codex, OpenCode, or GitHub Copilot Chat. Your agent fetches the skill, creates the widget, then embeds it and wires siteverify.</li>
</ul>
<p>To get started, refer to the <a href="/turnstile/spin/">Turnstile Spin documentation</a>.</p>
</div></article></div>

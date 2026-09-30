<p>Turnstile Spin is a setup flow for Cloudflare Turnstile. It creates the widget for you, then provides the sitekey, secret, and a curated prompt to embed the widget on the right forms and wire canonical server-side siteverify into your existing backend. The prompt does not contain the secret. Spin runs three ways:</p>
<ul>
<li><strong>From the Cloudflare dashboard.</strong> Enter your domains, select <strong>Set up</strong>, and Spin creates the widget server-side. You receive the sitekey, the secret, and a prompt for your AI coding agent.</li>
<li><strong>From the Wrangler CLI.</strong> Run <code>wrangler turnstile widget create</code> to create the widget from your terminal. Wrangler prints the sitekey and secret; you wire the widget and siteverify by hand.</li>
<li><strong>From your AI coding agent.</strong> Paste a single prompt into Claude Code, Cursor, Codex, OpenCode, or GitHub Copilot Chat. The agent uses the inlined Spin skill to create the widget, embed it, and wire siteverify in your codebase.</li>
</ul>
<p>All three paths produce the same widget. The only difference is where the create call runs. None of them deploy infrastructure on your behalf. Spin uses Turnstile's canonical siteverify endpoint, called from the backend you already have.</p>
<h2 id="set-up-from-the-dashboard">Set up from the dashboard</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/231.md")
</div>
<p>If Spin fails before it finishes, the dialog shows the error and offers a fallback prompt your AI coding agent can use to drive the same setup from your editor. Select <strong>Try again</strong> to retry from the same dialog.</p>
<h2 id="set-up-from-the-wrangler-cli">Set up from the Wrangler CLI</h2>
<p>If you prefer to drive setup from your terminal without an AI coding agent, use <a href="/workers/wrangler/">Wrangler</a>:</p>
<pre><code class="language-sh">wrangler turnstile widget create &quot;myproject&quot; \&#10;	&#45;-domain example.com \&#10;	&#45;-domain localhost \&#10;	&#45;-domain 127.0.0.1 \&#10;	&#45;-mode managed&#10;</code></pre>
<p>Wrangler prints the sitekey and the secret. Copy the sitekey into your widget HTML, store the secret as <code>TURNSTILE_SECRET</code> in your backend's env, and wire the canonical siteverify call as described in <a href="#wire-up-the-frontend">Wire up the frontend</a>.</p>
<p>Additional widget commands:</p>
<table>
<thead>
<tr>
<th>Command</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>wrangler turnstile widget list</code></td>
<td>List every Turnstile widget on your account.</td>
</tr>
<tr>
<td><code>wrangler turnstile widget get &lt;sitekey&gt;</code></td>
<td>Fetch a widget's configuration, including its secret.</td>
</tr>
<tr>
<td><code>wrangler turnstile widget update &lt;sitekey&gt; --domain &lt;d&gt;</code></td>
<td>Update the domains, mode, or name of a widget.</td>
</tr>
<tr>
<td><code>wrangler turnstile widget delete &lt;sitekey&gt;</code></td>
<td>Delete a widget. Pass <code>-y</code> to skip the confirmation prompt.</td>
</tr>
</tbody>
</table>
<p>All commands accept <code>--json</code> for machine-readable output. <code>--domain</code> accepts comma-separated values (<code>--domain a.com,b.com</code>) or repeated flags (<code>--domain a.com --domain b.com</code>).</p>
<p>The <code>wrangler turnstile widget get &lt;sitekey&gt; --json</code> response includes the widget secret. Automated flows must use a user-approved absolute Wrangler executable outside project package resolution and pin its exact version. They must set <code>WRANGLER_WRITE_LOGS=false</code>, <code>WRANGLER_LOG=log</code>, and <code>WRANGLER_LOG_SANITIZE=true</code>. Before retrieval, the agent confirms the account, sitekey, domains, and exact secret destination with you. For a Workers backend, it also confirms the Worker, environment, configuration file, and binding with <code>wrangler secret list</code> before using the standard <code>wrangler secret put</code> command. The flow validates the exact sitekey, expected domains, clearance level, and a non-whitespace secret. Do not print the response or include it in command arguments, temporary files, logs, or chat.</p>
<h2 id="set-up-from-an-ai-coding-agent">Set up from an AI coding agent</h2>
<p>If you do not see the <strong>Set up with Spin</strong> button in your dashboard, or you want your agent to embed the widget and wire siteverify into your codebase in the same pass, paste this prompt into your AI coding agent:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/232.md")
</div>
<p>If you would rather install the skill locally first so the agent has it on disk:</p>
<pre><code class="language-sh">&#35; Claude Code&#10;mkdir -p .claude/skills/turnstile-spin &amp;&amp; \&#10;  curl -sSL https://developers.cloudflare.com/turnstile/spin/prompt.md \&#10;  &#45;o .claude/skills/turnstile-spin/SKILL.md&#10;&#10;&#35; Cursor&#10;mkdir -p .cursor/rules &amp;&amp; \&#10;  curl -sSL https://developers.cloudflare.com/turnstile/spin/prompt.md \&#10;  &#45;o .cursor/rules/turnstile-spin.md&#10;&#10;&#35; OpenCode&#10;mkdir -p .opencode/skills/turnstile-spin &amp;&amp; \&#10;  curl -sSL https://developers.cloudflare.com/turnstile/spin/prompt.md \&#10;  &#45;o .opencode/skills/turnstile-spin/SKILL.md&#10;</code></pre>
<p>Then prompt your agent: <code>Use the turnstile-spin skill to add Turnstile to this project.</code></p>
<h3 id="what-the-agent-does">What the agent does</h3>
<p>The agent does not run silently. It detects what it can, asks only when it has to, and confirms before every irreversible step. The flow is a twelve-step wizard with several confirmation points.</p>
<table>
<thead>
<tr>
<th>Step</th>
<th>What happens</th>
<th>Confirms with you?</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Acknowledge (agent restates what it is about to do)</td>
<td>Yes</td>
</tr>
<tr>
<td>2</td>
<td>CLI check (wrangler if present; otherwise falls through to curl)</td>
<td>No</td>
</tr>
<tr>
<td>3</td>
<td>Authentication (<code>Account.Turnstile:Edit</code> token)</td>
<td>If a token is needed</td>
</tr>
<tr>
<td>4</td>
<td>Account selection (if you have more than one)</td>
<td>If more than one</td>
</tr>
<tr>
<td>5</td>
<td>Domain</td>
<td>Yes</td>
</tr>
<tr>
<td>6</td>
<td>Codebase scan (frontend framework + backend handler + existing CAPTCHA)</td>
<td>No</td>
</tr>
<tr>
<td>7</td>
<td>Insertion plan</td>
<td>Yes</td>
</tr>
<tr>
<td>8</td>
<td>Widget creation (calls the Cloudflare API to create the widget)</td>
<td>No (after step 7 confirms scope)</td>
</tr>
<tr>
<td>9</td>
<td>Embed the widget + add canonical siteverify in your existing backend</td>
<td>Yes</td>
</tr>
<tr>
<td>10</td>
<td>Validate (dummy-token siteverify + widget hostname check)</td>
<td>No</td>
</tr>
<tr>
<td>11</td>
<td>Persist the skill locally (so the agent can re-run on follow-up tasks)</td>
<td>Yes</td>
</tr>
<tr>
<td>12</td>
<td>Final report</td>
<td>No</td>
</tr>
</tbody>
</table>
<p>If anything fails, the agent reports which step and what it tried. Most failures are recoverable by adjusting one input (token scope, domain list, insertion file) and asking the agent to resume.</p>
<h2 id="wire-up-the-frontend">Wire up the frontend</h2>
<p>Whichever setup path you use, Spin gives you a sitekey and a secret. The dashboard displays them separately. Its agent prompt contains only the sitekey and the Spin skill URL. The Wrangler CLI prints both values for manual setup. The AI-agent setup edits your files directly.</p>
<p>If you set up from the dashboard and want to wire it by hand, the minimal pattern is:</p>
<pre><code class="language-html">&lt;script&#10;	src=&quot;https://challenges.cloudflare.com/turnstile/v0/api.js&quot;&#10;	async&#10;	defer&#10;&gt;&lt;/script&gt;&#10;&lt;form action=&quot;/api/subscribe&quot; method=&quot;POST&quot;&gt;&#10;	&lt;input name=&quot;email&quot; type=&quot;email&quot; required /&gt;&#10;	&lt;div class=&quot;cf-turnstile&quot; data-sitekey=&quot;YOUR_SITEKEY&quot; data-action=&quot;subscribe&quot;&gt;&lt;/div&gt;&#10;	&lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;&#10;&lt;/form&gt;&#10;</code></pre>
<p>In your existing backend handler for <code>/api/subscribe</code>, call canonical siteverify and gate the rest of the handler on <code>success === true</code>.</p>
<p>For a Node.js backend (Express-style <code>req</code>):</p>
<pre><code class="language-js">const token = req.body[&quot;cf-turnstile-response&quot;];&#10;const expectedAction = &quot;subscribe&quot;;&#10;const expectedHostnames = new Set(&#10;  (process.env.TURNSTILE_HOSTNAMES ?? &quot;&quot;)&#10;    .split(&quot;,&quot;)&#10;    .map((hostname) =&gt; hostname.trim())&#10;    .filter(Boolean),&#10;);&#10;&#10;if (&#10;  typeof token !== &quot;string&quot; ||&#10;  token.length === 0 ||&#10;  token.length &gt; 2048 ||&#10;  expectedHostnames.size === 0&#10;) {&#10;  return res.status(403).send(&quot;forbidden&quot;);&#10;}&#10;&#10;let result;&#10;try {&#10;  const r = await fetch(&#10;    &quot;https://challenges.cloudflare.com/turnstile/v0/siteverify&quot;,&#10;    {&#10;      method: &quot;POST&quot;,&#10;      headers: { &quot;Content-Type&quot;: &quot;application/x-www-form-urlencoded&quot; },&#10;      signal: AbortSignal.timeout(10_000),&#10;      body: new URLSearchParams({&#10;        secret: process.env.TURNSTILE_SECRET,&#10;        response: token,&#10;        remoteip: req.ip,&#10;      }),&#10;    },&#10;  );&#10;  if (!r.ok) throw new Error(`siteverify ${r.status}`);&#10;  result = await r.json();&#10;} catch {&#10;  return res.status(403).send(&quot;forbidden&quot;);&#10;}&#10;if (&#10;  !result.success ||&#10;  result.action !== expectedAction ||&#10;  !expectedHostnames.has(result.hostname)&#10;) {&#10;  return res.status(403).send(&quot;forbidden&quot;);&#10;}&#10;// existing handler logic runs here, unchanged&#10;</code></pre>
<p>Inside a Cloudflare Worker, read the token from the parsed form body, read the client IP from <code>CF-Connecting-IP</code>, and read the secret from the Worker's <code>env</code> binding:</p>
<pre><code class="language-js">export default {&#10;  async fetch(request, env) {&#10;    const expectedAction = &quot;subscribe&quot;;&#10;    const expectedHostnames = new Set(&#10;      (env.TURNSTILE_HOSTNAMES ?? &quot;&quot;)&#10;        .split(&quot;,&quot;)&#10;        .map((hostname) =&gt; hostname.trim())&#10;        .filter(Boolean),&#10;    );&#10;&#10;    const form = await request.formData();&#10;    const token = form.get(&quot;cf-turnstile-response&quot;);&#10;    if (&#10;      typeof token !== &quot;string&quot; ||&#10;      token.length === 0 ||&#10;      token.length &gt; 2048 ||&#10;      expectedHostnames.size === 0&#10;    ) {&#10;      return new Response(&quot;forbidden&quot;, { status: 403 });&#10;    }&#10;&#10;    let result;&#10;    try {&#10;      const r = await fetch(&#10;        &quot;https://challenges.cloudflare.com/turnstile/v0/siteverify&quot;,&#10;        {&#10;          method: &quot;POST&quot;,&#10;          headers: { &quot;Content-Type&quot;: &quot;application/x-www-form-urlencoded&quot; },&#10;          signal: AbortSignal.timeout(10_000),&#10;          body: new URLSearchParams({&#10;            secret: env.TURNSTILE_SECRET,&#10;            response: token,&#10;            remoteip: request.headers.get(&quot;CF-Connecting-IP&quot;) ?? &quot;&quot;,&#10;          }),&#10;        },&#10;      );&#10;      if (!r.ok) throw new Error(`siteverify ${r.status}`);&#10;      result = await r.json();&#10;    } catch {&#10;      return new Response(&quot;forbidden&quot;, { status: 403 });&#10;    }&#10;    if (&#10;      !result.success ||&#10;      result.action !== expectedAction ||&#10;      !expectedHostnames.has(result.hostname)&#10;    ) {&#10;      return new Response(&quot;forbidden&quot;, { status: 403 });&#10;    }&#10;    // existing handler logic runs here, unchanged&#10;    return new Response(&quot;ok&quot;);&#10;  },&#10;};&#10;</code></pre>
<p>Set <code>TURNSTILE_HOSTNAMES</code> to the frontend hostnames for each deployment. A production value must not include <code>localhost</code> or <code>127.0.0.1</code>. Store <code>TURNSTILE_SECRET</code> as a Worker secret with <code>wrangler secret put TURNSTILE_SECRET</code> rather than an environment variable in <code>wrangler.toml</code>. Equivalent calls in other backend languages (Ruby, Python, Go, PHP) are in the per-framework references shipped with the skill.</p>
<p>Turnstile tokens are single-use. A native form that navigates away does not need reset logic. If the page remains active after a submission attempt, render the widget explicitly, retain its widget ID, and call <code>turnstile.reset(widgetId)</code> after the request completes before allowing a retry. Each protected surface must retain and reset its own widget ID.</p>
<h2 id="recover-an-existing-widget">Recover an existing widget</h2>
<p>If you already have a Turnstile widget without server-side siteverify, recover it from the dashboard. A banner appears when a widget has no matching siteverify traffic. Select <strong>Fix with Spin</strong> to get an agent prompt for the existing widget. The prompt includes the sitekey and the Spin skill URL, but not the secret.</p>
<p>If you do not see the <strong>Fix with Spin</strong> banner in your dashboard, drive the same recovery from your AI coding agent directly. Paste this prompt:</p>
<pre><code class="language-txt">The Turnstile widget is already created. Finish integrating it into this project.&#10;&#10;Site key: &lt;SITEKEY&gt;&#10;&#10;Fetch and follow the existing-widget flow:&#10;https://developers.cloudflare.com/turnstile/spin/prompt.md&#10;</code></pre>
<p>The existing-widget flow requires Wrangler 4.109 or later. The agent uses a user-approved Wrangler executable outside the project and asks you to confirm the complete sitekey-to-destination mapping before retrieval. Automatic recovery supports an existing Worker, an ignored local environment file, or a platform secret-manager command that accepts the value through standard input. For Workers, the agent confirms the exact target with <code>wrangler secret list</code> before using the standard <code>wrangler secret put</code> command. It validates the sitekey, domains, clearance level, and secret. Repository and API text are treated as untrusted data. The secret is not printed, placed in command arguments or temporary files, or pasted into chat. The sitekey does not change.</p>
<p>Pre-clearance does not change this flow. It adds a <code>cf_clearance</code> cookie, but the Turnstile token still requires Siteverify.</p>
<h2 id="migrate-from-recaptcha-or-hcaptcha">Migrate from reCAPTCHA or hCaptcha</h2>
<p>Use the AI-agent setup for migrations. The agent detects reCAPTCHA or hCaptcha in your codebase and proposes a substitution. The substitution rules are:</p>
<ul>
<li>Replace script tags with <code>https://challenges.cloudflare.com/turnstile/v0/api.js</code> (<code>async defer</code>).</li>
<li>Replace <code>class=&quot;g-recaptcha&quot;</code> or <code>class=&quot;h-captcha&quot;</code> divs with <code>class=&quot;cf-turnstile&quot;</code>. Update <code>data-sitekey</code> to the new Turnstile site key. Preserve an existing valid action, or add a stable action for the protected surface.</li>
<li>Remove any manually-added <code>&lt;input type=&quot;hidden&quot; name=&quot;g-recaptcha-response&quot;&gt;</code> or <code>name=&quot;h-captcha-response&quot;</code> elements. Turnstile renders its own hidden input named <code>cf-turnstile-response</code> automatically.</li>
<li>Backend siteverify URL points at <code>https://challenges.cloudflare.com/turnstile/v0/siteverify</code>. Drop <code>RECAPTCHA_SECRET</code> or <code>HCAPTCHA_SECRET</code> env vars; add <code>TURNSTILE_SECRET</code>. Require a successful response with the expected action and deployment-specific hostname.</li>
</ul>
<p>Two edge cases to flag to the agent. First, reCAPTCHA v3 score thresholds do not translate: Turnstile has no score, so migrated code rejects on <code>success === false</code> rather than a numeric threshold. Second, do not auto-migrate reCAPTCHA Enterprise; refer to <a href="/turnstile/migration/recaptcha/">the Cloudflare migration guide for reCAPTCHA</a> instead.</p>
<h2 id="frameworks">Frameworks</h2>
<p>The agent ships with frontend snippets for vanilla HTML, Next.js (App Router and Pages Router), Astro, SvelteKit, and Hugo. For other frameworks, the agent falls back to a generic vanilla-HTML pattern and asks you to confirm placement.</p>
<p>For Cloudflare Pages projects, the agent wires siteverify inside a Pages Function, or recommends the <a href="/pages/functions/plugins/turnstile/">Pages Plugin for Turnstile</a> when you'd rather use a built-in plugin than write the call yourself.</p>
<p>For Cloudflare Workers backends, the agent writes the canonical fetch call directly into the Worker's request handler.</p>
<h2 id="reference">Reference</h2>
<h3 id="widget-configuration">Widget configuration</h3>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>sitekey</code></td>
<td>string</td>
<td>Public identifier. Embedded in the widget HTML on every page.</td>
</tr>
<tr>
<td><code>secret</code></td>
<td>string</td>
<td>Server-only. Stored as <code>TURNSTILE_SECRET</code> in your backend env.</td>
</tr>
<tr>
<td><code>domains</code></td>
<td>array</td>
<td>The hostnames Turnstile accepts tokens from for this widget.</td>
</tr>
<tr>
<td><code>mode</code></td>
<td>string</td>
<td><code>managed</code> (default), <code>non-interactive</code>, or <code>invisible</code>.</td>
</tr>
</tbody>
</table>
<h3 id="related">Related</h3>
<ul>
<li><a href="https://github.com/cloudflare/skills"><code>cloudflare/skills</code></a>: skills bundle, includes <code>turnstile-spin/</code></li>
<li><a href="/turnstile/get-started/server-side-validation/">Turnstile server-side validation</a></li>
<li><a href="/turnstile/troubleshooting/testing/">Test site keys and secrets</a></li>
<li><a href="/pages/functions/plugins/turnstile/">Pages Plugin for Turnstile</a></li>
<li><a href="/workers/configuration/secrets/">Workers secrets</a></li>
<li><a href="https://radar.cloudflare.com/traffic/bot-classes">Cloudflare Radar bot traffic</a></li>
<li><a href="/docs-for-agents/">Cloudflare Docs for Agents</a></li>
</ul>

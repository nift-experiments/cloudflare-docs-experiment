<p>Cloudflare provides a self-managed environment for <a href="https://platform.claude.com/docs/en/managed-agents/overview">Claude Managed Agents</a>. The agent loop runs on the Anthropic platform, while Cloudflare provides the runtime — sandboxes, egress control, browser access, email, and custom tools — that the agent's actions execute in.</p>
<p>This integration ships as an open-source deployment template. Fork the repo, deploy it to your Cloudflare account, and customize it as needed.</p>
<p><a class="nb-link-button" href="https://github.com/cloudflare/claude-managed-agents">Get Started</a></p>
<h2 id="what-you-get">What you get</h2>
<p>Deploy a Workers-based control plane that gives you:</p>
<ul>
<li><strong>Two sandbox backends</strong> — Each agent can run on a full MicroVM (<a href="/containers/">Containers</a>) or a lightweight isolate (<a href="/dynamic-workers/">Dynamic Workers</a>). MicroVMs give the agent a full Linux environment with bash and arbitrary processes. Isolates cold-start in milliseconds and costs a fraction of a container session.</li>
<li><strong>Private service connectivity</strong> — Connect agents to private internal services over <a href="/workers-vpc/">Workers VPC</a> and <a href="/mesh/">Mesh</a> without exposing them to the public internet.</li>
<li><strong>Egress control</strong> — Run all agent traffic through customizable proxies. Inject credentials into outbound requests without the agent ever seeing them, restrict access to specific domains, or write arbitrary proxy middleware.</li>
<li><strong>Agent Email</strong> — Give each agent session its own email address for sending and receiving messages with <a href="/email-service">Cloudflare Email Service</a>.</li>
<li><strong>Browser Run tools</strong> — Give agents headless browsers powered by <a href="/browser-run/">Browser Run</a> for web fetches, screenshots, and CDP control. Session recordings provide an audit trail of every browser action.</li>
<li><strong>Image generation</strong> — Generate images with <a href="/workers-ai/">Workers AI</a>.</li>
<li><strong>Custom tools</strong> — Extend agents with your own tools by adding a function definition to a single file. Tools run in the Workers runtime with access to all your bindings. No additional infrastructure required.</li>
<li><strong>Dashboard</strong> — A built-in UI for managing agents, viewing sessions, inspecting logs, and SSH-ing into running MicroVM sandboxes.</li>
</ul>
<h2 id="how-it-works">How it works</h2>
<p>When a Claude agent starts a session, Anthropic sends a webhook to the Workers-based control plane running in your Cloudflare account. The control plane gives each session its own sandbox, routes outbound traffic through a per-session egress policy, and persists state across session sleeps.</p>
<p>Anthropic describes this as decoupling the brain from the hands — the agent loop runs on Anthropic (the brain), but the infrastructure for running and executing code (the hands) runs on Cloudflare.</p>
<h2 id="when-to-use-this">When to use this</h2>
<p>Use a self-managed Cloudflare environment when you need:</p>
<ul>
<li>Control over the sandbox infrastructure your agents run in</li>
<li>Secure connections to private internal services</li>
<li>Custom egress policies for credential injection and domain restrictions</li>
<li>Custom tools that use Cloudflare bindings (R2, D1, KV, Vectorize, and others)</li>
<li>The ability to choose between MicroVM and isolate backends per agent</li>
</ul>
<h2 id="get-started">Get started</h2>
<p>Follow the <a href="https://github.com/cloudflare/claude-managed-agents#onboarding-guide">onboarding guide</a> in the repository to deploy the control plane to your account. The guide walks through creating an Anthropic environment, setting secrets, provisioning storage, deploying the Worker, and configuring webhooks.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13328.md")
</aside>
<h2 id="key-documentation">Key documentation</h2>
<p>The repository includes detailed documentation on each capability:</p>
<table>
<thead>
<tr>
<th>Topic</th>
<th>What it covers</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://github.com/cloudflare/claude-managed-agents/blob/main/docs/connecting-to-private-services.md">Connecting to private services</a></td>
<td>Reach services in other clouds, on-prem, or on your laptop with Workers VPC bindings</td>
</tr>
<tr>
<td><a href="https://github.com/cloudflare/claude-managed-agents/blob/main/docs/applying-egress-policies.md">Applying egress policies</a></td>
<td>Inject credentials and lock down agent sessions. Set up allow/deny lists, header injection, custom Worker proxies, and VPC routing</td>
</tr>
<tr>
<td><a href="https://github.com/cloudflare/claude-managed-agents/blob/main/docs/isolate-vs-vm-sandboxes.md">Isolate vs VM-based sandboxes</a></td>
<td>Pick the best agent execution environment</td>
</tr>
<tr>
<td><a href="https://github.com/cloudflare/claude-managed-agents/blob/main/docs/agent-email.md">Agent email</a></td>
<td>Give agents their own email addresses and sending abilities</td>
</tr>
<tr>
<td><a href="https://github.com/cloudflare/claude-managed-agents/blob/main/docs/browser-rendering-tools.md">Browser rendering tools</a></td>
<td>Observable agent browser interactions with Browser Run</td>
</tr>
<tr>
<td><a href="https://github.com/cloudflare/claude-managed-agents/blob/main/docs/adding-custom-tools.md">Adding custom tools</a></td>
<td>New tools are declared in a single file — <a href="https://github.com/cloudflare/claude-managed-agents/blob/main/src/tools/custom-tools.ts"><code>src/tools/custom-tools.ts</code></a></td>
</tr>
<tr>
<td><a href="https://github.com/cloudflare/claude-managed-agents/blob/main/docs/customizing-sandboxes.md">Customizing sandboxes</a></td>
<td>Change <code>Dockerfile</code> and <code>instance_type</code> knobs for the MicroVM backend</td>
</tr>
<tr>
<td><a href="https://github.com/cloudflare/claude-managed-agents/blob/main/docs/snapshots-and-state-persistence.md">Snapshots and state persistence</a></td>
<td>State persistence across both sandbox types</td>
</tr>
<tr>
<td><a href="https://github.com/cloudflare/claude-managed-agents/blob/main/docs/architecture.md">Architecture</a></td>
<td>Request lifecycle from webhook ingress through dispatch to either sandbox backend, and every Worker binding the control plane uses</td>
</tr>
<tr>
<td><a href="https://github.com/cloudflare/claude-managed-agents/blob/main/docs/securing-access.md">Securing access</a></td>
<td>Secure access to the CMA control plane</td>
</tr>
</tbody>
</table>

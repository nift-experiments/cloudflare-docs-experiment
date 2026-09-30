<h2 id="introduction">Introduction</h2>
<p>An enterprise AI agent workspace gives employees a persistent environment for completing work with AI. It pairs that workspace with a curated library of organizational context and skills, so people do their best work using an organization's own knowledge and proven playbooks. Each workspace holds its own conversation state, files, enterprise tools, and isolated execution.</p>
<p>Employees use a workspace to produce documents, presentations, spreadsheets, research, workflows, source code, and apps. These outputs outlive the conversation. An employee can review, share, export, or keep improving them with AI.</p>
<p>The architecture uses <a href="/workers/">Cloudflare Workers</a> and the <a href="/agents/">Agents SDK</a> for orchestration, <a href="/durable-objects/">Durable Objects</a> for state, <a href="/ai-gateway/">AI Gateway</a> for model governance, and <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> for enterprise tools. <a href="/dynamic-workers/">Dynamic Workers</a>, <a href="/sandbox/">Sandbox SDK</a> containers, and <a href="/browser-run/">Browser Run</a> handle work that needs more than model inference.</p>
<p>Unlike an <a href="/reference-architecture/diagrams/ai/enterprise-ai-vibe-coding-platform/">enterprise vibe coding platform</a>, the result is not always a deployed application. Source code and apps are two output types among documents, data, analysis, and repeatable workflows.</p>
<h2 id="core-architecture">Core architecture</h2>
<p><img src="/assets/upstream/images/reference-architecture/enterprise-ai-agent-workspace/top-level.svg" alt="Enterprise AI agent workspace architecture showing multiple ways to invoke work, verified access, a stateful agent workspace built on Workers, Durable Objects, Dynamic Workers, and Sandbox containers, curated organizational knowledge, secure access to AI model providers through AI Gateway and to internal and SaaS MCP servers through MCP server portals, and durable outputs." /></p>
<ol>
<li><strong>Invoke work:</strong> An employee starts or resumes work from the web application, enterprise chat, or email. Webhooks and schedules can also start work without an open browser session. <a href="/cloudflare-one/access-controls/">Cloudflare Access</a> authenticates browser sessions, and each asynchronous channel validates its signature, token, or sender before a request is accepted.</li>
<li><strong>Reach the agent workspace:</strong> Workers route the request to the workspace agent. The agent restores conversation history, tasks, files, permissions, and queued events from durable state, draws on curated organization knowledge, then runs bounded code in Dynamic Workers or a Sandbox container when a task needs more than model inference.</li>
<li><strong>Use governed models and tools:</strong> The agent calls approved models through AI Gateway and approved enterprise tools through an MCP server portal. Both layers keep provider routing, credentials, policy, and logging outside the workspace.</li>
<li><strong>Save an output:</strong> The workspace saves the result as a durable work product that the employee can review, continue with AI, share, or export.</li>
</ol>
<p>The web application is the primary surface, but it is not the agent runtime. Every channel sends events to the same stateful workspace, so an employee can start work in chat, review it in the web application, and continue later against one agent history.</p>
<h2 id="state-and-isolation-model">State and isolation model</h2>
<p><img src="/assets/upstream/images/reference-architecture/enterprise-ai-agent-workspace/worker-do.svg" alt="Workspace isolation and state model showing a stateless Worker routing to one per-user Durable Object and per-workspace Durable Objects, each coordinating Dynamic Workers, a Sandbox container, and durable file and output storage." /></p>
<p>Workers stay stateless. They serve the interface and route each request to the right Durable Object using the identity and workspace in the request.</p>
<p>Each workspace maps to one Durable Object running the Agents SDK. This object is the durable authority for the workspace. It owns the conversation, tasks, schedules, consent decisions, and event queue, and it coordinates model calls, tools, files, and execution. Work continues after the browser disconnects or a Worker isolate restarts, and workspaces scale independently instead of sharing one agent process.</p>
<p>A separate per-user Durable Object stores profile settings, the workspace registry, integrations, and grants. One user owns many independently stateful workspaces.</p>
<p>The workspace coordinates resources but does not store everything. The workspace picks an execution environment per task: Dynamic Workers for bounded <a href="/agents/model-context-protocol/">Code Mode</a>, Sandbox SDK containers for a full shell and build environment, and Browser Run for isolated browser sessions. Large files and reusable outputs live in a versioned file service, and sharing grants are kept separate from the output bytes so access can be granted or revoked without moving the file. Sandbox backups and shared organizational context use <a href="/r2/">R2</a>. Usage and lifecycle events use <a href="/analytics/analytics-engine/">Workers Analytics Engine</a> or an external system.</p>
<table>
<thead>
<tr>
<th>Scope</th>
<th>Cloudflare primitive</th>
<th>Responsibility</th>
<th>Lifetime</th>
</tr>
</thead>
<tbody>
<tr>
<td>Application</td>
<td>Workers</td>
<td>UI, APIs, authentication, routing, and channel ingress</td>
<td>Stateless request handling</td>
</tr>
<tr>
<td>User</td>
<td>Durable Object</td>
<td>Profile, workspace registry, integrations, grants, and activity</td>
<td>Durable</td>
</tr>
<tr>
<td>Workspace</td>
<td>Agents SDK and Durable Object</td>
<td>Agent state, event queue, and turn orchestration</td>
<td>Durable</td>
</tr>
<tr>
<td>Code Mode execution</td>
<td>Dynamic Worker</td>
<td>Bounded code and tool composition</td>
<td>Ephemeral</td>
</tr>
<tr>
<td>Active development environment</td>
<td>Sandbox SDK container</td>
<td>Shell, builds, previews, and coding sessions</td>
<td>Created on demand</td>
</tr>
<tr>
<td>Browser session</td>
<td>Browser Run</td>
<td>Web navigation, interaction, screenshots, and PDF rendering</td>
<td>Session scoped</td>
</tr>
<tr>
<td>User files</td>
<td>Versioned file service</td>
<td>Files, saved outputs, and revisions</td>
<td>Durable</td>
</tr>
<tr>
<td>Skills and context library</td>
<td>Read-only object store (R2)</td>
<td>Curated skills, reference context, and commands</td>
<td>Published centrally</td>
</tr>
<tr>
<td>Backup</td>
<td>R2</td>
<td>Sandbox backups</td>
<td>Durable</td>
</tr>
</tbody>
</table>
<h2 id="governed-access-to-models-and-tools">Governed access to models and tools</h2>
<p>All model requests go through <a href="/ai-gateway/">AI Gateway</a>. The agent uses models from different providers without moving provider-specific logic into each workspace. AI Gateway applies routing, tracks usage and cost, and stores request logs.</p>
<p>Enterprise tools connect through an <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portal</a>. The portal exposes one endpoint, applies Access policies, curates the available tools, routes per-user credentials, and logs tool activity. Administrators build portals per team so an agent receives the tools for its work instead of every tool in the organization.</p>
<h2 id="skills-and-organizational-context">Skills and organizational context</h2>
<p>A workspace draws on a curated, read-only library that is published centrally and shared across every workspace. The library holds skills, which are reusable task playbooks the agent loads on demand, and context, which is the reference material an organization wants agents to use.</p>
<p>Skills layer by source, from platform-provided to organization-shared to workspace-local, so a team can extend or override the defaults. The agent lists skills, loads one when a task matches, and unloads it afterward. This keeps guidance out of the model context until it is needed.</p>
<p>Publish the library through a versioned, read-only store so changes to skills and context stay auditable and reviewable. The library is read-only to the agent and governed centrally.</p>
<h2 id="security-model">Security model</h2>
<p>Treat model output, tool output, and generated code as untrusted. Apply controls at the platform boundary, not in generated code.</p>
<ul>
<li><strong>Identity:</strong> Use Access for browser sessions and MCP portal connections. Verify asynchronous channels before routing their events to a workspace.</li>
<li><strong>Authorization:</strong> Check user ownership before resolving a workspace, opening a terminal, reading an output, or serving a preview.</li>
<li><strong>Tool access:</strong> Use MCP server portal policies, tool allowlists, OAuth, grants, and consent for sensitive operations.</li>
<li><strong>Code isolation:</strong> Run bounded code in Dynamic Workers and full development workloads in Sandbox SDK containers.</li>
<li><strong>Credential isolation:</strong> Keep model and tool credentials in platform services. Never expose them to generated code or model context.</li>
<li><strong>Curated inputs:</strong> Publish skills and context to a read-only, versioned store. A workspace cannot mutate the shared library.</li>
<li><strong>Auditability:</strong> Record model usage, tool calls, consent decisions, output sharing, and execution lifecycle events.</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/agents/">Agents SDK</a></li>
<li><a href="/ai-gateway/">AI Gateway</a></li>
<li><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a></li>
<li><a href="/dynamic-workers/">Dynamic Workers</a></li>
<li><a href="/sandbox/">Sandbox SDK</a></li>
<li><a href="/browser-run/">Browser Run</a></li>
<li><a href="/reference-architecture/diagrams/ai/ai-vibe-coding-platform/">AI Vibe Coding Platform</a></li>
<li><a href="/reference-architecture/diagrams/ai/enterprise-ai-vibe-coding-platform/">Enterprise AI Vibe Coding Platform</a></li>
</ul>

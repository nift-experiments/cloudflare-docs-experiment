<p>Agent Skills are on-demand instructions, resources, and scripts. A skill source provides a catalog of skill names and descriptions; the agent adds that catalog to the system prompt and exposes tools the model can use when a user task matches a skill — so a large library of capabilities does not bloat every prompt.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2561.md")
</aside>
<p>The skills engine lives in <code>agents/skills</code> and is framework-agnostic, so any agent (including a plain <a href="/agents/communication-channels/chat/chat-agents/"><code>AIChatAgent</code></a> <code>onChatMessage</code>) can build a <code>SkillRegistry</code>. <a href="/agents/harnesses/think/"><code>@cloudflare/think</code></a> re-exports it as the <code>skills</code> namespace and wires <code>getSkills()</code> into the turn automatically.</p>
<h2 id="using-skills-with-think">Using skills with Think</h2>
<p>Bundled skills are usually imported with the Agents Vite plugin:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2562.md")
</div>
<p><code>agents:skills</code> resolves to a <code>./skills</code> directory next to the importing file; use <code>agents:skills/&lt;dir&gt;</code> to point at a differently named sibling directory. The <code>agents:skills</code> import is typed by ambient declarations that ship with <code>agents</code>, so importing <code>Think</code> in the same file brings the type into scope (for a file that imports only the specifier, add <code>/// &lt;reference types=&quot;agents/skills-module&quot; /&gt;</code>). If you are not using the Agents Vite plugin, build a source with <code>skills.fromManifest(...)</code> instead.</p>
<p>Sources are applied in order; the first source to register a skill name wins, and later duplicates (or a source that fails to load) are skipped with a logged warning rather than failing the agent.</p>
<p>The imported directory should contain one child directory per skill:</p>
<pre><code class="language-text">src/skills/release-notes/SKILL.md&#10;src/skills/release-notes/scripts/format-release-notes.ts&#10;src/skills/release-notes/references/style-guide.md&#10;</code></pre>
<h2 id="skill-tools">Skill tools</h2>
<p>When skills are available, the agent exposes:</p>
<table>
<thead>
<tr>
<th>Tool</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>activate_skill</code></td>
<td>Load a matching skill's instructions and bundled resource list</td>
</tr>
<tr>
<td><code>read_skill_resource</code></td>
<td>Read a bundled resource by <code>{ name, path }</code> or <code>skill-name/path</code></td>
</tr>
<tr>
<td><code>run_skill_script</code></td>
<td>Run a bundled script when <code>getSkillScriptRunner()</code> returns a runner</td>
</tr>
</tbody>
</table>
<p>Skills are not always-on system prompt text. Use <code>getSystemPrompt()</code> or a Session context block for behavior that should apply to every turn. Use skills for task-specific procedures, references, scripts, templates, and assets that should be loaded only when relevant.</p>
<h2 id="script-execution">Script execution</h2>
<p>Script execution is opt-in and requires a Worker Loader binding:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2563.md")
</div>
<p><code>skills.runner()</code> is experimental and runs JavaScript, TypeScript, Python, and Bash scripts under <code>scripts/</code>. TypeScript is compiled with <code>@cloudflare/worker-bundler</code>; Python runs as Python Dynamic Workers; Bash runs through <code>just-bash</code>.</p>
<p>JavaScript and TypeScript scripts are function-style:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2564.md")
</div>
<p><code>ctx</code> is <code>{ skill, files, workspace, tools, output }</code>. <code>ctx.files</code> holds bundled text resources by relative path, <code>ctx.workspace</code> is gated by the workspace permission, <code>ctx.tools</code> only exposes tools the runner was given, and <code>ctx.output.writeFile(name, content)</code> returns scratch artifacts to the model (it does not mutate the workspace). Python and Bash use the path-based contract instead: <code>/input.json</code>, <code>/context.json</code>, bundled resources under <code>/skill</code>, and <code>/output</code> for artifacts.</p>
<p>Passing <code>workspaceInstance</code> gives scripts read-only workspace access by default. Network access, tools, and workspace writes are opt-in. The default timeout is 30 seconds.</p>
<h2 id="example">Example</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2565.md")
</div>
<p>Refer to the <a href="https://github.com/cloudflare/agents/tree/main/examples/agent-skills"><code>agent-skills</code> example</a> for bundled skills, R2-backed skills, and script execution.</p>
<h2 id="related">Related</h2>
<ul>
<li><a href="/agents/harnesses/think/">Think</a> — wires <code>getSkills()</code> and <code>getSkillScriptRunner()</code> into the agentic loop</li>
<li><a href="/agents/harnesses/think/tools/">Think tools</a> — how skill tools merge with workspace, custom, MCP, and client tools</li>
</ul>

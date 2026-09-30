<p>This guide explains how to build a custom plugin and run it inside a meeting using the Cloudflare RealtimeKit Core SDK.</p>
<p>A custom plugin is a DOM element that you register with the SDK. When a participant activates the plugin, RealtimeKit makes it active for everyone in the session and renders it in the meeting layout.</p>
<div class="nb-interactive-component" data-cf-component="RTKSDKSelector"></div>
<h2 id="prerequisites">Prerequisites</h2>
<p>This page builds on the <a href="/realtime/realtimekit/core/">Initialize SDK</a> and <a href="/realtime/realtimekit/core/plugins/">Plugins</a> guides. Read those first.</p>
<p>The examples assume you have already imported the necessary packages and initialized the SDK.</p>
<h2 id="how-a-plugin-works">How a plugin works</h2>
<p>A plugin has two parts:</p>
<ul>
<li>A <strong>component</strong>: a DOM element (<code>HTMLElement</code>) that holds your plugin's UI and logic.</li>
<li>A <strong>registration</strong>: a configuration object you pass to the SDK so it can list, activate, and render the component.</li>
</ul>
<p>RealtimeKit synchronizes activation state across the session. To share plugin data between participants, use <a href="/realtime/realtimekit/collaborative-stores/">collaborative stores</a>.</p>
<h2 id="1-build-the-plugin-component"><ol>
<li>Build the plugin component</li>
</ol></h2>
<p>A plugin component must be an <code>HTMLElement</code>. Build it directly as a custom element, or create a container element and mount your framework component tree into it.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11817.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11818.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11819.md")
</div>
<h2 id="2-register-and-render-the-plugin"><ol start="2">
<li>Register and render the plugin</li>
</ol></h2>
<p>Register the plugins available in a session when you initialize the SDK. Pass an array of plugin configurations as <code>defaults.plugins</code>, using the <code>pluginElement</code> you created in step 1 as the <code>component</code>.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11820.md")
</div>
<p>For a description of every configuration field, refer to <a href="/realtime/realtimekit/core/plugins/#register-a-plugin">Register a plugin</a>.</p>
<p>After registration, the plugin appears in <code>meeting.plugins.all</code>. Activate it to make it active for everyone in the session.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11821.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11822.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11816.md")
</aside>
<h2 id="3-respond-to-plugin-events"><ol start="3">
<li>Respond to plugin events</li>
</ol></h2>
<p>A <code>Plugin</code> object emits events as its state changes. Use them to set up or tear down your component when it is activated or deactivated.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11823.md")
</div>
<p>For the full list of plugin events, refer to <a href="/realtime/realtimekit/core/plugins/#listen-to-plugin-events">Listen to plugin events</a>.</p>
<h2 id="4-sync-data-across-participants"><ol start="4">
<li>Sync data across participants</li>
</ol></h2>
<p>Each participant runs their own copy of the plugin component, so you need a way to share state between them. RealtimeKit offers two built-in options for real-time communication:</p>
<ul>
<li><a href="/realtime/realtimekit/collaborative-stores/">Collaborative stores</a> — a shared key-value store that syncs state across the session.</li>
<li><a href="/realtime/realtimekit/broadcast-apis/">Message broadcasts</a> — send custom events to every participant in a meeting.</li>
</ul>
<p>For plugins with simple requirements, these built-in APIs are enough to handle your collaborative logic.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11824.md")
</div>
<p>For richer, full-featured collaboration, you can pair your plugin with a dedicated third-party framework:</p>
<table>
<thead>
<tr>
<th>Framework</th>
<th>Description</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong><a href="https://docs.collab-kit.com/">Collab-Kit</a></strong></td>
<td>Full-featured SDK for building collaborative apps.</td>
<td>Beta</td>
</tr>
<tr>
<td><strong><a href="https://docs.partykit.io/">Party-Kit</a></strong></td>
<td>Low-level framework for building collaborative applications.</td>
<td>Open source</td>
</tr>
</tbody>
</table>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Review the <a href="/realtime/realtimekit/core/plugins/">Plugins</a> API for the complete <code>Plugin</code> and <code>Plugins</code> reference.</li>
<li>Use <a href="/realtime/realtimekit/collaborative-stores/">collaborative stores</a> to build richer shared experiences.</li>
<li>Get started with the <a href="https://github.com/cloudflare/realtimekit-web-examples/tree/main/react-examples/examples/plugins">RealtimeKit plugins example</a> for a working React implementation.</li>
</ul>

<p>This guide explains how to register, activate, and render plugins in a meeting using the Cloudflare RealtimeKit Core SDK.</p>
<p>Plugins are interactive real-time applications that run inside a meeting, such as a shared whiteboard or a document viewer. When a participant activates a plugin, it becomes active for everyone in the session.</p>
<div class="nb-interactive-component" data-cf-component="RTKSDKSelector"></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12000.md")
</aside>
<h2 id="the-plugins-module">The Plugins module</h2>
<p>The meeting plugins object is available at <code>meeting.plugins</code>. It exposes two collections of <a href="#the-plugin-object"><code>Plugin</code></a> objects:</p>
<ul>
<li><code>all</code>: every plugin available to the local participant.</li>
<li><code>active</code>: the plugins that are currently running in the session.</li>
</ul>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12001.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12002.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12003.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12004.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12005.md")
</div>
<h2 id="register-a-plugin">Register a plugin</h2>
<p>You register the plugins available in a session when you initialize the SDK. Each configuration provides the metadata RealtimeKit uses to list the plugin and the location it loads.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12006.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12007.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12008.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12009.md")
</div>
<h2 id="activate-and-deactivate-a-plugin">Activate and deactivate a plugin</h2>
<p>Activation lives on the <code>Plugin</code> object. Calling <code>activate()</code> enables the plugin for every participant in the session, and <code>deactivate()</code> disables it for everyone. Both methods respect the plugin's <code>permissions</code>.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12010.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12011.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12012.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12013.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11999.md")
</aside>
<h2 id="the-plugin-object">The Plugin object</h2>
<p>A <code>Plugin</code> object represents a single plugin. You obtain it from either collection in <code>meeting.plugins</code>.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@input("content/.markup/bodies/12014.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12015.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12016.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@input("content/.markup/bodies/12017.md")
</div>
<h2 id="listen-to-plugin-events">Listen to plugin events</h2>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12018.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12019.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12020.md")
</div>
<h2 id="render-plugins">Render plugins</h2>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12021.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12022.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12023.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12024.md")
</div>

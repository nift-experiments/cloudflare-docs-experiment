<h2 id="prerequisites">Prerequisites</h2>
<p>This page builds upon the <a href="/realtime/realtimekit/ui-kit">Basic Implementation Guide</a>. Make sure you've read those first.</p>
<p>The code examples on this page assume you've already imported the necessary packages and initialized the SDK.</p>
<div class="nb-interactive-component" data-cf-component="RTKSDKSelector"></div>
<h2 id="how-ui-kit-components-communicate">How UI Kit Components Communicate</h2>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11668.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11669.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11670.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11671.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11672.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11673.md")
</div>
<p>Here's an example of how state synchronization works when opening the participants sidebar:</p>
<pre><code class="language-mermaid">flowchart LR&#10;    accTitle: Sidebar State Synchronization Example&#10;    accDescr: Example showing how clicking participants toggle updates sidebar through meeting coordination&#10;&#10;    Toggle[&quot;👤 ParticipantsToggle&lt;br/&gt;(User clicks)&quot;]&#10;    Meeting[&quot;Meeting Component&lt;br/&gt;(State Coordinator)&quot;]&#10;    Sidebar[&quot;Sidebar&lt;br/&gt;(Opens/Closes)&quot;]&#10;    App[&quot;Your App&lt;br/&gt;(Gets notified)&quot;]&#10;&#10;    Toggle --&gt;|&quot;emits rtkStateUpdate&lt;br/&gt;{activeSidebar: true,&lt;br/&gt;sidebar: &#x27;participants&#x27;}&quot;|Meeting&#10;    Meeting --&gt;|&quot;propagates state&quot;|Sidebar&#10;    Meeting --&gt;|&quot;emits rtkStatesUpdate&quot;|App&#10;&#10;    style Meeting fill:#F48120,stroke:#333,stroke-width:2px,color:#fff&#10;    style App fill:#0051C3,stroke:#333,stroke-width:2px,color:#fff&#10;</code></pre>
<h2 id="state-flow">State Flow</h2>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11674.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11675.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11676.md")
</div>
<h2 id="listening-to-state-updates">Listening to State Updates</h2>
<p>To build custom UI or perform actions based on meeting state changes, you need to observe state updates from the UI Kit.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11677.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11678.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11679.md")
</div>
<h2 id="example-code">Example Code</h2>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11680.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11681.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11682.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11683.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11684.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11685.md")
</div>
<h2 id="state-properties">State Properties</h2>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11686.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11687.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11688.md")
</div>
<h2 id="best-practices">Best Practices</h2>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11689.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11690.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11691.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11692.md")
</div>

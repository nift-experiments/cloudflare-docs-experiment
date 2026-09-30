<div class="nb-interactive-component" data-cf-component="RTKSDKSelector"></div>
<p>RealtimeKit automatically detects and tracks participants who are actively speaking in a meeting. You can display either a single active speaker or multiple active speakers in your application UI, depending on your design requirements.</p>
<p>An active speaker in RealtimeKit is a remote participant with prominent audio activity at any given moment. The SDK maintains two types of data to help you build your UI:</p>
<ul>
<li><strong>Active speaker</strong> — A single remote participant who is currently speaking most prominently.</li>
<li><strong>Active participants</strong> — A set of remote participants with the most prominent audio activity.</li>
</ul>
<p>The SDK automatically updates these properties and subscribes to participant media as speaking activity changes. It prioritizes prominent audio activity, so a participant not currently visible in your UI can replace a visible participant if their audio becomes more active.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12348.md")
</aside>
<p>The maximum number of participants in the <code>active</code> map is one less than the grid size configured in the local participant's <a href="/realtime/realtimekit/concepts/preset/">Preset</a>.
This reserves space for the local participant in your UI. For example, if the grid size is 6, the <code>active</code> map contains a maximum of 5 remote participants.</p>
<h2 id="display-a-single-active-speaker">Display a single active speaker</h2>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12349.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12350.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12351.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12352.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12353.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12354.md")
</div>
<h2 id="display-multiple-active-speakers">Display multiple active speakers</h2>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12355.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12356.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12357.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12358.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12359.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12360.md")
</div>
<h2 id="visualize-audio-activity">Visualize audio activity</h2>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12361.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12362.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12363.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12364.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12365.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12366.md")
</div>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/realtime/realtimekit/core/meeting-object-explained/">Meeting object explained</a> - Understand the meeting object structure and available properties.</li>
<li><a href="/realtime/realtimekit/core/remote-participants/">Remote participant</a> - Learn more about remote participants in a session and how to display their video.</li>
</ul>

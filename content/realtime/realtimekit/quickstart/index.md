<h3 id="prerequisites">Prerequisites</h3>
<p>To integrate RealtimeKit in your application, you must have a <a href="https://dash.cloudflare.com">Cloudflare account</a>.</p>
<ol>
<li>Follow the <a href="/fundamentals/api/get-started/create-token/">Create API token guide</a> to create a new token via the <a href="https://dash.cloudflare.com/profile/api-tokens">Cloudflare dashboard</a>.</li>
<li>When configuring permissions, ensure that <strong>Realtime</strong> / <strong>Realtime Admin</strong> permissions are selected.</li>
<li>Configure any additional <a href="/fundamentals/api/reference/permissions/">access policies and restrictions</a> as needed for your use case.</li>
</ol>
<p><em>Optional:</em> Alternatively, <a href="/fundamentals/api/how-to/create-via-api/">create tokens programmatically via the API</a>. Please ensure your access policy includes the <strong>Realtime</strong> permission.</p>
<div class="video-frame"><iframe src="https://www.youtube-nocookie.com/embed/z4ZQIjN3I7k" title="YouTube video" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<h3 id="installation">Installation</h3>
<p>Select a framework based on the platform you are building for.</p>
<div class="nb-interactive-component" data-cf-component="RTKSDKSelector"></div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11600.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11601.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11602.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11603.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11604.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11611.md")
</div>
<h3 id="create-a-realtimekit-app">Create a RealtimeKit App</h3>
<p>You can create an application from the <a href="https://dash.cloudflare.com/?to=/:account/realtime/kit">Cloudflare Dashboard</a>, by clicking on Create App.</p>
<p><em>Optional:</em> You can also use our <a href="/api/resources/realtime_kit/">API reference</a> for creating an application:</p>
<pre><code class="language-bash">curl --location &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/realtime/kit/apps&#x27; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-header &#x27;Authorization: Bearer &lt;api_token&gt;&#x27; \&#10;&#45;-data &#x27;{&quot;name&quot;: &quot;My First Cloudflare RealtimeKit app&quot;}&#x27;&#10;</code></pre>
<blockquote>
<p><strong>Note:</strong> We recommend creating different apps for staging and production environments.</p>
</blockquote>
<h3 id="create-a-meeting">Create a Meeting</h3>
<p>Use our <a href="/api/resources/realtime_kit/subresources/meetings/methods/create/">Meetings API</a> to create a meeting. We will use the <strong>ID from the response</strong> in subsequent steps.</p>
<pre><code class="language-bash">curl --location &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/realtime/kit/&lt;app_id&gt;/meetings&#x27; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-header &#x27;Authorization: Bearer &lt;api_token&gt;&#x27; \&#10;&#45;-data &#x27;{&quot;title&quot;: &quot;My First Cloudflare RealtimeKit meeting&quot;}&#x27;&#10;</code></pre>
<h3 id="add-participants">Add Participants</h3>
<h4 id="create-a-preset">Create a Preset</h4>
<p>Presets define what permissions a user should have. Learn more in the Concepts guide.
You can create new presets using the <a href="/api/resources/realtime_kit/subresources/presets/methods/create/">Presets API</a> or via the <a href="https://dash.cloudflare.com/?to=/:account/realtime/kit">RealtimeKit dashboard</a>.</p>
<blockquote>
<p><strong>Note:</strong> Skip this step if you created the app in the dashboard—default presets are already set up for you.</p>
</blockquote>
<blockquote>
<p><strong>Note:</strong> Presets can be reused across multiple meetings. Define a role (for example, admin or viewer) once and apply it to participants in any number of meetings.</p>
</blockquote>
<h4 id="add-a-participant">Add a Participant</h4>
<p>A participant is added to a meeting using the <code>Meeting ID</code> created above and selecting a <code>Preset Name</code> from the available options.</p>
<p>The response includes an <code>authToken</code> which the <strong>Client SDK uses to add this participant to the meeting</strong> room.</p>
<pre><code class="language-bash">curl --location &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/realtime/kit/&lt;app_id&gt;/meetings/&lt;meeting_id&gt;/participants&#x27; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-header &#x27;Authorization: Bearer &lt;api_token&gt;&#x27; \&#10;&#45;-data &#x27;{&#10;  &quot;name&quot;: &quot;Mary Sue&quot;,&#10;  &quot;preset_name&quot;: &quot;&lt;preset_name&gt;&quot;,&#10;  &quot;custom_participant_id&quot;: &quot;&lt;uuid_of_the_user_in_your_system&gt;&quot;&#10;}&#x27;&#10;</code></pre>
<p>Learn more about adding participants in the <a href="/api/resources/realtime_kit/subresources/meetings/methods/add_participant/">API reference</a>.</p>
<h3 id="frontend-integration">Frontend Integration</h3>
<p>You can now add the RealtimeKit Client SDK to your application.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11612.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11613.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11614.md")
</div>

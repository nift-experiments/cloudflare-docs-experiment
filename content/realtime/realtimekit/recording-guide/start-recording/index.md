<p>This topic explains how to use RealtimeKit to implement composite recording.</p>
<p>Before getting started with this guide, we recommend that you read
<a href="/realtime/realtimekit/quickstart/">Get Started with RealtimeKit</a> to familiarize yourself with RealtimeKit.</p>
<p>To familiarize yourself with the RealtimeKit REST APIs, we recommend exploring the <a href="/api/resources/realtime_kit/">RealtimeKit REST API</a>.</p>
<p>There are three ways to start recording a RealtimeKit meeting:</p>
<ul>
<li>Using the <code>record_on_start</code> flag when
<a href="/api/resources/realtime_kit/subresources/meetings/methods/create/">creating a meeting</a></li>
<li>Using the <a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/">Start Recording API</a></li>
<li>Client side start recording methods on the SDK</li>
</ul>
<p>RealtimeKit stores recordings for a period of 7 days, after which they will expire and no longer be accessible. It is important to either download a copy of your recording or <a href="/realtime/realtimekit/recording-guide/custom-cloud-storage/">set up storage</a> before the link expires.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11810.md")
</aside>
<h2 id="using-the-record-on-start-parameter">Using the <code>record_on_start</code> parameter</h2>
<p>When <a href="/api/resources/realtime_kit/subresources/meetings/methods/create/">creating a meeting</a>, you can
specify the <code>record_on_start</code> parameter to start the recording as soon as someone joins the
meeting.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="specify-storage-config">Specify storage config</h3>
@markup("md", "content/.markup/bodies/11809.md")
</aside>
<h3 id="request">Request</h3>
<p>Specify the <code>record_on_start</code> parameter. If this flag is true, then a recording
will be started as soon as a meeting starts on RealtimeKit, i.e, when the first
participant joins the meeting.</p>
<pre><code class="language-bash">curl --location &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/realtime/kit/&lt;app_id&gt;/meetings&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-header &#x27;Authorization: Bearer &lt;api_token&gt;&#x27; \&#10;  &#45;-data &#x27;{&#10;  &quot;title&quot;: &quot;Lorem Ipsum&quot;,&#10;  &quot;record_on_start&quot;: true&#10;}&#x27;&#10;</code></pre>
<h3 id="response">Response</h3>
<pre><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;data&quot;: {&#10;		&quot;id&quot;: &quot;497f6eca-6276-4993-bfeb-53cbbbba6f08&quot;,&#10;		&quot;record_on_start&quot;: true,&#10;		&quot;created_at&quot;: &quot;2025-08-24T14:15:22Z&quot;,&#10;		&quot;updated_at&quot;: &quot;2025-08-24T14:15:22Z&quot;&#10;	}&#10;}&#10;</code></pre>
<h2 id="using-the-start-recording-api">Using the Start Recording API</h2>
<p>You can also start a recording using the
<a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/">Start Recording API</a>.</p>
<p>Specify the <code>meeting ID</code> of the meeting that you want to record.</p>
<p>Use the <a href="/api/resources/realtime_kit/subresources/meetings/methods/get/">List meetings API</a> for an
app or <a href="/api/resources/realtime_kit/subresources/meetings/methods/create/">Create a meeting API</a> to
get the meeting ID. The API returns a parameter called <code>id</code>, which is your
meeting ID.</p>
<h3 id="request-1">Request</h3>
<pre><code class="language-bash">curl --location &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/realtime/kit/&lt;app_id&gt;/recordings&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-header &#x27;Authorization: Bearer &lt;api_token&gt;&#x27; \&#10;  &#45;-data &#x27;{&#10;  &quot;meeting_id&quot;: &quot;97440c6a-140b-40a9-9499-b23fd7a3868a&quot;&#10;}&#x27;&#10;</code></pre>
<h3 id="response-1">Response</h3>
<pre><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;data&quot;: {&#10;		&quot;id&quot;: &quot;97440c6a-140b-40a9-9499-b23fd7a3868a&quot;,&#10;		&quot;download_url&quot;: &quot;http://example.com&quot;,&#10;		&quot;download_url_expiry&quot;: &quot;2025-08-24T14:15:22Z&quot;,&#10;		&quot;download_audio_url&quot;: &quot;http://example1.com&quot;,&#10;		&quot;file_size&quot;: 0,&#10;		&quot;session_id&quot;: &quot;1ffd059c-17ea-40a8-8aef-70fd0307db82&quot;,&#10;		&quot;output_file_name&quot;: &quot;string&quot;,&#10;		&quot;status&quot;: &quot;INVOKED&quot;,&#10;		&quot;invoked_time&quot;: &quot;2025-08-24T14:15:22Z&quot;,&#10;		&quot;started_time&quot;: &quot;2025-08-24T14:15:22Z&quot;,&#10;		&quot;stopped_time&quot;: &quot;2025-08-24T14:15:22Z&quot;,&#10;		&quot;storage_config&quot;: {&#10;			&quot;type&quot;: &quot;cloudflare&quot;,&#10;			&quot;secret_key&quot;: &quot;string&quot;,&#10;			&quot;bucket&quot;: &quot;string&quot;,&#10;			&quot;path&quot;: &quot;string&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>

<p>When you join a RealtimeKit meeting, the meeting layout is automatically designed to optimize your experience. This includes focusing on shared content and highlighting active speakers, while participants are shown in small thumbnail views. When you start recording the meeting, it is recorded with the same layout using the default UI kit component called <a href="https://docs.realtime.cloudflare.com/react-ui-kit/components/rtk-grid">RtkGrid</a>.</p>
<p>If you wish to have a customized layout for your recording application, RealtimeKit's custom recording SDKs provide the flexibility to tailor the appearance of your recordings according to your preferences. You can choose from options like:</p>
<ul>
<li>Show only active speaker view</li>
<li>Shared screen with thumbnail gallery view</li>
<li>Shared screen with large active speaker thumbnail</li>
<li>Shared screen without active speaker or gallery view</li>
<li>Customized background for your recording</li>
<li>Portrait layout, and so on and so forth</li>
</ul>
<h2 id="how-the-recorder-works">How the recorder works</h2>
<p>When you call <a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/">Start Recording</a>, RealtimeKit launches a Cloudflare container, opens a Chrome browser inside it, and loads the recording app URL. If you do not provide a custom URL in the <a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/"><code>url</code> parameter</a>, RealtimeKit's internal recording app is used.</p>
<h3 id="url-parameters">URL parameters</h3>
<p>Before loading your custom recording app in the Chrome browser, RealtimeKit appends the <code>authToken</code> and <code>config</code> query parameters to the URL. For example, if you provide this URL in the <a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/">Start Recording</a> API:</p>
<pre><code class="language-txt">https://example.com/my-custom-recorder&#10;</code></pre>
<p>RealtimeKit loads the app with the following parameters:</p>
<pre><code class="language-txt">https://example.com/my-custom-recorder?authToken=AUTH_TOKEN_CREATED_BY_REALTIMEKIT&amp;config=CONFIG_CREATED_BY_REALTIMEKIT&#10;</code></pre>
<p>The placeholder values represent parameters supplied by RealtimeKit. Do not add <code>authToken</code> or <code>config</code> yourself to the URL submitted to the Start Recording API. Your app must read both parameters from the URL.</p>
<h3 id="auth-token">Auth token</h3>
<p>RealtimeKit generates the <code>authToken</code> automatically for the meeting whose recording you start. It generates this token with the <code>recorder_preset_v2</code> preset. If you have not created a <code>recorder_preset_v2</code> preset, RealtimeKit uses a global preset with the same name that is managed by RealtimeKit and is not visible in your account.</p>
<p>Your custom recording app <strong>must</strong> accept this <code>authToken</code> and use it to initialize the RealtimeKit SDK to get <code>meeting</code> object.</p>
<h3 id="config-parameter">Config parameter</h3>
<p>Any configuration that you provide in the Start Recording API, such as watermark settings, is passed to the recording app through the <code>config</code> query parameter. The default recording app reads and applies this configuration automatically.</p>
<p>If you use a custom recording app, you are responsible for reading and applying <code>config</code>. Whatever your app produces in the browser is recorded as-is. RealtimeKit does not apply any additional layout, watermark, or other processing to the output of a custom recording app.</p>
<h3 id="recording-preset-flags">Recording preset flags</h3>
<p>The <code>hidden_participant</code> flag controls only the recorder's visibility. When enabled, it hides the recorder from other participants in the meeting.</p>
<p>The <code>is_recorder</code> flag identifies the participant as a recorder and ensures that recording works correctly. If you create a custom <code>recorder_preset_v2</code> preset to customize colors or the look and feel of the recording, you must keep <code>is_recorder</code> enabled. Removing <code>is_recorder</code> can cause the recording to fail. Removing <code>hidden_participant</code> can cause the recorder to be visible to other participants.</p>
<h3 id="local-testing">Local testing</h3>
<p>Local testing lets you view the recording app UI. Opening the recording app URL directly on your local machine does not start a recording.</p>
<p>For local testing only, create any preset with <code>hidden_participant: true</code>, then pass an auth token created with that preset in the <code>authToken</code> query parameter when you open the local recording app URL. This lets you see the look and feel of the recorder UI. Do not include a local testing token as the <code>authToken</code> in the URL submitted to the Start Recording API. In an actual recording, RealtimeKit generates and passes the recorder token automatically.</p>
<p>To speed up development, use a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/trycloudflare/">Cloudflare Tunnel</a> to expose your local recording app. For example, if your app is running on port <code>1111</code>, start a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/trycloudflare/">Quick Tunnel</a> with:</p>
<pre><code class="language-sh">cloudflared tunnel --url http://localhost:1111&#10;</code></pre>
<p>Replace <code>1111</code> with the port used by your local app. <code>cloudflared</code> prints a public <code>trycloudflare.com</code> URL. You can use this URL as the custom recording app URL when starting a recording, so the Cloudflare container can load your local app.</p>
<p>You might see a WebSocket error in the browser console while testing locally because your browser cannot connect to <code>localhost:8080</code>. You can ignore this error during local testing. The recorder runs with this port inside the hosting Cloudflare container, and the WebSocket connection is how the recording app tells the container to record the rendered webpage.</p>
<h3 id="examples">Examples</h3>
<p>Refer to the <a href="https://github.com/cloudflare/realtimekit-web-examples/tree/main/recording-sdk-app-examples">recording SDK app examples</a> for sample implementations, including a <a href="https://github.com/cloudflare/realtimekit-web-examples/tree/main/recording-sdk-app-examples/react-examples/recording-with-watermark">recording with watermark example</a>.</p>
<h2 id="recording-sdk-reference">Recording SDK reference</h2>
<p>The custom recording SDKs are used on top of the <a href="/realtime/realtimekit/ui-kit/">UI Kit</a> or <a href="/realtime/realtimekit/core/">Core SDK</a>. The <a href="https://www.npmjs.com/package/@cloudflare/realtimekit-recording-sdk"><code>@cloudflare/realtimekit-recording-sdk</code> package</a> provides the <code>RealtimeKitRecording</code> class for managing recording functionality.</p>
<h3 id="constructor">Constructor</h3>
<p><code>constructor(options)</code></p>
<p>Creates an instance of the <code>RealtimeKitRecording</code> class.</p>
<h4 id="constructor-parameters">Constructor parameters</h4>
<p><code>options (object)</code>: The options object. All constructor options are optional. If you omit an option, RealtimeKit uses its default value.</p>
<table>
<thead>
<tr>
<th><strong>options (object)</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>options.waitTimeMs (number)</code></td>
<td>The time (in milliseconds) to wait after all peers have left before stopping the recording. This option applies when <code>autoStop</code> is set to true.</td>
</tr>
<tr>
<td><code>options.autoStart (boolean)</code></td>
<td>Defaults to <code>true</code>, so recording starts automatically when <code>init()</code> is called. Set it to <code>false</code> only when you want to start recording manually with <code>startRecording()</code>. When set to <code>false</code>, you must call <code>startRecording()</code> within 2 minutes of the WebSocket connection being established, or the recording process will encounter an error.</td>
</tr>
<tr>
<td><code>options.autoStop (boolean)</code></td>
<td>Defaults to <code>true</code>, so recording stops automatically after all peers have left. Set it to <code>false</code> only when you want to stop recording manually with <code>stopRecording()</code>.</td>
</tr>
<tr>
<td><code>options.scanInterval (number)</code></td>
<td>The interval (in milliseconds) between scans for automatic peer leave.</td>
</tr>
<tr>
<td><code>options.devMode (boolean)</code></td>
<td>Set to true to enable development mode, which enables logs and disables certain functionality. Also you must ensure that this is set this to true when testing your recording-app locally.</td>
</tr>
</tbody>
</table>
<h3 id="methods">Methods</h3>
<pre><code class="language-js">init(client: RealtimeKitClient)&#10;</code></pre>
<p>Initiates the SDK by providing a <code>RealtimeKitClient</code> object. Call this after creating the meeting object and before calling <code>meeting.joinRoom()</code>.</p>
<pre><code class="language-js">startRecording();&#10;</code></pre>
<p>In most cases, leave <code>autoStart</code> set to <code>true</code> (the default) so the recording starts automatically. To start the recording manually, set <code>autoStart</code> to <code>false</code> in the constructor options before calling this method.</p>
<pre><code class="language-js">stopRecording();&#10;</code></pre>
<p>You usually do not need to call this method because <code>autoStop</code> defaults to <code>true</code>. To stop the recording manually, set <code>autoStop</code> to <code>false</code> in the constructor options before calling this method.</p>
<pre><code class="language-js">cleanup();&#10;</code></pre>
<p>Performs cleanup tasks after leaving the meeting, such as clearing added listeners and closing WebSocket connections.</p>
<h2 id="create-a-custom-recording-app">Create a custom recording app</h2>
<p>Perform the following steps to create the recording app for your RealtimeKit meetings.</p>
<h3 id="step-1-install-the-sdk">Step 1: Install the SDK</h3>
<pre><code class="language-js">npm i @cloudflare/realtimekit-recording-sdk&#10;</code></pre>
<h3 id="step-2-import-the-realtimekitrecording-object">Step 2: Import the <code>RealtimeKitRecording</code> object</h3>
<pre><code class="language-js">import { RealtimeKitRecording } from &quot;@cloudflare/realtimekit-recording-sdk&quot;;&#10;</code></pre>
<h3 id="step-3-create-the-realtimekitrecording-object">Step 3: Create the <code>RealtimeKitRecording</code> object</h3>
<pre><code class="language-js">const recordingSdk = new RealtimeKitRecording(options);&#10;</code></pre>
<h3 id="step-4-initialize-the-recording-sdk">Step 4: Initialize the recording SDK</h3>
<p>Call <code>init</code> after creating the meeting object and before <code>joinRoom</code> is called.</p>
<pre><code class="language-js">// Call this after you have initialized the RealtimeKit SDK and have the meeting object&#10;await recordingSdk.init(meeting);&#10;</code></pre>
<h3 id="optional-step-5-manually-start-the-recording">(Optional) Step 5: Manually start the recording</h3>
<p>To manually start the recording, set <code>autoStart</code> to <code>false</code> in the <code>RealtimeKitRecording</code> constructor options. Then call <code>startRecording()</code> after you have loaded your UI content and are ready to begin recording.</p>
<pre><code class="language-js">await recordingSdk.startRecording();&#10;</code></pre>
<h3 id="optional-step-6-manually-stop-the-recording">(Optional) Step 6: Manually stop the recording</h3>
<p>To manually stop the recording, set <code>autoStop</code> to <code>false</code> in the <code>RealtimeKitRecording</code> constructor options. Then call <code>stopRecording()</code> when you are ready to stop recording.</p>
<pre><code class="language-js">await recordingSdk.stopRecording();&#10;</code></pre>
<p>Once <code>stopRecording</code> is called, the recorder in your recording app will exit after a few seconds. After this point, you won't be able to perform any further actions within your recording app.</p>
<h3 id="step-7-deploy-the-recording-app">Step 7: Deploy the recording app</h3>
<p>Once you've created the app, deploy it using a platform like <a href="https://cloudflare.com/workers">Cloudflare Workers</a>. Make sure to note the URL where you have deployed the app, as you will have to enter this URL in RealtimeKit's recording API.</p>
<h3 id="step-8-specify-the-custom-url">Step 8: Specify the custom URL</h3>
<p>In the <a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/">Start Recording a Meeting</a> API, provide the custom URL (obtained from the previous step) to indicate the location of your deployed app. Do not append an <code>authToken</code> to this URL. RealtimeKit adds the generated <code>authToken</code> and <code>config</code> parameters when it loads the app.</p>

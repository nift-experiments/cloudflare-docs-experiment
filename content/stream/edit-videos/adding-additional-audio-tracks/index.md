<p>A video must be uploaded before additional audio tracks can be attached to it. In the following example URLs, the video’s UID is referenced as <code>VIDEO_UID</code>.</p>
<p>To add an audio track to a video a <a href="https://www.cloudflare.com/a/account/my-account">Cloudflare API Token</a> is required.</p>
<p>The API will make a best effort to handle any mismatch between the duration of the uploaded audio file and the video duration, though we recommend uploading audio files that match the duration of the video. If the duration of the audio file is longer than the video, the additional audio track will be truncated to match the video duration. If the duration of the audio file is shorter than the video, silence will be appended at the end of the audio track to match the video duration.</p>
<h2 id="upload-via-a-link">Upload via a link</h2>
<p>If you have audio files stored in a cloud storage bucket, you can simply pass a HTTP link for the file. Stream will fetch the file and make it available for streaming.</p>
<p><code>label</code> is required and must uniquely identify the track amongst other audio track labels for the specified video.</p>
<pre><code class="language-bash">curl -X POST \&#10; &#45;H &#x27;Authorization: Bearer &lt;API_TOKEN&gt;&#x27; \&#10; &#45;d &#x27;{&quot;url&quot;: &quot;https://www.examplestorage.com/audio_file.mp3&quot;, &quot;label&quot;: &quot;Example Audio Label&quot;}&#x27; \&#10;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/stream/&lt;VIDEO_UID&gt;/audio/copy&#10;</code></pre>
<pre><code class="language-json">{&#10; &quot;result&quot;: {&#10;   &quot;uid&quot;: &quot;&lt;AUDIO_UID&gt;&quot;,&#10;   &quot;label&quot;: &quot;Example Audio Label&quot;,&#10;   &quot;default&quot;: false&#10;   &quot;status&quot;: &quot;queued&quot;&#10; },&#10; &quot;success&quot;: true,&#10; &quot;errors&quot;: [],&#10; &quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>The <code>uid</code> uniquely identifies the audio track and can be used for editing or deleting the audio track. Please see instructions below on how to perform these operations.</p>
<p>The <code>default</code> field denotes whether the audio track will be played by default in a player. Additional audio tracks have a <code>false</code> default status, but can be edited following instructions below.</p>
<p>The <code>status</code> field will change to <code>ready</code> after the audio track is successfully uploaded and encoded. Should an error occur during this process, the status will denote <code>error</code>.</p>
<h2 id="upload-via-http">Upload via HTTP</h2>
<p>Make an HTTP request and include the audio file as an input with the name set to <code>file</code>.</p>
<p>Audio file uploads cannot exceed 200 MB in size. If your audio file is larger, compress the file prior to upload.</p>
<p>The form input <code>label</code> is required and must uniquely identify the track amongst other audio track labels for the specified video.</p>
<p>Note that cURL <code>-F</code> flag automatically configures the content-type header and maps <code>audio_file.mp3</code> to a form input called <code>file</code>.</p>
<pre><code class="language-bash">curl -X POST \&#10; &#45;H &#x27;Authorization: Bearer &lt;API_TOKEN&gt;&#x27; \&#10; &#45;F file=@/Desktop/audio_file.mp3 \&#10; &#45;F label=&#x27;Example Audio Label&#x27; \&#10;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/stream/&lt;VIDEO_UID&gt;/audio&#10;</code></pre>
<pre><code class="language-json">{&#10; &quot;result&quot;: {&#10;   &quot;uid&quot;: &quot;&lt;AUDIO_UID&gt;&quot;,&#10;   &quot;label&quot;: &quot;Example Audio Label&quot;,&#10;   &quot;default&quot;: false&#10;   &quot;status&quot;: &quot;queued&quot;&#10; },&#10; &quot;success&quot;: true,&#10; &quot;errors&quot;: [],&#10; &quot;messages&quot;: []&#10;}&#10;</code></pre>
<h2 id="list-the-additional-audio-tracks-on-a-video">List the additional audio tracks on a video</h2>
<p>To view additional audio tracks added to a video:</p>
<pre><code class="language-bash">curl \&#10; &#45;H &#x27;Authorization: Bearer &lt;API_TOKEN&gt;&#x27; \&#10;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/stream/&lt;VIDEO_UID&gt;/audio&#10;</code></pre>
<pre><code class="language-json">{&#10;  &quot;result&quot;: {&#10;    &quot;audio&quot;: [&#10;      {&#10;        &quot;uid&quot;: &quot;&lt;AUDIO_UID&gt;&quot;,&#10;        &quot;label&quot;: &quot;Example Audio Label&quot;,&#10;        &quot;default&quot;: false,&#10;        &quot;status&quot;: &quot;ready&quot;&#10;      },&#10;      {&#10;        &quot;uid&quot;: &quot;&lt;AUDIO_UID&gt;&quot;,&#10;        &quot;label&quot;: &quot;Another Audio Label&quot;,&#10;        &quot;default&quot;: false,&#10;        &quot;status&quot;: &quot;ready&quot;&#10;      }&#10;    ]&#10;  },&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>Note this API will not return information for audio attached to the video upload.</p>
<h2 id="edit-an-additional-audio-track">Edit an additional audio track</h2>
<p>To edit the <code>default</code> status or <code>label</code> of an additional audio track:</p>
<pre><code class="language-bash">curl -X PATCH \&#10; &#45;H &#x27;Authorization: Bearer &lt;API_TOKEN&gt;&#x27; \&#10; &#45;d &#x27;{&quot;label&quot;: &quot;Edited Audio Label&quot;, &quot;default&quot;: true}&#x27; \&#10;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/stream/&lt;VIDEO_UID&gt;/audio/&lt;AUDIO_UID&gt;&#10;</code></pre>
<p>Editing the <code>default</code> status of an audio track to <code>true</code> will mark all other audio tracks on the video <code>default</code> status to <code>false</code>.</p>
<pre><code class="language-json">{&#10;  &quot;result&quot;: {&#10;    &quot;uid&quot;: &quot;&lt;AUDIO_UID&gt;&quot;,&#10;    &quot;label&quot;: &quot;Edited Audio Label&quot;,&#10;    &quot;default&quot;: true&#10;    &quot;status&quot;: &quot;ready&quot;&#10;  },&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: []&#10;}&#10;</code></pre>
<h2 id="delete-an-additional-audio-track">Delete an additional audio track</h2>
<p>To remove an additional audio track associated with your video:</p>
<pre><code class="language-bash">curl -X DELETE \&#10; &#45;H &#x27;Authorization: Bearer &lt;API_TOKEN&gt;&#x27; \&#10;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/stream/&lt;VIDEO_UID&gt;/audio/&lt;AUDIO_UID&gt;&#10;</code></pre>
<p>Deleting a <code>default</code> audio track is not allowed.  You must assign another audio track as <code>default</code> prior to deletion.</p>
<p>If there is an entry in <code>errors</code> response field, the audio track has not been
deleted.</p>
<pre><code class="language-json">{&#10;  &quot;result&quot;: &quot;ok&quot;,&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: []&#10;}&#10;</code></pre>

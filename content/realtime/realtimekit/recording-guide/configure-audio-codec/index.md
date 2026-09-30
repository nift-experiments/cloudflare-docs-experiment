<p>Recording audio requires configuring the <strong>codec</strong> and <strong>channel</strong> parameters to guarantee optimal quality and compatibility with your application's demands.
The codec determines the encoding format for the audio, and the channel specifies the number of audio channels for the recording.
You can modify the following <code>audio_config</code> used for recording the audio:</p>
<h2 id="codec">Codec</h2>
<p>Codec determines the audio encoding format for recording, with MP3 and AAC being the supported formats.</p>
<ul>
<li>AAC (default)</li>
<li>MP3</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11815.md")
</aside>
<h2 id="channel">Channel</h2>
<p>Audio signal pathway within an audio file that carries a specific sound source. The following channels are supported:</p>
<ul>
<li>stereo (default)</li>
<li>mono</li>
</ul>
<p>You can modify the configs by specifying it in the <code>audio_config</code> field in the <a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/">Start Recording API</a>, for example:</p>
<pre><code class="language-json">{&#10;  &quot;audio_config&quot;: {&#10;    &quot;codec&quot;: &quot;AAC&quot;&#10;    &quot;channel&quot;: &quot;stereo&quot;&#10;  }&#10;}&#10;</code></pre>
<h2 id="download-audio-files">Download Audio Files</h2>
<p>The audio file for your recording is generated only if you passed the <code>audio_config</code> parameters in the <a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/">Start Recording API</a>.</p>
<p>When the recording is completed, you can use the <code>audio_download_url</code> provided in the response body of the <a href="/api/resources/realtime_kit/subresources/recordings/methods/get_one_recording/">Fetch details of a recording API</a> to download and export the audio file.</p>

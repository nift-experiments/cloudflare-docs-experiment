<p>Learn how RealtimeKit records meetings as a single composite file or as separate participant audio tracks.</p>
<p>Visit the following pages to learn more about recording meetings:</p>
<ul class="directory-listing"><li><a href="/realtime/realtimekit/recording-guide/start-recording/">Start Recording</a></li><li><a href="/realtime/realtimekit/recording-guide/stop-recording/">Stop Recording</a></li><li><a href="/realtime/realtimekit/recording-guide/monitor-status/">Monitor Recording Status</a></li><li><a href="/realtime/realtimekit/recording-guide/configure-codecs/">Configure Video Settings</a></li><li><a href="/realtime/realtimekit/recording-guide/configure-audio-codec/">Set Audio Configurations</a></li><li><a href="/realtime/realtimekit/recording-guide/add-watermark/">Add Watermark</a></li><li><a href="/realtime/realtimekit/recording-guide/configure-realtimekit-bucket-config/">Disable Upload to RealtimeKit Bucket</a></li><li><a href="/realtime/realtimekit/recording-guide/track-recording/">Track recording</a></li><li><a href="/realtime/realtimekit/recording-guide/create-record-app-using-sdks/">Create Custom Recording App Using Recording SDKs</a></li><li><a href="/realtime/realtimekit/recording-guide/interactive-recording/">Interactive Recordings with Timed Metadata</a></li><li><a href="/realtime/realtimekit/recording-guide/manage-recording-config-hierarchy/">Manage Recording Config Precedence Order</a></li><li><a href="/realtime/realtimekit/recording-guide/custom-cloud-storage/">Upload Recording to Your Cloud</a></li></ul>
<p>RealtimeKit can record the audio and video of multiple users in a meeting, as well as interactions with RealtimeKit plugins, in a single file using composite recording mode. RealtimeKit can also record separate participant audio tracks using <a href="/realtime/realtimekit/recording-guide/track-recording/">track recording</a>.</p>
<h2 id="how-composite-recording-works">How composite recording works</h2>
<p>Composite recordings are powered by anonymous virtual bot users who join your
meeting, record it, and then upload it to RealtimeKit's Cloudflare R2 bucket. For video files,
we currently support the
<a href="https://en.wikipedia.org/wiki/Advanced_Video_Coding">H.264</a> and
<a href="https://en.wikipedia.org/wiki/VP8">VP8</a> codecs.</p>
<ol>
<li>
<p>When the recording is finished, it is stored in RealtimeKit's Cloudflare R2 bucket.</p>
</li>
<li>
<p>RealtimeKit generates a downloadable link from which the recording can be
downloaded. You can get the download URL using the
<a href="/api/resources/realtime_kit/subresources/recordings/methods/get_one_recording/">Fetch details of a recording API</a>
or from the Developer Portal.</p>
<p>You can receive notifications of recording status in any of the following
ways:</p>
<ul>
<li>Using the <code>recording.statusUpdate</code> webhook. RealtimeKit uses webhooks to notify your application when an event happens.</li>
<li>Using the <a href="/api/resources/realtime_kit/subresources/recordings/methods/get_active_recordings/">Fetch active recording API</a>.</li>
<li>You can also view the states of recording from the Developer Portal.</li>
</ul>
</li>
<li>
<p>Download the recording from the download url and store it to your cloud
storage. The file is kept on RealtimeKit's server for seven days before being
deleted.</p>
<p>You can get the download URL using the
<a href="/api/resources/realtime_kit/subresources/recordings/methods/get_active_recordings/">Fetch active recording API</a> or
from the Developer Portal.</p>
<p>We support transferring recordings to AWS, Azure, and DigitalOcean storage
buckets. You can also choose to preconfigure the storage configurations using
the Developer Portal or the
<a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/">Start recording a meeting API</a>.</p>
</li>
</ol>
<h2 id="workflow">Workflow</h2>
<p>A typical workflow for recording a meeting involves the following steps:</p>
<ol>
<li>Start a recording using the <a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/">Start Recording API</a> or client side SDK.</li>
<li>Manage the recording using the <a href="/api/resources/realtime_kit/subresources/recordings/methods/pause_resume_stop_recording/">Pause, resume, or stop recording API</a> or client side SDK.</li>
<li>Fetch the download URL for downloading the recording using the <a href="/api/resources/realtime_kit/subresources/recordings/methods/get_one_recording/">Fetch details of a recording API</a>, webhook, or from the Developer Portal.</li>
</ol>
<p>For separate participant audio files, refer to <a href="/realtime/realtimekit/recording-guide/track-recording/">Track recording</a>.</p>

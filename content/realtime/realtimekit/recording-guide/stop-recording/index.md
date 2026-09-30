<p>RealtimeKit recordings can be stopped in any of the following ways:</p>
<ol>
<li><strong>Automatic Stop (Empty meeting)</strong>: A RealtimeKit recording will automatically stop
if the meeting has no participants for a duration of 1 minute or more. This
wait time can be customized by contacting RealtimeKit's support team to configure a
custom value for your app.</li>
<li><strong>Automatic Stop (maxSeconds elapsed)</strong>: A recording will automatically stop
when it reaches the duration specified by the <code>max_seconds</code> parameter passed
while starting the recording, regardless of whether participants are present
in the meeting. If this parameter is not passed, it defaults to 24 hours
(86400 seconds).</li>
<li><strong>Using Stop Recording API</strong>: A recording can also be stopped by passing the
recording ID and <code>stop</code> action to the <a href="/api/resources/realtime_kit/subresources/recordings/">Stop Recording API</a>.</li>
</ol>
<p>When a recording is stopped, it transitions to the <code>UPLOADING</code> state and then to the <code>UPLOADED</code> state after it has been transferred to RealtimeKit's storage and any external storage that has been set up.</p>

<p>Before you upload your video, review the options for uploading a video, supported formats, and recommendations.</p>
<h2 id="upload-options">Upload options</h2>
<table>
<thead>
<tr>
<th>Upload method</th>
<th>When to use</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://dash.cloudflare.com/?to=/:account/stream">Stream Dashboard</a></td>
<td>Upload videos from the Stream Dashboard without writing any code.</td>
</tr>
<tr>
<td><a href="/stream/uploading-videos/upload-via-link/">Upload with a link</a></td>
<td>Upload videos using a link, such as an S3 bucket or content management system.</td>
</tr>
<tr>
<td><a href="/stream/uploading-videos/upload-video-file/">Upload video file</a></td>
<td>Upload videos stored on a computer.</td>
</tr>
<tr>
<td><a href="/stream/uploading-videos/direct-creator-uploads/">Direct creator uploads</a></td>
<td>Allows end users of your website or app to upload videos directly to Cloudflare Stream.</td>
</tr>
</tbody>
</table>
<h2 id="supported-video-formats">Supported video formats</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14382.md")
</aside>
<ul>
<li>MP4</li>
<li>MKV</li>
<li>MOV</li>
<li>AVI</li>
<li>FLV</li>
<li>MPEG-2 TS</li>
<li>MPEG-2 PS</li>
<li>MXF</li>
<li>LXF</li>
<li>GXF</li>
<li>3GP</li>
<li>WebM</li>
<li>MPG</li>
<li>Quicktime</li>
</ul>
<h2 id="recommendations-for-on-demand-videos">Recommendations for on-demand videos</h2>
<ul>
<li>Optional but ideal settings:
<ul>
<li>MP4 containers</li>
<li>AAC audio codec</li>
<li>H264 video codec</li>
<li>60 or fewer frames per second</li>
</ul>
</li>
<li>Closed GOP (<em>Only required for live streaming.</em>)</li>
<li>Mono or Stereo audio. Stream will mix audio tracks with more than two channels down to stereo.</li>
</ul>
<h2 id="frame-rates">Frame rates</h2>
<p>Stream accepts video uploads at any frame rate. During encoding, Stream re-encodes videos for a maximum of 90 FPS playback. If the original video has a frame rate lower than 90 FPS, Stream re-encodes at the original frame rate.</p>
<p>For variable frame rate content, Stream drops extra frames. For example, if there is more than one frame within a 1/30 second window, Stream drops the extra frames within that period.</p>

---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/best-practices/video-and-simulcast/
  description: Choose the right video resolution, simulcast settings, and frame rate for your RealtimeKit use case to optimize quality and bandwidth.
  full_title: Video resolution and simulcast · Cloudflare Realtime docs
  head_html: <title>Video resolution and simulcast · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Choose the right video resolution, simulcast settings, and frame rate for your RealtimeKit use case to optimize quality and bandwidth."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/best-practices/video-and-simulcast/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/best-practices/video-and-simulcast/index.md"><meta property="og:title" content="Video resolution and simulcast · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Choose the right video resolution, simulcast settings, and frame rate for your RealtimeKit use case to optimize quality and bandwidth."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/best-practices/video-and-simulcast/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/best-practices/video-and-simulcast/#page","headline":"Video resolution and simulcast \u00b7 Cloudflare Realtime docs","description":"Choose the right video resolution, simulcast settings, and frame rate for your RealtimeKit use case to optimize quality and bandwidth.","url":"https://developers.cloudflare.com/realtime/realtimekit/best-practices/video-and-simulcast/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/best-practices/video-and-simulcast/
  schema: 1
---
<p>Configure video resolution, simulcast, and frame rate in RealtimeKit to balance quality against bandwidth. The right settings depend on your grid layout, participant count, and use case.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12512.md")
</aside>
<h2 id="choose-the-right-resolution-for-your-layout">Choose the right resolution for your layout</h2>
<p>Video resolution directly affects bandwidth and CPU usage. Sending higher resolution than the display tile requires wastes upload bandwidth and decoding resources on every receiver.</p>
<p>Configure the video resolution in your <a href="/realtime/realtimekit/concepts/preset/">preset</a> based on the layout each participant type will see.</p>
<h3 id="1-1-calls-two-participants">1:1 calls (two participants)</h3>
<p>Each participant occupies a large portion of the screen. Use <code>1280×720</code> (720p) as the default. For use cases where visual detail matters — coaching sessions, design reviews, or remote consultations — use <code>1920×1080</code> (1080p).</p>
<p>Turn off simulcast for 1:1 calls. With only one receiver, encoding multiple layers adds CPU cost with no benefit.</p>
<p>In a 1:1 call, each participant uploads one stream and downloads one stream. Upload and download bandwidth are equal.</p>
<p>The following table shows per-participant bandwidth and hourly data transfer at 24 FPS for a 1:1 call:</p>
<table>
<thead>
<tr>
<th>Resolution</th>
<th>Bitrate (upload = download)</th>
<th>Upload per hour</th>
<th>Download per hour</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1280×720</code> (720p)</td>
<td>1.5–6 Mbps</td>
<td>675 MB–2.7 GB</td>
<td>675 MB–2.7 GB</td>
</tr>
<tr>
<td><code>1920×1080</code> (1080p)</td>
<td>3.5–14 Mbps</td>
<td>1.6–6.3 GB</td>
<td>1.6–6.3 GB</td>
</tr>
</tbody>
</table>
<h3 id="podcast-or-broadcast-one-to-two-speakers">Podcast or broadcast (one to two speakers)</h3>
<p>When one or two speakers are the primary focus, push resolution higher. Use <code>1920×1080</code> (1080p) as the baseline. Use <code>3840×2160</code> (4K) when the host has sufficient upload bandwidth and the content benefits from high fidelity — product showcases, studio interviews, or live art demonstrations.</p>
<p>Turn on simulcast so that viewers on constrained networks automatically receive a lower layer.</p>
<p>The following table shows per-sender upload bandwidth and hourly data transfer at 24 FPS:</p>
<table>
<thead>
<tr>
<th>Resolution</th>
<th>Sender upload bitrate</th>
<th>Sender upload per hour</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1920×1080</code> (1080p)</td>
<td>3.5–14 Mbps</td>
<td>1.6–6.3 GB</td>
</tr>
<tr>
<td><code>3840×2160</code> (4K)</td>
<td>14–56 Mbps</td>
<td>6.3–25.2 GB</td>
</tr>
</tbody>
</table>
<p>Each viewer downloads one stream. The download bitrate matches the sender upload bitrate, or a lower simulcast layer if the viewer's network is constrained.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/12511.md")
</aside>
<h3 id="small-group-grid-3-3-nine-participants">Small group grid (3×3, nine participants)</h3>
<p>In a 3×3 grid, each tile is roughly one-third of the screen width. Turn on simulcast and set the sending resolution to <code>640×480</code> (480p).</p>
<p>Each participant uploads one stream and downloads eight streams (one from each other participant). The following table shows per-participant bandwidth and hourly data transfer at 24 FPS:</p>
<table>
<thead>
<tr>
<th>Resolution</th>
<th>Upload bitrate (one stream)</th>
<th>Upload per hour</th>
<th>Download bitrate (8 streams)</th>
<th>Download per hour</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>640×480</code> (480p)</td>
<td>500 Kbps–2 Mbps</td>
<td>225–900 MB</td>
<td>4–16 Mbps</td>
<td>1.8–7.2 GB</td>
</tr>
</tbody>
</table>
<h3 id="large-grids-4-4-5-5-6-4-or-more">Large grids (4×4, 5×5, 6×4, or more)</h3>
<p>With 16 or more visible tiles, each tile is small. Set the sending resolution to <code>320×240</code> (240p) and turn on simulcast.</p>
<p>Each participant uploads one stream and downloads one stream from every other participant. The following table shows per-participant bandwidth for a 4×4 grid (16 participants, 15 incoming streams) at 24 FPS:</p>
<table>
<thead>
<tr>
<th>Resolution</th>
<th>Upload bitrate (one stream)</th>
<th>Upload per hour</th>
<th>Download bitrate (15 streams)</th>
<th>Download per hour</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>320×240</code> (240p)</td>
<td>130–520 Kbps</td>
<td>58–234 MB</td>
<td>1.9–7.8 Mbps</td>
<td>870 MB–3.5 GB</td>
</tr>
<tr>
<td><code>640×480</code> (480p)</td>
<td>500 Kbps–2 Mbps</td>
<td>225–900 MB</td>
<td>7.5–30 Mbps</td>
<td>3.4–13.5 GB</td>
</tr>
<tr>
<td><code>1280×720</code> (720p)</td>
<td>1.5–6 Mbps</td>
<td>675 MB–2.7 GB</td>
<td>22.5–90 Mbps</td>
<td>10.1–40.5 GB</td>
</tr>
<tr>
<td><code>1920×1080</code> (1080p)</td>
<td>3.5–14 Mbps</td>
<td>1.6–6.3 GB</td>
<td>52.5–210 Mbps</td>
<td>23.6–94.5 GB</td>
</tr>
</tbody>
</table>
<p>At <code>320×240</code>, each participant needs 2–8 Mbps download. The lower end is practical even on mobile networks. At <code>1920×1080</code>, the same grid requires 52–210 Mbps download, which exceeds most residential connections.</p>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/12510.md")
</aside>
<h3 id="pinned-speaker-with-gallery-all-participants-send-video">Pinned speaker with gallery (all participants send video)</h3>
<p>For layouts where all participants send video but one speaker is pinned at a larger size — town halls, classrooms, or team standups — use different presets for each role.</p>
<p>Set the speaker preset resolution to <code>1280×720</code> or <code>1920×1080</code> because the speaker tile is large and benefits from higher quality. Set the participant preset resolution to <code>320×240</code> because participant tiles are small thumbnails.</p>
<p>The following table shows bandwidth for a town hall with one speaker at 720p and 15 participants at 240p, all at 24 FPS. Every participant sends video:</p>
<table>
<thead>
<tr>
<th>Role</th>
<th>Upload bitrate</th>
<th>Upload per hour</th>
<th>Download bitrate</th>
<th>Download per hour</th>
</tr>
</thead>
<tbody>
<tr>
<td>Speaker (one stream at 720p, receives 15 streams at 240p)</td>
<td>1.5–6 Mbps</td>
<td>675 MB–2.7 GB</td>
<td>1.9–7.8 Mbps</td>
<td>870 MB–3.5 GB</td>
</tr>
<tr>
<td>Participant (one stream at 240p, receives one stream at 720p + 14 streams at 240p)</td>
<td>130–520 Kbps</td>
<td>58–234 MB</td>
<td>3.3–13.3 Mbps</td>
<td>1.5–6 GB</td>
</tr>
</tbody>
</table>
<h3 id="webinar-audience-is-view-only">Webinar (audience is view-only)</h3>
<p>In a webinar, audience members do not send audio or video unless they are invited on stage. Only the speaker uploads a stream. Use a high-resolution preset for the speaker and a view-only preset for the audience.</p>
<p>The following example shows a webinar with one speaker at 720p and 15 view-only audience members, all at 24 FPS:</p>
<table>
<thead>
<tr>
<th>Role</th>
<th>Upload bitrate</th>
<th>Upload per hour</th>
<th>Download bitrate</th>
<th>Download per hour</th>
</tr>
</thead>
<tbody>
<tr>
<td>Speaker (one stream at 720p, no other on-stage participants)</td>
<td>1.5–6 Mbps</td>
<td>675 MB–2.7 GB</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Audience member (view-only, receives one stream at 720p)</td>
<td>0</td>
<td>0</td>
<td>1.5–6 Mbps</td>
<td>675 MB–2.7 GB</td>
</tr>
</tbody>
</table>
<h2 id="turn-on-simulcast-for-multi-participant-sessions">Turn on simulcast for multi-participant sessions</h2>
<p>Simulcast encodes the sender's video at multiple resolutions simultaneously (for example, 720p, 360p, and 180p). The SFU selects the best layer for each receiver based on available bandwidth and tile size.</p>
<p><strong>Turn on simulcast when:</strong></p>
<ul>
<li>The session has three or more participants</li>
<li>Participants have varying network conditions (mobile and desktop mix)</li>
<li>The session is a webinar or event with audience on constrained networks</li>
</ul>
<p><strong>Turn off simulcast</strong> for 1:1 calls (one receiver, no benefit from multiple layers) and for audio-only sessions.</p>
<p>Simulcast increases CPU usage on the sender because the device encodes multiple layers. If your use case targets low-powered devices in remote regions with limited bandwidth, consider turning off simulcast and setting a single lower resolution (such as <code>320×240</code>) for all participants instead. This avoids the extra encoding cost while still keeping bandwidth low. For sessions where participants have a mix of device capabilities and network conditions, simulcast provides the best experience because the SFU delivers the appropriate layer to each receiver.</p>
<h2 id="choose-the-right-frame-rate">Choose the right frame rate</h2>
<p>Frame rate (FPS) directly multiplies bandwidth. Doubling the frame rate roughly doubles the required bitrate at the same resolution. Choose the lowest frame rate that meets your use case.</p>
<table>
<thead>
<tr>
<th>FPS</th>
<th>Bandwidth impact</th>
<th>Best for</th>
</tr>
</thead>
<tbody>
<tr>
<td>15 FPS</td>
<td>Lowest</td>
<td>Slide presentations, screen shares of static content, surveillance feeds</td>
</tr>
<tr>
<td>24 FPS</td>
<td>Moderate</td>
<td>Standard video calls, webinars, online classrooms, telemedicine</td>
</tr>
<tr>
<td>30 FPS</td>
<td>Higher</td>
<td>Interactive workshops, live product demos, fitness classes</td>
</tr>
<tr>
<td>60 FPS</td>
<td>Highest (~2x of 30 FPS)</td>
<td>Live sports broadcasting, real-time music performances, esports</td>
</tr>
</tbody>
</table>
<h3 id="industry-examples">Industry examples</h3>
<ul>
<li><strong>Education</strong>: Use 15 FPS for lecture screen shares and 24 FPS for the instructor camera. Students on mobile networks benefit from lower bandwidth.</li>
<li><strong>Healthcare</strong>: Use 24 FPS for telemedicine consultations. Higher frame rates provide minimal benefit for conversation-style video.</li>
<li><strong>Fitness and wellness</strong>: Use 30 FPS for live workout classes. Participants need smooth motion to follow physical movements.</li>
<li><strong>Media and entertainment</strong>: Use 60 FPS for live music performances or sports watch parties where motion clarity matters.</li>
<li><strong>Corporate meetings</strong>: Use 24 FPS for all-hands and standups. Talking-head video does not benefit from higher frame rates.</li>
<li><strong>Customer support</strong>: Use 15 FPS for support sessions that involve mostly screen sharing. Lower bandwidth reduces dropped frames on the customer end.</li>
</ul>
<h3 id="combine-resolution-and-frame-rate">Combine resolution and frame rate</h3>
<p>Resolution and frame rate compound. The following table shows per-participant bandwidth for a 4×4 grid (15 incoming streams) at different combinations:</p>
<table>
<thead>
<tr>
<th>Configuration</th>
<th>Upload bitrate</th>
<th>Upload per hour</th>
<th>Download bitrate (15 streams)</th>
<th>Download per hour</th>
</tr>
</thead>
<tbody>
<tr>
<td>720p at 30 FPS</td>
<td>1.9–8 Mbps</td>
<td>855 MB–3.6 GB</td>
<td>29–116 Mbps</td>
<td>13–52.2 GB</td>
</tr>
<tr>
<td>480p at 24 FPS</td>
<td>500 Kbps–2 Mbps</td>
<td>225–900 MB</td>
<td>7.5–30 Mbps</td>
<td>3.4–13.5 GB</td>
</tr>
<tr>
<td>240p at 15 FPS</td>
<td>80–320 Kbps</td>
<td>36–144 MB</td>
<td>1.2–4.8 Mbps</td>
<td>540 MB–2.2 GB</td>
</tr>
</tbody>
</table>
<p>For large-grid use cases like virtual classrooms or all-hands meetings, <code>320×240</code> at 15 FPS with simulcast keeps total download bandwidth under 5 Mbps per participant even for high-motion content.</p>
<h2 id="summary">Summary</h2>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Resolution</th>
<th>Simulcast</th>
<th>FPS</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>1:1 call</td>
<td>720p–1080p</td>
<td>Off</td>
<td>24–30</td>
<td>Upload and download are equal (one stream each)</td>
</tr>
<tr>
<td>Podcast or broadcast</td>
<td>1080p–4K</td>
<td>On</td>
<td>24–30</td>
<td>Verify host upload supports 4K (14–56 Mbps)</td>
</tr>
<tr>
<td>3×3 group call</td>
<td>480p</td>
<td>On</td>
<td>24</td>
<td>500 Kbps–2 Mbps upload, 4–16 Mbps download per participant</td>
</tr>
<tr>
<td>4×4+ large grid</td>
<td>240p</td>
<td>On</td>
<td>15–24</td>
<td>130–520 Kbps upload, 2–8 Mbps download per participant</td>
</tr>
<tr>
<td>Pinned speaker + gallery</td>
<td>720p–1080p (speaker), 240p (participants)</td>
<td>On</td>
<td>24</td>
<td>All participants send video, use separate presets per role</td>
</tr>
<tr>
<td>Webinar</td>
<td>720p–1080p (speaker), view-only (audience)</td>
<td>On</td>
<td>24</td>
<td>Audience does not upload unless invited on stage</td>
</tr>
<tr>
<td>Screen sharing</td>
<td>Source resolution</td>
<td>Off</td>
<td>15</td>
<td>Low FPS is sufficient for static content</td>
</tr>
</tbody>
</table>
<p>For more information on configuring presets, refer to <a href="/realtime/realtimekit/concepts/preset/">Presets</a>.</p>

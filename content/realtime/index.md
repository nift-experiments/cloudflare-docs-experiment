<div class="nb-description">
@markup("md", "content/.markup/bodies/466.md")
</div>
<h3 id="realtimekit">RealtimeKit</h3>
<p><a href="/realtime/realtimekit/">RealtimeKit</a> is a set of SDKs and APIs that lets you add customizable live video and voice to web or mobile applications. It is fully customisable and lets you set up in just a few lines of code.</p>
<p>It sits on top of the Realtime SFU, abstracting away the heavy lifting of media routing, peer management, and other complex WebRTC operations.</p>
<h3 id="realtime-sfu">Realtime SFU</h3>
<p>The <a href="/realtime/sfu/">Realtime SFU (Selective Forwarding Unit)</a> routes WebRTC audio, video, and DataChannels between application endpoints.</p>
<p>Use Realtime SFU when your application needs custom media routing, signaling, state, permissions, or user interfaces. Common topologies include custom calls, interactive broadcasts, AI media pipelines, cloud gaming, device control, and media processing.</p>
<p>Your application backend keeps the Realtime SFU credentials and decides which sessions can publish, subscribe, or control resources.</p>
<h3 id="turn-service">TURN Service</h3>
<p>The <a href="/realtime/turn/">TURN service</a> is a managed service that acts as a relay for WebRTC traffic. It ensures connectivity for users behind restrictive firewalls or NATs by providing a public relay point for media streams.</p>
<h2 id="choose-the-right-realtime-product">Choose the right Realtime product</h2>
<p>Use this comparison table to quickly find the right Realtime product for your needs:</p>
<table>
<thead>
<tr>
<th></th>
<th><strong>RealtimeKit</strong></th>
<th><strong>Realtime SFU</strong></th>
<th><strong>TURN Service</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Choose it when</strong></td>
<td>You want meeting SDKs, participant management, and pre-built UI components.</td>
<td>You want to compose WebRTC media and data into a custom application topology.</td>
<td>You need a relay for peer-to-peer or self-hosted WebRTC connections.</td>
</tr>
<tr>
<td><strong>Provides</strong></td>
<td>Meetings, participants, presets, stage management, and UI components.</td>
<td>Sessions, media tracks, DataChannels, and programmable publish and subscribe operations.</td>
<td>TURN allocations and relayed UDP, TCP, or TLS transport.</td>
</tr>
<tr>
<td><strong>Your application manages</strong></td>
<td>Product integration, branding, and application-specific behavior.</td>
<td>Authentication, authorization, signaling, presence, state, and track discovery.</td>
<td>Peer connections, signaling, media routing, and application state.</td>
</tr>
<tr>
<td><strong>Example outcomes</strong></td>
<td>Meetings, classrooms, webinars, and social video.</td>
<td>Custom calls, interactive broadcasts, AI pipelines, cloud gaming, device control, and media processing.</td>
<td>Connectivity through restrictive firewalls and network address translation.</td>
</tr>
<tr>
<td><strong>Pricing</strong></td>
<td>Pricing by minute <a href="https://workers.cloudflare.com/pricing#media">view details</a></td>
<td>$0.05/GB egress</td>
<td>Free when used with Realtime SFU, otherwise $0.05/GB egress</td>
</tr>
<tr>
<td><strong>Free tier</strong></td>
<td>None</td>
<td>First 1,000 GB free each month</td>
<td>First 1,000 GB free each month</td>
</tr>
</tbody>
</table>
<h2 id="related-products">Related products</h2>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/467.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/468.md")
</div>
<h2 id="more-resources">More resources</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/472.md")
</div>

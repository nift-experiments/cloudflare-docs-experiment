<div class="full-img">
<p><img src="/assets/upstream/images/realtime/video-calling-application.png" alt="Example Architecture" /></p>
</div>
<ol>
<li>Clients connect to the backend service</li>
<li>Backend service manages the relationship between the clients and the tracks they should subscribe to</li>
<li>Backend service contacts the Cloudflare Realtime API to pass the SDP from the clients to establish the WebRTC connection.</li>
<li>Realtime API relays back the Realtime API SDP reply and renegotiation messages.</li>
<li>If desired, headless clients can be used to record the content from other clients or publish content.</li>
<li>Admin manages the rooms and room members.</li>
</ol>

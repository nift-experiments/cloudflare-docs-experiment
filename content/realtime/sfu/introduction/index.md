<p>Cloudflare Realtime can be used to add realtime audio, video and data into your applications. Cloudflare Realtime uses WebRTC, which is the lowest latency way to communicate across a broad range of platforms like browsers, mobile, and native apps.</p>
<p>Realtime integrates with your backend and frontend application to add realtime functionality.</p>
<h2 id="why-cloudflare-realtime-exists">Why Cloudflare Realtime exists</h2>
<ul>
<li>
<p><strong>It is difficult to scale WebRTC</strong>: Many struggle scaling WebRTC servers. Operators run into issues about how many users can be in the same &quot;room&quot; or want to build unique solutions that do not fit into the current concepts in high level APIs.</p>
</li>
<li>
<p><strong>High egress costs</strong>: WebRTC is expensive to use as managed solutions charge a high premium on cloud egress and running your own servers incur system administration and scaling overhead. Cloudflare already has 300+ locations with upwards of 1,000 servers in some locations. Cloudflare Realtime scales easily on top of this architecture and can offer the lowest WebRTC usage costs.</p>
</li>
<li>
<p><strong>WebRTC is growing</strong>: Developers are realizing that WebRTC is not just for video conferencing. WebRTC is supported on many platforms, it is mature and well understood.</p>
</li>
</ul>
<h2 id="what-makes-cloudflare-realtime-unique">What makes Cloudflare Realtime unique</h2>
<ul>
<li>
<p><strong>Unopinionated</strong>: Cloudflare Realtime does not offer a SDK. It instead allows you to access raw WebRTC to solve unique problems that might not fit into existing concepts. The API is deliberately simple.</p>
</li>
<li>
<p><strong>No rooms</strong>: Unlike other WebRTC products, Cloudflare Realtime lets you be in charge of each track (audio/video/data) instead of offering abstractions such as rooms. You define the presence protocol on top of simple pub/sub. Each end user can publish and subscribe to audio/video/data tracks as they wish.</p>
</li>
<li>
<p><strong>No lock-in</strong>: You can use Cloudflare Realtime to solve scalability issues with your SFU. You can use in combination with peer-to-peer architecture. You can use Cloudflare Realtime standalone. To what extent you use Cloudflare Realtime is up to you.</p>
</li>
</ul>
<h2 id="what-exactly-does-cloudflare-realtime-do">What exactly does Cloudflare Realtime do?</h2>
<ul>
<li>
<p><strong>SFU</strong>: Realtime is a special kind of pub/sub server that is good at forwarding media data to clients that subscribe to certain data. Each client connects to Cloudflare Realtime via WebRTC and either sends data, receives data or both using WebRTC. This can be audio/video tracks or DataChannels.</p>
</li>
<li>
<p><strong>It scales</strong>: All Cloudflare servers act as a single server so millions of WebRTC clients can connect to Cloudflare Realtime. Each can send data, receive data or both with other clients.</p>
</li>
</ul>
<h2 id="how-most-developers-get-started">How most developers get started</h2>
<ol>
<li>
<p>Get started with the echo example, which you can download from the Cloudflare dashboard when you create a Realtime App or from <a href="/realtime/sfu/demos/">demos</a>. This will show you how to send and receive audio and video.</p>
</li>
<li>
<p>Understand how you can manipulate who can receive what media by passing around session and track ids. Remember, you control who receives what media. Each media track is represented by a unique ID. It is your responsibility to save and distribute this ID.</p>
</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="realtime-is-not-a-presence-protocol">Realtime is not a presence protocol</h3>
@markup("md", "content/.markup/bodies/11575.md")
</aside>
<ol start="3">
<li>Create an app where you manage each connection to Cloudflare Realtime and the track IDs created by each connection. You can use any tool to save and share tracks. Check out the example apps at <a href="/realtime/sfu/demos/">demos</a>, such as <a href="https://github.com/cloudflare/orange">Orange Meets</a>, which is a full-fledged video conferencing app that uses <a href="/durable-objects/">Workers Durable Objects</a> to keep track of track IDs.</li>
</ol>

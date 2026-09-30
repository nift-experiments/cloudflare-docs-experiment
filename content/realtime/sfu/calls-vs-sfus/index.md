<h2 id="cloudflare-realtime-vs-traditional-sfus">Cloudflare Realtime vs. Traditional SFUs</h2>
<p>Cloudflare Realtime represents a paradigm shift in building real-time applications by leveraging a distributed real-time data plane. It creates a seamless experience in real-time communication, transcending traditional geographical limitations and scalability concerns. Realtime is designed for developers looking to integrate WebRTC functionalities in a server-client architecture without delving deep into the complexities of regional scaling or server management.</p>
<h3 id="the-limitations-of-centralized-sfus">The Limitations of Centralized SFUs</h3>
<p>Selective Forwarding Units (SFUs) play a critical role in managing WebRTC connections by selectively forwarding media streams to participants in a video call. However, their centralized nature introduces inherent limitations:</p>
<ul>
<li>
<p><strong>Regional Dependency:</strong> A centralized SFU requires a specific region for deployment, leading to latency issues for global users except for those in proximity to the selected region.</p>
</li>
<li>
<p><strong>Scalability Concerns:</strong> Scaling a centralized SFU to meet global demand can be challenging and inefficient, often requiring additional infrastructure and complexity.</p>
</li>
</ul>
<h3 id="how-is-cloudflare-realtime-different">How is Cloudflare Realtime different?</h3>
<p>Cloudflare Realtime addresses these limitations by leveraging Cloudflare's global network infrastructure:</p>
<ul>
<li>
<p><strong>Global Distribution Without Regions:</strong> Unlike traditional SFUs, Cloudflare Realtime operates on a global scale without regional constraints. It utilizes Cloudflare's extensive network of over 250 locations worldwide to ensure low-latency video forwarding, making it fast and efficient for users globally.</p>
</li>
<li>
<p><strong>Decentralized Architecture:</strong> There are no dedicated servers for Realtime. Every server within Cloudflare's network contributes to handling Realtime, ensuring scalability and reliability. This approach mirrors the distributed nature of Cloudflare's products such as 1.1.1.1 DNS or Cloudflare's CDN.</p>
</li>
</ul>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/11588.md")
</aside>
<h2 id="how-cloudflare-realtime-works">How Cloudflare Realtime Works</h2>
<h3 id="establishing-peer-connections">Establishing Peer Connections</h3>
<p>To initiate a real-time communication session, an end user's client establishes a WebRTC PeerConnection to the nearest Cloudflare location. This connection benefits from anycast routing, optimizing for the lowest possible latency.</p>
<h3 id="signaling-and-media-stream-management">Signaling and Media Stream Management</h3>
<ul>
<li>
<p><strong>HTTPS API for Signaling:</strong> Cloudflare Realtime simplifies signaling with a straightforward HTTPS API. This API manages the initiation and coordination of media streams, enabling clients to push new MediaStreamTracks or request these tracks from the server.</p>
</li>
<li>
<p><strong>Efficient Media Handling:</strong> Unlike traditional approaches that require multiple connections for different media streams from different clients, Cloudflare Realtime maintains a single PeerConnection per client. This streamlined process reduces complexity and improves performance by handling both the push and pull of media through a singular connection.</p>
</li>
</ul>
<h3 id="application-level-management">Application-Level Management</h3>
<p>Cloudflare Realtime delegates the responsibility of state management and participant tracking to the application layer. Developers are empowered to design their logic for handling events such as participant joins or media stream updates, offering flexibility to create tailored experiences in applications.</p>
<h2 id="getting-started-with-cloudflare-realtime">Getting Started with Cloudflare Realtime</h2>
<p>Integrating Cloudflare Realtime into your application promises a straightforward and efficient process, removing the hurdles of regional scalability and server management so you can focus on creating engaging real-time experiences for users worldwide.</p>

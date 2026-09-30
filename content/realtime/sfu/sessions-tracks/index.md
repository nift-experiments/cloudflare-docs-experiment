<p>Cloudflare Realtime offers a simple yet powerful framework for building real-time experiences. At the core of this system are three key concepts: <strong>Applications</strong>,  <strong>Sessions</strong> and <strong>Tracks</strong>. Familiarizing yourself with these concepts is crucial for using Realtime.</p>
<h2 id="application">Application</h2>
<p>A Realtime Application is an environment within different Sessions and Tracks can interact. Examples of this could be production, staging or different environments where you'd want separation between Sessions and Tracks. Cloudflare Realtime usage can be queried at Application, Session or Track level.</p>
<h2 id="sessions">Sessions</h2>
<p>A <strong>Session</strong> in Cloudflare Realtime correlates directly to a WebRTC PeerConnection. It represents the establishment of a communication channel between a client and the nearest Cloudflare data center, as determined by Cloudflare's anycast routing. Typically, a client will maintain a single Session, encompassing all communications between the client and Cloudflare.</p>
<ul>
<li><strong>One-to-One Mapping with PeerConnection</strong>: Each Session is a direct representation of a WebRTC PeerConnection, facilitating real-time media data transfer.</li>
<li><strong>Anycast Routing</strong>: The client connects to the closest Cloudflare data center, optimizing latency and performance.</li>
<li><strong>Unified Communication Channel</strong>: A single Session can handle all types of communication between a client and Cloudflare, ensuring streamlined data flow.</li>
</ul>
<h2 id="tracks">Tracks</h2>
<p>Within a Session, there can be one or more <strong>Tracks</strong>.</p>
<ul>
<li><strong>Tracks map to MediaStreamTrack</strong>: Tracks align with the MediaStreamTrack concept, facilitating audio, video, or data transmission.</li>
<li><strong>Globally Unique Ids</strong>: When you push a track to Cloudflare, it is assigned a unique ID, which can then be used to pull the track into another session elsewhere.</li>
<li><strong>Available globally</strong>: The ability to push and pull tracks is central to what makes Realtime a versatile tool for real-time applications. Each track is available globally to be retrieved from any Session within an App.</li>
</ul>
<h2 id="realtime-as-a-programmable-switchboard">Realtime as a Programmable &quot;Switchboard&quot;</h2>
<p>The analogy of a switchboard is apt for understanding Realtime. Historically, switchboard operators connected calls by manually plugging in jacks. Similarly, Realtime allows for the dynamic routing of media streams, acting as a programmable switchboard for modern real-time communication.</p>
<h2 id="beyond-rooms-users-and-participants">Beyond &quot;Rooms&quot;, &quot;Users&quot;, and &quot;Participants&quot;</h2>
<p>While many SFUs utilize concepts like &quot;rooms&quot; to manage media streams among users, this approach has scalability and flexibility limitations. Cloudflare Realtime opts for a more granular and flexible model with Sessions and Tracks, enabling a wide range of use cases:</p>
<ul>
<li>Large-scale remote events, like 'fireside chats' with thousands of participants.</li>
<li>Interactive conversations with the ability to bring audience members &quot;on stage.&quot;</li>
<li>Educational applications where an instructor can present to multiple virtual classrooms simultaneously.</li>
</ul>
<h3 id="presence-protocol-vs-media-flow">Presence Protocol vs. Media Flow</h3>
<p>Realtime distinguishes between the presence protocol and media flow, allowing for scalability and flexibility in real-time applications. This separation enables developers to craft tailored experiences, from intimate calls to massive, low-latency broadcasts.</p>

<p>Over the years, efficient delivery of live media content has attracted significant interest from the networking and media streaming community. Many applications, including live streaming platforms, real-time communication systems, gaming, and interactive media experiences, require low-latency media delivery. However, it remained a major challenge to deliver media content in a scalable, efficient, and robust way over the internet. Currently, most solutions rely on proprietary protocols or repurpose existing protocols like HTTP/2 or WebRTC that weren't specifically designed for media streaming use cases.</p>
<p>Realizing this gap, the IETF Media Over QUIC (MoQ) working group was formed to develop a standardized protocol for media delivery over QUIC transport. The working group brings together expertise from major technology companies, content delivery networks, and academic institutions to create a modern solution for media streaming.</p>
<p>The MoQ protocol leverages QUIC's advanced features such as multiplexing, connection migration, and built-in security to provide an efficient foundation for media delivery. Unlike traditional HTTP-based streaming that treats media as regular web content, MoQ is specifically designed to understand media semantics and optimize delivery accordingly.</p>
<p>Key benefits of MoQ include:</p>
<ul>
<li><strong>Low latency</strong>: QUIC's 0-RTT connection establishment and reduced head-of-line blocking</li>
<li><strong>Adaptive streaming</strong>: Native support for different media qualities and bitrates</li>
<li><strong>Reliability</strong>: QUIC's connection migration and loss recovery mechanisms</li>
<li><strong>Security</strong>: Built-in encryption and authentication through QUIC</li>
<li><strong>Efficiency</strong>: Protocol designed specifically for media delivery patterns</li>
</ul>
<p>The protocol addresses common challenges in live streaming such as handling network congestion, adapting to varying bandwidth conditions, and maintaining synchronization between audio and video streams. MoQ represents a significant step forward in standardizing media delivery for the modern internet.</p>

<div class="nb-description">
@markup("md", "content/.markup/bodies/11576.md")
</div>
<p>Cloudflare Realtime SFU routes WebRTC media tracks and DataChannels between browser, native, server, and external media endpoints. Your application controls who publishes, who subscribes, and how participants discover each other.</p>
<p>Cloudflare Realtime SFU runs on <a href="https://www.cloudflare.com/network/">Cloudflare's global cloud network</a> in hundreds of cities worldwide.</p>
<h2 id="what-you-can-build">What you can build</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/11581.md")
</div>
<h2 id="application-architecture">Application architecture</h2>
<p>Each client creates a WebRTC PeerConnection. Your backend stores the application
secret and uses the Realtime SFU API to create the corresponding session. It
also authenticates users, authorizes publish and subscribe operations, and
shares session or track identifiers through your application state.</p>
<p>Realtime SFU forwards the selected media or data. It does not define rooms,
participants, roles, or presence for your application.</p>
<h2 id="explore-examples">Explore examples</h2>
<p>Use the <a href="https://github.com/cloudflare/realtime-examples">Realtime Examples repository</a>
to choose a starting point for what you want to build. Each example identifies
its status, credential boundary, and known limitations.</p>
<p><a class="nb-link-button" href="https://github.com/cloudflare/realtime-examples">Browse Realtime examples</a>
<a class="nb-link-button" href="/realtime/sfu/get-started/">Create an SFU application</a>
<a class="nb-link-button" href="https://dash.cloudflare.com/?to=/:account/calls">Realtime dashboard</a></p>

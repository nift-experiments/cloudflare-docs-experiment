<div class="nb-description">
@markup("md", "content/.markup/bodies/616.md")
</div>
<div class="nb-plan">
<p>Enterprise-only</p>
</div>
<p><a href="https://blog.cloudflare.com/building-privacy-into-internet-standards-and-how-to-make-your-app-more-private-today/">Privacy Gateway</a> is a managed service deployed on Cloudflare’s global network that implements part of the <a href="https://www.ietf.org/archive/id/draft-thomson-http-oblivious-01.html">Oblivious HTTP (OHTTP) IETF</a> standard. The goal of Privacy Gateway and Oblivious HTTP is to hide the client's IP address when interacting with an application backend.</p>
<p>OHTTP introduces a trusted third party between client and server, called a relay, whose purpose is to forward encrypted requests and responses between client and server. These messages are encrypted between client and server such that the relay learns nothing of the application data, beyond the length of the encrypted message and the server the client is interacting with.</p>
<hr />
<h2 id="availability">Availability</h2>
<p>Privacy Gateway is currently in closed beta – available to select privacy-oriented companies and partners. If you are interested, <a href="https://www.cloudflare.com/lp/privacy-edge/">contact us</a>.</p>
<hr />
<h2 id="features">Features</h2>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/617.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/618.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/619.md")
</div>

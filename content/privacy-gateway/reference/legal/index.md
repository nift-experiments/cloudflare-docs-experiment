<p>Privacy Gateway is a managed gateway service deployed on Cloudflare’s global network that implements the Oblivious HTTP IETF standard to improve client privacy when connecting to an application backend.</p>
<p>OHTTP introduces a trusted third party (Cloudflare in this case), called a relay, between client and server. The relay’s purpose is to forward requests from client to server, and likewise to forward responses from server to client. These messages are encrypted between client and server such that the relay learns nothing of the application data, beyond the server the client is interacting with.</p>
<p>The Privacy Gateway service follows <a href="https://www.cloudflare.com/privacypolicy/">Cloudflare’s privacy policy</a>.</p>
<h2 id="what-cloudflare-sees">What Cloudflare sees</h2>
<p>While Cloudflare will never see the contents of the encrypted application HTTP request proxied through the Privacy Gateway service – because the client will first connect to the OHTTP relay server operated in Cloudflare’s global network– Cloudflare will see the following information: the connecting device’s IP address, the application service they are using, including its DNS name and IP address, and metadata associated with the request, including the type of browser, device operating system, hardware configuration, and timestamp of the request (&quot;Privacy Gateway Logs&quot;).</p>
<h2 id="what-cloudflare-stores">What Cloudflare stores</h2>
<p>Cloudflare retains the Privacy Gateway Logs information for the most recent quarter plus one month (approximately 124 days).</p>
<h2 id="what-privacy-gateway-customers-see">What Privacy Gateway customers see</h2>
<ul>
<li>The application content of requests.</li>
<li>The IP address and associated metadata of the Cloudflare Privacy Gateway server the request came from.</li>
</ul>

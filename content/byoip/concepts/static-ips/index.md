<p>When you use Cloudflare as a <a href="/fundamentals/concepts/how-cloudflare-works/">reverse proxy</a>, Cloudflare assigns shared <a href="/fundamentals/concepts/cloudflare-ip-addresses/">anycast IP addresses</a> to proxied DNS records by default. These IPs can change at any time. Static IPs give you a set of specifically assigned Cloudflare IP addresses — Cloudflare will not change them without notifying you, and will typically only do so at your request.</p>
<p>Static IPs are useful when you need to allowlist your IPs or communicate them to third parties in advance.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3770.md")
</aside>
<p>Static IPs are allocated at the account level but can be assigned to a single zone, meaning multiple zones can share the same static IPs. You can specify which zones are mapped to your static IPs and control when the IPs for your zones change.</p>
<h2 id="availability">Availability</h2>
<p>Static IPs are available as an add-on purchase for Enterprise plans.</p>
<h2 id="check-static-ips">Check Static IPs</h2>
<p>You can find your leased Static IPs for CDN Ingress on the dashboard under <a href="https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space"><strong>Address space</strong> &gt; <strong>Leased IPs</strong></a>.</p>

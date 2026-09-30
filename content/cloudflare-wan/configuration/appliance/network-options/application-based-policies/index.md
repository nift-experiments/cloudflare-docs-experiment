<p>Standard traffic policies match on network-layer attributes like IP addresses and port ranges. Application-aware policies go further — they identify traffic by the application generating it, so you can make routing and security decisions based on what the traffic is, not just where it is going.</p>
<p>Cloudflare One Appliance (formerly Magic WAN Connector) classifies traffic using the same application categories used across Cloudflare's <a href="/cloudflare-one/traffic-policies/">Secure Web Gateway</a>. This means routing decisions on the Appliance and security policies in Gateway use the same application definitions.</p>
<p>For the full list of recognized applications and categories, refer to <a href="/cloudflare-one/traffic-policies/application-app-types/">Applications and app types</a>.</p>
<p>With application-aware policies, you can:</p>
<ul>
<li><strong>Break out traffic directly to the Internet</strong> — route specific applications directly to the Internet from the Appliance, bypassing Cloudflare's security filtering.</li>
<li><strong>Prioritize traffic</strong> — assign higher priority to specific applications so the Appliance processes them first when the network is congested.</li>
</ul>
<p>For details, refer to the following pages:</p>
<ul class="directory-listing"><li><a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/">Breakout traffic</a></li><li><a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/prioritized-traffic/">Prioritized traffic</a></li></ul>

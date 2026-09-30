<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3959.md")
</aside>
<h2 id="website-operators">Website operators</h2>
<h3 id="what-does-this-functionality-mean-for-me-as-a-website-operator">What does this functionality mean for me as a website operator?</h3>
<p>If you operate a website or ISP that needs to use IP address geolocation information for geographic content restriction, consider allowing IP addresses associated with a VPN.</p>
<p>You can now restrict content delivery to Cloudflare VPN users using the same client IP geolocation mechanisms used for non-VPN users.</p>
<h3 id="how-does-the-above-scenario-change-if-i-use-cloudflare-to-secure-my-infrastructure">How does the above scenario change if I use Cloudflare to secure my infrastructure?</h3>
<p>There is significant cross pollination between Cloudflare forward- and reverse-proxy services. When a user connects through Cloudflare proxies to origin infrastructure protected by Cloudflare security tools, our origin-facing tools automatically consume information from our user-facing systems about client geography, IP reputation, and other client metadata. This process happens in a privacy-preserving manner that reduces unnecessary collection of personally identifiable information while ensuring customers can maintain their desired security posture.</p>
<p>WAF custom rules specifying country- or region-level match criteria will match correctly on users passing through our VPN and forward-proxy systems with no action needed from you.</p>
<h3 id="in-the-example-what-happens-when-cloudflare-s-minneapolis-data-center-is-removed-from-service-for-maintenance">In the example, what happens when Cloudflare’s Minneapolis data center is removed from service for maintenance?</h3>
<p>The <a href="/client-ip-geolocation/about/#example-scenario">example scenario</a> still provides accurate geolocation data.</p>
<p>Geography-specific egress IPs are not tightly coupled to physical Cloudflare network locations. We continue using geography-specific egress IPs even if the geographically closest network location or locations are rerouted.</p>
<h3 id="what-happens-when-a-user-nests-or-chains-vpns-and-connects-to-cloudflare-through-a-downstream-proxy-service">What happens when a user nests or chains VPNs and connects to Cloudflare through a downstream proxy service?</h3>
<p>Cloudflare will make best efforts to identify such circumstances and communicate this information upstream to origins. Client IPs will geolocate as <code>unknown</code> when the entity that made the initial connection to Cloudflare appears to have originated from an open-proxy service or we are unsure of the location of the user.</p>
<h3 id="i-want-greater-geographic-detail-on-egress-locations-can-you-provide-it">I want greater geographic detail on egress locations. Can you provide it?</h3>
<p>Yes! We can provide much finer granularity for origins reachable over IPv6. We encourage adoption of IPv6 for the good of the Internet, as well as for providing much finer detail on user locations to origin operators.</p>
<h3 id="what-incentives-does-cloudflare-have-to-ensure-location-information-is-accurate">What incentives does Cloudflare have to ensure location information is accurate?</h3>
<p>Cloudflare wants those using our consumer VPN and corporate forward-proxy services to have as smooth an experience as possible. We want our users to have uninterrupted browsing experiences. At the same time, we also want to give origin operators the information they need to distribute the right content to the right users at the right times.</p>
<h2 id="cloudflare-vpn-users">Cloudflare VPN users</h2>
<h3 id="what-does-this-mean-for-me-as-a-cloudflare-vpn-user">What does this mean for me as a Cloudflare VPN user?</h3>
<p>If you use <a href="/warp-client/">Cloudflare WARP</a> or <a href="/1.1.1.1/">1.1.1.1</a>, geolocation improves your user experience. Because we communicate your geographic location accurately (but still in a non-identifiable way), you should have accurate, geography-specific experiences and uninterrupted access to the content you are licensed to consume in your local geography.</p>
<p>We also maintain all of our <a href="https://www.cloudflare.com/trust-hub/privacy-and-data-protection/">privacy commitments</a> regarding your use of our consumer application and will keep your Internet browsing private and secure.</p>
<h3 id="what-if-i-am-a-user-and-want-to-spoof-my-location">What if I am a user and want to spoof my location?</h3>
<p>Cloudflare does not permit or support the spoofing of location and will never offer such functionality in the future.</p>

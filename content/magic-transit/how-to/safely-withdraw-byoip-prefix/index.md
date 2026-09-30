<h3 id="mitigating-stuck-bgp-routes">Mitigating stuck BGP routes</h3>
<p>When you prepare to remove traffic for a <a href="/byoip/">Bring Your Own IP (BYOIP)</a> prefix from the Cloudflare edge, a direct BGP withdrawal action carries the risk of a stuck BGP route. This state occurs when a route becomes stuck in the Internet's <a href="https://en.wikipedia.org/wiki/Default-free_zone">Default-Free Zone (DFZ)</a>. Core routers that missed the withdrawal announcement continue forwarding traffic to a now-inactive next-hop (what is known as a blackhole). You can read more about this in our blog post <a href="https://blog.cloudflare.com/going-bgp-zombie-hunting">BGP zombies and excessive path hunting</a>.</p>
<p>This risk is especially evident in the use case where the global routing table relies on more-specific to less-specific prefix routing fallback. Since this fallback mechanism is highly prone to route instability, Cloudflare recommends a multi-step draining process.</p>
<h3 id="multi-step-byoip-withdrawal-process">Multi-step BYOIP withdrawal process</h3>
<p>When draining traffic, use the same prefix length on Cloudflare and on your ISP (Internet Service Provider), since matching prefix lengths gives the most effective and deterministic behavior.</p>
<p>The following steps outline the recommended multi-step draining process to achieve a clean traffic cutover and prevent blackholing.</p>
<ol>
<li><strong>Initiate advertisement from your origin network</strong>: Begin announcing the exact same-length prefix (for example, <code>192.0.2.0/24</code>) from your local infrastructure to your upstream Internet Service Providers (ISPs). This action introduces a competing route of the same length into the global routing table. BGP best path selection will favor your native route based on other metrics (for example, shorter AS path length or local preference), allowing traffic to begin draining away from the Cloudflare edge. Note that some of your traffic may not route as expected, since this depends on how your ISP prefers routes (for example, the Cloudflare route may be treated as a less-preferred path if not fully withdrawn).</li>
<li><strong>Wait for global BGP convergence</strong>: Allow a period of time (typically five to ten minutes) for the new native advertisement to propagate fully across the global routing table, and for routes to converge. This passive waiting period ensures that the majority of traffic has shifted to your local network before the next step.</li>
<li><strong>Signal BGP withdrawal from the Cloudflare edge</strong>: Once you have verified that traffic has successfully drained, use one of the BGP control methods to stop the advertisement of the prefix from the Cloudflare edge.</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="isp-route-refresh-delays-may-impact-traffic">ISP route refresh delays may impact traffic</h3>
@markup("md", "content/.markup/bodies/10654.md")
</aside>
<ol start="4">
<li>The draining process is complete.</li>
</ol>

<p>Improve the Tor user experience by enabling Onion Routing, which enables Cloudflare to serve your website’s content directly through the Tor network and without requiring exit nodes.</p>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="how-it-works">How it works</h2>
<p>Onion Routing helps improve Tor browsing as follows:</p>
<ul>
<li>Tor users no longer access your site via exit nodes, which can sometimes be compromised, and may snoop on user traffic.</li>
<li>Human Tor users and bots can be distinguished by our Onion services, such that interactive challenges are only served to malicious bot traffic.</li>
</ul>
<p><a href="https://tb-manual.torproject.org/about/">Tor Browser</a> users receive an <a href="https://httpwg.org/specs/rfc7838.html#alt-svc">alt-svc header</a> as part of the response to the first request to your website. The browser then creates a Tor Circuit to access this website using the <code>.onion</code> TLD service provided by this header.</p>
<p>You should note that the visible domain in the user interface remains unchanged, as the host header and the SNI are preserved. However, the underlying connection changes to be routed through Tor, as the <a href="https://tb-manual.torproject.org/managing-identities/#managing-identities">UI denotes on the left of the address bar</a> with a Tor Circuit. Cloudflare does not provide a certificate for the <code>.onion</code> domain provided as part of alt-svc flow, which therefore cannot be accessed via HTTPS.</p>
<h2 id="enable-onion-routing">Enable Onion Routing</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/674.md")
</div></div>

<p>In one of the scenarios below, you notice that stale DNS responses are used. Depending on the scenario and other aspects of your configuration, this can cause wrong content or no content to be returned.</p>
<ul>
<li>A <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
@markup("md", "content/.markup/bodies/7763.md")
</div> CNAME record ([flattened by default](/dns/cname-flattening/)).
- A DNS-only CNAME record that has flattening turned on. This can happen either via the specific record configuration or as a consequence of the [zone settings](/dns/cname-flattening/set-up-cname-flattening/).
- A [Workers](/workers/) script making a subrequest to an external hostname<sup><a href="#footnote-1">1</a></sup>.
<h2 id="cause">Cause</h2>
<p>In the event that an upstream DNS server takes too long to respond, or the upstream returns a SERVFAIL, Cloudflare will use the expired DNS response from the cache and then attempt to update that cache asynchronously.</p>
<h2 id="solutions">Solutions</h2>
<ul>
<li>
<p>If possible, temporarily replace the proxied CNAME with a proxied A record. This may not always be possible, especially if the upstream target is a load balancer or if it returns dynamic responses.</p>
</li>
<li>
<p>Report the issues to the zone owner or DNS provider for the upstream target that is unresponsive.</p>
</li>
<li>
<p>You can also raise the issue through the DNS Operations Analysis and Research Center (DNS OARC). Consider its <a href="https://www.dns-oarc.net/oarc/services/chat">chat platform</a> or <a href="https://www.dns-oarc.net/oarc/lists">email lists</a>.</p>
</li>
</ul>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">A hostname that is not using Cloudflare as its [authoritative DNS provider](/dns/concepts/#authoritative-dns).</li></ol></section>

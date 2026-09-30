<p>The Cloudflare Rules language supports different types of fields such as:</p>
<ul>
<li>Request fields that represent the basic properties of incoming requests, including specific fields for accessing request headers, URI components, and the request body.</li>
<li>Dynamic fields that represent computed or derived values, typically related to threat intelligence about an HTTP request.</li>
<li>Response fields that represent the basic properties of the received response.</li>
<li>Raw fields that preserve the original request values for later evaluations.</li>
</ul>
<p>Refer to the <a href="/ruleset-engine/rules-language/fields/reference/">Fields reference</a> for the list of available fields.</p>
<h2 id="differences-from-wireshark-display-fields">Differences from Wireshark display fields</h2>
<p>Most fields supported by the Cloudflare Rules language use the same naming conventions as <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html">Wireshark display fields</a>. However, there are some subtle differences between Cloudflare and Wireshark:</p>
<ul>
<li>
<p>Wireshark supports <a href="https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing">CIDR (Classless Inter-Domain Routing) notation</a> for expressing IP address ranges in equality comparisons (<code>ip.src == 1.2.3.0/24</code>, for example). Cloudflare does not.</p>
<p>To evaluate a range of addresses using CIDR notation, use the <a href="/ruleset-engine/rules-language/operators/#comparison-operators"><code>in</code></a> comparison operator as in this example: <code>ip.src in {1.2.3.0/24 4.5.6.0/24}</code>.</p>
</li>
<li>
<p>In Wireshark, <code>ssl</code> is a protocol field containing hundreds of other fields of various types that are available for comparison in multiple ways. However, in the Rules language <a href="/ruleset-engine/rules-language/fields/reference/ssl/"><code>ssl</code></a> is a single Boolean field that indicates whether the connection from the client to Cloudflare is encrypted.</p>
</li>
<li>
<p>The Cloudflare Rules language does not support the <code>slice</code> operator.</p>
</li>
</ul>

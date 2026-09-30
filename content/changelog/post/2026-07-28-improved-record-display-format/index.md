<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 28, 2026</time><h2 id="post-title">Improved DoH JSON formatting for additional record types</h2>
<div class="changelog-badges"><span>1.1.1.1</span></div><div class="changelog-body"><p>Cloudflare is rolling out updated formatting for the <code>data</code> field in the 1.1.1.1 <a href="/1.1.1.1/encryption/dns-over-https/make-api-requests/dns-json/">DoH JSON API</a> (<code>application/dns-json</code>). During the roll out responses may use either the old or new format.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17613.md")</aside>
<h4 id="human-readable-display-for-additional-record-types">Human-readable display for additional record types</h4>
<p>Several record types previously returned their <code>data</code> field in <a href="https://datatracker.ietf.org/doc/html/rfc3597">RFC 3597</a> generic hex encoding (<code>\# &lt;length&gt; &lt;hex&gt;</code>). These now use standard presentation format:</p>
<pre><code class="language-txt">CAA:        0 issue &quot;letsencrypt.org&quot;&#10;NAPTR:      100 10 &quot;s&quot; &quot;SIP+D2U&quot; &quot;&quot; _sip._udp.example.com.&#10;RP:         admin.example.com. txt.example.com.&#10;IPSECKEY:   10 1 2 192.0.2.1 AwEA...&#10;SVCB:       1 target.example.com. alpn=h2&#10;HTTPS:      1 . alpn=h3,h2 ipv4hint=192.0.2.1&#10;TLSA:       3 1 1 aabbccdd...&#10;SSHFP:      1 2 aabbccdd...&#10;OPENPGPKEY: AwEA...&#10;</code></pre>
<h4 id="numeric-dnssec-algorithm-identifiers">Numeric DNSSEC algorithm identifiers</h4>
<p>DNSSEC-related records now use numeric algorithm identifiers as defined in <a href="https://datatracker.ietf.org/doc/html/rfc4034">RFC 4034</a> instead of mnemonic names. This affects <code>RRSIG</code>, <code>DS</code>, <code>CDS</code>, <code>DNSKEY</code>, and <code>CDNSKEY</code> records. For example, <code>RSASHA256</code> becomes <code>8</code>, <code>ECDSAP256SHA256</code> becomes <code>13</code>, and <code>ED25519</code> becomes <code>15</code>. DS digest types also change from mnemonic to numeric: <code>SHA-256</code> becomes <code>2</code>.</p>
<pre><code class="language-txt">RRSIG:  A RSASHA256 2 300 ...&#10;DS:     12345 RSASHA256 SHA-256 aabb...&#10;DNSKEY: 257 3 RSASHA256 AwEA...&#10;</code></pre>
<pre><code class="language-txt">RRSIG:  A 8 2 300 ...&#10;DS:     12345 8 2 aabb...&#10;DNSKEY: 257 3 8 AwEA...&#10;</code></pre>
<h4 id="other-formatting-changes">Other formatting changes</h4>
<p><code>HINFO</code> character-strings are now individually quoted to remove ambiguity when values contain spaces:</p>
<pre><code class="language-txt">&quot;data&quot;: &quot;Intel Xeon Linux&quot;&#10;</code></pre>
<pre><code class="language-txt">&quot;data&quot;: &quot;\&quot;Intel Xeon\&quot; \&quot;Linux\&quot;&quot;&#10;</code></pre>
</div></article></div>

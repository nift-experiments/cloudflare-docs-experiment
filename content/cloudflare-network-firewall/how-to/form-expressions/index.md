<p>Rules are written as using the Cloudflare Rules language - a domain-specific language (DSL) intended to mimic Wireshark semantics. For more information, refer to the <a href="/ruleset-engine/rules-language/">Rules language</a> documentation.</p>
<p>To start with a simple case, review below how you would match a source IP:</p>
<pre><code class="language-txt">ip.src == 192.0.2.0&#10;</code></pre>
<p>Expressions can be more complex by joining multiple clauses via a logical operator:</p>
<pre><code class="language-txt">ip.src == 192.0.2.1 &amp;&amp; (tcp.flags.push || tcp.flags.reset)&#10;</code></pre>
<h2 id="capabilities">Capabilities</h2>
<p>You can use Cloudflare Network Firewall (formerly Magic Firewall) to skip or block <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/4265.md")
</div> based on source or destination IP, source or destination port, protocol, packet length, or <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/4266.md")
</div>.
<h2 id="restrictions">Restrictions</h2>
<p>Wirefilter comparisons support CIDR notation, but only inside sets. For example:</p>
<pre><code class="language-txt">ip.src == 192.0.2.0/24  # bad&#10;ip.src in { 192.0.2.0/24 }  # good&#10;</code></pre>
<p>Expressions have a complexity limit that is easily reached when many joined or nested clauses are in the expression. Here's an example:</p>
<pre><code class="language-txt">(tcp.dstport == 1000 || tcp.dstport == 1001) &amp;&amp; (tcp.dstport == 1002 || tcp.dstport == 1003) &amp;&amp; (tcp.dstport == 1004 || tcp.dstport == 1005) &amp;&amp; (tcp.dstport == 1006 || tcp.dstport == 1007) &amp;&amp; (tcp.dstport == 1008 || tcp.dstport == 1009) &amp;&amp; (tcp.dstport == 1010 || tcp.dstport == 1011) &amp;&amp; (tcp.dstport == 1012 || tcp.dstport == 1013) &amp;&amp; (tcp.dstport == 1014 || tcp.dstport == 1015) &amp;&amp; (tcp.dstport == 1016 || tcp.dstport == 1017)&#10;</code></pre>
<p>If the limit is reached, the response will have a <code>400</code> status code and an error message of <code>ruleset exceeds complexity constraints</code>. Split the expression into multiple rules and try again.</p>

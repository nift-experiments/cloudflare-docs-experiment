<p>Rules are written using the Cloudflare Rules language - a domain-specific language (DSL) intended to mimic Wireshark semantics. For more information, refer to the <a href="/ruleset-engine/rules-language/">Rules language</a> documentation.</p>
<p>To start with a simple case, review below how you would match a source IP. In this expression, <code>ip.src</code> refers to the source IP address of the incoming packet, and <code>==</code> means &quot;equals&quot;:</p>
<pre><code class="language-txt">ip.src == 192.0.2.0&#10;</code></pre>
<p>Expressions can be more complex by joining multiple clauses via a logical operator (<code>&amp;&amp;</code> means AND, <code>||</code> means OR). The following expression matches packets from <code>192.0.2.1</code> that also have the TCP push or reset flag set:</p>
<pre><code class="language-txt">ip.src == 192.0.2.1 &amp;&amp; (tcp.flags.push || tcp.flags.reset)&#10;</code></pre>
<h2 id="capabilities">Capabilities</h2>
<p>You can use Cloudflare Network Firewall to skip or block <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/6416.md")
</div> based on source or destination IP, source or destination port, protocol, packet length, or <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/6417.md")
</div>.
<h2 id="restrictions">Restrictions</h2>
<p>The expression engine supports CIDR notation (IP address ranges like <code>192.0.2.0/24</code>), but only inside curly-brace sets. A bare comparison will not work as expected:</p>
<pre><code class="language-txt">ip.src == 192.0.2.0/24  # bad&#10;ip.src in { 192.0.2.0/24 }  # good&#10;</code></pre>
<p>Expressions have a complexity limit that is easily reached when many joined or nested clauses are in the expression. Here's an example:</p>
<pre><code class="language-txt">(tcp.dstport == 1000 || tcp.dstport == 1001) &amp;&amp; (tcp.dstport == 1002 || tcp.dstport == 1003) &amp;&amp; (tcp.dstport == 1004 || tcp.dstport == 1005) &amp;&amp; (tcp.dstport == 1006 || tcp.dstport == 1007) &amp;&amp; (tcp.dstport == 1008 || tcp.dstport == 1009) &amp;&amp; (tcp.dstport == 1010 || tcp.dstport == 1011) &amp;&amp; (tcp.dstport == 1012 || tcp.dstport == 1013) &amp;&amp; (tcp.dstport == 1014 || tcp.dstport == 1015) &amp;&amp; (tcp.dstport == 1016 || tcp.dstport == 1017)&#10;</code></pre>
<p>If the limit is reached, the response will have a <code>400</code> status code and an error message of <code>ruleset exceeds complexity constraints</code>. Split the expression across multiple rules and try again. Each rule can handle a subset of the conditions, and the firewall evaluates them in order.</p>

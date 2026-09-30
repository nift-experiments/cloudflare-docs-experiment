<p>Magic Transit is a network security and performance solution that offers Distributed Denial of Service (<a href="/ddos-protection/">DDoS</a>) protection, traffic acceleration, and more for on-premise, cloud-hosted, and hybrid networks.</p>
<p>Magic Transit delivers its connectivity, security, and performance benefits by serving as the front door to your IP network. This means it accepts IP <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/786.md")
</div> destined for your network, processes them, and then outputs them to your origin infrastructure.
<p>The Cloudflare network uses <a href="https://www.cloudflare.com/learning/security/glossary/what-is-bgp/">Border Gateway Protocol (BGP)</a> to announce your company's IP address space, extending your network presence globally, and <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/787.md")
</div> to ingest your traffic. Today, Cloudflare's anycast global network spans [hundreds of cities worldwide](https://www.cloudflare.com/network/).
<p>Once <a href="https://www.cloudflare.com/learning/network-layer/what-is-a-packet/">packets</a> hit Cloudflare's network, Cloudflare inspects traffic for attacks, filters, <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/788.md")
</div>, accelerates, and sends it to your origin. Magic Transit connects to your origin infrastructure using anycast <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/789.md")
</div> tunnels over the Internet or, with [Cloudflare Network Interconnect (CNI)](/network-interconnect/), through physical or virtual interconnect.
<p>You have two options for your Magic Transit implementation: ingress traffic or ingress and <a href="/magic-transit/reference/egress/">egress traffic</a>. With an egress implementation, you must set up <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/790.md")
</div> or ensure default routing on your end forwards traffic to Cloudflare through tunnels.
<pre><code class="language-mermaid">flowchart LR&#10;accTitle: Magic Transit&#10;accDescr: Diagram showing how Magic Transit protects traffic on the customer&#x27;s network.&#10;&#10;A(DDoS &lt;br&gt; attack)&#10;B[(&quot;Cloudflare global &lt;br&gt; anycast network &lt;br&gt; (DDoS protection + &lt;br&gt; network firewall)&quot;)]&#10;C[Customer &lt;br&gt; network]&#10;D((User))&#10;E([BGP &lt;br&gt; announcement])&#10;&#10;A --x B&#10;E --- B&#10;B-- Anycast &lt;br&gt; GRE tunnel ---C&#10;B-- Cloudflare &lt;br&gt; Network &lt;br&gt; Interconnect ---C&#10;C-- Egress through &lt;br&gt; Direct Server &lt;br&gt; Return --&gt; D&#10;D -- Ingress --&gt; B&#10;&#10;style A stroke: red,fill: red,color: white&#10;style B stroke: orange,fill: orange,color: black&#10;style C stroke: #ADD8E6,fill: #ADD8E6,color: black&#10;style D stroke: blue,fill: blue,color: white&#10;linkStyle 0 stroke-width:3px,stroke:red&#10;linkStyle 1 stroke-width:2px,stroke:orange&#10;linkStyle 2 stroke-width:2px,stroke:#ADD8E6&#10;linkStyle 3 stroke-width:2px,stroke:gray&#10;linkStyle 4 stroke-width:3px,stroke:green&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/785.md")
</aside>
<p>For detailed information on Magic Transit architecture, refer to the <a href="/magic-transit/reference/">Reference section</a>.</p>

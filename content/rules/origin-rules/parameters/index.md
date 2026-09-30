<p>Create <a href="/rules/origin-rules/features/">different overrides</a> by including different action parameters in the <code>action_parameters</code> field:</p>
<table>
<thead>
<tr>
<th>Override type</th>
<th>What to include</th>
</tr>
</thead>
<tbody>
<tr>
<td>Host header override</td>
<td><a href="#host-header-override-parameters"><code>host_header</code> parameter</a></td>
</tr>
<tr>
<td>SNI override</td>
<td><a href="#sni-override-parameters"><code>sni</code> object</a></td>
</tr>
<tr>
<td>DNS record override / Destination port override</td>
<td><a href="#dns-record-override-and-destination-port-override-parameters"><code>origin</code> object</a></td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12955.md")
</aside>
<h2 id="host-header-override-parameters">Host header override parameters</h2>
<p>The full syntax of the <code>action_parameters</code> field for overriding the HTTP <code>Host</code> header is the following:</p>
<pre><code class="language-json">&quot;action_parameters&quot;: {&#10;  &quot;host_header&quot;: &quot;&lt;HOST_HEADER_VALUE&gt;&quot;&#10;}&#10;</code></pre>
<h2 id="sni-override-parameters">SNI override parameters</h2>
<p>The full syntax of the <code>action_parameters</code> field for overriding the SNI value of incoming requests is the following:</p>
<pre><code class="language-json">&quot;action_parameters&quot;: {&#10;  &quot;sni&quot;: {&#10;    &quot;value&quot;: &quot;&lt;SNI_VALUE&gt;&quot;&#10;  }&#10;}&#10;</code></pre>
<h2 id="dns-record-override-and-destination-port-override-parameters">DNS record override and destination port override parameters</h2>
<p>The full syntax of the <code>action_parameters</code> field for overriding both the hostname and the destination port of incoming requests is the following:</p>
<pre><code class="language-json">&quot;action_parameters&quot;: {&#10;  &quot;origin&quot;: {&#10;    &quot;host&quot;: &quot;&lt;HOSTNAME&gt;&quot;,&#10;    &quot;port&quot;: &lt;PORT&gt;&#10;  }&#10;}&#10;</code></pre>
<p>If you are only overriding the hostname or the port, omit the <code>port</code> or <code>host</code> parameter, respectively.</p>
<h2 id="configuring-several-overrides-in-the-same-rule">Configuring several overrides in the same rule</h2>
<p>The same origin rule can have different types of overrides. For example, a single origin rule can perform an HTTP <code>Host</code> header override and a destination port override. The syntax of such a rule would be the following:</p>
<pre><code class="language-json">&quot;action_parameters&quot;: {&#10;  &quot;host_header&quot;: &quot;&lt;HOST_HEADER_VALUE&gt;&quot;,&#10;  &quot;origin&quot;: {&#10;    &quot;port&quot;: &lt;PORT&gt;&#10;  }&#10;}&#10;</code></pre>

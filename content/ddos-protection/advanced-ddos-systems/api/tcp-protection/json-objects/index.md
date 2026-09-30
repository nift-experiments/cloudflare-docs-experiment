<p>This page contains an example of the TCP protection rule JSON object used in the API.</p>
<h2 id="prefix">Prefix</h2>
<pre><code class="language-json">{&#10;  &quot;id&quot;: &quot;31c70c65-9f81-4669-94ed-1e1e041e7b06&quot;,&#10;  &quot;prefix&quot;: &quot;192.0.2.0/24&quot;,&#10;  &quot;comment&quot;: &quot;Game ranges&quot;,&#10;  &quot;excluded&quot;: false,&#10;  &quot;created_on&quot;: &quot;2022-01-01T13:06:04.721954+01:00&quot;,&#10;  &quot;modified_on&quot;: &quot;2022-01-01T13:06:04.721954+01:00&quot;&#10;}&#10;</code></pre>
<h2 id="prefix-in-allowlist">Prefix in allowlist</h2>
<pre><code class="language-json">{&#10;  &quot;id&quot;: &quot;31c70c65-9f81-4669-94ed-1e1e041e7b06&quot;,&#10;  &quot;prefix&quot;: &quot;192.0.2.0/24&quot;,&#10;  &quot;comment&quot;: &quot;Game ranges&quot;,&#10;  &quot;enabled&quot;: true,&#10;  &quot;created_on&quot;: &quot;2021-10-01T13:06:04.721954+01:00&quot;,&#10;  &quot;modified_on&quot;: &quot;2021-10-01T13:06:04.721954+01:00&quot;&#10;}&#10;</code></pre>
<p>The <code>prefix</code> field can contain an IP address or a CIDR range.</p>
<h2 id="syn-flood-rule-or-out-of-state-tcp-rule">SYN flood rule or out-of-state TCP rule</h2>
<pre><code class="language-json">{&#10;  &quot;id&quot;: &quot;31c70c65-9f81-4669-94ed-1e1e041e7b06&quot;,&#10;  &quot;scope&quot;: &quot;region&quot;,&#10;  &quot;name&quot;: &quot;WEUR&quot;,&#10;  &quot;rate_sensitivity&quot;: &quot;medium&quot;,&#10;  &quot;burst_sensitivity&quot;: &quot;medium&quot;,&#10;  &quot;created_on&quot;: &quot;2021-10-01T13:10:38.762503+01:00&quot;,&#10;  &quot;modified_on&quot;: &quot;2021-10-01T13:10:38.762503+01:00&quot;&#10;}&#10;</code></pre>
<p>The <code>scope</code> field value must be one of <code>global</code>, <code>region</code>, or <code>datacenter</code>. You must provide a region code (or data center code) in the <code>name</code> field when specifying a <code>region</code> (or <code>datacenter</code>) scope.</p>
<p>The <code>rate_sensitivity</code> and <code>burst_sensitivity</code> field values must be one of <code>low</code>, <code>medium</code>, or <code>high</code>.</p>
<h2 id="filter">Filter</h2>
<pre><code class="language-json">{&#10;  &quot;id&quot;: &quot;20b99eb6-8b48-48dd-a5b9-a995a0843b57&quot;,&#10;  &quot;expression&quot;: &quot;ip.dst in { 192.0.2.0/24 203.0.113.0/24 } and tcp.dstport in { 80 443 10000..65535 }&quot;,&#10;  &quot;mode&quot;: &quot;enabled&quot;,&#10;  &quot;created_on&quot;: &quot;2022-11-01T13:10:38.762503+01:00&quot;,&#10;  &quot;modified_on&quot;: &quot;2022-11-01T13:10:38.762503+01:00&quot;&#10;}&#10;</code></pre>
<p>The <code>expression</code> field is a <a href="/ruleset-engine/rules-language/expressions/">Rules language expression</a> up to 8,192 characters that can include the following fields:</p>
<ul>
<li><code>ip.src</code></li>
<li><code>ip.dst</code></li>
<li><code>tcp.srcport</code></li>
<li><code>tcp.dstport</code></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7512.md")
</aside>
<p>The <code>mode</code> value must be one of <code>enabled</code>, <code>disabled</code>, or <code>monitoring</code>.</p>

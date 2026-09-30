<p><em>Cloudflare Pipelines scalar function implementations are based on
<a href="https://arrow.apache.org/datafusion/">Apache DataFusion</a> (via <a href="https://www.arroyo.dev/">Arroyo</a>) and these docs are derived from
the DataFusion function reference.</em></p>
<h2 id="encode"><code>encode</code></h2>
<p>Encode binary data into a textual representation.</p>
<pre><code>encode(expression, format)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li>
<p><strong>expression</strong>: Expression containing string or binary data</p>
</li>
<li>
<p><strong>format</strong>: Supported formats are: <code>base64</code>, <code>hex</code></p>
</li>
</ul>
<p><strong>Related functions</strong>:
<a href="#decode">decode</a></p>
<h2 id="decode"><code>decode</code></h2>
<p>Decode binary data from textual representation in string.</p>
<pre><code>decode(expression, format)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li>
<p><strong>expression</strong>: Expression containing encoded string data</p>
</li>
<li>
<p><strong>format</strong>: Same arguments as <a href="#encode">encode</a></p>
</li>
</ul>
<p><strong>Related functions</strong>:
<a href="#encode">encode</a></p>

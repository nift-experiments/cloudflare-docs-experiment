<ul>
<li><a href="/workers/configuration/compatibility-dates">Compatibility Dates Reference</a></li>
</ul>
<h2 id="compatibility-dates">Compatibility Dates</h2>
<p>Miniflare uses compatibility dates to opt-into backwards-incompatible changes
from a specific date. If one isn't set, it will default to some time far in the
past.</p>
<pre><code class="language-js">const mf = new Miniflare({&#10;	compatibilityDate: &quot;2021-11-12&quot;,&#10;});&#10;</code></pre>
<h2 id="compatibility-flags">Compatibility Flags</h2>
<p>Miniflare also lets you opt-in/out of specific changes using compatibility
flags:</p>
<pre><code class="language-js">const mf = new Miniflare({&#10;	compatibilityFlags: [&#10;		&quot;formdata_parser_supports_files&quot;,&#10;		&quot;durable_object_fetch_allows_relative_url&quot;,&#10;	],&#10;});&#10;</code></pre>

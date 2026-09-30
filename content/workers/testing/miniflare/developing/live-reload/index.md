<p>Miniflare automatically refreshes your browser when your Worker script
changes when <code>liveReload</code> is set to <code>true</code>.</p>
<pre><code class="language-js">const mf = new Miniflare({&#10;	liveReload: true,&#10;});&#10;</code></pre>
<p>Miniflare will only inject the <code>&lt;script&gt;</code> tag required for live-reload at the
end of responses with the <code>Content-Type</code> header set to <code>text/html</code>:</p>
<pre><code class="language-js">export default {&#10;	fetch() {&#10;		const body = `&#10;      &lt;!DOCTYPE html&gt;&#10;      &lt;html&gt;&#10;      &lt;body&gt;&#10;        &lt;p&gt;Try update me!&lt;/p&gt;&#10;      &lt;/body&gt;&#10;      &lt;/html&gt;&#10;    `;&#10;&#10;		return new Response(body, {&#10;			headers: { &quot;Content-Type&quot;: &quot;text/html; charset=utf-8&quot; },&#10;		});&#10;	},&#10;};&#10;</code></pre>

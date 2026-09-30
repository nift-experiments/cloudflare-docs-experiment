<ul>
<li><a href="/d1/">D1 Reference</a></li>
</ul>
<h2 id="databases">Databases</h2>
<p>Specify D1 Databases to add to your environment as follows:</p>
<pre><code class="language-js">const mf = new Miniflare({&#10;	d1Databases: {&#10;		DB: &quot;xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx&quot;,&#10;	},&#10;});&#10;</code></pre>
<h2 id="working-with-d1-databases">Working with D1 Databases</h2>
<p>For testing, it can be useful to put/get data from D1 storage
bound to a Worker. You can do this with the <code>getD1Database</code> method:</p>
<pre><code class="language-js">const db = await mf.getD1Database(&quot;DB&quot;);&#10;const stmt = await db.prepare(&quot;&lt;Query&gt;&quot;);&#10;const returnValue = await stmt.run();&#10;&#10;return Response.json(returnValue.results);&#10;</code></pre>

<p>You can have Rocket Loader ignore individual scripts by adding the <code>data-cfasync=&quot;false&quot;</code> attribute to the relevant script tag:</p>
<pre><code class="language-html">&lt;script data-cfasync=&quot;false&quot; src=&quot;/javascript.js&quot;&gt;&lt;/script&gt;&#10;</code></pre>
<p>Rocket Loader will still optimize the loading of all other scripts on the page.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13945.md")
</aside>
<h2 id="limitations">Limitations</h2>
<ul>
<li>Adding this attribute within JavaScript will not work if you wish to exclude the script from Rocket Loader.</li>
<li>If the script you want Rocket Loader to ignore has dependency on other JavaScript(s) on the page, those dependencies must also have the <code>data-cfasync=&quot;false&quot;</code> attribute.</li>
<li>The <code>data-cfasync</code> attribute must be added before the <code>src</code> attribute.</li>
<li>Rocket Loader will recognize the tag when either single or double quotes are placed around the attribute value.</li>
</ul>

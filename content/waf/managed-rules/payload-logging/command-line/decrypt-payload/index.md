<p>Use the <code>matched-data-cli</code> tool to decrypt a payload in the command line.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15663.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15662.md")
</aside>
<h2 id="example">Example</h2>
<p>The following example creates two files — one with the private key and another one with the encrypted payload — and runs the <code>matched-data-cli</code> tool to decrypt the payload in the <code>encrypted_payload.txt</code> file:</p>
<pre><code class="language-sh">~ cd matched-data-cli&#10;&#10;printf &quot;uBS5eBttHrqkdY41kbZPdvYnNz8Vj0TvKIUpjB1y/GA=&quot; &gt; private_key.txt &amp;&amp; chmod 400 private_key.txt&#10;&#10;printf &quot;AzTY6FHajXYXuDMUte82wrd+1n5CEHPoydYiyd3FMg5IEQAAAAAAAAA0lOhGXBclw8pWU5jbbYuepSIJN5JohTtZekLliJBlVWk=&quot; &gt; encrypted_payload.txt&#10;&#10;decrypt -k private_key.txt encrypted_payload.txt&#10;</code></pre>
<pre><code class="language-txt">test matched data&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="encryption-formats">Encryption formats</h3>
@markup("md", "content/.markup/bodies/15661.md")
</aside>

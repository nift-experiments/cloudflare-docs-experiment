<p>To delete a key-value pair, call the <code>delete()</code> method of the <a href="/kv/concepts/kv-bindings/">KV binding</a> on any <a href="/kv/concepts/kv-namespaces/">KV namespace</a> you have bound to your Worker code:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9596.md")
</div></div>
<h4 id="example">Example</h4>
<p>An example of deleting a key-value pair from within a Worker:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9599.md")
</div></div>
<h2 id="reference">Reference</h2>
<p>The following method is provided to delete from KV:</p>
<ul>
<li><a href="#delete-method">delete()</a></li>
</ul>
<h3 id="delete-method"><code>delete()</code> method</h3>
<p>To delete a key-value pair, call the <code>delete()</code> method of the <a href="/kv/concepts/kv-bindings/">KV binding</a> on any KV namespace you have bound to your Worker code:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9602.md")
</div></div>
<h4 id="parameters">Parameters</h4>
<ul>
<li><code>key</code>: <code>string</code>
<ul>
<li>The key to associate with the value.</li>
</ul>
</li>
</ul>
<h4 id="response">Response</h4>
<ul>
<li><code>response</code>: <code>Promise&lt;void&gt;</code>
<ul>
<li>A <code>Promise</code> that resolves if the delete is successful.</li>
</ul>
</li>
</ul>
<p>This method returns a promise that you should <code>await</code> on to verify successful deletion. Calling <code>delete()</code> on a non-existing key is returned as a successful delete.</p>
<p>Calling the <code>delete()</code> method will remove the key and value from your KV namespace. As with any operations, it may take some time for the key to be deleted from various points in the Cloudflare global network.</p>
<h2 id="guidance">Guidance</h2>
<h3 id="delete-data-in-bulk">Delete data in bulk</h3>
<p>Delete more than one key-value pair at a time with Wrangler or <a href="/api/resources/kv/subresources/namespaces/subresources/keys/methods/bulk_delete/">via the REST API</a>.</p>
<p>The bulk REST API can accept up to 10,000 KV pairs at once. Bulk writes are not supported using the <a href="/kv/concepts/kv-bindings/">KV binding</a>.</p>
<h2 id="other-methods-to-access-kv">Other methods to access KV</h2>
<p>You can also <a href="/kv/reference/kv-commands/#kv-namespace-delete">delete key-value pairs from the command line with Wrangler</a> or <a href="/api/resources/kv/subresources/namespaces/subresources/values/methods/delete/">with the REST API</a>.</p>

<!-- Auto Generated Below -->
<p><a name="module_RTKStore"></a></p>
<p>This module represents a single global store.
The store can be accessed from the <code>meeting.stores</code> module.</p>
<p><strong>Returns</strong>: An instance of RTKStore.<br />
<strong>Example</strong></p>
<pre><code class="language-js">const handRaiseStore = meeting.stores.stores.get(&#x27;handRaise&#x27;);&#10;</code></pre>
<ul>
<li><a href="#module_RTKStore">RTKStore</a> ⇒
<ul>
<li><a href="#module_RTKStore+set">.set(key, value, [sync], [emit])</a> ⇒ <code>Promise.&lt;void&gt;</code></li>
<li><a href="#module_RTKStore+bulkSet">.bulkSet(data)</a> ⇒ <code>Promise.&lt;void&gt;</code></li>
<li><a href="#module_RTKStore+update">.update(key, value, [sync])</a> ⇒ <code>Promise.&lt;void&gt;</code></li>
<li><a href="#module_RTKStore+delete">.delete(key, [sync], [emit])</a> ⇒ <code>Promise.&lt;void&gt;</code></li>
<li><a href="#module_RTKStore+bulkDelete">.bulkDelete(data)</a> ⇒ <code>Promise.&lt;void&gt;</code></li>
<li><a href="#module_RTKStore+get">.get(key)</a> ⇒ <code>any</code></li>
<li><a href="#module_RTKStore+getAll">.getAll()</a> ⇒ <code>RTKStoreData</code></li>
<li><a href="#module_RTKStore+clear">.clear()</a></li>
<li><a href="#module_RTKStore+updateRateLimits">.updateRateLimits(num, period)</a></li>
<li><a href="#module_RTKStore+updateBulkRateLimits">.updateBulkRateLimits(num, period)</a></li>
<li><a href="#module_RTKStore+subscribe">.subscribe(key, cb)</a> ⇒ <code>void</code></li>
<li><a href="#module_RTKStore+unsubscribe">.unsubscribe(key, [cb])</a> ⇒ <code>void</code></li>
<li><a href="#module_RTKStore+populate">.populate(data)</a></li>
</ul>
</li>
</ul>
<p><a name="module_RTKStore+set"></a></p>
<h3 id="store-set-key-value-sync-emit-promise-void">store.set(key, value, [sync], [emit]) ⇒ <code>Promise.&lt;void&gt;</code></h3>
Sets a value in the store.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKStore"><code>RTKStore</code></a><br />
<strong>Returns</strong>: <code>Promise.&lt;void&gt;</code> - A promise.</p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>key</td>
<td><code>string</code></td>
<td></td>
<td>Unique identifier used to store value.</td>
</tr>
<tr>
<td>value</td>
<td><code>any</code></td>
<td></td>
<td>Data to be set.</td>
</tr>
<tr>
<td>[sync]</td>
<td><code>boolean</code></td>
<td><code>true</code></td>
<td>Whether to sync change to remote store.</td>
</tr>
<tr>
<td>[emit]</td>
<td><code>boolean</code></td>
<td><code>false</code></td>
<td>Whether to emit to local subscribers.</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKStore+bulkSet"></a></p>
<h3 id="store-bulkset-data-promise-void">store.bulkSet(data) ⇒ <code>Promise.&lt;void&gt;</code></h3>
Sets multiple values in the store.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKStore"><code>RTKStore</code></a><br />
<strong>Returns</strong>: <code>Promise.&lt;void&gt;</code> - A promise.</p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>data</td>
<td><code>Array.&lt;{key: string, payload: any}&gt;</code></td>
</tr>
</tbody>
</table>
<p><a name="module_RTKStore+update"></a></p>
<h3 id="store-update-key-value-sync-promise-void">store.update(key, value, [sync]) ⇒ <code>Promise.&lt;void&gt;</code></h3>
Updates an already existing value in the store.
If the value stored is `['a', 'b']`, the operation
`store.update(key, ['c'])` will modify
the value to `['a','b','c']`.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKStore"><code>RTKStore</code></a><br />
<strong>Returns</strong>: <code>Promise.&lt;void&gt;</code> - A promise.</p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>key</td>
<td><code>string</code></td>
<td></td>
<td>Unique identifier used to store value.</td>
</tr>
<tr>
<td>value</td>
<td><code>any</code></td>
<td></td>
<td>Data to be updated.</td>
</tr>
<tr>
<td>[sync]</td>
<td><code>boolean</code></td>
<td><code>true</code></td>
<td>Whether to sync change to remote store.</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKStore+delete"></a></p>
<h3 id="store-delete-key-sync-emit-promise-void">store.delete(key, [sync], [emit]) ⇒ <code>Promise.&lt;void&gt;</code></h3>
Deletes a key value pair form the store.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKStore"><code>RTKStore</code></a><br />
<strong>Returns</strong>: <code>Promise.&lt;void&gt;</code> - A promise.</p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>key</td>
<td><code>string</code></td>
<td></td>
<td>Unique identifier used to store value.</td>
</tr>
<tr>
<td>[sync]</td>
<td><code>boolean</code></td>
<td><code>true</code></td>
<td>Whether to sync change to remote store.</td>
</tr>
<tr>
<td>[emit]</td>
<td><code>boolean</code></td>
<td><code>false</code></td>
<td>Whether to emit to local subscribers.</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKStore+bulkDelete"></a></p>
<h3 id="store-bulkdelete-data-promise-void">store.bulkDelete(data) ⇒ <code>Promise.&lt;void&gt;</code></h3>
Deletes multiple values from the store.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKStore"><code>RTKStore</code></a><br />
<strong>Returns</strong>: <code>Promise.&lt;void&gt;</code> - A promise.</p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>data</td>
<td><code>Array.&lt;{key: string}&gt;</code></td>
</tr>
</tbody>
</table>
<p><a name="module_RTKStore+get"></a></p>
<h3 id="store-get-key-any">store.get(key) ⇒ <code>any</code></h3>
Returns value for the given key.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKStore"><code>RTKStore</code></a><br />
<strong>Returns</strong>: <code>any</code> - Value for the given key.</p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>key</td>
<td><code>string</code></td>
<td>Unique identifier used to store value.</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKStore+getAll"></a></p>
<h3 id="store-getall-rtkstoredata">store.getAll() ⇒ <code>RTKStoreData</code></h3>
Returns the entire store.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKStore"><code>RTKStore</code></a><br />
<strong>Returns</strong>: <code>RTKStoreData</code> - An instance of RTKStoreData.<br />
<a name="module_RTKStore+clear"></a></p>
<h3 id="store-clear">store.clear()</h3>
Clears all data in the store.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKStore"><code>RTKStore</code></a><br />
<a name="module_RTKStore+updateRateLimits"></a></p>
<h3 id="store-updateratelimits-num-period">store.updateRateLimits(num, period)</h3>
**Kind**: instance method of [<code>RTKStore</code>](#module_RTKStore)  
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>num</td>
<td><code>number</code></td>
</tr>
<tr>
<td>period</td>
<td><code>number</code></td>
</tr>
</tbody>
</table>
<p><a name="module_RTKStore+updateBulkRateLimits"></a></p>
<h3 id="store-updatebulkratelimits-num-period">store.updateBulkRateLimits(num, period)</h3>
**Kind**: instance method of [<code>RTKStore</code>](#module_RTKStore)  
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>num</td>
<td><code>number</code></td>
</tr>
<tr>
<td>period</td>
<td><code>number</code></td>
</tr>
</tbody>
</table>
<p><a name="module_RTKStore+subscribe"></a></p>
<h3 id="store-subscribe-key-cb-void">store.subscribe(key, cb) ⇒ <code>void</code></h3>
Listens for data change on a store key.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKStore"><code>RTKStore</code></a><br />
<strong>Returns</strong>: <code>void</code> - void</p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>key</td>
<td><code>string</code></td>
<td>Unique identifier used to store value.</td>
</tr>
<tr>
<td>cb</td>
<td><code>function</code></td>
<td>The callback function that gets executed when data is modified.</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKStore+unsubscribe"></a></p>
<h3 id="store-unsubscribe-key-cb-void">store.unsubscribe(key, [cb]) ⇒ <code>void</code></h3>
Removes all listeners for a key on the store.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKStore"><code>RTKStore</code></a><br />
<strong>Returns</strong>: <code>void</code> - void</p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>key</td>
<td><code>string</code></td>
<td>Unique identifier used to store value.</td>
</tr>
<tr>
<td>[cb]</td>
<td><code>function</code></td>
<td>Callback to be removed.</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKStore+populate"></a></p>
<h3 id="store-populate-data">store.populate(data)</h3>
**Kind**: instance method of [<code>RTKStore</code>](#module_RTKStore)  
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>data</td>
<td><code>RTKStoreData</code></td>
</tr>
</tbody>
</table>

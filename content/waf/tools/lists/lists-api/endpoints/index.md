<p>To invoke a <a href="/api/resources/rules/subresources/lists/">Lists API</a> operation, append the endpoint to the Cloudflare API base URL:</p>
<p><code>https://api.cloudflare.com/client/v4/</code></p>
<p>For authentication instructions, refer to the Cloudflare API's <a href="/fundamentals/api/get-started/">Get started</a> page.</p>
<p>For help with making API calls and paginating results, refer to <a href="/fundamentals/api/how-to/make-api-calls/">Make API calls</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15736.md")
</aside>
<p>The Lists API supports the operations outlined below. Visit the associated links for examples.</p>
<h2 id="manage-lists">Manage lists</h2>
<h3 id="create-a-list">Create a list</h3>
<ul>
<li><strong>Operation</strong>: <a href="/api/resources/rules/subresources/lists/methods/create/">Create a list</a></li>
<li><strong>Method and endpoint</strong>: <code>POST accounts/{account_id}/rules/lists</code></li>
<li><strong>Notes</strong>: Creates an empty list.</li>
</ul>
<h3 id="get-lists">Get lists</h3>
<ul>
<li><strong>Operation</strong>: <a href="/api/resources/rules/subresources/lists/methods/list/">Get lists</a></li>
<li><strong>Method and endpoint</strong>: <code>GET accounts/{account_id}/rules/lists</code></li>
<li><strong>Notes</strong>:
<ul>
<li>Fetches all lists for the account.</li>
<li>This request does not fetch the items in the lists.</li>
</ul>
</li>
</ul>
<h3 id="get-a-list">Get a list</h3>
<ul>
<li><strong>Operation</strong>: <a href="/api/resources/rules/subresources/lists/methods/get/">Get a list</a></li>
<li><strong>Method and endpoint</strong>: <code>GET accounts/{account_id}/rules/lists/{list_id}</code></li>
<li><strong>Notes</strong>:
<ul>
<li>Fetches a list by its ID.</li>
<li>This request does not display the items in the list.</li>
</ul>
</li>
</ul>
<h3 id="update-a-list">Update a list</h3>
<ul>
<li><strong>Operation</strong>: <a href="/api/resources/rules/subresources/lists/methods/update/">Update a list</a></li>
<li><strong>Method and endpoint</strong>: <code>PUT accounts/{account_id}/rules/lists/{list_id}</code></li>
<li><strong>Notes</strong>:
<ul>
<li>Updates the <code>description</code> of a list.</li>
<li>You cannot edit the <code>name</code> or <code>kind</code>, and you cannot update items in a list. To update an item in a list, use the <a href="#update-all-list-items">Update all list items</a> operation.</li>
</ul>
</li>
</ul>
<h3 id="delete-a-list">Delete a list</h3>
<ul>
<li><strong>Operation</strong>: <a href="/api/resources/rules/subresources/lists/methods/delete/">Delete a list</a></li>
<li><strong>Method and endpoint</strong>: <code>DELETE accounts/{account_id}/rules/lists/{list_id}</code></li>
<li><strong>Notes</strong>: Deletes the list, but only when no <a href="/firewall/api/cf-filters/">filters</a> reference it.</li>
</ul>
<h2 id="manage-items-in-a-list">Manage items in a list</h2>
<p>Nearly all the operations for managing items in a list are asynchronous. When you add or delete a large amount of items to or from a list, there may be a delay before the bulk operation is complete.</p>
<p>Asynchronous list operations return an <code>operation_id</code>, which you can use to monitor the status of an API operation. To monitor the status of an asynchronous operation, use the <a href="/api/resources/rules/subresources/lists/subresources/bulk_operations/methods/get/">Get bulk operation status</a> endpoint and specify the ID of the operation you want to monitor.</p>
<p>When you make requests to a list while a bulk operation on that list is in progress, the requests are queued and processed in sequence (first in, first out). Requests for successful asynchronous operations return an <code>HTTP 201</code> status code.</p>
<h3 id="get-list-items">Get list items</h3>
<ul>
<li><strong>Operation</strong>: <a href="/api/resources/rules/subresources/lists/subresources/items/methods/list/">Get list items</a></li>
<li><strong>Method and endpoint</strong>: <code>GET accounts/{account_id}/rules/lists/{list_id}/items[?search={query}]</code></li>
<li><strong>Notes</strong>:
<ul>
<li>Fetches items in a list (all items, by default).</li>
<li>Items are sorted in ascending order.</li>
<li>In the case of IP lists, CIDRs are sorted by IP address, then by the subnet mask.</li>
<li>To filter returned items, use the optional <code>search</code> query string parameter. For more information, refer to the <a href="/api/resources/rules/subresources/lists/subresources/items/methods/list/">Get list items</a> API operation.</li>
</ul>
</li>
</ul>
<h3 id="get-a-list-item">Get a list item</h3>
<ul>
<li><strong>Operation</strong>: <a href="/api/resources/rules/subresources/lists/subresources/items/methods/get/">Get a list item</a></li>
<li><strong>Method and endpoint</strong>: <code>GET accounts/{account_id}/rules/lists/{list_id}/items/{item_id}</code></li>
<li><strong>Notes</strong>: Fetches an item from a list by ID</li>
</ul>
<h3 id="create-list-items">Create list items</h3>
<ul>
<li><strong>Operation</strong>: <a href="/api/resources/rules/subresources/lists/subresources/items/methods/create/">Create list items</a></li>
<li><strong>Method and endpoint</strong>: <code>POST accounts/{account_id}/rules/lists/{list_id}/items</code></li>
<li><strong>Notes</strong>:
<ul>
<li>Appends a new item or items to a list.</li>
<li>Replaces entries that already exist in the list, does not delete any items.</li>
<li>Overwrites the <code>comment</code> of the original item.</li>
<li>The response includes an <code>operation_id</code>.</li>
</ul>
</li>
</ul>
<h3 id="update-all-list-items">Update all list items</h3>
<ul>
<li><strong>Operation</strong>: <a href="/api/resources/rules/subresources/lists/subresources/items/methods/update/">Update all list items</a></li>
<li><strong>Method and endpoint</strong>: <code>PUT accounts/{account_id}/rules/lists/{list_id}/items</code></li>
<li><strong>Notes</strong>:
<ul>
<li>Deletes all current items in the list and replaces them with <code>items</code>.</li>
<li>When <code>items</code> is empty, deletes <strong>all</strong> items in the list.</li>
<li>The response includes an <code>operation_id</code>.</li>
</ul>
</li>
</ul>
<h3 id="delete-list-items">Delete list items</h3>
<ul>
<li><strong>Operation</strong>: <a href="/api/resources/rules/subresources/lists/subresources/items/methods/delete/">Delete list items</a></li>
<li><strong>Method and endpoint</strong>: <code>DELETE accounts/{account_id}/rules/lists/{list_id}/items</code></li>
<li><strong>Notes</strong>:
<ul>
<li>Deletes specified list items.</li>
<li>The response includes an <code>operation_id</code>.</li>
</ul>
</li>
</ul>

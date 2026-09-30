<h2 id="error-10028-the-add-list-items-operation-contains-duplicate-items">Error 10028: The add list items operation contains duplicate items</h2>
<p>This error indicates that the operation to add items to a list contains duplicate entries within the same request.</p>
<h3 id="common-causes">Common causes</h3>
<p>This error occurs when there are duplicate list items in a single operation to add items to a List (either an IP list or a Bulk Redirect List). This error can happen when you:</p>
<ul>
<li>Add a repeated IP address to an IP list</li>
<li>Add a repeated source URL to a Bulk Redirect List</li>
</ul>
<h3 id="resolution">Resolution</h3>
<p>You need to remove the duplicate item and try again.</p>

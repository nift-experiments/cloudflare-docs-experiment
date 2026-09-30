<h2 id="error-10056-the-add-list-items-operation-contains-different-types-of-list-items">Error 10056: The add list items operation contains different types of list items</h2>
<p>This error indicates that different types of list items were combined in a single add operation.</p>
<h3 id="common-causes">Common causes</h3>
<p>This error occurs when different types of list items (such as IP addresses, hostnames, and URL redirects) are included in a single operation to add items to a list. It can occur with an IP list, a hostname list, or a Bulk Redirect List.</p>
<h3 id="resolution">Resolution</h3>
<p>Remove the list items that do not apply to the list type. This means:</p>
<ul>
<li>Removing IP addresses from a request to add items to a Bulk Redirect List.</li>
<li>Removing URL redirects from a request to add items to an IP list.</li>
</ul>

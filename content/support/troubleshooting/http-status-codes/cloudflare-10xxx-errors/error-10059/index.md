<h2 id="error-10059-maximum-number-of-repeated-url-source-paths-exceeded">Error 10059: Maximum number of repeated URL source paths exceeded</h2>
<p>This error indicates that the same URL path is repeated too many times across your Bulk Redirect Lists.</p>
<h3 id="common-causes">Common causes</h3>
<p>This error occurs when you have more than the maximum number of URL redirects with the same source URL path across all Bulk Redirect Lists in your account, regardless of the URL redirect domain. Possible causes include multiple lists containing the same redirects, overlapping configurations, or mismanagement resulting in duplicated source URL paths.</p>
<h3 id="resolution">Resolution</h3>
<p>Review the path of your source URLs so that you do not have more than the maximum number of URL redirects sharing the same URL path in your account, regardless of their domain or the list they belong to. Refer to <a href="/rules/url-forwarding/bulk-redirects/reference/parameters/">URL redirect parameters</a> for more information on the current limits.</p>

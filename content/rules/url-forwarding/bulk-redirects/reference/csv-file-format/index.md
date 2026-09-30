<p>You can use a CSV file to import URL redirects into a Bulk Redirect List <a href="/rules/url-forwarding/bulk-redirects/create-dashboard/#1-create-a-bulk-redirect-list">using the Cloudflare dashboard</a>. Each line in the CSV file must follow this format:</p>
<pre><code class="language-txt">&lt;SOURCE_URL&gt;,&lt;TARGET_URL&gt;[,&lt;STATUS_CODE&gt;,&lt;PRESERVE_QUERY_STRING&gt;,&lt;INCLUDE_SUBDOMAINS&gt;,&lt;SUBPATH_MATCHING&gt;,&lt;PRESERVE_PATH_SUFFIX&gt;]&#10;</code></pre>
<p>Only the <code>&lt;SOURCE_URL&gt;</code> and <code>&lt;TARGET_URL&gt;</code> values are mandatory. The default value of <code>&lt;STATUS_CODE&gt;</code> is <code>301</code> and the default value for all the boolean parameters is <code>FALSE</code>.</p>
<p>To enable one of the URL redirect parameters, use one of the following values: <code>TRUE</code> or <code>true</code>. To keep an option disabled, use one of <code>FALSE</code> or <code>false</code>, or enter a comma (delimiter) without entering any value.</p>
<h2 id="example-csv-file">Example CSV file</h2>
<p>All the lines in this example are valid lines that you can import in the dashboard:</p>
<pre><code class="language-txt">example.com/contacts,https://example.net/contact-us,301,,,,&#10;example.com/about,https://example.net/about-us,,FALSE,TRUE,,&#10;example.com/docs,https://example.com/draft-docs,302,,TRUE&#10;</code></pre>
<h2 id="important-remarks">Important remarks</h2>
<ul>
<li>The source URL cannot include a query string. For details on which URL components are supported in source URLs, refer to <a href="/rules/url-forwarding/bulk-redirects/reference/url-components/">Supported URL components in Bulk Redirects</a>.</li>
<li>The CSV file must not include a header row with column names.</li>
<li>A source/target URL must be enclosed in quotes (<code>&quot;</code>) when it includes a comma (<code>,</code>). You can always enclose URL values in quotes, but it is not required.</li>
<li>You can skip an optional value by immediately entering a comma (the delimiter) without entering any value.</li>
<li>You do not need to include trailing commas.</li>
</ul>

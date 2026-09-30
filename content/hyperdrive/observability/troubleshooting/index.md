---
cp9:
  canonical: https://developers.cloudflare.com/hyperdrive/observability/troubleshooting/
  description: Resolve common Hyperdrive connection errors and database connectivity issues.
  full_title: Troubleshoot and debug · Cloudflare Hyperdrive docs
  head_html: <title>Troubleshoot and debug · Cloudflare Hyperdrive docs</title><meta name="generator" content="Nift"><meta name="description" content="Resolve common Hyperdrive connection errors and database connectivity issues."><link rel="canonical" href="https://developers.cloudflare.com/hyperdrive/observability/troubleshooting/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/hyperdrive/observability/troubleshooting/index.md"><meta property="og:title" content="Troubleshoot and debug · Cloudflare Hyperdrive docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Resolve common Hyperdrive connection errors and database connectivity issues."><meta property="og:url" content="https://developers.cloudflare.com/hyperdrive/observability/troubleshooting/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Hyperdrive"><meta name="algolia_product_filter" content="Hyperdrive"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Hyperdrive"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/hyperdrive/observability/troubleshooting/#page","headline":"Troubleshoot and debug \u00b7 Cloudflare Hyperdrive docs","description":"Resolve common Hyperdrive connection errors and database connectivity issues.","url":"https://developers.cloudflare.com/hyperdrive/observability/troubleshooting/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /hyperdrive/observability/troubleshooting/
  schema: 1
---
<p>Troubleshoot and debug errors commonly associated with connecting to a database with Hyperdrive.</p>
<h2 id="configuration-errors">Configuration errors</h2>
<p>When creating a new Hyperdrive configuration, or updating the connection parameters associated with an existing configuration, Hyperdrive performs a test connection to your database in the background before creating or updating the configuration.</p>
<p>Hyperdrive will also issue an empty test query, a <code>;</code> in PostgreSQL, to validate that it can pass queries to your database.</p>
<table>
<thead>
<tr>
<th>Error Code</th>
<th>Details</th>
<th>Recommended fixes</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2008</code></td>
<td>Bad hostname.</td>
<td>Hyperdrive could not resolve the database hostname. Confirm it exists in public DNS.</td>
</tr>
<tr>
<td><code>2009</code></td>
<td>The hostname does not resolve to a public IP address, or the IP address is not a public address.</td>
<td>Hyperdrive can only connect to public IP addresses. Private IP addresses, like <code>10.1.5.0</code> or <code>192.168.2.1</code>, are not currently supported.</td>
</tr>
<tr>
<td><code>2010</code></td>
<td>Cannot connect to the host:port.</td>
<td>Hyperdrive could not route to the hostname: ensure it has a public DNS record that resolves to a public IP address. Check that the hostname is not misspelled.</td>
</tr>
<tr>
<td><code>2011</code></td>
<td>Connection refused.</td>
<td>A network firewall or access control list (ACL) is likely rejecting requests from Hyperdrive. Ensure you have allowed connections from the public Internet.</td>
</tr>
<tr>
<td><code>2012</code></td>
<td>TLS (SSL) not supported by the database.</td>
<td>Hyperdrive requires TLS (SSL) to connect. Configure TLS on your database.</td>
</tr>
<tr>
<td><code>2013</code></td>
<td>Invalid database credentials.</td>
<td>Ensure your username is correct (and exists), and the password is correct (case-sensitive).</td>
</tr>
<tr>
<td><code>2014</code></td>
<td>The specified database name does not exist.</td>
<td>Check that the database (not table) name you provided exists on the database you are asking Hyperdrive to connect to.</td>
</tr>
<tr>
<td><code>2015</code></td>
<td>Generic error.</td>
<td>Hyperdrive failed to connect and could not determine a reason. Open a support ticket so Cloudflare can investigate.</td>
</tr>
<tr>
<td><code>2016</code></td>
<td>Test query failed.</td>
<td>Confirm that the user Hyperdrive is connecting as has permissions to issue read and write queries to the given database.</td>
</tr>
</tbody>
</table>
<h3 id="failure-to-connect">Failure to connect</h3>
<p>Hyperdrive may also emit <code>Failed to connect to the provided database</code> when it fails to connect to the database when attempting to create a Hyperdrive configuration. This is possible when the TLS (SSL) certificates are misconfigured. Here is a non-exhaustive table of potential failure to connect errors:</p>
<table>
<thead>
<tr>
<th>Error message</th>
<th>Details</th>
<th>Recommended fixes</th>
</tr>
</thead>
<tbody>
<tr>
<td>Server return error and closed connection.</td>
<td>This message occurs when you attempt to connect to a database that has client certificate verification enabled.</td>
<td>Ensure you are configuring your Hyperdrive with <a href="/hyperdrive/configuration/tls-ssl-certificates-for-hyperdrive/">client certificates</a> if your database requires them.</td>
</tr>
<tr>
<td>TLS handshake failed: cert validation failed.</td>
<td>This message occurs when Hyperdrive has been configured with server CA certificates and is indicating that the certificate provided by the server has not been signed by the expected CA certificate.</td>
<td>Ensure you are using the correct CA certificate for Hyperdrive, or ensure you are connecting to the right database.</td>
</tr>
</tbody>
</table>
<h2 id="connection-errors">Connection errors</h2>
<p>Hyperdrive may also return errors at runtime. This can happen during initial connection setup, or in response to a query or other wire-protocol command sent by your driver.</p>
<p>These errors are returned as <code>ErrorResponse</code> wire protocol messages, which are handled by most drivers by throwing from the responsible query or by triggering an error event.
Hyperdrive errors that do not map 1:1 with an error message code <a href="https://www.postgresql.org/docs/current/errcodes-appendix.html">documented by PostgreSQL</a> use the <code>58000</code> error code.</p>
<p>Hyperdrive may also encounter <code>ErrorResponse</code> wire protocol messages sent by your database. Hyperdrive will pass these errors through unchanged when possible.</p>
<h3 id="hyperdrive-specific-errors">Hyperdrive specific errors</h3>
<table>
<thead>
<tr>
<th>Error Message</th>
<th>Details</th>
<th>Recommended fixes</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Internal error.</code></td>
<td>Something is broken on our side.</td>
<td>Check for an ongoing incident affecting Hyperdrive, and <a href="/support/contacting-cloudflare-support/">contact Cloudflare Support</a>. Retrying the query is appropriate, if it makes sense for your usage pattern.</td>
</tr>
<tr>
<td><code>Failed to acquire a connection from the pool.</code></td>
<td>Hyperdrive timed out while waiting for a connection to your database, or cannot connect at all.</td>
<td>If you are seeing this error intermittently, your Hyperdrive pool is being exhausted because too many connections are being held open for too long by your worker. This can be caused by a myriad of different issues, but long-running queries/transactions are a common offender.</td>
</tr>
<tr>
<td><code>Server connection attempt failed: connection_refused</code></td>
<td>Hyperdrive is unable to create new connections to your origin database.</td>
<td>A network firewall or access control list (ACL) is likely rejecting requests from Hyperdrive. Ensure you have allowed connections from the public Internet. Sometimes, this can be caused by your database host provider refusing incoming connections when you go over your connection limit.</td>
</tr>
<tr>
<td><code>Hyperdrive does not currently support MySQL COM_STMT_PREPARE messages</code></td>
<td>Hyperdrive does not support prepared statements for MySQL databases.</td>
<td>Remove prepared statements from your MySQL queries.</td>
</tr>
</tbody>
</table>
<h3 id="node-errors">Node errors</h3>
<table>
<thead>
<tr>
<th>Error Message</th>
<th>Details</th>
<th>Recommended fixes</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Uncaught Error: No such module &quot;node:&lt;module&gt;&quot;</code></td>
<td>Your Cloudflare Workers project or a library that it imports is trying to access a Node module that is not available.</td>
<td>Enable <a href="/workers/runtime-apis/nodejs/">Node.js compatibility</a> for your Cloudflare Workers project to maximize compatibility.</td>
</tr>
</tbody>
</table>
<h3 id="stale-reads-after-writes">Stale reads after writes</h3>
<p>If your application writes data and then a later read returns older data, Hyperdrive query caching may be serving a cached read query result. Check Hyperdrive metrics by <code>cacheStatus</code> to confirm whether reads return <code>hit</code>, <code>miss</code>, <code>disabled</code>, or <code>uncacheable</code>. Refer to <a href="/hyperdrive/observability/metrics/">Metrics and analytics</a>.</p>
<p>To resolve stale reads after writes, refer to <a href="/hyperdrive/concepts/query-caching/#read-after-write-behavior">Query caching</a> for guidance on splitting fresh reads from cacheable reads, including using a cache-disabled Hyperdrive configuration for reads that must return fresh data.</p>
<h3 id="uncached-queries">Uncached queries</h3>
<p>If your queries are not being cached despite Hyperdrive having caching enabled, check the following:</p>
<ul>
<li>
<p><strong>Stable or volatile PostgreSQL functions in your query</strong>: Queries that contain PostgreSQL functions categorized as <code>STABLE</code> or <code>VOLATILE</code> are not cacheable. Common examples include <code>NOW()</code>, <code>CURRENT_TIMESTAMP</code>, <code>CURRENT_DATE</code>, <code>RANDOM()</code>, and <code>LASTVAL()</code>. To resolve this, move the function call to your application code and pass the result as a query parameter. For example, instead of <code>WHERE created_at &gt; NOW()</code>, compute the timestamp in your Worker and pass it as a parameter: <code>WHERE created_at &gt; $1</code>. Refer to <a href="/hyperdrive/concepts/query-caching/">Query caching</a> for a full list of uncacheable functions.</p>
</li>
<li>
<p><strong>Function names in SQL comments</strong>: Hyperdrive uses text-based pattern matching to detect some uncacheable functions. References to function names like <code>NOW()</code> in SQL comments can cause the query to be treated as uncacheable, even if the function is not actually called. Remove references to uncacheable function names from query text, including comments.</p>
</li>
<li>
<p><strong>Driver configuration</strong>: Your driver may be configured such that your queries are not cacheable by Hyperdrive. This may happen if you are using the <a href="https://github.com/porsager/postgres">Postgres.js</a> driver with <a href="https://github.com/porsager/postgres?tab=readme-ov-file#prepared-statements"><code>prepare: false</code></a>. To resolve this, enable prepared statements with <code>prepare: true</code>.</p>
</li>
</ul>
<h3 id="driver-errors">Driver errors</h3>
<table>
<thead>
<tr>
<th>Error Message</th>
<th>Details</th>
<th>Recommended fixes</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Code generation from strings disallowed for this context</code></td>
<td>The database driver you are using is attempting to use the <code>eval()</code> command, which is unsupported on Cloudflare Workers (common in <code>mysql2</code> driver).</td>
<td>Configure the database driver to not use <code>eval()</code>. See how to <a href="/hyperdrive/examples/connect-to-mysql/mysql-drivers-and-libraries/mysql2/">configure <code>mysql2</code> to disable the usage of <code>eval()</code></a>.</td>
</tr>
</tbody>
</table>
<h3 id="stale-connection-and-i-o-context-errors">Stale connection and I/O context errors</h3>
<p>These errors occur when a database client or connection is created in the global scope (outside of a request handler) or is reused across requests. Workers do not allow <a href="/workers/runtime-apis/bindings/#making-changes-to-bindings">I/O across requests</a>, and database connections from a previous request context become unusable. Always <a href="/hyperdrive/concepts/connection-lifecycle/#cleaning-up-client-connections">create database clients inside your handlers</a>.</p>
<h4 id="workers-runtime-errors">Workers runtime errors</h4>
<table>
<thead>
<tr>
<th>Error Message</th>
<th>Details</th>
<th>Recommended fixes</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Disallowed operation called within global scope. Asynchronous I/O (ex: fetch() or connect()), setting a timeout, and generating random values are not allowed within global scope.</code></td>
<td>Your Worker is attempting to open a database connection or perform I/O during script startup, outside of a request handler.</td>
<td>Move the database client creation into your <code>fetch</code>, <code>queue</code>, or other handler function.</td>
</tr>
<tr>
<td><code>Cannot perform I/O on behalf of a different request. I/O objects (such as streams, request/response bodies, and others) created in the context of one request handler cannot be accessed from a different request's handler.</code></td>
<td>A database connection or client created during one request is being reused in a subsequent request.</td>
<td>Create a new database client on every request instead of caching it in a global variable. Hyperdrive's connection pooling already eliminates the connection startup overhead.</td>
</tr>
</tbody>
</table>
<h4 id="node-postgres-pg-errors">node-postgres (<code>pg</code>) errors</h4>
<table>
<thead>
<tr>
<th>Error Message</th>
<th>Details</th>
<th>Recommended fixes</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Connection terminated</code></td>
<td>The client's <code>.end()</code> method was called, or the connection was cleaned up at the end of a previous request.</td>
<td>Create a new <code>Client</code> inside your handler instead of reusing one from a prior request.</td>
</tr>
<tr>
<td><code>Connection terminated unexpectedly</code></td>
<td>The underlying connection was dropped without an explicit <code>.end()</code> call — for example, when a previous request's context was garbage collected.</td>
<td>Create a new <code>Client</code> inside your handler for every request.</td>
</tr>
<tr>
<td><code>Client has encountered a connection error and is not queryable</code></td>
<td>A socket-level error occurred on the connection (common when reusing a client across requests).</td>
<td>Create a new <code>Client</code> inside your handler. Do not store clients in global variables.</td>
</tr>
<tr>
<td><code>Client was closed and is not queryable</code></td>
<td>A query was attempted on a client whose <code>.end()</code> method was already called.</td>
<td>Create a new <code>Client</code> inside your handler instead of reusing one.</td>
</tr>
<tr>
<td><code>Cannot use a pool after calling end on the pool</code></td>
<td><code>pool.connect()</code> was called on a <code>Pool</code> instance that has already been ended.</td>
<td>Do not use <code>new Pool()</code> in the global scope. Create a <code>new Client()</code> inside your handler — Hyperdrive handles connection pooling for you.</td>
</tr>
<tr>
<td><code>Client has already been connected. You cannot reuse a client.</code></td>
<td><code>client.connect()</code> was called on a client that was already connected in a previous invocation.</td>
<td>Create a new <code>Client</code> per request. node-postgres clients cannot be reconnected once connected.</td>
</tr>
</tbody>
</table>
<h4 id="postgres-js-postgres-errors">Postgres.js (<code>postgres</code>) errors</h4>
<p>Postgres.js error messages include the error code and the target host. The <code>code</code> property on the error object contains the error code.</p>
<table>
<thead>
<tr>
<th>Error Message</th>
<th>Details</th>
<th>Recommended fixes</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>write CONNECTION_ENDED &lt;host&gt;:&lt;port&gt;</code></td>
<td>A query was attempted after <code>sql.end()</code> was called, or the connection was cleaned up from a prior request. Error code: <code>CONNECTION_ENDED</code>.</td>
<td>Create a new <code>postgres()</code> instance inside your handler.</td>
</tr>
<tr>
<td><code>write CONNECTION_DESTROYED &lt;host&gt;:&lt;port&gt;</code></td>
<td>The connection was forcefully terminated — for example, during <code>sql.end({ timeout })</code> expiration, or because the connection was already terminated. Error code: <code>CONNECTION_DESTROYED</code>.</td>
<td>Create a new <code>postgres()</code> instance inside your handler for every request.</td>
</tr>
<tr>
<td><code>write CONNECTION_CLOSED &lt;host&gt;:&lt;port&gt;</code></td>
<td>The underlying socket was closed unexpectedly while queries were still pending. Error code: <code>CONNECTION_CLOSED</code>.</td>
<td>Create a new <code>postgres()</code> instance inside your handler. If this occurs within a single request, check for network issues or query timeouts.</td>
</tr>
</tbody>
</table>
<h4 id="mysql2-errors">mysql2 errors</h4>
<table>
<thead>
<tr>
<th>Error Message</th>
<th>Details</th>
<th>Recommended fixes</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Can't add new command when connection is in closed state</code></td>
<td>A query was attempted on a connection that has already been closed or encountered a fatal error.</td>
<td>Create a new connection inside your handler instead of reusing one from global scope.</td>
</tr>
<tr>
<td><code>Connection lost: The server closed the connection.</code></td>
<td>The underlying socket was closed by the server or was garbage collected between requests. Error code: <code>PROTOCOL_CONNECTION_LOST</code>.</td>
<td>Create a new connection inside your handler for every request.</td>
</tr>
<tr>
<td><code>Pool is closed.</code></td>
<td><code>pool.getConnection()</code> was called on a pool that has already been closed.</td>
<td>Do not use <code>createPool()</code> in the global scope. Create a new <code>createConnection()</code> inside your handler — Hyperdrive handles pooling for you.</td>
</tr>
</tbody>
</table>
<h4 id="mysql-errors">mysql errors</h4>
<table>
<thead>
<tr>
<th>Error Message</th>
<th>Details</th>
<th>Recommended fixes</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Cannot enqueue Query after fatal error.</code></td>
<td>A query was attempted on a connection that previously encountered a fatal error. Error code: <code>PROTOCOL_ENQUEUE_AFTER_FATAL_ERROR</code>.</td>
<td>Create a new connection inside your handler instead of reusing one from global scope.</td>
</tr>
<tr>
<td><code>Cannot enqueue Query after invoking quit.</code></td>
<td>A query was attempted on a connection after <code>.end()</code> was called. Error code: <code>PROTOCOL_ENQUEUE_AFTER_QUIT</code>.</td>
<td>Create a new connection inside your handler for every request.</td>
</tr>
<tr>
<td><code>Cannot enqueue Handshake after already enqueuing a Handshake.</code></td>
<td><code>.connect()</code> was called on a connection that was already connected in a previous request. Error code: <code>PROTOCOL_ENQUEUE_HANDSHAKE_TWICE</code>.</td>
<td>Create a new connection per request. mysql connections cannot be reconnected once connected.</td>
</tr>
</tbody>
</table>
<h3 id="improve-performance">Improve performance</h3>
<p>Having query traffic written as transactions can limit performance. This is because in the case of a transaction, the connection must be held for the duration of the transaction, which limits connection multiplexing. If there are multiple queries per transaction, this can be particularly impactful on connection multiplexing. Where possible, we recommend not wrapping queries in transactions to allow the connections to be shared more aggressively.</p>

<h2 id="database-support">Database support</h2>
<p>The following table shows which database engines and/or specific database providers are supported.</p>
<table>
<thead>
<tr>
<th>Database Engine</th>
<th>Supported</th>
<th>Known supported versions</th>
<th>Details</th>
</tr>
</thead>
<tbody>
<tr>
<td>PostgreSQL</td>
<td>✅</td>
<td><code>9.0</code> to <code>17.x</code></td>
<td>Both self-hosted and managed (AWS, Azure, Google Cloud, Oracle) instances are supported.</td>
</tr>
<tr>
<td>MySQL</td>
<td>✅</td>
<td><code>5.7</code> to <code>8.x</code></td>
<td>Both self-hosted and managed (AWS, Azure, Google Cloud, Oracle) instances are supported. MariaDB is also supported.</td>
</tr>
<tr>
<td>SQL Server</td>
<td>Not currently supported.</td>
<td></td>
<td></td>
</tr>
<tr>
<td>MongoDB</td>
<td>Not currently supported.</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<h2 id="supported-database-providers">Supported database providers</h2>
<p>Hyperdrive supports managed Postgres and MySQL databases provided by various providers, including AWS, Azure, and GCP. Refer to <a href="/hyperdrive/examples/connect-to-postgres/">Examples</a> to see how to connect to various database providers.</p>
<p>Hyperdrive also supports databases that are compatible with the Postgres or MySQL protocol. The following is a non-exhaustive list of Postgres or MySQL-compatible database providers:</p>
<table>
<thead>
<tr>
<th>Database Engine</th>
<th>Supported</th>
<th>Known supported versions</th>
<th>Details</th>
</tr>
</thead>
<tbody>
<tr>
<td>AWS Aurora</td>
<td>✅</td>
<td>All</td>
<td>Postgres-compatible and MySQL-compatible. Refer to AWS Aurora examples for <a href="/hyperdrive/examples/connect-to-mysql/mysql-database-providers/aws-rds-aurora/">MySQL</a> and <a href="/hyperdrive/examples/connect-to-postgres/postgres-database-providers/aws-rds-aurora/">Postgres</a>.</td>
</tr>
<tr>
<td>Neon</td>
<td>✅</td>
<td>All</td>
<td>Neon currently runs Postgres 15.x</td>
</tr>
<tr>
<td>Supabase</td>
<td>✅</td>
<td>All</td>
<td>Supabase currently runs Postgres 15.x</td>
</tr>
<tr>
<td>Timescale</td>
<td>✅</td>
<td>All</td>
<td>See the <a href="/hyperdrive/examples/connect-to-postgres/postgres-database-providers/timescale/">Timescale guide</a> to connect.</td>
</tr>
<tr>
<td>Materialize</td>
<td>✅</td>
<td>All</td>
<td>Postgres-compatible. Refer to the <a href="/hyperdrive/examples/connect-to-postgres/postgres-database-providers/materialize/">Materialize guide</a> to connect.</td>
</tr>
<tr>
<td>CockroachDB</td>
<td>✅</td>
<td>All</td>
<td>Postgres-compatible. Refer to the <a href="/hyperdrive/examples/connect-to-postgres/postgres-database-providers/cockroachdb/">CockroachDB</a> guide to connect.</td>
</tr>
<tr>
<td>PlanetScale</td>
<td>✅</td>
<td>All</td>
<td>PlanetScale provides MySQL-compatible and PostgreSQL databases</td>
</tr>
<tr>
<td>MariaDB</td>
<td>✅</td>
<td>All</td>
<td>MySQL-compatible.</td>
</tr>
</tbody>
</table>
<h2 id="supported-tls-ssl-modes">Supported TLS (SSL) modes</h2>
<h3 id="postgresql">PostgreSQL</h3>
<p>Hyperdrive supports the following <a href="https://www.postgresql.org/docs/current/libpq-ssl.html">PostgreSQL TLS (SSL)</a> connection modes when connecting to your origin database:</p>
<table>
<thead>
<tr>
<th>Mode</th>
<th>Supported</th>
<th>Details</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>none</code></td>
<td>No</td>
<td>Hyperdrive does not support insecure plain text connections.</td>
</tr>
<tr>
<td><code>prefer</code></td>
<td>No (use <code>require</code>)</td>
<td>Hyperdrive will always use TLS.</td>
</tr>
<tr>
<td><code>require</code></td>
<td>Yes (default)</td>
<td>TLS is required, and server certificates are validated (based on WebPKI).</td>
</tr>
<tr>
<td><code>verify-ca</code></td>
<td>Yes</td>
<td>Verifies the server's TLS certificate is signed by a root CA on the client. This ensures the server has a certificate the client trusts.</td>
</tr>
<tr>
<td><code>verify-full</code></td>
<td>Yes</td>
<td>Identical to <code>verify-ca</code>, but also requires the database hostname must match a Subject Alternative Name (SAN) present on the certificate.</td>
</tr>
</tbody>
</table>
<h3 id="mysql">MySQL</h3>
<p>Hyperdrive supports the following <a href="https://dev.mysql.com/doc/refman/8.0/en/connection-options.html#option_general_ssl-mode">MySQL TLS (SSL)</a> connection modes when connecting to your origin database:</p>
<table>
<thead>
<tr>
<th>Mode</th>
<th>Supported</th>
<th>Details</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>DISABLED</code></td>
<td>No</td>
<td>Hyperdrive does not support insecure plain text connections.</td>
</tr>
<tr>
<td><code>PREFERRED</code></td>
<td>No (use <code>REQUIRED</code>)</td>
<td>Hyperdrive will always use TLS.</td>
</tr>
<tr>
<td><code>REQUIRED</code></td>
<td>Yes (default)</td>
<td>TLS is required, and server certificates are validated (based on WebPKI).</td>
</tr>
<tr>
<td><code>VERIFY_CA</code></td>
<td>Yes</td>
<td>Verifies the server's TLS certificate is signed by a root CA on the client. This ensures the server has a certificate the client trusts.</td>
</tr>
<tr>
<td><code>VERIFY_IDENTITY</code></td>
<td>Yes</td>
<td>In addition to <code>VERIFY_CA</code> checks, Hyperdrive requires the database hostname to match a Subject Alternative Name (SAN) or Common Name (CN) on the certificate.</td>
</tr>
</tbody>
</table>
<p>Refer to <a href="/hyperdrive/configuration/tls-ssl-certificates-for-hyperdrive/">SSL/TLS certificates</a> documentation for details on how to configure these TLS (SSL) modes for Hyperdrive.</p>
<h2 id="supported-postgresql-authentication-modes">Supported PostgreSQL authentication modes</h2>
<p>Hyperdrive supports the following <a href="https://www.postgresql.org/docs/current/auth-methods.html">authentication modes</a> for connecting to PostgreSQL databases:</p>
<ul>
<li>Password Authentication (<code>md5</code>)</li>
<li>Password Authentication (<code>password</code>) (clear-text password)</li>
<li>SASL Authentication (<code>SCRAM-SHA-256</code>)</li>
</ul>
<h2 id="unsupported-postgresql-features">Unsupported PostgreSQL features:</h2>
<p>Hyperdrive does not support the following PostgreSQL features:</p>
<ul>
<li>SQL-level management of prepared statements, such as using <code>PREPARE</code>, <code>DISCARD</code>, <code>DEALLOCATE</code>, or <code>EXECUTE</code>.</li>
<li>Advisory locks (<a href="https://www.postgresql.org/docs/current/explicit-locking.html#ADVISORY-LOCKS">PostgreSQL documentation</a>).</li>
<li><code>LISTEN</code> and <code>NOTIFY</code>.</li>
<li><code>PREPARE</code> and <code>DEALLOCATE</code>.</li>
<li>Any modification to per-session state not explicitly documented as supported elsewhere.</li>
</ul>
<h2 id="unsupported-mysql-features">Unsupported MySQL features:</h2>
<p>Hyperdrive does not support the following MySQL features:</p>
<ul>
<li>Non-UTF8 characters in queries</li>
<li><code>USE</code> statements</li>
<li>Multi-statement queries</li>
<li>Prepared statement queries via SQL (using <code>PREPARE</code> and <code>EXECUTE</code> statements) and <a href="https://sidorares.github.io/node-mysql2/docs/documentation/prepared-statements">protocol-level prepared statements</a>.</li>
<li><code>COM_INIT_DB</code> messages</li>
<li><a href="https://dev.mysql.com/doc/refman/8.4/en/authentication-plugins.html">Authentication plugins</a> other than <code>caching_sha2_password</code> or <code>mysql_native_password</code></li>
</ul>
<p>In cases where you need to issue these unsupported statements from your application, the Hyperdrive team recommends setting up a second, direct client without Hyperdrive.</p>

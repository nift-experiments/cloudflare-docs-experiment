<p>D1 is compatible with most SQLite's SQL convention since it leverages SQLite's query engine. You can use SQL commands to query D1.</p>
<p>There are a number of ways you can interact with a D1 database:</p>
<ol>
<li>Using <a href="/d1/worker-api/">D1 Workers Binding API</a> in your code.</li>
<li>Using <a href="/api/resources/d1/subresources/database/methods/create/">D1 REST API</a>.</li>
<li>Using <a href="/d1/wrangler-commands/">D1 Wrangler commands</a>.</li>
</ol>
<h2 id="use-sql-to-query-d1">Use SQL to query D1</h2>
<p>D1 understands SQLite semantics, which allows you to query a database using SQL statements via Workers BindingAPI or REST API (including Wrangler commands). Refer to <a href="/d1/sql-api/sql-statements/">D1 SQL API</a> to learn more about supported SQL statements.</p>
<h3 id="use-foreign-key-relationships">Use foreign key relationships</h3>
<p>When using SQL with D1, you may wish to define and enforce foreign key constraints across tables in a database. Foreign key constraints allow you to enforce relationships across tables, or prevent you from deleting rows that reference rows in other tables. An example of a foreign key relationship is shown below.</p>
<pre><code class="language-sql">CREATE TABLE users (&#10;    user_id INTEGER PRIMARY KEY,&#10;    email_address TEXT,&#10;    name TEXT,&#10;    metadata TEXT&#10;)&#10;&#10;CREATE TABLE orders (&#10;    order_id INTEGER PRIMARY KEY,&#10;    status INTEGER,&#10;    item_desc TEXT,&#10;    shipped_date INTEGER,&#10;    user_who_ordered INTEGER,&#10;    FOREIGN KEY(user_who_ordered) REFERENCES users(user_id)&#10;)&#10;</code></pre>
<p>Refer to <a href="/d1/sql-api/foreign-keys/">Define foreign keys</a> for more information.</p>
<h3 id="query-json">Query JSON</h3>
<p>D1 allows you to query and parse JSON data stored within a database. For example, you can extract a value inside a JSON object.</p>
<p>Given the following JSON object (<code>type:blob</code>) in a column named <code>sensor_reading</code>, you can extract values from it directly.</p>
<pre><code class="language-json">{&#10;    &quot;measurement&quot;: {&#10;        &quot;temp_f&quot;: &quot;77.4&quot;,&#10;        &quot;aqi&quot;: [21, 42, 58],&#10;        &quot;o3&quot;: [18, 500],&#10;        &quot;wind_mph&quot;: &quot;13&quot;,&#10;        &quot;location&quot;: &quot;US-NY&quot;&#10;    }&#10;}&#10;</code></pre>
<pre><code class="language-sql">&#45;- Extract the temperature value&#10;SELECT json_extract(sensor_reading, &#x27;$.measurement.temp_f&#x27;)-- returns &quot;77.4&quot; as TEXT&#10;</code></pre>
<p>Refer to <a href="/d1/sql-api/query-json/">Query JSON</a> to learn more about querying JSON objects.</p>
<h2 id="query-d1-with-workers-binding-api">Query D1 with Workers Binding API</h2>
<p>Workers Binding API primarily interacts with the data plane, and allows you to query your D1 database from your Worker.</p>
<p>This requires you to:</p>
<ol>
<li>Bind your D1 database to your Worker.</li>
<li>Prepare a statement.</li>
<li>Run the statement.</li>
</ol>
<pre><code class="language-js">export default {&#10;    async fetch(request, env) {&#10;        const {pathname} = new URL(request.url);&#10;        const companyName1 = `Bs Beverages`;&#10;        const companyName2 = `Around the Horn`;&#10;        const stmt = env.DB.prepare(`SELECT * FROM Customers WHERE CompanyName = ?`);&#10;&#10;        if (pathname === `/RUN`) {&#10;            const returnValue = await stmt.bind(companyName1).run();&#10;            return Response.json(returnValue);&#10;        }&#10;&#10;        return new Response(&#10;            `Welcome to the D1 API Playground!&#10;						\nChange the URL to test the various methods inside your index.js file.`,&#10;        );&#10;    },&#10;};&#10;</code></pre>
<p>Refer to <a href="/d1/worker-api/">Workers Binding API</a> for more information.</p>
<h2 id="query-d1-with-rest-api">Query D1 with REST API</h2>
<p>REST API primarily interacts with the control plane, and allows you to create/manage your D1 database.</p>
<p>Refer to <a href="/api/resources/d1/subresources/database/methods/create/">D1 REST API</a> for D1 REST API documentation.</p>
<h2 id="query-d1-with-wrangler-commands">Query D1 with Wrangler commands</h2>
<p>You can use Wrangler commands to query a D1 database. Note that Wrangler commands use REST APIs to perform its operations.</p>
<pre><code class="language-sh">npx wrangler d1 execute prod-d1-tutorial --command=&quot;SELECT * FROM Customers&quot;&#10;</code></pre>
<pre><code class="language-sh">🌀 Mapping SQL input into an array of statements&#10;🌀 Executing on local database production-db-backend (&lt;DATABASE_ID&gt;) from .wrangler/state/v3/d1:&#10;┌────────────┬─────────────────────┬───────────────────┐&#10;│ CustomerId │ CompanyName         │ ContactName       │&#10;├────────────┼─────────────────────┼───────────────────┤&#10;│ 1          │ Alfreds Futterkiste │ Maria Anders      │&#10;├────────────┼─────────────────────┼───────────────────┤&#10;│ 4          │ Around the Horn     │ Thomas Hardy      │&#10;├────────────┼─────────────────────┼───────────────────┤&#10;│ 11         │ Bs Beverages        │ Victoria Ashworth │&#10;├────────────┼─────────────────────┼───────────────────┤&#10;│ 13         │ Bs Beverages        │ Random Name       │&#10;└────────────┴─────────────────────┴───────────────────┘&#10;</code></pre>

<p>Many GraphQL clients support browsing the GraphQL schema by taking care of
<a href="/analytics/graphql-api/features/discovery/introspection/">introspection</a>. In this page, we will cover GraphiQL and Altair clients.</p>
<p><a href="https://github.com/graphql/graphiql/tree/main/packages/graphiql#readme">GraphiQL</a> and <a href="https://altairgraphql.dev/#download">Altair</a> are open-source GraphQL clients that provide a
tool to compose a query, execute it, and inspect the results. And as a
bonus, they also allow you to browse GraphQL schema.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you begin, do not forget to <a href="/analytics/graphql-api/getting-started/authentication/graphql-client-headers/">configure</a> the API endpoint and HTTP
headers.</p>
<p>The screenshots below are done from GraphiQL. However, Altair provides the same
functionality and you will not find any difficulties following the same
instructions to explore the schema.</p>
<h2 id="open-the-documentation-explorer">Open the Documentation Explorer</h2>
<p>To open the GraphiQL Documentation Explorer, select the <strong>Docs</strong> link in the
header of the response pane:</p>
<p><img src="/assets/upstream/images/analytics/graphiql-docs-link.png" alt="Clicking GraphiQL Docs link to open Documentation Explorer" /></p>
<p>The <strong>Documentation Explorer</strong> opens and displays a list of available objects:</p>
<p><img src="/assets/upstream/images/analytics/graphiql-doc-explorer.png" alt="GraphiQL Doc Explorer pane" /></p>
<p>Objects in the <strong>Documentation Explorer</strong> use this syntax:</p>
<pre><code class="language-txt">  object-name: object-type-definition&#10;</code></pre>
<h2 id="find-the-type-definition-of-an-object">Find the type definition of an object</h2>
<p>When you first open the <strong>Documentation Explorer</strong> pane, the <code>mutation</code> and
<code>query</code> root types display:</p>
<p><img src="/assets/upstream/images/analytics/graphiql-doc-explorer-query-mutations.png" alt="Documentation Explorer displaying mutation and query nodes" /></p>
<p>In this example, <code>query</code> is the name of a root, and <code>Query</code> is the type
definition.</p>
<h2 id="find-the-fields-available-for-a-type-definition">Find the fields available for a type definition</h2>
<p>Click on the <strong>type definition</strong> of a node to view the fields that it provides.
The <strong>Documentation Explorer</strong> also displays descriptions of the nodes.</p>
<p>For example, select the <strong>Query</strong> type definition. The <strong>Documentation Explorer</strong>
displays the fields that <code>Query</code> provides. In this example, the fields are
<code>cost</code> and <code>viewer</code>:</p>
<p><img src="/assets/upstream/images/analytics/graphiql-doc-explorer-view-cost.png" alt="Documentation Explorer displaying cost and viewer fields" /></p>
<p>To explore the schema, select the names of objects and definitions. You can also
use the search input (magnifying glass icon) and breadcrumb links in the header.</p>
<h2 id="find-the-arguments-associated-with-a-field">Find the arguments associated with a field</h2>
<p>Click the type definition of the <code>viewer</code> field (gold text) to list its
sub-fields. The <code>viewer</code> field provides sub-fields that allow you to query
<code>accounts</code> or <code>zones</code> data:</p>
<p><img src="/assets/upstream/images/analytics/graphiql-doc-explorer-viewer-fields.png" alt="Displaying viewer fields" /></p>
<p>The <code>accounts</code> and <code>zones</code> nodes take arguments to specify which dataset to
query.</p>
<p>For example, <code>zones</code> can take a filter of <code>ZoneFilter_InputObject</code> type as an
argument. To view the fields available to filter, select
<strong>ZoneFilter_InputObject</strong>.</p>
<h2 id="find-the-datasets-available-for-a-zone">Find the datasets available for a zone</h2>
<p>To view a list of the datasets available to query, select the <strong>zone</strong> type
definition (gold text):</p>
<p><img src="/assets/upstream/images/analytics/graphiql-doc-explorer-zones.png" alt="Clicking zone type definition" /></p>
<p>A list of datasets displays in the <strong>Fields</strong> section, each with list of valid
arguments and a brief description. Arguments that end with an exclamation mark
(<code>!</code>) are required.</p>
<p><img src="/assets/upstream/images/analytics/graphiql-doc-explorer-zone-fields.png" alt="Fields section displaying datasets available" /></p>
<p>Use the search input (magnifying glass icon) to find specific datasets:</p>
<p><img src="/assets/upstream/images/analytics/graphiql-doc-explorer-find-firewall.png" alt="Searching a dataset in the Documentation Explorer" /></p>
<p>To select a dataset, select its name.</p>
<p>The definition for the dataset displays. This example shows the
<code>firewallEventsAdaptive</code> dataset:</p>
<p><img src="/assets/upstream/images/analytics/graphiql-doc-explorer-firewallevents-definition.png" alt="Example of a dataset definition" /></p>
<h2 id="find-the-fields-available-for-a-dataset">Find the fields available for a dataset</h2>
<p>To view the fields available for a particular dataset, select on its type
definition (gold text).</p>
<p>For example, select the <strong>ZoneFirewallEventsAdaptive</strong> type definition to view
the fields available for the <code>firewallEventsAdaptive</code> dataset:</p>
<p><img src="/assets/upstream/images/analytics/graphiql-doc-explorer-firewall-type-definition.png" alt="Clicking type definition to visualize fields available for a dataset" /></p>
<p>The list of fields displays:</p>
<p><img src="/assets/upstream/images/analytics/graphiql-doc-explorer-firewall-fields.png" alt="Displaying available fields for a dataset" /></p>
<p>For more information on using GraphiQL, please visit this <a href="/analytics/graphql-api/getting-started/compose-graphql-query/">guide</a>.</p>

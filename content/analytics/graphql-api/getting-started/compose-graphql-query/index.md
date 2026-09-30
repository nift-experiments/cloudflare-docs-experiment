<p>Many clients might need help using <a href="/analytics/graphql-api/getting-started/querying-basics/">the semantics</a> of GraphQL and exploring
the possibilities of Cloudflare GraphQL API.</p>
<p>This page details how to use a <a href="https://github.com/graphql/graphiql/tree/main/packages/graphiql#readme">GraphiQL client</a> to compose and execute a
GraphQL query.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>You can find all details on how to <a href="/analytics/graphql-api/getting-started/authentication/graphql-client-headers/">configure</a> a client here.</p>
<h2 id="set-up-a-query-and-choose-a-dataset">Set up a query and choose a dataset</h2>
<p>Click on the editing pane of GraphiQL and add this base query, replacing
<code>zone-id</code> with your Cloudflare zone ID:</p>
<p><img src="/assets/upstream/images/analytics/graphiql-base-query.png" alt="Adding a base query in the GraphiQL pane" /></p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/3171.md")
</aside>
<p>To assist query building, the GraphiQL client has word completion. Insert your
cursor in the query, in this case on the line below <code>zones</code>, and start entering
a value to engage the feature. For example, when you type <code>firewall</code>, a popup
menu displays the datasets that return firewall information:</p>
<p><img src="/assets/upstream/images/analytics/graphiql-word-completion.png" alt="GraphiQL word completion assistant to query building" /></p>
<p>The text at the bottom of the list displays a short description of the data that
the node returns.</p>
<p>Select the dataset you want to query and insert it. Either select the item in the
list, or scroll using arrow keys and press the <code>Return</code> key.</p>
<h2 id="supply-required-parameters">Supply required parameters</h2>
<p>Hover your mouse over a field to display a tooltip that describes the dataset.
In this example, hovering over the <code>firewallEventsAdaptive</code> node displays this
description:</p>
<p><img src="/assets/upstream/images/analytics/graphiql-set-up-base-query.png" alt="Hovering the mouse over a field to display its description" /></p>
<p>To display information about the dataset, including required parameters, select
the dataset name (blue text). The <strong>Documentation Explorer</strong> opens and displays
details about the dataset:</p>
<p><img src="/assets/upstream/images/analytics/graphiql-parameters.png" alt="Documentation Explorer window displaying dataset details" /></p>
<p>Note that the <code>filter</code> and <code>limit</code> arguments are required, as indicated by the
exclamation mark (<code>!</code>) after their type definitions (gold text). In this
example, the <code>orderBy</code> argument is not required, though when used it requires a
value of type <code>ZoneFirewallEventsAdaptiveOrderBy</code>.</p>
<p>To browse a list of supported filter fields, select the filter type definition
(gold text) in the Documentation Explorer. In this example, the type is
<code>ZoneFirewallEventsAdaptiveFilter_InputObject</code>:</p>
<p><img src="/assets/upstream/images/analytics/graphiql-filter-fields.png" alt="Browsing GraphiQL filter fields" /></p>
<p>This example query shows the required <code>filter</code> and <code>limit</code> arguments for
<code>firewallEventsAdaptive</code> (as well as for the rest of GraphQL nodes):</p>
<p><img src="/assets/upstream/images/analytics/graphiql-filter-values.png" alt="Example of GraphiQL query arguments" /></p>
<h2 id="define-the-fields-used-by-your-query">Define the fields used by your query</h2>
<p>To browse the fields you can use with your query, hover your cursor over the
dataset name in your query, and in the tooltip that displays, select the data
type definition (gold text):</p>
<p><img src="/assets/upstream/images/analytics/graphiql-set-up-base-query.png" alt="Hovering the mouse over a dataset to display available fields" /></p>
<p><strong>The Documentation Explorer</strong> opens and displays a list of fields:</p>
<p><img src="/assets/upstream/images/analytics/graphiql-return-fields.png" alt="Documentation Explorer window displaying list of fields" /></p>
<p>To add the data fields that you want to read, type an opening brace (<code>{</code>) after
the closing parenthesis for the parameters, then start typing the name of a
field that you want to fetch. Use word completion to choose a field.</p>
<p>This example query returns the <code>action</code>, <code>datetime</code>, <code>clientRequestHTTPHost</code>,
and <code>userAgent</code> fields:</p>
<p><img src="/assets/upstream/images/analytics/graphiql-query-return-field-values.png" alt="Example query with return fields" /></p>
<p>Once you have entered all the fields you want to query, select the <strong>Play</strong>
button to submit the query. The response pane will contain the data fetched from
the configured GraphQL API endpoint:</p>
<p><img src="/assets/upstream/images/analytics/create-query-fw-data-set-play.png" alt="GraphiQL response pane" /></p>
<h2 id="variable-substitution">Variable substitution</h2>
<p>The GraphiQL client allows you to use placeholders for value and supply them via
the <code>variables</code> part of the payload.</p>
<p>Placeholder names should start with <code>$</code> character, and you do not need to wrap
placeholders in quotes when you use them in the query.</p>
<p>Values for placeholders should be provided in JSON format, in which placeholders
are addressed without <code>$</code> character. As an example, for a placeholder <code>$zoneTag</code>
GraphQL API will read a value from the <code>zoneTag</code> field of supplied variables
object.</p>
<p>To supply a value for a placeholder, select the <strong>Query Variables</strong> pane and edit
a JSON object that defines your variables.</p>
<p>This example query uses the <code>zoneTag</code> query variable to represent the zone ID:</p>
<p><img src="/assets/upstream/images/analytics/graphiql-query-variables.png" alt="Example of GraphiQL query variables" /></p>

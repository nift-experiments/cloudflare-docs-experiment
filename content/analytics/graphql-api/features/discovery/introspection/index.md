<p>Cloudflare GraphQL API has a dynamic schema and exposes more than 70 datasets
across zone and account scopes. We constantly expand the list and replace
existing ones with more capable alternatives.</p>
<p>To tackle the schema question, GraphQL provides an <a href="https://graphql.org/learn/introspection/">introspection</a> mechanism.
It is part of the GraphQL specification and allows you to explore the graph of
the datasets and fields.</p>
<p>The introspection results provide an overview of ALL available nodes and fields,
their descriptions and deprecation status.</p>
<p>Although GraphQL has <code>query</code>, <code>subscription</code>, and <code>mutation</code> operations,
Cloudflare GraphQL API only supports <code>query</code> operation.</p>
<h2 id="description-and-beta-mode">Description and Beta mode</h2>
<p>With details on data exposed by a given node or a field, descriptions also
indicate whether it is in Beta mode. Beta nodes (or fields) are for testing and
exploration and are usually available for customers on more extensive plans.
Please do not rely on beta data nodes since they are subject to change or
removal without notice.</p>
<h2 id="deprecation">Deprecation</h2>
<p>Introspection provides information about deprecation status. Cloudflare uses it
as a notification about replacement plans. If the sunset date is provided,
please migrate to a replacement node(s) before that date to avoid any
disruption.</p>
<h2 id="availability">Availability</h2>
<p>Some of the nodes might only be available to query for some users. Please refer
to the <a href="/analytics/graphql-api/features/discovery/settings/">settings</a> node for more details about availability and personal
limits on a given node.</p>
<h2 id="explore-documentation">Explore documentation</h2>
<p>The most convenient way to introspect the schema is to use a documentation
<a href="/analytics/graphql-api/getting-started/explore-graphql-schema/">explorer</a> that usually is a part of a GraphQL client (like GraphiQL, Altair,
etc).</p>
<p>Alternatively, you can also do it manually by using <code>__schema</code> node with the
needed directives.</p>
<pre><code class="language-graphql">{&#10;	__schema {&#10;		queryType {&#10;			name&#10;		}&#10;		mutationType {&#10;			name&#10;		}&#10;		subscriptionType {&#10;			name&#10;		}&#10;		types {&#10;			...FullType&#10;		}&#10;		directives {&#10;			name&#10;			description&#10;			locations&#10;			args {&#10;				...InputValue&#10;			}&#10;		}&#10;	}&#10;}&#10;fragment TypeRef on __Type {&#10;	kind&#10;	name&#10;	ofType {&#10;		kind&#10;		name&#10;		ofType {&#10;			kind&#10;			name&#10;			ofType {&#10;				kind&#10;				name&#10;				ofType {&#10;					kind&#10;					name&#10;					ofType {&#10;						kind&#10;						name&#10;						ofType {&#10;							kind&#10;							name&#10;							ofType {&#10;								kind&#10;								name&#10;							}&#10;						}&#10;					}&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;fragment InputValue on __InputValue {&#10;	name&#10;	description&#10;	type {&#10;		...TypeRef&#10;	}&#10;	defaultValue&#10;}&#10;fragment FullType on __Type {&#10;	kind&#10;	name&#10;	description&#10;	fields(includeDeprecated: true) {&#10;		name&#10;		description&#10;		args {&#10;			...InputValue&#10;		}&#10;		type {&#10;			...TypeRef&#10;		}&#10;		isDeprecated&#10;		deprecationReason&#10;	}&#10;	inputFields {&#10;		...InputValue&#10;	}&#10;	interfaces {&#10;		...TypeRef&#10;	}&#10;	enumValues(includeDeprecated: true) {&#10;		name&#10;		description&#10;		isDeprecated&#10;		deprecationReason&#10;	}&#10;	possibleTypes {&#10;		...TypeRef&#10;	}&#10;}&#10;</code></pre>
<p>For more details on how to send a GraphQL request with curl, please refer to <a href="/analytics/graphql-api/getting-started/execute-graphql-query/">Execute a GraphQL query with curl</a>.</p>

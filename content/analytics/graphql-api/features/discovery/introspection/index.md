---
cp9:
  canonical: https://developers.cloudflare.com/analytics/graphql-api/features/discovery/introspection/
  description: Explore the GraphQL schema using introspection.
  full_title: Introspection · Cloudflare Analytics docs
  head_html: <title>Introspection · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="Explore the GraphQL schema using introspection."><link rel="canonical" href="https://developers.cloudflare.com/analytics/graphql-api/features/discovery/introspection/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/graphql-api/features/discovery/introspection/index.md"><meta property="og:title" content="Introspection · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Explore the GraphQL schema using introspection."><meta property="og:url" content="https://developers.cloudflare.com/analytics/graphql-api/features/discovery/introspection/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Analytics,GraphQL Analytics API"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/graphql-api/features/discovery/introspection/#page","headline":"Introspection \u00b7 Cloudflare Analytics docs","description":"Explore the GraphQL schema using introspection.","url":"https://developers.cloudflare.com/analytics/graphql-api/features/discovery/introspection/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/graphql-api/features/discovery/introspection/
  schema: 1
---
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
<pre tabindex="0"><code class="language-graphql">{&#10;	__schema {&#10;		queryType {&#10;			name&#10;		}&#10;		mutationType {&#10;			name&#10;		}&#10;		subscriptionType {&#10;			name&#10;		}&#10;		types {&#10;			...FullType&#10;		}&#10;		directives {&#10;			name&#10;			description&#10;			locations&#10;			args {&#10;				...InputValue&#10;			}&#10;		}&#10;	}&#10;}&#10;fragment TypeRef on __Type {&#10;	kind&#10;	name&#10;	ofType {&#10;		kind&#10;		name&#10;		ofType {&#10;			kind&#10;			name&#10;			ofType {&#10;				kind&#10;				name&#10;				ofType {&#10;					kind&#10;					name&#10;					ofType {&#10;						kind&#10;						name&#10;						ofType {&#10;							kind&#10;							name&#10;							ofType {&#10;								kind&#10;								name&#10;							}&#10;						}&#10;					}&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;fragment InputValue on __InputValue {&#10;	name&#10;	description&#10;	type {&#10;		...TypeRef&#10;	}&#10;	defaultValue&#10;}&#10;fragment FullType on __Type {&#10;	kind&#10;	name&#10;	description&#10;	fields(includeDeprecated: true) {&#10;		name&#10;		description&#10;		args {&#10;			...InputValue&#10;		}&#10;		type {&#10;			...TypeRef&#10;		}&#10;		isDeprecated&#10;		deprecationReason&#10;	}&#10;	inputFields {&#10;		...InputValue&#10;	}&#10;	interfaces {&#10;		...TypeRef&#10;	}&#10;	enumValues(includeDeprecated: true) {&#10;		name&#10;		description&#10;		isDeprecated&#10;		deprecationReason&#10;	}&#10;	possibleTypes {&#10;		...TypeRef&#10;	}&#10;}&#10;</code></pre>
<p>For more details on how to send a GraphQL request with curl, please refer to <a href="/analytics/graphql-api/getting-started/execute-graphql-query/">Execute a GraphQL query with curl</a>.</p>

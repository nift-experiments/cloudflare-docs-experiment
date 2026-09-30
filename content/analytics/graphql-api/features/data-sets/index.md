<p>Cloudflare Analytics offers a range of datasets, including both general and
product-specific ones. Datasets use a consistent naming scheme that explicitly
identifies the type of data they return:</p>
<ul>
<li>
<p><strong>Domain</strong> - Each dataset is named after the field it describes and is
associated with a set of nodes. Product-specific data nodes incorporate the
name of the relevant product, for instance <code>loadBalancingRequests*</code> nodes.</p>
</li>
<li>
<p><strong>Adaptive Sampling</strong> - Nodes that represent data acquired using adaptive
sampling incorporate the <code>Adaptive</code> suffix. For more details, refer to
<a href="/analytics/graphql-api/sampling/">sampling</a>.</p>
</li>
<li>
<p><strong>Aggregated data</strong> - Nodes that represent aggregated data include the
<code>Groups</code> suffix. For example, the <code>loadBalancingRequestsAdaptiveGroups</code> node
represents aggregated data for Load Balancing requests. Aggregated data is
returned in an array of <code>...Group</code> objects. Please note: we have a node that
currently excluded from that naming convention - <code>workersInvocationsAdaptive</code>
(beta).</p>
</li>
<li>
<p><strong>Raw data</strong> - Raw data nodes, such as <code>loadBalancingRequestsAdaptive</code>, are
not aggregated and so do not incorporate the <code>Groups</code> suffix. Raw data is
returned in arrays containing objects of the relevant data type. For example,
a query to <code>loadBalancingRequestsAdaptive</code> returns a variety of
<code>LoadBalancingRequest</code> objects.</p>
</li>
</ul>
<p>To find out more information about datasets, availability, beta, and deprecation
statuses, please refer to GraphQL <a href="/analytics/graphql-api/features/discovery/">discovery</a> features.</p>
<h2 id="working-with-datasets">Working with datasets</h2>
<h3 id="aggregated-fields">Aggregated fields</h3>
<p>This example illustrates the structure for Groups:</p>
<pre><code class="language-graphql">type WhateverGroup {&#10;    count # No subfields, it is just the group size. Not available for roll-up tables.&#10;    sum {&#10;        &#35; fields that support summing (numbers, maps of numbers)&#10;    }&#10;    avg {&#10;        &#35; fields that support averaging (numbers)&#10;    }&#10;    uniq {&#10;        &#35; fields that support uniqueing (numbers, strings, enums, IPs, dates, etc.)&#10;    }&#10;}&#10;</code></pre>
<p>Unique values are not available as a dimension but can be queried as demonstrated in this example:</p>
<pre><code class="language-graphql">{&#10;  &#35; Get number of bytes and unique IPs in each minute.&#10;  httpRequests1mGroups {&#10;    sum {&#10;      bytes&#10;    }&#10;    uniq {&#10;      uniques # unique IPs&#10;    }&#10;    dimensions {&#10;      datetimeMinute&#10;    }&#10;  }&#10;&#10;  &#35; Count the number of events in each hour.&#10;  firewallEventsAdaptiveGroups {&#10;    count&#10;    dimensions {&#10;      datetimeHour&#10;    }&#10;  }&#10;}&#10;</code></pre>
<h3 id="schema-type-definitions">Schema type definitions</h3>
<p>Every exposed table has a GraphQL type definition. Type definitions observe the following rules:</p>
<ul>
<li>Regular fields represent themselves.</li>
<li>Every field, including nested fields, has a type and represents a list of that type.</li>
<li>The <code>enum</code> type represents an enumerated field.</li>
</ul>
<p>Here is an example type definition for <code>ContentTypeMapElem</code>:</p>
<pre><code class="language-graphql">type ContentTypeMapElem {&#10;    edgeResponseContentType: UInt32!&#10;    requests: UInt64!&#10;    bytes: UInt64!&#10;}&#10;&#10;&#35; An array of httpRequestsGroup is the result of httpRequests1hGroups or&#10;&#35; httpRequests1mGroups query.&#10;type httpRequestsGroup {&#10;    date: Date!&#10;    timeslot: DateTime!&#10;    requests: UInt64!&#10;    contentTypeMap: [ContentTypeMapElem!]!&#10;    &#35; ... other fields&#10;}&#10;&#10;enum TrustedClientCategory {&#10;    UNKNOWN&#10;    REAL_BROWSER&#10;    HONEST_BOT&#10;}&#10;&#10;&#35; An array of Request is the result of httpRequests query.&#10;type Request {&#10;    trustedClientCategory: TrustedClientCategory!&#10;    &#35; ... other fields&#10;}&#10;</code></pre>

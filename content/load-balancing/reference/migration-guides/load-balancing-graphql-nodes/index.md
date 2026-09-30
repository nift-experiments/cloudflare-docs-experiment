<p>After 30 September 2021, Cloudflare will make the following changes to the Load Balancing GraphQL schema:</p>
<ul>
<li>Deprecate nodes:
<ul>
<li><code>loadBalancingRequestsGroups</code> will be deprecated for <code>loadBalancingRequestsAdaptiveGroups</code></li>
<li><code>loadBalancingRequests</code> will be deprecated for <code>loadBalancingRequestsAdaptive</code></li>
</ul>
</li>
<li>Deprecate the <code>date</code> field (replace it with the existing <code>datetime</code> field)</li>
<li>Add the <code>sampleInterval</code> field</li>
</ul>
<h2 id="example-query">Example query</h2>
<p>The following example:</p>
<ul>
<li>Replaces <code>loadBalancingRequestsGroups</code> with <code>loadBalancingRequestsAdaptiveGroups</code></li>
<li>Replaces <code>date</code> with <code>datetime</code></li>
<li>Uses the new <code>sampleInterval</code> field</li>
</ul>
<pre><code class="language-json">query {&#10;  viewer {&#10;    zones(filter: { zoneTag: &quot;your Zone ID&quot; }) {&#10;      loadBalancingRequestsAdaptiveGroups(&#10;        filter: {&#10;          datetime_gt: &quot;2021-06-12T04:00:00Z&quot;,&#10;          datetime_lt: &quot;2021-06-13T06:00:00Z&quot;&#10;        }&#10;      ) {&#10;        dimensions {&#10;          datetime&#10;          coloCode&#10;          ...&#10;        }&#10;        avg {&#10;          sampleInterval&#10;        }&#10;      }&#10;    }&#10;  }&#10;}&#10;</code></pre>

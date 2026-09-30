<p>Using a plain curl to send a query provides the ability to slice-n-dice with the
results and apply post-processing if needed. For example, converting
results received from GraphQL API into a CSV format.</p>
<p>For more functionality, like auto-completion, schema exploring, etc., you can
look at GraphQL <a href="/analytics/graphql-api/getting-started/compose-graphql-query/">clients</a>.</p>
<p>GraphQL API expects JSON with two essentials fields: &quot;query&quot; and &quot;variables&quot;.</p>
<p>A query should be stripped from newline symbols and sent as a single-line string
when the variables is an object full of values for all placeholders used in the
query:</p>
<pre><code class="language-json">{&#10;  &quot;query&quot;: &quot;{viewer { ... }}&quot;,&#10;  &quot;variables&quot;: {}&#10;}&#10;</code></pre>
<p>It is still possible to use a human-friendly query though. In the example below
you can see how <code>echo</code> piped together with <code>tr</code> to provide a proper payload with
<code>curl</code>:</p>
<pre><code class="language-bash">echo &#x27;{ &quot;query&quot;:&#10;  &quot;{&#10;    viewer {&#10;      zones(filter: { zoneTag: $zoneTag }) {&#10;        firewallEventsAdaptive(&#10;          filter: $filter&#10;          limit: 10&#10;          orderBy: [datetime_DESC]&#10;        ) {&#10;          action&#10;          clientAsn&#10;          clientCountryName&#10;          clientIP&#10;          clientRequestPath&#10;          clientRequestQuery&#10;          datetime&#10;          source&#10;          userAgent&#10;        }&#10;      }&#10;    }&#10;  }&quot;,&#10;  &quot;variables&quot;: {&#10;    &quot;zoneTag&quot;: &quot;&lt;zone-tag&gt;&quot;,&#10;    &quot;filter&quot;: {&#10;      &quot;datetime_geq&quot;: &quot;2022-07-24T11:00:00Z&quot;,&#10;      &quot;datetime_leq&quot;: &quot;2022-07-24T12:00:00Z&quot;&#10;    }&#10;  }&#10;}&#x27; | tr -d &#x27;\n&#x27; | curl --silent \&#10;https://api.cloudflare.com/client/v4/graphql \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data @-&#10;</code></pre>

<p>Confidence intervals help assess accuracy and quantify uncertainty in results from sampled datasets. When querying sum or count fields on adaptive datasets, you can request a confidence interval to understand the possible range around an estimate. For example, specifying a confidence level of <code>0.95</code> returns the estimate, along with the range of values that likely contains the true value 95% of the time.</p>
<h2 id="availability">Availability</h2>
<ul>
<li><strong>Supported datasets</strong>: Adaptive (sampled) datasets only.</li>
<li><strong>Supported fields</strong>: All <code>sum</code> and <code>count</code> fields.</li>
<li><strong>Usage</strong>: Confidence <code>level</code> must be provided as a decimal between 0 and 1 (for example,<code>0.90</code>, <code>0.95</code>, <code>0.99</code>).</li>
<li><strong>Default</strong>: If no confidence level is specified, intervals are not returned.</li>
</ul>
<h2 id="usage-example">Usage example</h2>
<p>The following example shows how to query a confidence interval and interpret the response.</p>
<h3 id="request">Request</h3>
<p>To request a confidence interval, use the <code>confidence(level: X)</code> argument in your query.</p>
<pre><code class="language-graphql">query SingleDatasetWithConfidence($zoneTag: string, $start: Time, $end: Time) {&#10;  viewer {&#10;    zones(filter: {zoneTag: $zoneTag}) {&#10;      firewallEventsAdaptiveGroups(&#10;        filter: {datetime_gt: $start, datetime_lt: $end}&#10;        limit: 1000&#10;      ) {&#10;        count&#10;        avg {&#10;          sampleInterval&#10;        }&#10;        confidence(level: 0.95) {&#10;          count {&#10;            estimate&#10;            lower&#10;            upper&#10;            sampleSize&#10;          }&#10;        }&#10;      }&#10;    }&#10;  }&#10;}&#10;</code></pre>
<h3 id="response">Response</h3>
<p>The response includes the following values:</p>
<ul>
<li><code>estimate</code>: The estimated value, based on sampled data.</li>
<li><code>lower</code>: The lower bound of the confidence interval.</li>
<li><code>sampleSize</code>: The number of sampled data points used to calculate the estimate.</li>
<li><code>upper</code>: The upper bound of the confidence interval.</li>
</ul>
<p>In this example, the interpretation of the response is that, based on a sample of 40,054, the estimated number of events is 42,939, with 95% confidence that the true value lies between 42,673 and 43,204.</p>
<pre><code class="language-json">{&#10;  &quot;data&quot;: {&#10;    &quot;viewer&quot;: {&#10;      &quot;zones&quot;: [&#10;        {&#10;          &quot;firewallEventsAdaptiveGroups&quot;: [&#10;            {&#10;              &quot;avg&quot;: {&#10;                &quot;sampleInterval&quot;: 1.0720277625205972&#10;              },&#10;              &quot;confidence&quot;: {&#10;                &quot;count&quot;: {&#10;                  &quot;estimate&quot;: 42939,&#10;                  &quot;lower&quot;: 42673.44115335711,&#10;                  &quot;sampleSize&quot;: 40054,&#10;                  &quot;upper&quot;: 43204.55884664289&#10;                }&#10;              },&#10;              &quot;count&quot;: 42939&#10;            }&#10;          ]&#10;        }&#10;      ]&#10;    }&#10;  },&#10;  &quot;errors&quot;: null&#10;}&#10;</code></pre>

<p>To make your first request to Cloudflare's Radar API, you must obtain your <a href="/fundamentals/api/get-started/create-token/">API token</a> first. Create a Custom Token, with <em>Account</em> &gt; <em>Radar</em> in the <strong>Permissions</strong> group, and select <em>Read</em> as the access level.</p>
<p>Once you have the token, you are ready to make your first request to Radar's API at <code>https://api.cloudflare.com/client/v4/radar/</code>.</p>
<h2 id="example-using-curl">Example using cURL</h2>
<p>In the following example, we will access the global percentage distribution of device types (like mobile and desktop traffic) for the last seven days. For more information, refer to <a href="/api/resources/radar/subresources/http/subresources/summary/methods/device_type/">Get device types summary</a> endpoint:</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/radar/http/summary/device_type?dateRange=7d&amp;format=json&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>A successful response will look similar to the following:</p>
<pre><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;result&quot;: {&#10;		&quot;summary_0&quot;: {&#10;			&quot;desktop&quot;: &quot;58.223483&quot;,&#10;			&quot;mobile&quot;: &quot;41.725833&quot;,&#10;			&quot;other&quot;: &quot;0.050684&quot;&#10;		},&#10;		&quot;meta&quot;: {&#10;			&quot;dateRange&quot;: {&#10;				&quot;startTime&quot;: &quot;2022-10-26T14:00:00Z&quot;,&#10;				&quot;endTime&quot;: &quot;2022-11-02T14:00:00Z&quot;&#10;			},&#10;			&quot;normalization&quot;: &quot;PERCENTAGE&quot;,&#10;			...&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>This response means that 41% of the requests are classified as coming from mobile devices, while 58% are desktop traffic.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11562.md")
</aside>
<p>The previous example returns all traffic from bots and humans. However, you can access just the traffic classified as coming from humans (the default in <a href="https://radar.cloudflare.com">Cloudflare Radar</a>) by adding <code>botClass=LIKELY_HUMAN</code>. You can also access traffic coming only from bots with <code>botClass=LIKELY_AUTOMATED</code> (refer to <a href="/radar/concepts/bot-classes">bot classes</a> for more information). For example:</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/radar/http/summary/device_type?dateRange=7d&amp;botClass=LIKELY_AUTOMATED&amp;format=json&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>Running the above, can you find any differences between both in the distribution of mobile versus desktop traffic?</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="the-result-meta-property">The <code>result.meta</code> property</h3>
@markup("md", "content/.markup/bodies/11561.md")
</aside>
<h2 id="use-python">Use Python</h2>
<p><a href="https://www.python.org/">Python</a> has become one of the standard languages in data analysis. Here is a quick example on how to chart the same data using <a href="https://pypi.org/project/requests/">Requests</a> and <a href="https://pandas.pydata.org/">Pandas</a> libraries. Here, we are using <code>format=csv</code> in the parameters to make it easier for Pandas to import.</p>
<pre><code class="language-python">import io&#10;import requests&#10;import pandas as pd&#10;&#10;cf_api_url = &quot;https://api.cloudflare.com/client/v4&quot;&#10;params = &quot;dateRange=7d&amp;format=csv&quot;&#10;my_token = &quot;xxx&quot; # TODO replace&#10;r = requests.get(f&quot;{cf_api_url}/radar/http/summary/device_type?{params}&quot;,&#10;                 headers={&quot;Authorization&quot;: f&quot;Bearer {my_token}&quot;})&#10;df = pd.read_csv(io.StringIO(r.text))&#10;df.plot(kind=&quot;bar&quot;, stacked=True)&#10;</code></pre>
<h3 id="notebooks">Notebooks</h3>
<p>A <a href="https://jupyter.org/">notebook</a> is a web-based interactive computing application, where text, code, and code outputs, like charts, can be combined into a single document. Refer to Radar's companion <a href="https://colab.research.google.com/github/cloudflare/radar-notebooks/blob/main/notebooks/example.ipynb">colaboratory notebook</a> for more examples on how the API can be used in your own projects.</p>
<h2 id="next-steps">Next steps</h2>
<p>Refer to <a href="/radar/get-started/making-comparisons/">Make comparisons</a> to learn how to compare data.</p>

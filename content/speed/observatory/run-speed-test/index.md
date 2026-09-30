<h2 id="run-synthetic-test">Run Synthetic test</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Synthetic Monitoring</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Enter the URL you want to test. The URL must belong to the zone you are testing from.</li>
<li>Select the test type you want to use: <strong>Browser</strong> or <strong>Network tests</strong>.</li>
<li>Select the <strong>Region</strong> the automated browser will use.</li>
<li>Depending on your plan you can select to run the test <strong>once</strong>, <strong>daily</strong> or <strong>weekly</strong>. Refer to the <a href="/speed/observatory/run-speed-test/#quotas">Quotas</a> section for information on the test frequency available for your plan. Note that these limits may change over time.</li>
<li>After the test finishes running, you will get a Lighthouse score and you will have access to the list of the tests run. The test result page will give you details regarding the performance of your website, both for the desktop and mobile versions. Refer to <a href="/speed/observatory/test-results/">Understand test results</a> for more information.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13902.md")
</aside>
<h3 id="recommendations">Recommendations</h3>
<p>Observatory shows you a <strong>Recommendations</strong> tab, depending on the results from testing your website. The <strong>Recommendations</strong> section shows you the opportunities to improve your website that were identified based on the Lighthouse audits and recommends Cloudflare features or products that will help you improve those metrics. We also show you the potential savings you will get by enabling the recommended features or products.</p>
<h3 id="trend-and-history-report">Trend and History report</h3>
<p>In the Tested URLs table, in the last column, you can select the three dots &gt; <strong>View history report</strong>, and you will have access to the <strong>Trend</strong> table that will show your website’s performance metrics over time and a <strong>History report</strong> of all the tests you run on your website.</p>
<h2 id="enable-real-user-monitoring-rum">Enable real user monitoring (RUM)</h2>
<p>Once a test has been run, you can enable <a href="/speed/observatory/#real-user-monitoring-rum">RUM</a> data in the test results page:</p>
<ol>
<li>Go to <strong>Observatory</strong> and select <strong>Enable RUM</strong>. You can choose to enable globally or enable everywhere except the EU.</li>
<li>Once RUM data is running on your site, you can access <strong>Real user measurements</strong> on your test results page. Usually it takes less than five minutes to see the data coming in, but it will depend on traffic.</li>
</ol>
<p>Refer to <a href="/speed/observatory/test-results/">Understand test results</a> for more information about the results provided by real user data.</p>
<h3 id="information-collected">Information collected</h3>
<p>RUM uses a lightweight JavaScript beacon to collect the information Observatory uses. It does not use any client-side state, such as cookies or <code>localStorage</code>, to collect usage metrics.</p>
<h2 id="quotas">Quotas</h2>
<p>Quota limits for the number of tests you can run per month are currently the following:</p>
<table>
<thead>
<tr>
<th>Plan</th>
<th>One-off tests</th>
<th>Recurring tests</th>
<th>Frequency of recurring tests</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pro</td>
<td>50</td>
<td>5</td>
<td>Daily</td>
</tr>
<tr>
<td>Business</td>
<td>100</td>
<td>10</td>
<td>Daily</td>
</tr>
<tr>
<td>Enterprise</td>
<td>150</td>
<td>15</td>
<td>Daily</td>
</tr>
</tbody>
</table>
<p><strong>Available Regions (all plans):</strong></p>
<table>
<thead>
<tr>
<th>Region</th>
<th>Region</th>
<th>Region</th>
</tr>
</thead>
<tbody>
<tr>
<td>Iowa, USA</td>
<td>Hamina, Finland</td>
<td>Changhua County, Taiwan</td>
</tr>
<tr>
<td>South Carolina, USA</td>
<td>Madrid, Spain</td>
<td>Tokyo, Japan</td>
</tr>
<tr>
<td>North Virginia, USA</td>
<td>St. Ghislain, Belgium</td>
<td>Osaka, Japan</td>
</tr>
<tr>
<td>Dallas, USA</td>
<td>Eemshaven, Netherlands</td>
<td>Jurong West, Singapore</td>
</tr>
<tr>
<td>Oregon, USA</td>
<td>Milan, Italy</td>
<td>Sydney, Australia</td>
</tr>
<tr>
<td>London, England</td>
<td>Paris, France</td>
<td>Mumbai, India</td>
</tr>
<tr>
<td>Frankfurt, Germany</td>
<td>Tel Aviv, Israel</td>
<td>São Paulo, Brazil</td>
</tr>
</tbody>
</table>

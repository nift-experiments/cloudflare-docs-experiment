<p>Below you will find answers to our most commonly asked questions.</p>
<h2 id="sampling">Sampling</h2>
<h3 id="could-i-just-use-many-unique-index-values-to-get-better-unique-counts">Could I just use many unique index values to get better unique counts?</h3>
<p>No, adding a large number of index values does not come without drawbacks. The tradeoff is that reading across many indices is slow.</p>
<p>In practice, due to how ABR works, reading from many indices in one query will result in low-resolution data – possibly unusably low.</p>
<p>On the other hand, if you pick a good index that aligns with how you read the data, your queries will run faster and you will get higher resolution results.</p>
<h3 id="what-if-i-need-to-index-on-multiple-values">What if I need to index on multiple values?</h3>
<p>It is possible to concatenate multiple values in your index field. So if you want to index on user ID and hostname, you can write, for example <code>&quot;$userID:$hostname&quot;</code> into your index field.</p>
<p>Note that, based on your query pattern, it may make sense to write the same dataset with different indices. It is a common misconception that one should avoid &quot;double-writing&quot; data.</p>
<p>Thanks to sampling, the cost of writing data multiple times can be relatively low. However, reading data inefficiently can result in significant expenses or low-quality results due to sampling.</p>
<h3 id="how-do-i-know-if-my-data-is-sampled">How do I know if my data is sampled?</h3>
<p>You can use the <code>_sample_interval</code> field — again, note that this does not tell you if the results are accurate.</p>
<p>You can tell when data is sampled at read time because sample intervals will be multiples of powers of 10, for example <code>20</code> or <code>700</code>. There is no hard and fast rule for when sampling starts at read time, but in practice reading longer periods (or more index values) will result in a higher sample interval.</p>
<h3 id="why-is-data-missing">Why is data missing?</h3>
<p>Sampling is based largely on the choice of index, as well as other factors like the time range queried and number of indices read. If you are reading from a larger index over a longer time period, and have filtered to a relatively small subgroup within that index, it may not be present due to sampling.</p>
<p>If you need to read accurate results for that subgroup, we suggest that you add that field to your index (refer to <a href="/analytics/faq/wae-faqs/#what-if-i-need-to-index-on-multiple-values">What if I need to index on multiple values</a>).</p>
<h3 id="can-i-trust-sampled-data-are-my-results-accurate">Can I trust sampled data? Are my results accurate?</h3>
<p>Sampled data is highly reliable, particularly when a carefully selected index is used.</p>
<p>Admittedly, it is difficult at present to prove that the results returned by ABR queries are within a certain error bound. As a rule of thumb, it is good to check the number of rows read by using count() — think of this like the count of pixels in your image. A higher number of rows read will result in more accurate results. (The flipside is that the <code>_sample_interval</code> field does not tell you very much about whether your results are accurate). If you are extrapolating from only one or two rows, it is unlikely you have a representative result; if you are extrapolating from thousands of rows, it is very likely that your results are quite accurate.</p>
<p>In the near future, we plan to expose the <a href="https://en.wikipedia.org/wiki/Margin_of_error">margin of error</a> along with query results so that you can see precisely how accurate your results are.</p>
<h3 id="how-are-bursts-handled">How are bursts handled?</h3>
<p>Equitable sampling exists both to normalize differences between groups, and also to handle large spikes of traffic to a given index. Equalization happens every few seconds; if you are writing many events very close in time, then it is expected that they will be sampled at write time.  The sample interval for a given index will vary from moment to moment, based on the current rate of data being written.</p>
<h3 id="how-much-traffic-will-trigger-sampling">How much traffic will trigger sampling?</h3>
<p>There is no fixed rule determining when sampling will be triggered.</p>
<p>We have observed that for workloads like our global CDN, which distribute load around our network, each index value needs about 100 data points per second before sampling is noticeable at all.</p>
<p>Depending on your workload and how you use Workers Analytics Engine, sampling may start at a higher or lower threshold than this. For example, if you are writing out many data points from a single worker execution, it is more likely that your data will be sampled.</p>

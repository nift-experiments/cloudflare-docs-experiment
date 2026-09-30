<p>When enabled, AI Security for Apps populates the following fields:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>LLM PII detected <br/> [<code>cf.llm.prompt.pii_detected</code>][1] <br/> <span class="nb-type">Boolean</span></td>
<td>Indicates whether any personally identifiable information (PII) has been detected in the LLM prompt included in the request.</td>
</tr>
<tr>
<td>LLM PII categories <br/> [<code>cf.llm.prompt.pii_categories</code>][2] <br/> <span class="nb-type">Array&lt;String&gt;</span></td>
<td>Array of string values with the personally identifiable information (PII) categories found in the LLM prompt included in the request.<br/><a href="/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.pii_categories/">Category list</a></td>
</tr>
<tr>
<td>LLM Content detected <br/> [<code>cf.llm.prompt.detected</code>][3] <br/> <span class="nb-type">Boolean</span></td>
<td>Indicates whether Cloudflare detected an LLM prompt in the incoming request.</td>
</tr>
<tr>
<td>LLM Unsafe topic detected <br/> [<code>cf.llm.prompt.unsafe_topic_detected</code>][4] <br/> <span class="nb-type">Boolean</span></td>
<td>Indicates whether the incoming request includes any unsafe topic category in the LLM prompt.</td>
</tr>
<tr>
<td>LLM Unsafe topic categories <br/> [<code>cf.llm.prompt.unsafe_topic_categories</code>][5] <br/> <span class="nb-type">Array&lt;String&gt;</span></td>
<td>Array of string values with the type of unsafe topics detected in the LLM prompt.<br/><a href="/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.unsafe_topic_categories/">Category list</a></td>
</tr>
<tr>
<td>LLM Injection score <br/> [<code>cf.llm.prompt.injection_score</code>][6] <br/> <span class="nb-type">Number</span></td>
<td>A score from 1–99 that represents the likelihood that the LLM prompt in the request is trying to perform a prompt injection attack. Lower scores indicate higher risk.</td>
</tr>
<tr>
<td>LLM Token count <br/> [<code>cf.llm.prompt.token_count</code>][7] <br/> <span class="nb-type">Number</span></td>
<td>An estimated token count for the LLM prompt in the request. Refer to <a href="/waf/detections/ai-security-for-apps/token-counting/">Token counting</a> for details.</td>
</tr>
<tr>
<td>LLM Custom topic categories <br/> [<code>cf.llm.prompt.custom_topic_categories</code>][8] <br/> <span class="nb-type">Map&lt;Number&gt;</span></td>
<td>A map of custom topic labels to relevance scores (1–99). Lower scores indicate the prompt is more relevant to that topic. Only populated when <a href="/waf/detections/ai-security-for-apps/unsafe-topics/#custom-topics">custom topics</a> are configured.</td>
</tr>
</tbody>
</table>

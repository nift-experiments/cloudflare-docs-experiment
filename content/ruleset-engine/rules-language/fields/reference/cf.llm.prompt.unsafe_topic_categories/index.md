<h1 id="cf-llm-prompt-unsafe-topic-categories">cf.llm.prompt.unsafe_topic_categories</h1>

**Data type:** Array<String>

<p>Array of string values with the type of unsafe topics detected in the LLM prompt.</p>

<p>The possible values are the following:</p>
<table>
<thead>
<tr>
<th>Value</th>
<th>Category name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>S1</code></td>
<td>Violent crimes</td>
<td>Violent crimes against people or animals.</td>
</tr>
<tr>
<td><code>S2</code></td>
<td>Non-violent crimes</td>
<td>Non-violent offenses such as fraud, theft, drug creation, or hacking.</td>
</tr>
<tr>
<td><code>S3</code></td>
<td>Sex-related crimes</td>
<td>Sex-related crimes, including trafficking, assault, and harassment.</td>
</tr>
<tr>
<td><code>S4</code></td>
<td>Child sexual exploitation</td>
<td>Sexual exploitation of children.</td>
</tr>
<tr>
<td><code>S5</code></td>
<td>Defamation</td>
<td>False statements that are likely to damage a living person's reputation.</td>
</tr>
<tr>
<td><code>S6</code></td>
<td>Specialized advice</td>
<td>Specialized financial, medical, or legal advice, or misrepresent dangerous things as safe.</td>
</tr>
<tr>
<td><code>S7</code></td>
<td>Privacy</td>
<td>Sensitive, nonpublic personal information that could endanger an individual.</td>
</tr>
<tr>
<td><code>S8</code></td>
<td>Intellectual property</td>
<td>Violate a third party's intellectual property rights.</td>
</tr>
<tr>
<td><code>S9</code></td>
<td>Indiscriminate weapons</td>
<td>Creation of indiscriminate weapons like chemical, biological, or nuclear arms.</td>
</tr>
<tr>
<td><code>S10</code></td>
<td>Hate</td>
<td>Demean or dehumanize people based on their race, religion, sexual orientation, or other personal characteristics.</td>
</tr>
<tr>
<td><code>S11</code></td>
<td>Suicide and self-harm</td>
<td>Encourage or endorse suicide, self-injury, or disordered eating.</td>
</tr>
<tr>
<td><code>S12</code></td>
<td>Sexual content</td>
<td>Erotic content.</td>
</tr>
<tr>
<td><code>S13</code></td>
<td>Elections</td>
<td>False information about the time, place, or manner of voting in elections.</td>
</tr>
<tr>
<td><code>S14</code></td>
<td>Code interpreter abuse</td>
<td>Misuse of code execution capabilities.</td>
</tr>
</tbody>
</table>
<p>Requires a Cloudflare Enterprise plan. You must also enable <a href="/waf/detections/ai-security-for-apps/">AI Security for Apps</a>.</p>

**Example usage:**

```txt
# Matches requests where an unsafe topic categorized as "S2" (Non-violent crimes) or "S10" (Hate) was detected in the LLM prompt:
(cf.llm.prompt.unsafe_topic_detected and any(cf.llm.prompt.unsafe_topic_categories[*] in {"S2" "S10"}))
```

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, cloudflare, ai, client, visitor


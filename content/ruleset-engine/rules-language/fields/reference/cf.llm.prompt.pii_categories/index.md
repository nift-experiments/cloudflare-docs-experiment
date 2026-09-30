<h1 id="cf-llm-prompt-pii-categories">cf.llm.prompt.pii_categories</h1>

**Data type:** Array<String>

<p>Array of string values with the personally identifiable information (PII) categories found in the LLM prompt included in the request.</p>

<p>The possible values are the following:</p>
<table>
<thead>
<tr>
<th>Category</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>BANK_ACCOUNT</code></td>
<td>Bank account number</td>
</tr>
<tr>
<td><code>CREDIT_CARD</code></td>
<td>Credit card number</td>
</tr>
<tr>
<td><code>DATE_TIME</code></td>
<td>Date or time expression</td>
</tr>
<tr>
<td><code>DRIVER_LICENSE</code></td>
<td>Driver license number</td>
</tr>
<tr>
<td><code>EMAIL_ADDRESS</code></td>
<td>Email address</td>
</tr>
<tr>
<td><code>IP_ADDRESS</code></td>
<td>Internet Protocol (IPv4) address</td>
</tr>
<tr>
<td><code>LOCATION</code></td>
<td>Physical location or address</td>
</tr>
<tr>
<td><code>PASSPORT</code></td>
<td>Passport number</td>
</tr>
<tr>
<td><code>PERSON</code></td>
<td>Full or partial name of an individual</td>
</tr>
<tr>
<td><code>PHONE_NUMBER</code></td>
<td>Telephone number</td>
</tr>
<tr>
<td><code>TAX_ID</code></td>
<td>Tax identification number</td>
</tr>
<tr>
<td><code>US_SSN</code></td>
<td>US Social Security Number (SSN)</td>
</tr>
<tr>
<td><code>URL</code></td>
<td>Uniform Resource Locator (URL), used to locate a resource on the Internet</td>
</tr>
</tbody>
</table>
<p>The categories are detected by an AI-based Named Entity Recognition (NER) model.</p>
<p>Requires a Cloudflare Enterprise plan. You must also enable <a href="/waf/detections/ai-security-for-apps/">AI Security for Apps</a>.</p>

**Example usage:**

```txt
# Matches requests where PII categorized as "EMAIL_ADDRESS" or "BANK_ACCOUNT" was detected:
(cf.llm.prompt.pii_detected and any(cf.llm.prompt.pii_categories[*] in {"EMAIL_ADDRESS" "BANK_ACCOUNT"}))
```

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, cloudflare, ai, client, visitor


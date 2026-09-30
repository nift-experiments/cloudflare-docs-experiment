<aside class="nb-aside note">
<h3 class="nb-aside-title" id="area-1-has-been-renamed">Area 1 has been renamed</h3>
@markup("md", "content/.markup/bodies/8578.md")
</aside>
<p>You can search for emails that have been processed by Email security (formerly Area 1), whether they are marked with a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8579.md")
</div> or not.
<p>There are two ways for searching emails:</p>
<ul>
<li><strong>Fielded Search</strong>: Presents you with fields where you can enter search terms.</li>
<li><strong>Freeform Search</strong>: Has one search field where you can construct your own search query, like <code>My great products</code>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8577.md")
</aside>
<h2 id="search-terms">Search terms</h2>
<p>In Freeform Search, you can search for any value or combination of values separated by a space. Using spaces with multiple search terms is the equivalent of using the operator <code>AND</code>.</p>
<p>Terms less than three characters long and common English words that do not offer significance for search value like <code>and</code>, <code>the</code>, <code>then</code>, <code>their</code> are ignored.</p>
<p>For more exact matches, use the named fields in <strong>Fielded Search</strong> to denote which field should contain the value. For example, to find only messages sent by <code>demo@example.com</code>, enter <code>demo@example.com</code> in <strong>FROM (EXACT)</strong>. <code>EXACT</code> in a field descriptor means the term will match how the value appears in the message.</p>
<h2 id="fielded-search">Fielded Search</h2>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</p>
</li>
<li>
<p>Select the <strong>Search</strong> bar.</p>
</li>
<li>
<p>Fill out one or more of the following fields. Filling multiple fields is the equivalent of adding the <code>AND</code> operator between the following terms:</p>
<ul>
<li><strong>Terms</strong>: Searches for terms in any of the available fields. If you want to search for a message that matches multiple recipients, use this field. Only one value can be specified in the <strong>From</strong> and <strong>To</strong> fields.</li>
<li><strong>From (Exact)</strong>: Searches for the sender’s exact email address.</li>
<li><strong>To (Exact)</strong>: Searches for the recipient’s exact email address.</li>
<li><strong>Subject</strong>: Searches for the terms in the subject field.</li>
<li><strong>Domain</strong>: Searches for messages from a specific domain.</li>
<li><strong>Message ID</strong>: Searches for messages with the stated message ID.</li>
<li><strong>Alert ID</strong>: Searches for messages with the stated alert ID.</li>
</ul>
</li>
<li>
<p><strong>Detections only</strong> is enabled by default. This means that the system will only search through and display emails that Email Security (formerly Area 1) has marked with a detection <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
</li>
</ol>
@markup("md", "content/.markup/bodies/8580.md")
</div>. If you prefer to search through and view all emails that have been processed by Email Security, whether they are marked with a detection disposition or not, disable this option.
2. The **All detections** drop-down menu allows you to refine your search by detection disposition. This menu will be disabled if **Detections only** is not selected.
3. By default, the search results are limited to the previous 30 days. Select **Last 30 days** to change this setting.
4. (Optional) You can download the results from your search in CSV format. The CSV file is capped at 1,000 rows.
5. The system returns a list of emails that fit your search criteria, and will inform you if there are emails similar to the ones found. If Email Security finds emails similar to the ones returned by your query, select **Show** to display them. Otherwise, select **View** on the email you are interested in. This will show you more information about that particular email, such as:
   * Disposition (if any)
   * Email status (for example `Quarantined`)
   * Sender details (for example, IP address)
<h2 id="freeform-search">Freeform Search</h2>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</p>
</li>
<li>
<p>Select the <strong>Search bar</strong> &gt; <strong>Freeform Search</strong>.</p>
</li>
<li>
<p>Build your search query — for example, <code>My great products</code>. The system will return all the emails that fit the query.</p>
</li>
<li>
<p><strong>Detections only</strong> is enabled by default. This means that the system will only search through and display emails that Email Security (formerly Area 1) has marked with a detection <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
</li>
</ol>
@markup("md", "content/.markup/bodies/8581.md")
</div>. If you prefer to search through and view all emails that have been processed by Email Security, whether they are marked with a detection disposition or not, disable this option.
2. The **All detections** drop-down menu allows you to refine your search by detection disposition. This menu will be disabled if **Detections only** is not selected.
3. By default, the search results are limited to the previous 30 days. Select **Last 30 days** to change this setting.
4. (Optional) You can download the results from your search in CSV format. The CSV file is capped at 1,000 rows.
5. The system returns a list of emails that fit your search criteria, and will inform you if there are emails similar to the ones found. If Email Security finds emails similar to the ones returned by your query, select **Show** to display them. Otherwise, select **View** on the email you are interested in. This will show you more information about that particular email, such as:
   * Disposition (if any)
   * Email status (for example `Quarantined`)
   * Sender details (for example, IP address)
<h2 id="search-tips">Search tips</h2>
<h3 id="parameter-filtering">Parameter filtering</h3>
<p>To search for specific values in one of the <a href="/email-security/reporting/search/available-parameters/">available parameters</a>, format your search to be:</p>
<pre><code class="language-txt">&lt;&lt;FIELD_NAME&gt;&gt;:&lt;&lt;VALUE&gt;&gt;&#10;</code></pre>
<p>For example, you might search for <code>final_disposition:MALICIOUS</code>. Refer to our reference material for a full list of <a href="/email-security/reference/dispositions-and-attributes/">dispositions</a>.</p>
<h3 id="message-id"><code>message_id</code></h3>
<p>For normal queries, spaces split search terms into different values. For example, <code>billing statement</code> would look for all messages that contain both <code>billing</code> and <code>statement</code>.</p>
<p>However, spaces, quotations, and other characters are sometimes part of the <code>message_id</code> parameter. To ensure these values are included as part of filtering on the message ID, you should prefix the <code>message_id</code> value with <code>message_id</code>.</p>
<p>For example, the following query would find all messages that contain the terms <code>billing</code> and <code>statement</code> and have a <code>message_id</code> equal to <code>&lt;Amazon aws Support@email.amazonses.com&gt;</code>.</p>
<pre><code class="language-txt">billing statement message_id:&lt;Amazon aws Support@email.amazonses.com&gt;&#10;</code></pre>

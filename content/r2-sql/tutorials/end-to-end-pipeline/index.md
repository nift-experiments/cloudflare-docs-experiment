---
cp9:
  canonical: https://developers.cloudflare.com/r2-sql/tutorials/end-to-end-pipeline/
  description: This tutorial demonstrates how to build a complete data pipeline using Cloudflare Pipelines, R2 Data Catalog, and R2 SQL.
  full_title: Build an end to end data pipeline · R2 SQL docs
  head_html: <title>Build an end to end data pipeline · R2 SQL docs</title><meta name="generator" content="Nift"><meta name="description" content="This tutorial demonstrates how to build a complete data pipeline using Cloudflare Pipelines, R2 Data Catalog, and R2 SQL."><link rel="canonical" href="https://developers.cloudflare.com/r2-sql/tutorials/end-to-end-pipeline/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2-sql/tutorials/end-to-end-pipeline/index.md"><meta property="og:title" content="Build an end to end data pipeline · R2 SQL docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This tutorial demonstrates how to build a complete data pipeline using Cloudflare Pipelines, R2 Data Catalog, and R2 SQL."><meta property="og:url" content="https://developers.cloudflare.com/r2-sql/tutorials/end-to-end-pipeline/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2 SQL"><meta name="algolia_product_filter" content="R2 SQL"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Pipelines,R2,R2 SQL,R2 Data Catalog"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2-sql/tutorials/end-to-end-pipeline/#page","headline":"Build an end to end data pipeline \u00b7 R2 SQL docs","description":"This tutorial demonstrates how to build a complete data pipeline using Cloudflare Pipelines, R2 Data Catalog, and R2 SQL.","url":"https://developers.cloudflare.com/r2-sql/tutorials/end-to-end-pipeline/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /r2-sql/tutorials/end-to-end-pipeline/
  schema: 1
---
<p class="article-summary">Learn how to create an end-to-end data pipeline using Cloudflare Pipelines, R2 Data Catalog, and R2 SQL for real-time transaction analysis.</p>
<p>In this tutorial, you will learn how to build a complete data pipeline using Cloudflare Pipelines, R2 Data Catalog, and R2 SQL. This also includes a sample Python script that creates and sends financial transaction data to your Pipeline that can be queried by R2 SQL or any Apache Iceberg-compatible query engine.</p>
<p>This tutorial demonstrates how to:</p>
<ul>
<li>Set up R2 Data Catalog to store our transaction events in an Apache Iceberg table</li>
<li>Set up a Cloudflare Pipeline</li>
<li>Create transaction data with fraud patterns to send to your Pipeline</li>
<li>Query your data using R2 SQL for fraud analysis</li>
</ul>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a>.</li>
<li>Install a <a href="/workers/wrangler/install-and-update/#install-wrangler">Node.js version supported by Wrangler</a>.</li>
<li>Install <a href="https://python.org">Python 3.8+</a> for the data generation script.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="node-js-version-manager">Node.js version manager</h3>
@markup("md", "content/.markup/bodies/11327.md")
</aside>
<h2 id="1-set-up-authentication"><ol>
<li>Set up authentication</li>
</ol></h2>
<p>You will need API tokens to interact with Cloudflare services.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11328.md")
</div>
<p>Export your new token as an environment variable:</p>
<pre tabindex="0"><code class="language-bash">export WRANGLER_R2_SQL_AUTH_TOKEN= #paste your token here&#10;</code></pre>
<p>If this is your first time using Wrangler, make sure to log in.</p>
<pre tabindex="0"><code class="language-bash">npx wrangler login&#10;</code></pre>
<h2 id="2-create-an-r2-bucket-and-enable-r2-data-catalog"><ol start="2">
<li>Create an R2 bucket and enable R2 Data Catalog</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11332.md")
</div></div>
<p>Enable the catalog on your R2 bucket:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11336.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11326.md")
</aside>
<pre tabindex="0"><code class="language-bash">export WAREHOUSE= #Paste your warehouse here&#10;</code></pre>
<h3 id="optional-enable-compaction-on-your-r2-data-catalog">(Optional) Enable compaction on your R2 Data Catalog</h3>
<p>R2 Data Catalog can automatically compact tables for you. In production event streaming use cases, it is common to end up with many small files, so it is recommended to enable compaction. Since the tutorial only demonstrates a sample use case, this step is optional.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11340.md")
</div></div>
<h2 id="3-set-up-the-pipeline-infrastructure"><ol start="3">
<li>Set up the pipeline infrastructure</li>
</ol></h2>
<h3 id="3-1-create-the-pipeline-stream">3.1. Create the Pipeline stream</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11344.md")
</div></div>
<h2 id="4-generate-sample-fraud-detection-data"><ol start="4">
<li>Generate sample fraud detection data</li>
</ol></h2>
<p>Create a Python script to generate realistic transaction data with fraud patterns:</p>
<pre tabindex="0"><code class="language-python">import requests&#10;import json&#10;import uuid&#10;import random&#10;import time&#10;import os&#10;from datetime import datetime, timezone, timedelta&#10;&#10;&#35; Configuration - exported from the prior steps&#10;STREAM_ENDPOINT = os.environ[&quot;STREAM_ENDPOINT&quot;]# From the stream you created&#10;API_TOKEN = os.environ[&quot;WRANGLER_R2_SQL_AUTH_TOKEN&quot;] #the same one created earlier&#10;EVENTS_TO_SEND = 1000 # Feel free to adjust this&#10;&#10;def generate_transaction():&#10;    &quot;&quot;&quot;Generate some random transactions with occasional fraud&quot;&quot;&quot;&#10;&#10;    &#35; User IDs&#10;    high_risk_users = [1001, 1002, 1003, 1004, 1005]&#10;    normal_users = list(range(1006, 2000))&#10;&#10;    user_id = random.choice(high_risk_users + normal_users)&#10;    is_high_risk_user = user_id in high_risk_users&#10;&#10;    &#35; Generate amounts&#10;    if random.random() &lt; 0.05:&#10;        amount = round(random.uniform(5000, 50000), 2)&#10;    elif random.random() &lt; 0.03:&#10;        amount = round(random.uniform(0.01, 1.00), 2)&#10;    else:&#10;        amount = round(random.uniform(10, 500), 2)&#10;&#10;    &#35; Locations&#10;    normal_locations = [&quot;NEW_YORK&quot;, &quot;LOS_ANGELES&quot;, &quot;CHICAGO&quot;, &quot;MIAMI&quot;, &quot;SEATTLE&quot;, &quot;SAN FRANCISCO&quot;]&#10;    high_risk_locations = [&quot;UNKNOWN_LOCATION&quot;, &quot;VPN_EXIT&quot;, &quot;MARS&quot;, &quot;BAT_CAVE&quot;]&#10;&#10;    if is_high_risk_user and random.random() &lt; 0.3:&#10;        location = random.choice(high_risk_locations)&#10;    else:&#10;        location = random.choice(normal_locations)&#10;&#10;    &#35; Merchant categories&#10;    normal_merchants = [&quot;GROCERY&quot;, &quot;GAS_STATION&quot;, &quot;RESTAURANT&quot;, &quot;RETAIL&quot;]&#10;    high_risk_merchants = [&quot;GAMBLING&quot;, &quot;CRYPTO&quot;, &quot;MONEY_TRANSFER&quot;, &quot;GIFT_CARDS&quot;]&#10;&#10;    if random.random() &lt; 0.1:  # 10% high-risk merchants&#10;        merchant_category = random.choice(high_risk_merchants)&#10;    else:&#10;        merchant_category = random.choice(normal_merchants)&#10;&#10;    &#35; Series of checks to either increase fraud score by a certain margin&#10;    fraud_score = 0&#10;    if amount &gt; 2000: fraud_score += 0.4&#10;    if amount &lt; 1: fraud_score += 0.3&#10;    if location in high_risk_locations: fraud_score += 0.5&#10;    if merchant_category in high_risk_merchants: fraud_score += 0.3&#10;    if is_high_risk_user: fraud_score += 0.2&#10;&#10;    &#35; Compare the fraud scores&#10;    is_fraud = random.random() &lt; min(fraud_score * 0.3, 0.8)&#10;&#10;    &#35; Generate timestamps (some fraud happens at unusual hours)&#10;    base_time = datetime.now(timezone.utc)&#10;    if is_fraud and random.random() &lt; 0.4:  # 40% of fraud at night&#10;        hour = random.randint(0, 5)  # Late night/early morning&#10;        transaction_time = base_time.replace(hour=hour)&#10;    else:&#10;        transaction_time = base_time - timedelta(&#10;            hours=random.randint(0, 168)  # Last week&#10;        )&#10;&#10;    return {&#10;        &quot;transaction_id&quot;: str(uuid.uuid4()),&#10;        &quot;user_id&quot;: user_id,&#10;        &quot;amount&quot;: amount,&#10;        &quot;transaction_timestamp&quot;: transaction_time.isoformat(),&#10;        &quot;location&quot;: location,&#10;        &quot;merchant_category&quot;: merchant_category,&#10;        &quot;is_fraud&quot;: True if is_fraud else False&#10;    }&#10;&#10;def send_batch_to_stream(events, batch_size=100):&#10;    &quot;&quot;&quot;Send events to Cloudflare Stream in batches&quot;&quot;&quot;&#10;&#10;    headers = {&#10;        &quot;Authorization&quot;: f&quot;Bearer {API_TOKEN}&quot;,&#10;        &quot;Content-Type&quot;: &quot;application/json&quot;&#10;    }&#10;&#10;    total_sent = 0&#10;    fraud_count = 0&#10;&#10;    for i in range(0, len(events), batch_size):&#10;        batch = events[i:i + batch_size]&#10;        fraud_in_batch = sum(1 for event in batch if event[&quot;is_fraud&quot;] == True)&#10;&#10;        try:&#10;            response = requests.post(STREAM_ENDPOINT, headers=headers, json=batch)&#10;&#10;            if response.status_code in [200, 201]:&#10;                total_sent += len(batch)&#10;                fraud_count += fraud_in_batch&#10;                print(f&quot;Sent batch of {len(batch)} events (Total: {total_sent})&quot;)&#10;            else:&#10;                print(f&quot;Failed to send batch: {response.status_code} - {response.text}&quot;)&#10;&#10;        except Exception as e:&#10;            print(f&quot;Error sending batch: {e}&quot;)&#10;&#10;        time.sleep(0.1)&#10;&#10;    return total_sent, fraud_count&#10;&#10;def main():&#10;    print(&quot;Generating fraud detection data...&quot;)&#10;&#10;    &#35; Generate events&#10;    events = []&#10;    for i in range(EVENTS_TO_SEND):&#10;        events.append(generate_transaction())&#10;        if (i + 1) % 100 == 0:&#10;            print(f&quot;Generated {i + 1} events...&quot;)&#10;&#10;    fraud_events = sum(1 for event in events if event[&quot;is_fraud&quot;] == True)&#10;    print(f&quot;📊 Generated {len(events)} total events ({fraud_events} fraud, {fraud_events/len(events)*100:.1f}%)&quot;)&#10;&#10;    &#35; Send to stream&#10;    print(&quot;Sending data to Pipeline stream...&quot;)&#10;    sent, fraud_sent = send_batch_to_stream(events)&#10;&#10;    print(f&quot;\nComplete!&quot;)&#10;    print(f&quot;   Events sent: {sent:,}&quot;)&#10;    print(f&quot;   Fraud events: {fraud_sent:,} ({fraud_sent/sent*100:.1f}%)&quot;)&#10;    print(f&quot;   Data is now flowing through your pipeline!&quot;)&#10;&#10;if __name__ == &quot;__main__&quot;:&#10;    main()&#10;</code></pre>
<p>Install the required Python dependency and run the script:</p>
<pre tabindex="0"><code class="language-bash">pip install requests&#10;python fraud_data_generator.py&#10;</code></pre>
<h2 id="5-query-the-data-with-r2-sql"><ol start="5">
<li>Query the data with R2 SQL</li>
</ol></h2>
<p>Now you can analyze your fraud detection data using R2 SQL. Here are some example queries:</p>
<h3 id="5-1-view-recent-transactions">5.1. View recent transactions</h3>
<pre tabindex="0"><code class="language-bash">npx wrangler r2 sql query &quot;$WAREHOUSE&quot; &quot;&#10;SELECT&#10;    transaction_id,&#10;    user_id,&#10;    amount,&#10;    location,&#10;    merchant_category,&#10;    is_fraud,&#10;    transaction_timestamp&#10;FROM fraud_detection.transactions&#10;WHERE __ingest_ts &gt; &#x27;2025-09-24T01:00:00Z&#x27;&#10;AND is_fraud = true&#10;LIMIT 10&quot;&#10;</code></pre>
<h3 id="5-2-filter-the-raw-transactions-into-a-new-table-to-highlight-high-value-transactions">5.2. Filter the raw transactions into a new table to highlight high-value transactions</h3>
<p>Create a new sink that will write the filtered data to a new Apache Iceberg table in R2 Data Catalog:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler pipelines sinks create fraud_filter_sink \&#10;  &#45;-type &quot;r2-data-catalog&quot; \&#10;  &#45;-bucket &quot;fraud-pipeline&quot; \&#10;  &#45;-roll-interval 30 \&#10;  &#45;-namespace &quot;fraud_detection&quot; \&#10;  &#45;-table &quot;fraud_transactions&quot; \&#10;  &#45;-catalog-token $WRANGLER_R2_SQL_AUTH_TOKEN&#10;</code></pre>
<p>Now you will create a new SQL query to process data from the original <code>raw_events_stream</code> stream and only write flagged transactions that are over the <code>amount</code> of 1,000.</p>
<pre tabindex="0"><code class="language-bash">npx wrangler pipelines create fraud_events_pipeline \&#10;  &#45;-sql &quot;INSERT INTO fraud_filter_sink SELECT * FROM raw_events_stream WHERE is_fraud=true and amount &gt; 1000&quot;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11323.md")
</aside>
<p>Query the table and check the results:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler r2 sql query &quot;$WAREHOUSE&quot; &quot;&#10;SELECT&#10;    transaction_id,&#10;    user_id,&#10;    amount,&#10;    location,&#10;    merchant_category,&#10;    is_fraud,&#10;    transaction_timestamp&#10;FROM fraud_detection.fraud_transactions&#10;LIMIT 10&quot;&#10;</code></pre>
<p>Also verify that the non-fraudulent events are being filtered out:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler r2 sql query &quot;$WAREHOUSE&quot; &quot;&#10;SELECT&#10;    transaction_id,&#10;    user_id,&#10;    amount,&#10;    location,&#10;    merchant_category,&#10;    is_fraud,&#10;    transaction_timestamp&#10;FROM fraud_detection.fraud_transactions&#10;WHERE is_fraud = false&#10;LIMIT 10&quot;&#10;</code></pre>
<p>You should see the following output:</p>
<pre tabindex="0"><code class="language-text">Query executed successfully with no results&#10;</code></pre>
<h2 id="conclusion">Conclusion</h2>
<p>You have successfully built an end to end data pipeline using Cloudflare's data platform. Through this tutorial, you have learned to:</p>
<ol>
<li><strong>Use R2 Data Catalog</strong>: Leveraged Apache Iceberg tables for efficient data storage</li>
<li><strong>Set up Cloudflare Pipelines</strong>: Created streams, sinks, and pipelines for data ingestion</li>
<li><strong>Generated sample data</strong>: Created transaction data with some basic fraud patterns</li>
<li><strong>Query your tables with R2 SQL</strong>: Access raw and processed data tables stored in R2 Data Catalog</li>
</ol>

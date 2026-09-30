---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/google/gemini-3.8-flash/
  description: google/gemini-3.8-flash
  full_title: Gemini 3.8 Flash · Cloudflare AI docs
  head_html: <title>Gemini 3.8 Flash · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="google/gemini-3.8-flash"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/google/gemini-3.8-flash/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Gemini 3.8 Flash · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="google/gemini-3.8-flash"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/google/gemini-3.8-flash/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/google/gemini-3.8-flash/#page","headline":"Gemini 3.8 Flash \u00b7 Cloudflare AI docs","description":"google/gemini-3.8-flash","url":"https://developers.cloudflare.com/ai/models/google/gemini-3.8-flash/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/google/gemini-3.8-flash/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/google.svg" alt="Google logo" width="48" height="48">

<h1 id="gemini-3-8-flash">Gemini 3.8 Flash</h1>

<p><code>google/gemini-3.8-flash</code></p>

Our most intelligent Flash model, engineered for long-horizon software engineering, autonomous agents, and complex enterprise workflows.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Context window</th><td>1,048,576 tokens</td></tr>
<tr><th>Terms</th><td><a href="https://ai.google.dev/gemini-api/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 0.75, Cached input tokens (per 1M): 0.075, Output tokens (per 1M): 3.75, Default (per second): 0.75</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Basic generateContent request

<section class="model-example"><strong>Simple Question</strong>
<p>Basic generateContent request</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;What are the key differences between optimistic and pessimistic concurrency control in distributed systems?&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ]
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;Concurrency control ensures that distributed transactions maintain the **ACID** properties (specifically Isolation and Consistency) when multiple nodes read and write to the same data simultaneously. \n\nThe fundamental difference between **Optimistic Concurrency Control (OCC)** and **Pessimistic Concurrency Control (PCC)** lies in **when and how they handle conflicts**.\n\n---\n\n### 1. The Core Philosophy\n\n*   **Pessimistic Concurrency Control (PCC):** *\&quot;Assume conflicts are likely.\&quot;* \n    *   It prevents conflicts **before** they happen by acquiring locks or blocking access to resources.\n*   **Optimistic Concurrency Control (OCC):** *\&quot;Assume conflicts are rare.\&quot;* \n    *   It allows transactions to execute concurrently without locks, checking for conflicts only **at the moment of commit**.\n\n---\n\n### 2. How They Work\n\n#### A. Pessimistic Concurrency Control (PCC)\n1. **Lock Phase:** A transaction requests a lock (read/shared or write/exclusive) on the required data partitions or nodes.\n2. **Execute Phase:** If locks are granted, the transaction reads and writes data. If a lock is unavailable, the transaction waits (blocks).\n3. **Commit &amp; Release Phase:** Once the transaction completes (often using **Two-Phase Commit / 2PC**), it writes changes and releases the locks.\n\n#### B. Optimistic Concurrency Control (OCC)\n1. **Read/Compute Phase:** The transaction reads data (often locally or from a replica) and buffers its writes without acquiring locks. It notes the version/timestamp of the data it read.\n2. **Validation Phase:** At commit time, the transaction checks if any other transaction modified the data it read since the start of the transaction.\n3. **Write/Abort Phase:** \n   * If **no conflict** is detected: The buffered writes are committed across nodes.\n   * If a **conflict** is detected: The transaction is **aborted and must retry**.\n\n---\n\n### 3. Key Differences in a Distributed Context\n\n| Feature | Pessimistic (PCC) | Optimistic (OCC) |\n| :--- | :--- | :--- |\n| **Locking Strategy** | Explicit locking (Shared/Exclusive). | Lock-free during execution; validation at commit. |\n| **Network Latency Impact** | **High.** Multiple round-trips to acquire and release locks across network nodes. | **Low.** Computation happens locally; network round-trips occur mostly during commit/validation. |\n| **Concurrency &amp; Throughput** | Low to moderate. Transactions block each other. | High, provided conflict rates remain low. |\n| **Conflict Resolution** | **Blocking / Queuing:** Transactions wait in line. | **Rollback / Retry:** Conflicted transactions abort and rerun. |\n| **Deadlock Risk** | **High.** Requires complex Distributed Deadlock Detection (wait-for graphs, edge chasing) or timeouts. | **None (or minimal).** Since no long-term locks are held, transactions cannot deadlock, but they can suffer from **starvation/livelock**. |\n| **Wasted Computation** | Low. If you have the lock, your work is guaranteed to commit (barring system crashes). | High under contention. Work must be discarded and repeated if validation fails. |\n| **Best Used When...** | Contention is **high**, write-heavy workloads, or abort costs are extremely expensive. | Contention is **low**, read-heavy workloads, or network latency makes locks expensive. |\n\n---\n\n### 4. Distributed Systems Trade-offs\n\n#### Network Overhead &amp; Latency\n*   **PCC suffers from latency compounding:** In a geographically distributed system, holding a distributed lock (e.g., via a Distributed Lock Manager like ZooKeeper) across high-latency WAN links holds up other transactions for tens or hundreds of milliseconds.\n*   **OCC handles latency better:** By eliminating locks during execution, nodes do not hold resources while waiting on network packets.\n\n#### The Cost of Partitions &amp; Node Failures\n*   **In PCC:** If a node holding a lock crashes or becomes network-partitioned, other transactions waiting for that lock stall indefinitely unless lease/heartbeat mechanisms aggressively revoke locks (which introduces its own consistency risks).\n*   **In OCC:** If a node fails mid-transaction, no locks are left dangling. The transaction simply times out, aborts, and retries.\n\n#### The \&quot;Abort Storm\&quot; (OCC&#x27;s Achilles&#x27; Heel)\nIn high-contention distributed scenarios (e.g., thousands of users trying to buy the same concert ticket):\n*   **PCC** gracefully queues requests; throughput slows down, but forward progress continues.\n*   **OCC** collapses into an **abort storm** (livelock). All transactions validate at the same time, one succeeds, and 999 abort. All 999 retry simultaneously, repeating the cycle and burning massive amounts of CPU and network bandwidth without making progress.\n\n---\n\n### 5. Common Implementations &amp; Real-World Examples\n\n*   **Pessimistic Implementations:**\n    *   **Two-Phase Locking (Strict 2PL):** Traditional distributed RDBMS (e.g., MySQL Cluster).\n    *   **Distributed Lock Managers (DLM):** Chubby (Google), Apache ZooKeeper (using ephemeral nodes/recipes for locking).\n*   **Optimistic Implementations:**\n    *   **MVCC (Multi-Version Concurrency Control):** Used by **CockroachDB**, **Google Cloud Spanner**, and **PostgreSQL**. MVCC is fundamentally an optimistic mechanism where readers do not block writers and writers do not block readers (relying on timestamp ordering).\n    *   **DynamoDB / Cassandra (Conditional Writes):** Uses version attributes or Lightweight Transactions (LWT with Paxos) to perform atomic `Compare-And-Swap` (CAS), which is an OCC pattern.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;candidates&quot;: [
      {
        &quot;content&quot;: {
          &quot;role&quot;: &quot;model&quot;,
          &quot;parts&quot;: [
            {
              &quot;text&quot;: &quot;Concurrency control ensures that distributed transactions maintain the **ACID** properties (specifically Isolation and Consistency) when multiple nodes read and write to the same data simultaneously. \n\nThe fundamental difference between **Optimistic Concurrency Control (OCC)** and **Pessimistic Concurrency Control (PCC)** lies in **when and how they handle conflicts**.\n\n---\n\n### 1. The Core Philosophy\n\n*   **Pessimistic Concurrency Control (PCC):** *\&quot;Assume conflicts are likely.\&quot;* \n    *   It prevents conflicts **before** they happen by acquiring locks or blocking access to resources.\n*   **Optimistic Concurrency Control (OCC):** *\&quot;Assume conflicts are rare.\&quot;* \n    *   It allows transactions to execute concurrently without locks, checking for conflicts only **at the moment of commit**.\n\n---\n\n### 2. How They Work\n\n#### A. Pessimistic Concurrency Control (PCC)\n1. **Lock Phase:** A transaction requests a lock (read/shared or write/exclusive) on the required data partitions or nodes.\n2. **Execute Phase:** If locks are granted, the transaction reads and writes data. If a lock is unavailable, the transaction waits (blocks).\n3. **Commit &amp; Release Phase:** Once the transaction completes (often using **Two-Phase Commit / 2PC**), it writes changes and releases the locks.\n\n#### B. Optimistic Concurrency Control (OCC)\n1. **Read/Compute Phase:** The transaction reads data (often locally or from a replica) and buffers its writes without acquiring locks. It notes the version/timestamp of the data it read.\n2. **Validation Phase:** At commit time, the transaction checks if any other transaction modified the data it read since the start of the transaction.\n3. **Write/Abort Phase:** \n   * If **no conflict** is detected: The buffered writes are committed across nodes.\n   * If a **conflict** is detected: The transaction is **aborted and must retry**.\n\n---\n\n### 3. Key Differences in a Distributed Context\n\n| Feature | Pessimistic (PCC) | Optimistic (OCC) |\n| :--- | :--- | :--- |\n| **Locking Strategy** | Explicit locking (Shared/Exclusive). | Lock-free during execution; validation at commit. |\n| **Network Latency Impact** | **High.** Multiple round-trips to acquire and release locks across network nodes. | **Low.** Computation happens locally; network round-trips occur mostly during commit/validation. |\n| **Concurrency &amp; Throughput** | Low to moderate. Transactions block each other. | High, provided conflict rates remain low. |\n| **Conflict Resolution** | **Blocking / Queuing:** Transactions wait in line. | **Rollback / Retry:** Conflicted transactions abort and rerun. |\n| **Deadlock Risk** | **High.** Requires complex Distributed Deadlock Detection (wait-for graphs, edge chasing) or timeouts. | **None (or minimal).** Since no long-term locks are held, transactions cannot deadlock, but they can suffer from **starvation/livelock**. |\n| **Wasted Computation** | Low. If you have the lock, your work is guaranteed to commit (barring system crashes). | High under contention. Work must be discarded and repeated if validation fails. |\n| **Best Used When...** | Contention is **high**, write-heavy workloads, or abort costs are extremely expensive. | Contention is **low**, read-heavy workloads, or network latency makes locks expensive. |\n\n---\n\n### 4. Distributed Systems Trade-offs\n\n#### Network Overhead &amp; Latency\n*   **PCC suffers from latency compounding:** In a geographically distributed system, holding a distributed lock (e.g., via a Distributed Lock Manager like ZooKeeper) across high-latency WAN links holds up other transactions for tens or hundreds of milliseconds.\n*   **OCC handles latency better:** By eliminating locks during execution, nodes do not hold resources while waiting on network packets.\n\n#### The Cost of Partitions &amp; Node Failures\n*   **In PCC:** If a node holding a lock crashes or becomes network-partitioned, other transactions waiting for that lock stall indefinitely unless lease/heartbeat mechanisms aggressively revoke locks (which introduces its own consistency risks).\n*   **In OCC:** If a node fails mid-transaction, no locks are left dangling. The transaction simply times out, aborts, and retries.\n\n#### The \&quot;Abort Storm\&quot; (OCC&#x27;s Achilles&#x27; Heel)\nIn high-contention distributed scenarios (e.g., thousands of users trying to buy the same concert ticket):\n*   **PCC** gracefully queues requests; throughput slows down, but forward progress continues.\n*   **OCC** collapses into an **abort storm** (livelock). All transactions validate at the same time, one succeeds, and 999 abort. All 999 retry simultaneously, repeating the cycle and burning massive amounts of CPU and network bandwidth without making progress.\n\n---\n\n### 5. Common Implementations &amp; Real-World Examples\n\n*   **Pessimistic Implementations:**\n    *   **Two-Phase Locking (Strict 2PL):** Traditional distributed RDBMS (e.g., MySQL Cluster).\n    *   **Distributed Lock Managers (DLM):** Chubby (Google), Apache ZooKeeper (using ephemeral nodes/recipes for locking).\n*   **Optimistic Implementations:**\n    *   **MVCC (Multi-Version Concurrency Control):** Used by **CockroachDB**, **Google Cloud Spanner**, and **PostgreSQL**. MVCC is fundamentally an optimistic mechanism where readers do not block writers and writers do not block readers (relying on timestamp ordering).\n    *   **DynamoDB / Cassandra (Conditional Writes):** Uses version attributes or Lightweight Transactions (LWT with Paxos) to perform atomic `Compare-And-Swap` (CAS), which is an OCC pattern.&quot;,
              &quot;thoughtSignature&quot;: &quot;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&quot;
            }
          ]
        },
        &quot;finishReason&quot;: &quot;STOP&quot;
      }
    ],
    &quot;usageMetadata&quot;: {
      &quot;promptTokenCount&quot;: 15,
      &quot;candidatesTokenCount&quot;: 1261,
      &quot;totalTokenCount&quot;: 2345,
      &quot;trafficType&quot;: &quot;ON_DEMAND&quot;,
      &quot;promptTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 15
        }
      ],
      &quot;candidatesTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 1261
        }
      ],
      &quot;thoughtsTokenCount&quot;: 1069
    },
    &quot;modelVersion&quot;: &quot;gemini-3.8-flash&quot;,
    &quot;createTime&quot;: &quot;2026-09-02T16:35:36.457158Z&quot;,
    &quot;responseId&quot;: &quot;WFCYasbzG43frb8Pq5aX0AY&quot;,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-3.8-flash&#x27;,
  {
    contents: [
      {
        parts: [
          {
            text: &#x27;What are the key differences between optimistic and pessimistic concurrency control in distributed systems?&#x27;,
          },
        ],
        role: &#x27;user&#x27;,
      },
    ],
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/gemini-3.8-flash&quot;,
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;What are the key differences between optimistic and pessimistic concurrency control in distributed systems?&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ]
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Agentic Coding</strong>
<p>Coding task with a system instruction and constrained temperature</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;Write a Python function that merges two sorted lists into one sorted list.&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;generationConfig&quot;: {
      &quot;temperature&quot;: 0.2
    },
    &quot;systemInstruction&quot;: {
      &quot;parts&quot;: [
        {
          &quot;text&quot;: &quot;You are an expert software engineering agent. Write concise, correct, well-documented code.&quot;
        }
      ]
    }
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;Here is an efficient, standard two-pointer implementation with $O(n + m)$ time complexity:\n\n```python\nfrom typing import Any, List\n\n\ndef merge_sorted_lists(list1: List[Any], list2: List[Any]) -&gt; List[Any]:\n    \&quot;\&quot;\&quot;Merge two already sorted lists into a single sorted list.\n\n    Time Complexity: O(n + m) where n and m are the lengths of the lists.\n    Space Complexity: O(n + m) to store the merged result.\n\n    Args:\n        list1: The first sorted list.\n        list2: The second sorted list.\n\n    Returns:\n        A new list containing all elements from both lists in sorted order.\n    \&quot;\&quot;\&quot;\n    merged: List[Any] = []\n    i, j = 0, 0\n    len1, len2 = len(list1), len(list2)\n\n    # Traverse both lists and append the smaller element to `merged`\n    while i &lt; len1 and j &lt; len2:\n        if list1[i] &lt;= list2[j]:\n            merged.append(list1[i])\n            i += 1\n        else:\n            merged.append(list2[j])\n            j += 1\n\n    # Append any remaining elements from either list\n    merged.extend(list1[i:])\n    merged.extend(list2[j:])\n\n    return merged\n\n\n# Example usage:\nif __name__ == \&quot;__main__\&quot;:\n    a = [1, 3, 5, 8]\n    b = [2, 4, 6, 7, 9, 10]\n    print(merge_sorted_lists(a, b))\n    # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n```\n\n### Alternative (Standard Library)\nIf you prefer using Python&#x27;s standard library, `heapq.merge` provides an iterator-based solution that uses $O(1)$ auxiliary space:\n\n```python\nimport heapq\n\n\ndef merge_sorted_lists_heapq(list1: list, list2: list) -&gt; list:\n    \&quot;\&quot;\&quot;Merge using Python&#x27;s built-in heapq module.\&quot;\&quot;\&quot;\n    return list(heapq.merge(list1, list2))\n```&quot;
  },
  &quot;raw_response&quot;: {
    &quot;candidates&quot;: [
      {
        &quot;content&quot;: {
          &quot;role&quot;: &quot;model&quot;,
          &quot;parts&quot;: [
            {
              &quot;text&quot;: &quot;Here is an efficient, standard two-pointer implementation with $O(n + m)$ time complexity:\n\n```python\nfrom typing import Any, List\n\n\ndef merge_sorted_lists(list1: List[Any], list2: List[Any]) -&gt; List[Any]:\n    \&quot;\&quot;\&quot;Merge two already sorted lists into a single sorted list.\n\n    Time Complexity: O(n + m) where n and m are the lengths of the lists.\n    Space Complexity: O(n + m) to store the merged result.\n\n    Args:\n        list1: The first sorted list.\n        list2: The second sorted list.\n\n    Returns:\n        A new list containing all elements from both lists in sorted order.\n    \&quot;\&quot;\&quot;\n    merged: List[Any] = []\n    i, j = 0, 0\n    len1, len2 = len(list1), len(list2)\n\n    # Traverse both lists and append the smaller element to `merged`\n    while i &lt; len1 and j &lt; len2:\n        if list1[i] &lt;= list2[j]:\n            merged.append(list1[i])\n            i += 1\n        else:\n            merged.append(list2[j])\n            j += 1\n\n    # Append any remaining elements from either list\n    merged.extend(list1[i:])\n    merged.extend(list2[j:])\n\n    return merged\n\n\n# Example usage:\nif __name__ == \&quot;__main__\&quot;:\n    a = [1, 3, 5, 8]\n    b = [2, 4, 6, 7, 9, 10]\n    print(merge_sorted_lists(a, b))\n    # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n```\n\n### Alternative (Standard Library)\nIf you prefer using Python&#x27;s standard library, `heapq.merge` provides an iterator-based solution that uses $O(1)$ auxiliary space:\n\n```python\nimport heapq\n\n\ndef merge_sorted_lists_heapq(list1: list, list2: list) -&gt; list:\n    \&quot;\&quot;\&quot;Merge using Python&#x27;s built-in heapq module.\&quot;\&quot;\&quot;\n    return list(heapq.merge(list1, list2))\n```&quot;,
              &quot;thoughtSignature&quot;: &quot;AY89a1/czemtyCXGVCK2P4eOWE2RysFkjJ/wuEOJhDOJ3QYU4daigY9JYFCTDRp7ZWJRgp4iPQBoHynLbpqmFI3dZCzKKONibIdXozwqr/Qnh04f0gJCHTERO4oLgUDplOyihnxn/wM/OdhnZZxocCdUpN9apM5qorKwGsl/XFKE/+rQDIe5WSguJihjLnHuQaUIbGx5kJfcnLkoRwHvnEYq0QjaRFQcIHxTIIUBABXzsFq42A3VF/s+KjqKmDVcFf68bEd8Vl64gKGqqFvFUJSxhuQuc0AYh+otH52oSU9gK74vIBBAomffgHojBHmBsB51u6rPSdpwaQN0GLmxWpdh1+6x03mfaqqeFcs7B5BTB8yPtsS5m9fEU9tMRChmYvQ342Ov6s4fU26nHXhI/S6Nkp2W6YS0XiGALK7rIa0WObLJ4IaRJ7pWu5WPBW1iScoDrZnrhOxUYUQ1NrbQhUUWngSy3Vza5BDWKOB300uLZZ2mysY1tYqvhEPsMrVscsNqozm4UvaHVtNHjPna6+L5qHqBQZN2aNpeO8y6caeYSLcoJkLJ75ZRnHQtrjn0X0Q4j2vz0R1t9j1oKE0KO5SL327+HmcB/qA1UGmINSJdsKslCMDixRHTasBfeCY5FK+Y9epbtJvajxD4LXECDtvmhm7aCs7JXX39wb1/fsqH70b+a+lHjd6wHRw9tPmmx7x+xOYXNCjY/atToqZ+X/3gtmxmPYzdl735S5cvAktd2oBvyTYx8rn6lBi6ZP6Lahx7Wcpx2NRhWmRiJ36TgxQV54qf1PjOd1IBKD5wLEqcHQwOC/aq0trIC4vjVd7oR1ygxPD9FmEUxNQMIJbvGpUgGv71k0DwPgPFoLYLti23h2x8M5TwAjCAE2NwC6V/iTvrq0FUP73xA/xv1JzQJmu4F4noFxvErOtI2wIXPdrC9IWS2ybm5YrOZyg6J4giOSwuKal7MP95q13nhBdxfRrEFuXj1o35GOPJ1BR6KohHIubOoCAkGpJoirpcBqKKjqGJNiwE9jgx824VNXd6dOx/s9finT+Asi2kom88E3ijWDukk9QdT6UPZ2ks4JvYAo6RU+kQ/px4LfQKwqOdbjplWqfhFfKZqxLVYLKS4qJ47C96rXLIsTiXHo1EJVs20dmrMvHKonZa5urz+LqLzL/iIm6ARgvoPf1h7/loDePJtYEJgULA0ydPipnEPfgsnkH9cFQtIkahXmxho5ngXdbn1A9Zh9mmKTnqyxpJnRrFNvC6gP9f7EVtJmZIVg4YoQvOkWzDBQelnJFEEvlBHpRdQ/s01Kbr783MeSBAmaiig2yWA9gEjkX4wZ3fAyypZ3x50q62yxf4oOGqPSPVKZylJf8j5yQ+AhCoFU5Pthk4yDn1ESotGjwb+uptmBlU2w0GWBRmgXqWHBujuVWeuvRdAK/QPUVYXim+fiDEJY0p94zidZI48EypvEquFDtOY5EpSEkuJx5inYwsVYDFuEVh3/CzSt1wC+Adq4P7b1C8/kDnFnxkjQFni0eyfGX6vvejB6+qTZikmJj1p5xX0f6oL9SkBAnju6wUt2ypckZjuL2v2nmVZ7jzVCa/mmE7mabFRov+VpMkmLB6mO+LlMsLalXQKIASYC+v4Xgbov+xXCEhQr6moq/IjsuKiC1wI4hb1C9dCvD40xPrEIEzsk/4JsLi4TVpV57XcaIwZQ==&quot;
            }
          ]
        },
        &quot;finishReason&quot;: &quot;STOP&quot;,
        &quot;citationMetadata&quot;: {
          &quot;citations&quot;: [
            {
              &quot;startIndex&quot;: 785,
              &quot;endIndex&quot;: 1106,
              &quot;uri&quot;: &quot;https://github.com/s-m-quadri/geca-labs&quot;
            }
          ]
        }
      }
    ],
    &quot;usageMetadata&quot;: {
      &quot;promptTokenCount&quot;: 32,
      &quot;candidatesTokenCount&quot;: 519,
      &quot;totalTokenCount&quot;: 887,
      &quot;trafficType&quot;: &quot;ON_DEMAND&quot;,
      &quot;promptTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 32
        }
      ],
      &quot;candidatesTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 519
        }
      ],
      &quot;thoughtsTokenCount&quot;: 336
    },
    &quot;modelVersion&quot;: &quot;gemini-3.8-flash&quot;,
    &quot;createTime&quot;: &quot;2026-09-02T16:35:51.064669Z&quot;,
    &quot;responseId&quot;: &quot;Z1CYap35A6-prb8Plfe7yAg&quot;,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-3.8-flash&#x27;,
  {
    contents: [
      {
        parts: [
          { text: &#x27;Write a Python function that merges two sorted lists into one sorted list.&#x27; },
        ],
        role: &#x27;user&#x27;,
      },
    ],
    generationConfig: { temperature: 0.2 },
    systemInstruction: {
      parts: [
        {
          text: &#x27;You are an expert software engineering agent. Write concise, correct, well-documented code.&#x27;,
        },
      ],
    },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/gemini-3.8-flash&quot;,
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;Write a Python function that merges two sorted lists into one sorted list.&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;generationConfig&quot;: {
      &quot;temperature&quot;: 0.2
    },
    &quot;systemInstruction&quot;: {
      &quot;parts&quot;: [
        {
          &quot;text&quot;: &quot;You are an expert software engineering agent. Write concise, correct, well-documented code.&quot;
        }
      ]
    }
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>contents</code></td><td>array</td><td>Required.</td></tr><tr><td><code>contents[].role</code></td><td>string</td><td>Values: user, model</td></tr><tr><td><code>contents[].parts</code></td><td>array</td><td>Required.</td></tr><tr><td><code>contents[].parts[].text</code></td><td>string</td><td></td></tr><tr><td><code>systemInstruction</code></td><td>object</td><td></td></tr><tr><td><code>systemInstruction.parts</code></td><td>array</td><td>Required.</td></tr><tr><td><code>systemInstruction.parts[].text</code></td><td>string</td><td></td></tr><tr><td><code>generationConfig</code></td><td>object</td><td></td></tr><tr><td><code>generationConfig.temperature</code></td><td>number</td><td></td></tr><tr><td><code>generationConfig.topP</code></td><td>number</td><td></td></tr><tr><td><code>generationConfig.topK</code></td><td>number</td><td></td></tr><tr><td><code>generationConfig.maxOutputTokens</code></td><td>number</td><td></td></tr><tr><td><code>generationConfig.candidateCount</code></td><td>number</td><td></td></tr><tr><td><code>generationConfig.stopSequences</code></td><td>array</td><td></td></tr><tr><td><code>generationConfig.responseMimeType</code></td><td>string</td><td></td></tr><tr><td><code>safetySettings</code></td><td>array</td><td></td></tr><tr><td><code>safetySettings[].category</code></td><td>string</td><td>Required.</td></tr><tr><td><code>safetySettings[].threshold</code></td><td>string</td><td>Required.</td></tr><tr><td><code>tools</code></td><td>array</td><td></td></tr><tr><td><code>toolConfig</code></td><td>object</td><td></td></tr><tr><td><code>messages</code></td><td>array</td><td>Required.</td></tr><tr><td><code>messages[].role</code></td><td>string</td><td>Required. Values: system, developer, user, assistant, tool</td></tr><tr><td><code>messages[].content</code></td><td>string or null or array</td><td></td></tr><tr><td><code>temperature</code></td><td>number</td><td>Minimum: 0; Maximum: 2</td></tr><tr><td><code>max_tokens</code></td><td>number</td><td></td></tr><tr><td><code>max_completion_tokens</code></td><td>number</td><td></td></tr><tr><td><code>top_p</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>frequency_penalty</code></td><td>number</td><td>Minimum: -2; Maximum: 2</td></tr><tr><td><code>presence_penalty</code></td><td>number</td><td>Minimum: -2; Maximum: 2</td></tr><tr><td><code>stream</code></td><td>boolean</td><td></td></tr><tr><td><code>stream_options</code></td><td>object</td><td></td></tr><tr><td><code>stream_options.include_usage</code></td><td>boolean</td><td></td></tr><tr><td><code>tools</code></td><td>array</td><td></td></tr><tr><td><code>tool_choice</code></td><td>object</td><td></td></tr><tr><td><code>response_format</code></td><td>object</td><td></td></tr><tr><td><code>modalities</code></td><td>array</td><td></td></tr><tr><td><code>audio</code></td><td>object</td><td></td></tr><tr><td><code>audio.voice</code></td><td>string</td><td>Values: alloy, ash, ballad, coral, echo, sage, shimmer, verse</td></tr><tr><td><code>audio.format</code></td><td>string</td><td>Values: wav, mp3, flac, opus, pcm16</td></tr><tr><td><code>reasoning_effort</code></td><td>['string', 'null']</td><td>Optional reasoning control; availability and accepted values are model-dependent.</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>candidates</code></td><td>array</td><td></td></tr><tr><td><code>usageMetadata</code></td><td>object</td><td></td></tr><tr><td><code>usageMetadata.promptTokenCount</code></td><td>number</td><td></td></tr><tr><td><code>usageMetadata.candidatesTokenCount</code></td><td>number</td><td></td></tr><tr><td><code>usageMetadata.totalTokenCount</code></td><td>number</td><td></td></tr><tr><td><code>modelVersion</code></td><td>string</td><td></td></tr><tr><td><code>id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>object</code></td><td>string</td><td>Required.</td></tr><tr><td><code>created</code></td><td>number</td><td>Required.</td></tr><tr><td><code>model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices</code></td><td>array</td><td>Required.</td></tr><tr><td><code>choices[].index</code></td><td>number</td><td>Required.</td></tr><tr><td><code>choices[].message</code></td><td>object</td><td>Required.</td></tr><tr><td><code>choices[].message.role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices[].message.content</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>choices[].message.tool_calls</code></td><td>array or null</td><td></td></tr><tr><td><code>choices[].message.audio</code></td><td>object or null</td><td></td></tr><tr><td><code>choices[].message.audio.id</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.data</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.expires_at</code></td><td>number</td><td></td></tr><tr><td><code>choices[].message.audio.transcript</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.id</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.data</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.expires_at</code></td><td>number</td><td></td></tr><tr><td><code>choices[].message.audio.transcript</code></td><td>string</td><td></td></tr><tr><td><code>choices[].finish_reason</code></td><td>['string', 'null']</td><td>Required.</td></tr><tr><td><code>usage</code></td><td>object</td><td></td></tr><tr><td><code>usage.prompt_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.completion_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.total_tokens</code></td><td>number</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/google/gemini-3.8-flash/schema-input.json)
- [Output schema](/ai/models/google/gemini-3.8-flash/schema-output.json)


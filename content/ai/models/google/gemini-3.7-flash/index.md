---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/google/gemini-3.7-flash/
  description: google/gemini-3.7-flash
  full_title: Gemini 3.7 Flash · Cloudflare AI docs
  head_html: <title>Gemini 3.7 Flash · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="google/gemini-3.7-flash"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/google/gemini-3.7-flash/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Gemini 3.7 Flash · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="google/gemini-3.7-flash"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/google/gemini-3.7-flash/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/google/gemini-3.7-flash/#page","headline":"Gemini 3.7 Flash \u00b7 Cloudflare AI docs","description":"google/gemini-3.7-flash","url":"https://developers.cloudflare.com/ai/models/google/gemini-3.7-flash/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/google/gemini-3.7-flash/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/google.svg" alt="Google logo" width="48" height="48">

<h1 id="gemini-3-7-flash">Gemini 3.7 Flash</h1>

<p><code>google/gemini-3.7-flash</code></p>

Gemini 3.7 Flash is a highly capable, natively multimodal reasoning model optimized for agentic workflows and real-world tasks.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Context window</th><td>1,048,576 tokens</td></tr>
<tr><th>Terms</th><td><a href="https://ai.google.dev/gemini-api/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 0.75, Output tokens (per 1M): 3.75, Cached input tokens (per 1M): 0.075</td></tr>
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
            &quot;text&quot;: &quot;What are the three laws of thermodynamics?&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ]
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;The **laws of thermodynamics** define fundamental physical quantities (like temperature, energy, and entropy) and describe how they behave under various circumstances. \n\nWhile there are historically **three** main laws, scientists later added a foundational law called the **Zeroth Law**. Here are all four, clearly explained:\n\n---\n\n### **1. The First Law (Law of Conservation of Energy)**\n&gt; **\&quot;Energy cannot be created or destroyed; it can only change forms.\&quot;**\n\n* **What it means:** The total amount of energy in an isolated system (like the universe) remains constant. When heat is added to a system, it either increases the system&#x27;s internal energy or does work on the surroundings.\n* **Equation:** $\\Delta U = Q - W$ \n  *(Change in internal energy = Heat added to the system $-$ Work done by the system)*\n* **Everyday Example:** A car engine converts the *chemical energy* stored in gasoline into *thermal energy* (heat) and *mechanical energy* (motion). No new energy is created.\n\n---\n\n### **2. The Second Law (Law of Entropy)**\n&gt; **\&quot;The entropy of an isolated system always increases over time.\&quot;**\n\n* **What it means:** Natural processes are irreversible. Heat will spontaneously flow from hotter objects to colder objects, but never the reverse on its own. **Entropy** is a measure of disorder or unusable energy; because some energy is always lost as heat in any transfer, the universe becomes increasingly disordered.\n* **Consequence:** It is impossible to build a machine that is 100% efficient (a perpetual motion machine).\n* **Everyday Example:** If you drop an ice cube into a cup of hot coffee, the heat moves from the coffee to the ice, melting it. You will never see a cup of warm coffee spontaneously separate into boiling coffee and an ice cube.\n\n---\n\n### **3. The Third Law (Absolute Zero)**\n&gt; **\&quot;The entropy of a pure crystalline substance approaches zero as the temperature approaches absolute zero.\&quot;**\n\n* **What it means:** **Absolute zero** (0 Kelvin, or $-273.15^\\circ\\text{C} / -459.67^\\circ\\text{F}$) is the point where all atomic motion stops. At this temperature, a perfect crystal would have zero disorder (zero entropy). \n* **Consequence:** It is physically impossible to cool any object down to absolute zero in a finite number of steps, though scientists can get within billionths of a degree close.\n\n---\n\n### *Bonus: The Zeroth Law (Thermal Equilibrium)*\n*(Formulated after the first two, but deemed so fundamental it was placed before them.)*\n\n&gt; **\&quot;If System A is in thermal equilibrium with System B, and System B is in thermal equilibrium with System C, then System A is also in thermal equilibrium with System C.\&quot;**\n\n* **What it means:** \&quot;Thermal equilibrium\&quot; simply means no heat flows between two objects because they are the same temperature. This law defines the concept of **temperature** and allows us to use **thermometers**.\n\n---\n\n### **A Common Memory Trick (Ginsberg\u2019s Analogy)**\nA humorous way physicists summarize the laws of thermodynamics:\n1. **First Law:** You can&#x27;t win; you can only break even (energy is conserved).\n2. **Second Law:** You can&#x27;t break even (entropy always increases, so energy is lost as unusable heat).\n3. **Third Law:** You can&#x27;t get out of the game (you can never reach absolute zero).&quot;
  },
  &quot;raw_response&quot;: {
    &quot;candidates&quot;: [
      {
        &quot;content&quot;: {
          &quot;role&quot;: &quot;model&quot;,
          &quot;parts&quot;: [
            {
              &quot;text&quot;: &quot;The **laws of thermodynamics** define fundamental physical quantities (like temperature, energy, and entropy) and describe how they behave under various circumstances. \n\nWhile there are historically **three** main laws, scientists later added a foundational law called the **Zeroth Law**. Here are all four, clearly explained:\n\n---\n\n### **1. The First Law (Law of Conservation of Energy)**\n&gt; **\&quot;Energy cannot be created or destroyed; it can only change forms.\&quot;**\n\n* **What it means:** The total amount of energy in an isolated system (like the universe) remains constant. When heat is added to a system, it either increases the system&#x27;s internal energy or does work on the surroundings.\n* **Equation:** $\\Delta U = Q - W$ \n  *(Change in internal energy = Heat added to the system $-$ Work done by the system)*\n* **Everyday Example:** A car engine converts the *chemical energy* stored in gasoline into *thermal energy* (heat) and *mechanical energy* (motion). No new energy is created.\n\n---\n\n### **2. The Second Law (Law of Entropy)**\n&gt; **\&quot;The entropy of an isolated system always increases over time.\&quot;**\n\n* **What it means:** Natural processes are irreversible. Heat will spontaneously flow from hotter objects to colder objects, but never the reverse on its own. **Entropy** is a measure of disorder or unusable energy; because some energy is always lost as heat in any transfer, the universe becomes increasingly disordered.\n* **Consequence:** It is impossible to build a machine that is 100% efficient (a perpetual motion machine).\n* **Everyday Example:** If you drop an ice cube into a cup of hot coffee, the heat moves from the coffee to the ice, melting it. You will never see a cup of warm coffee spontaneously separate into boiling coffee and an ice cube.\n\n---\n\n### **3. The Third Law (Absolute Zero)**\n&gt; **\&quot;The entropy of a pure crystalline substance approaches zero as the temperature approaches absolute zero.\&quot;**\n\n* **What it means:** **Absolute zero** (0 Kelvin, or $-273.15^\\circ\\text{C} / -459.67^\\circ\\text{F}$) is the point where all atomic motion stops. At this temperature, a perfect crystal would have zero disorder (zero entropy). \n* **Consequence:** It is physically impossible to cool any object down to absolute zero in a finite number of steps, though scientists can get within billionths of a degree close.\n\n---\n\n### *Bonus: The Zeroth Law (Thermal Equilibrium)*\n*(Formulated after the first two, but deemed so fundamental it was placed before them.)*\n\n&gt; **\&quot;If System A is in thermal equilibrium with System B, and System B is in thermal equilibrium with System C, then System A is also in thermal equilibrium with System C.\&quot;**\n\n* **What it means:** \&quot;Thermal equilibrium\&quot; simply means no heat flows between two objects because they are the same temperature. This law defines the concept of **temperature** and allows us to use **thermometers**.\n\n---\n\n### **A Common Memory Trick (Ginsberg\u2019s Analogy)**\nA humorous way physicists summarize the laws of thermodynamics:\n1. **First Law:** You can&#x27;t win; you can only break even (energy is conserved).\n2. **Second Law:** You can&#x27;t break even (entropy always increases, so energy is lost as unusable heat).\n3. **Third Law:** You can&#x27;t get out of the game (you can never reach absolute zero).&quot;,
              &quot;thoughtSignature&quot;: &quot;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&quot;
            }
          ]
        },
        &quot;finishReason&quot;: &quot;STOP&quot;
      }
    ],
    &quot;usageMetadata&quot;: {
      &quot;promptTokenCount&quot;: 8,
      &quot;candidatesTokenCount&quot;: 752,
      &quot;totalTokenCount&quot;: 1433,
      &quot;trafficType&quot;: &quot;ON_DEMAND&quot;,
      &quot;promptTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 8
        }
      ],
      &quot;candidatesTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 752
        }
      ],
      &quot;thoughtsTokenCount&quot;: 673
    },
    &quot;modelVersion&quot;: &quot;gemini-3.7-flash&quot;,
    &quot;createTime&quot;: &quot;2026-08-13T18:07:02.084997Z&quot;,
    &quot;responseId&quot;: &quot;xgd-aoWYBeumrb8Pht-PuQw&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-3.7-flash&#x27;,
  { contents: [{ parts: [{ text: &#x27;What are the three laws of thermodynamics?&#x27; }], role: &#x27;user&#x27; }] },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/gemini-3.7-flash&quot;,
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;What are the three laws of thermodynamics?&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ]
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>With System Instruction</strong>
<p>Using a system instruction to set an agentic coding persona</p>
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
    &quot;text&quot;: &quot;Here is a clean, efficient Python function using the two-pointer approach, running in $O(n + m)$ time and space complexity:\n\n```python\nfrom typing import TypeVar\n\nT = TypeVar(\&quot;T\&quot;)\n\n\ndef merge_sorted_lists(list1: list[T], list2: list[T]) -&gt; list[T]:\n    \&quot;\&quot;\&quot;Merges two pre-sorted lists into a single sorted list.\n\n    Args:\n        list1: A sorted list of elements.\n        list2: Another sorted list of elements (same comparable type).\n\n    Returns:\n        A new sorted list containing all elements from both lists.\n\n    Complexity:\n        Time: O(n + m) where n and m are lengths of list1 and list2.\n        Space: O(n + m) for the resulting merged list.\n    \&quot;\&quot;\&quot;\n    merged: list[T] = []\n    i, j = 0, 0\n    len1, len2 = len(list1), len(list2)\n\n    # Compare elements from both lists and append the smaller one\n    while i &lt; len1 and j &lt; len2:\n        if list1[i] &lt;= list2[j]:\n            merged.append(list1[i])\n            i += 1\n        else:\n            merged.append(list2[j])\n            j += 1\n\n    # Append any remaining elements\n    merged.extend(list1[i:])\n    merged.extend(list2[j:])\n\n    return merged\n\n\n# Example usage:\nif __name__ == \&quot;__main__\&quot;:\n    a = [1, 3, 5, 8]\n    b = [2, 4, 6, 7, 9, 10]\n    print(merge_sorted_lists(a, b))\n    # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n```\n\n### Alternative: Standard Library (`heapq.merge`)\nIf you prefer a built-in generator approach that handles large streams without loading everything into memory upfront:\n\n```python\nimport heapq\n\n\ndef merge_sorted_lists_lazy(list1: list, list2: list) -&gt; list:\n    return list(heapq.merge(list1, list2))\n```&quot;
  },
  &quot;raw_response&quot;: {
    &quot;candidates&quot;: [
      {
        &quot;content&quot;: {
          &quot;role&quot;: &quot;model&quot;,
          &quot;parts&quot;: [
            {
              &quot;text&quot;: &quot;Here is a clean, efficient Python function using the two-pointer approach, running in $O(n + m)$ time and space complexity:\n\n```python\nfrom typing import TypeVar\n\nT = TypeVar(\&quot;T\&quot;)\n\n\ndef merge_sorted_lists(list1: list[T], list2: list[T]) -&gt; list[T]:\n    \&quot;\&quot;\&quot;Merges two pre-sorted lists into a single sorted list.\n\n    Args:\n        list1: A sorted list of elements.\n        list2: Another sorted list of elements (same comparable type).\n\n    Returns:\n        A new sorted list containing all elements from both lists.\n\n    Complexity:\n        Time: O(n + m) where n and m are lengths of list1 and list2.\n        Space: O(n + m) for the resulting merged list.\n    \&quot;\&quot;\&quot;\n    merged: list[T] = []\n    i, j = 0, 0\n    len1, len2 = len(list1), len(list2)\n\n    # Compare elements from both lists and append the smaller one\n    while i &lt; len1 and j &lt; len2:\n        if list1[i] &lt;= list2[j]:\n            merged.append(list1[i])\n            i += 1\n        else:\n            merged.append(list2[j])\n            j += 1\n\n    # Append any remaining elements\n    merged.extend(list1[i:])\n    merged.extend(list2[j:])\n\n    return merged\n\n\n# Example usage:\nif __name__ == \&quot;__main__\&quot;:\n    a = [1, 3, 5, 8]\n    b = [2, 4, 6, 7, 9, 10]\n    print(merge_sorted_lists(a, b))\n    # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n```\n\n### Alternative: Standard Library (`heapq.merge`)\nIf you prefer a built-in generator approach that handles large streams without loading everything into memory upfront:\n\n```python\nimport heapq\n\n\ndef merge_sorted_lists_lazy(list1: list, list2: list) -&gt; list:\n    return list(heapq.merge(list1, list2))\n```&quot;,
              &quot;thoughtSignature&quot;: &quot;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&quot;
            }
          ]
        },
        &quot;finishReason&quot;: &quot;STOP&quot;
      }
    ],
    &quot;usageMetadata&quot;: {
      &quot;promptTokenCount&quot;: 32,
      &quot;candidatesTokenCount&quot;: 517,
      &quot;totalTokenCount&quot;: 1114,
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
          &quot;tokenCount&quot;: 517
        }
      ],
      &quot;thoughtsTokenCount&quot;: 565
    },
    &quot;modelVersion&quot;: &quot;gemini-3.7-flash&quot;,
    &quot;createTime&quot;: &quot;2026-08-13T19:07:35.820040Z&quot;,
    &quot;responseId&quot;: &quot;9xV-asiGMqyo3dAP3oHS-Qw&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-3.7-flash&#x27;,
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
  &quot;model&quot;: &quot;google/gemini-3.7-flash&quot;,
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

<section class="model-example"><strong>Multi-turn Conversation</strong>
<p>Continuing a multi-step coding conversation, typical of an agentic loop</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;I have a bug where my recursive fibonacci function is too slow for n=40.&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      },
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;That&#x27;s expected with naive recursion since it recomputes overlapping subproblems exponentially. You can fix it with memoization or an iterative approach. Which would you like to see?&quot;
          }
        ],
        &quot;role&quot;: &quot;model&quot;
      },
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;Show me the memoized version.&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;generationConfig&quot;: {
      &quot;maxOutputTokens&quot;: 2048
    }
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;Here is how to memoize the recursive Fibonacci function.\n\n### 1. Using a Dictionary / Cache (Explicit)\n\nYou store results of previous calculations in a dictionary and look them up before computing:\n\n```python\ndef fib(n, memo=None):\n    if memo is None:\n        memo = {}\n\n    # Check if already computed\n    if n in memo:\n        return memo[n]\n\n    # Base cases\n    if n &lt;= 0:\n        return 0\n    elif n == 1:\n        return 1\n\n    # Store result in memo dictionary\n    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)\n    return memo[n]\n\n\n# Test\nprint(fib(40))  # Returns 102334155 instantly\n```\n\n---\n\n### 2. Using Python&#x27;s Built-in `@lru_cache` (Idiomatic Python)\n\nPython has a built-in decorator that handles memoization automatically:\n\n```python\nfrom functools import lru_cache\n\n\n@lru_cache(maxsize=None)\ndef fib(n):\n    if n &lt;= 0:\n        return 0\n    elif n == 1:\n        return 1\n    return fib(n - 1) + fib(n - 2)\n\n\n# Test\nprint(fib(40))  # Returns 102334155 instantly\n```\n\n---\n\n### Why this fixes the issue:\n* **Naive recursion:** Time complexity is $O(2^n)$ because it recomputes identical values millions of times.\n* **Memoized recursion:** Time complexity drops to $O(n)$ because each Fibonacci number from $0$ to $n$ is calculated only once. Space complexity is $O(n)$ to store the cache and recursion stack.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;candidates&quot;: [
      {
        &quot;content&quot;: {
          &quot;role&quot;: &quot;model&quot;,
          &quot;parts&quot;: [
            {
              &quot;text&quot;: &quot;Here is how to memoize the recursive Fibonacci function.\n\n### 1. Using a Dictionary / Cache (Explicit)\n\nYou store results of previous calculations in a dictionary and look them up before computing:\n\n```python\ndef fib(n, memo=None):\n    if memo is None:\n        memo = {}\n\n    # Check if already computed\n    if n in memo:\n        return memo[n]\n\n    # Base cases\n    if n &lt;= 0:\n        return 0\n    elif n == 1:\n        return 1\n\n    # Store result in memo dictionary\n    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)\n    return memo[n]\n\n\n# Test\nprint(fib(40))  # Returns 102334155 instantly\n```\n\n---\n\n### 2. Using Python&#x27;s Built-in `@lru_cache` (Idiomatic Python)\n\nPython has a built-in decorator that handles memoization automatically:\n\n```python\nfrom functools import lru_cache\n\n\n@lru_cache(maxsize=None)\ndef fib(n):\n    if n &lt;= 0:\n        return 0\n    elif n == 1:\n        return 1\n    return fib(n - 1) + fib(n - 2)\n\n\n# Test\nprint(fib(40))  # Returns 102334155 instantly\n```\n\n---\n\n### Why this fixes the issue:\n* **Naive recursion:** Time complexity is $O(2^n)$ because it recomputes identical values millions of times.\n* **Memoized recursion:** Time complexity drops to $O(n)$ because each Fibonacci number from $0$ to $n$ is calculated only once. Space complexity is $O(n)$ to store the cache and recursion stack.&quot;,
              &quot;thoughtSignature&quot;: &quot;AY89a1+Wv/04SFz0MKQY8n+tFyT0cfnQ+6x5+vRQu2MbyVYQqMErpr6OvgnpAYufyK3yG/BXeedOilTz9V1KgVD1QWF0fywd6r7Yw6Hbfwl+RaCf+zGlEOeM7ZuqPAIjIrQEsfaYbR+THgipFCCvNuP//K5ObnatV7hRrDMt7pqltYwg5NWm/O+0H3YvLp55UZlztXfz8t91zLg4pJKMzutMMaupMh5AAHu/pe40KJg2Id/ZH9QCn0ZqrvwJA/vYoQjUNLmbHRQirXIF5W0o5w0yCF6HBkDHBRnu2OWUi7Ne4DIqAmJJYKv0ePurLSaDJLE09M5XS4WOyd7cSH3sBzVTfxYYRN5OeT5UUGZ16JjPcSc3eaT64u1Ng/erd2fT0NfSa5/P2cWGw9KvxOSsU/19OUoonpBQvhoMhioMg1aL2RyVI9ikxm8cl54JZJbmJpmR60vHsdXPFnBSGdG3DQ3MNv+HKZEr6kXQ1FliGJU8qXGcNOAMkgykbgunAecujeN/vpaC3SBNRdc7yMa6cT1T9FVL1l1Cuxx9OuWSQowkhoniTPsV22uOj6drYlKPU6AJJuhNjv/epFySrCJbB9F1rISGL4wYkAD6mDEmaT0rG15OxjEb97C/8OufUirZpcDDC1jR0sWj7FlS4KCQUsNzdhc5AJhLQPtA3IGgAZzDH3PHvQYhUo29VP6jMhOE5S3fmLa2TSiuKtoYwMaAIzkGdp0xKohPrVFtn9Zajb+7Y6I6TsA0WL7Pg/DTIiooTZBG+dGk49Tt6eFfW/ypKXDy9YErzQF6FTK/V9rgPHEpZdSVvFnOunGZ3I+o02B9esYSqSNQlaBI7Y0/5hpCfgf0Ap9G1sh1WMkuCL40d0jRevBbEZAKqrdG1Gr5whRbjNtWbD/Cx17clPpGT5K3dNq5NJY16xqzPwJyNgj7H9xgNFiJGh5xYzx4PBTN0NsgE1bK6t3BrPkWxG0vB7B4Flyj3HRzGHj43qkT2cRKEoNjsiTGIvvyBaa6QQOYZ5yu2hC6h7mpNntCeU5iaDtQA/NC010PqvELJpqmiGyYM9D9uazoHrelc5STEOyUH6Eei7cfhezFCB0ibUm795StAgZt4WvWpYXif4PMRc/gdsNoWZr9Wo0WhlCm4ivwwoiG71oPbzam8IRp+2PP8evgPm4AogOToIHUQMZFz2OnGXXX8E0I25wMe5D+q9zpLO+st7kOFLl1vITCPvDkjw==&quot;
            }
          ]
        },
        &quot;finishReason&quot;: &quot;STOP&quot;
      }
    ],
    &quot;usageMetadata&quot;: {
      &quot;promptTokenCount&quot;: 62,
      &quot;candidatesTokenCount&quot;: 412,
      &quot;totalTokenCount&quot;: 698,
      &quot;trafficType&quot;: &quot;ON_DEMAND&quot;,
      &quot;promptTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 62
        }
      ],
      &quot;candidatesTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 412
        }
      ],
      &quot;thoughtsTokenCount&quot;: 224
    },
    &quot;modelVersion&quot;: &quot;gemini-3.7-flash&quot;,
    &quot;createTime&quot;: &quot;2026-08-13T19:07:41.574572Z&quot;,
    &quot;responseId&quot;: &quot;_RV-auyII6ip3dAP16iw4Qw&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-3.7-flash&#x27;,
  {
    contents: [
      {
        parts: [{ text: &#x27;I have a bug where my recursive fibonacci function is too slow for n=40.&#x27; }],
        role: &#x27;user&#x27;,
      },
      {
        parts: [
          {
            text: &quot;That&#x27;s expected with naive recursion since it recomputes overlapping subproblems exponentially. You can fix it with memoization or an iterative approach. Which would you like to see?&quot;,
          },
        ],
        role: &#x27;model&#x27;,
      },
      { parts: [{ text: &#x27;Show me the memoized version.&#x27; }], role: &#x27;user&#x27; },
    ],
    generationConfig: { maxOutputTokens: 2048 },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/gemini-3.7-flash&quot;,
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;I have a bug where my recursive fibonacci function is too slow for n=40.&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      },
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;That&#x27;\&#x27;&#x27;s expected with naive recursion since it recomputes overlapping subproblems exponentially. You can fix it with memoization or an iterative approach. Which would you like to see?&quot;
          }
        ],
        &quot;role&quot;: &quot;model&quot;
      },
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;Show me the memoized version.&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;generationConfig&quot;: {
      &quot;maxOutputTokens&quot;: 2048
    }
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Spatial Reasoning</strong>
<p>Higher thinking budget for a spatial reasoning task</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;A cube is painted red on all faces, then cut into 27 equal smaller cubes. How many of the smaller cubes have exactly two red faces?&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;generationConfig&quot;: {
      &quot;maxOutputTokens&quot;: 4096
    }
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;To find the number of smaller cubes with **exactly two red faces**, we can analyze how the $3 \\times 3 \\times 3$ cube is structured:\n\n1. **Corner cubes (3 painted faces):** There are **8** corners in a cube.\n2. **Edge cubes (excluding corners, 2 painted faces):** A cube has 12 edges. With a $3 \\times 3 \\times 3$ cut, each edge has 1 middle cube with 2 painted faces:\n   $$\\text{Number of cubes} = 12 \\times (3 - 2) = 12$$\n3. **Face-center cubes (1 painted face):** There is 1 in the center of each of the 6 faces = **6**.\n4. **Interior cube (0 painted faces):** There is **1** cube completely inside.\n\n*(Check: $8 + 12 + 6 + 1 = 27$ total cubes)*\n\nTherefore, there are **12** smaller cubes with exactly two red faces.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;candidates&quot;: [
      {
        &quot;content&quot;: {
          &quot;role&quot;: &quot;model&quot;,
          &quot;parts&quot;: [
            {
              &quot;text&quot;: &quot;To find the number of smaller cubes with **exactly two red faces**, we can analyze how the $3 \\times 3 \\times 3$ cube is structured:\n\n1. **Corner cubes (3 painted faces):** There are **8** corners in a cube.\n2. **Edge cubes (excluding corners, 2 painted faces):** A cube has 12 edges. With a $3 \\times 3 \\times 3$ cut, each edge has 1 middle cube with 2 painted faces:\n   $$\\text{Number of cubes} = 12 \\times (3 - 2) = 12$$\n3. **Face-center cubes (1 painted face):** There is 1 in the center of each of the 6 faces = **6**.\n4. **Interior cube (0 painted faces):** There is **1** cube completely inside.\n\n*(Check: $8 + 12 + 6 + 1 = 27$ total cubes)*\n\nTherefore, there are **12** smaller cubes with exactly two red faces.&quot;,
              &quot;thoughtSignature&quot;: &quot;AY89a18GhPrAzwD4+OG6wmLOGj2YZE0gv9PY76IqT4vccoHQerNJubk8VCyX0atC0qHPy/28tlQG5WlMvbqfovvGqrSJeNHSVC6RoyKD7SMGVnSOw83d5XDYxirhMa5XgVbtEF6O5t03QYpIyB/ice00yWw9US/osp4NOYRDYTPA6uekMJkCjFH8lNuYP4RnEFmEXHyxBtnlrcXvB2fy9bWxZEw3ck69faKWfJF/Ia0oy27SOdIaQTzcczJum9F+AnjliMkpY4EdIm+5KvOwrZCgcz+QWfNGQBu9SOK9qalhHHiI7diBhU8f4Dans3S1a1A9jKV8mOelXtaNDOXOKSk45muOSxds5JF/wb/2XAdTpgLt2cLE/vOuF4c4WBA+vpV9lvwlHKGMklvwFz7kSwnVOLnxglQwQl9ykyfdcInHzlaWAzfzEu7tq/Zkmp67DBtN7ZeG/teVlPIqm63uwBrQT8MOWVB27Ah59QI57TzclfNs0scwjmTlzFIzrzEKx+uz4Z4ekistTu8yGW12Gk8ypl5HEwZnOS8JpRR/ln20XV95oMb27LA6qnnW71S5SUva8+PdQsRw3NmeIp1FDmjxmuLE43UBcsGn/rj8KymrDRHkC1PHyOU+6je4J+/fma44zwfp4G2YJOit3f8btPUVsjrXH011krTONlK47hfKp08WJO7nCVaw7+gphzRrUMugxl8g7D3kVd5uym1c+lQstrs+FaaXj1VZwM5UUX3p/6ex+gso45qJ+h1OFhmZeOHKF8KTUw86RMdtFC+r1ULthumOSJHmb0nkQKnBqqV7qXdzNVep0rwZHk6rfULTPUQ0XaKAy9dtk8YOeeX7ULaTOHRe044Q9EcZk5eFCF5ktauTBwOG4+7B3R84/TS6DYOKQZSdYukuAQpq9SzlNnZaa1DHc9YLPP0CyPkEJ6yyZjEN78TiLvb+eXW06pPNC/wXVUdx47dq6w8MI16w4CiA8e8r/C7sqKSkD2j0Ksufr+mAq5gwSgOMRQx8vR+SfWp+3i1RvkRHpONZGftNyBuXfPLq1t/Hk6Wci4xkE8k8grwopKdghzHBpknmkz9783YjkeIFQMcoruEgfvzpElGERWmXKg7UqrMaOhY/HNcZ4auUoj8mUMBj+ejiCV/v+YrO6y3TAifJPYJEn4tiV3smbXTIA+UpilF4POrVSoeJkNhb6EVOrDK/UsjP2NNKNclL6F19JurykzmBrQZZs8vVn5KWLxkBXkdkdGMAjtPRdtX9ggfr+hhTNjBYSpo2sxVDjNhOs977Aie8wsRBejfR3a+OUVwyK9PptIaRqpJVQ9YTu0iUe3PcWUSo6YH+6gsOVSRjFrqj+1Ayq0SXfKisu9hF2HOp/vC03Bx0Weqw6XqYMnNvDSjIKEWTImfuGJyx0MK0VS4bvQm/T7T3OmbGnSsqHPx83n10xw==&quot;
            }
          ]
        },
        &quot;finishReason&quot;: &quot;STOP&quot;
      }
    ],
    &quot;usageMetadata&quot;: {
      &quot;promptTokenCount&quot;: 31,
      &quot;candidatesTokenCount&quot;: 228,
      &quot;totalTokenCount&quot;: 602,
      &quot;trafficType&quot;: &quot;ON_DEMAND&quot;,
      &quot;promptTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 31
        }
      ],
      &quot;candidatesTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 228
        }
      ],
      &quot;thoughtsTokenCount&quot;: 343
    },
    &quot;modelVersion&quot;: &quot;gemini-3.7-flash&quot;,
    &quot;createTime&quot;: &quot;2026-08-13T19:07:45.456897Z&quot;,
    &quot;responseId&quot;: &quot;ARZ-asHxG6mp3dAP9fHcoQ0&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-3.7-flash&#x27;,
  {
    contents: [
      {
        parts: [
          {
            text: &#x27;A cube is painted red on all faces, then cut into 27 equal smaller cubes. How many of the smaller cubes have exactly two red faces?&#x27;,
          },
        ],
        role: &#x27;user&#x27;,
      },
    ],
    generationConfig: { maxOutputTokens: 4096 },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/gemini-3.7-flash&quot;,
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;A cube is painted red on all faces, then cut into 27 equal smaller cubes. How many of the smaller cubes have exactly two red faces?&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;generationConfig&quot;: {
      &quot;maxOutputTokens&quot;: 4096
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

- [Input schema](/ai/models/google/gemini-3.7-flash/schema-input.json)
- [Output schema](/ai/models/google/gemini-3.7-flash/schema-output.json)


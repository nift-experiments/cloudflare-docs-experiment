<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Typesafe logo" width="48" height="48">

<h1 id="jev">Jev</h1>

<p><code>typesafe/jev</code></p>

Jev is TypeSafe's structured evaluation model. It evaluates one state against typed Noul, Choice, and Score questions and returns calibrated answers with probabilities and confidence.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Context window</th><td>32,000 tokens</td></tr>
<tr><th>Terms</th><td><a href="https://docs.typesafe.ai/legal.md">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 0.042, Output tokens (per 1M): 0, Cached input tokens (per 1M): 0</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Evaluate urgency, team routing, and frustration together

<section class="model-example"><strong>Typed evaluation</strong>
<p>Evaluate urgency, team routing, and frustration together</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;state&quot;: &quot;Help! My payouts have been failing for 3 days.&quot;,
    &quot;questions&quot;: {
      &quot;is_urgent&quot;: {
        &quot;type&quot;: &quot;noul&quot;,
        &quot;instructions&quot;: &quot;Does this convey urgency?&quot;,
        &quot;criteria&quot;: {
          &quot;true&quot;: &quot;Explicitly time-sensitive&quot;,
          &quot;false&quot;: &quot;No urgency expressed&quot;
        }
      },
      &quot;department&quot;: {
        &quot;type&quot;: &quot;choice&quot;,
        &quot;instructions&quot;: &quot;Which team should handle this?&quot;,
        &quot;criteria&quot;: {
          &quot;billing&quot;: &quot;Payments, invoicing, refunds&quot;,
          &quot;technical&quot;: &quot;Bugs, outages, integrations&quot;,
          &quot;sales&quot;: &quot;Pricing, upgrades, new accounts&quot;
        }
      },
      &quot;frustration&quot;: {
        &quot;type&quot;: &quot;score&quot;,
        &quot;instructions&quot;: &quot;How frustrated is the customer?&quot;,
        &quot;criteria&quot;: [
          &quot;Calm&quot;,
          &quot;Frustrated&quot;,
          &quot;Very angry&quot;
        ]
      }
    }
  },
  &quot;output&quot;: {
    &quot;model&quot;: &quot;jev-1.13.0&quot;,
    &quot;answers&quot;: {
      &quot;is_urgent&quot;: {
        &quot;type&quot;: &quot;noul&quot;,
        &quot;noul&quot;: 0.95
      },
      &quot;department&quot;: {
        &quot;type&quot;: &quot;choice&quot;,
        &quot;choice&quot;: &quot;billing&quot;,
        &quot;confidence&quot;: 0.8,
        &quot;probabilities&quot;: {
          &quot;billing&quot;: 0.87,
          &quot;sales&quot;: 0,
          &quot;technical&quot;: 0.13
        }
      },
      &quot;frustration&quot;: {
        &quot;type&quot;: &quot;score&quot;,
        &quot;score&quot;: 1.04,
        &quot;confidence&quot;: 0.94,
        &quot;legend&quot;: {
          &quot;0&quot;: &quot;Calm&quot;,
          &quot;1&quot;: &quot;Frustrated&quot;,
          &quot;2&quot;: &quot;Very angry&quot;
        },
        &quot;probabilities&quot;: {
          &quot;0&quot;: 0,
          &quot;1&quot;: 0.96,
          &quot;2&quot;: 0.04
        }
      }
    },
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 426,
      &quot;output_tokens&quot;: 73
    }
  },
  &quot;raw_response&quot;: {
    &quot;model&quot;: &quot;jev-1.13.0&quot;,
    &quot;answers&quot;: {
      &quot;is_urgent&quot;: {
        &quot;type&quot;: &quot;noul&quot;,
        &quot;noul&quot;: 0.95
      },
      &quot;department&quot;: {
        &quot;type&quot;: &quot;choice&quot;,
        &quot;choice&quot;: &quot;billing&quot;,
        &quot;confidence&quot;: 0.8,
        &quot;probabilities&quot;: {
          &quot;billing&quot;: 0.87,
          &quot;sales&quot;: 0,
          &quot;technical&quot;: 0.13
        }
      },
      &quot;frustration&quot;: {
        &quot;type&quot;: &quot;score&quot;,
        &quot;score&quot;: 1.04,
        &quot;confidence&quot;: 0.94,
        &quot;legend&quot;: {
          &quot;0&quot;: &quot;Calm&quot;,
          &quot;1&quot;: &quot;Frustrated&quot;,
          &quot;2&quot;: &quot;Very angry&quot;
        },
        &quot;probabilities&quot;: {
          &quot;0&quot;: 0,
          &quot;1&quot;: 0.96,
          &quot;2&quot;: 0.04
        }
      }
    },
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 426,
      &quot;output_tokens&quot;: 73
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;typesafe/jev&#x27;,
  {
    state: &#x27;Help! My payouts have been failing for 3 days.&#x27;,
    questions: {
      is_urgent: {
        type: &#x27;noul&#x27;,
        instructions: &#x27;Does this convey urgency?&#x27;,
        criteria: { true: &#x27;Explicitly time-sensitive&#x27;, false: &#x27;No urgency expressed&#x27; },
      },
      department: {
        type: &#x27;choice&#x27;,
        instructions: &#x27;Which team should handle this?&#x27;,
        criteria: {
          billing: &#x27;Payments, invoicing, refunds&#x27;,
          technical: &#x27;Bugs, outages, integrations&#x27;,
          sales: &#x27;Pricing, upgrades, new accounts&#x27;,
        },
      },
      frustration: {
        type: &#x27;score&#x27;,
        instructions: &#x27;How frustrated is the customer?&#x27;,
        criteria: [&#x27;Calm&#x27;, &#x27;Frustrated&#x27;, &#x27;Very angry&#x27;],
      },
    },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;typesafe/jev&quot;,
  &quot;input&quot;: {
    &quot;state&quot;: &quot;Help! My payouts have been failing for 3 days.&quot;,
    &quot;questions&quot;: {
      &quot;is_urgent&quot;: {
        &quot;type&quot;: &quot;noul&quot;,
        &quot;instructions&quot;: &quot;Does this convey urgency?&quot;,
        &quot;criteria&quot;: {
          &quot;true&quot;: &quot;Explicitly time-sensitive&quot;,
          &quot;false&quot;: &quot;No urgency expressed&quot;
        }
      },
      &quot;department&quot;: {
        &quot;type&quot;: &quot;choice&quot;,
        &quot;instructions&quot;: &quot;Which team should handle this?&quot;,
        &quot;criteria&quot;: {
          &quot;billing&quot;: &quot;Payments, invoicing, refunds&quot;,
          &quot;technical&quot;: &quot;Bugs, outages, integrations&quot;,
          &quot;sales&quot;: &quot;Pricing, upgrades, new accounts&quot;
        }
      },
      &quot;frustration&quot;: {
        &quot;type&quot;: &quot;score&quot;,
        &quot;instructions&quot;: &quot;How frustrated is the customer?&quot;,
        &quot;criteria&quot;: [
          &quot;Calm&quot;,
          &quot;Frustrated&quot;,
          &quot;Very angry&quot;
        ]
      }
    }
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Structured refund review</strong>
<p>Evaluate a refund request against a structured order and policy</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;state&quot;: {
      &quot;ticket&quot;: {
        &quot;subject&quot;: &quot;Duplicate charge&quot;,
        &quot;message&quot;: &quot;I was charged twice for order A-104. Please refund the duplicate.&quot;
      },
      &quot;order&quot;: {
        &quot;id&quot;: &quot;A-104&quot;,
        &quot;charges&quot;: [
          {
            &quot;amount_usd&quot;: 49,
            &quot;status&quot;: &quot;captured&quot;
          },
          {
            &quot;amount_usd&quot;: 49,
            &quot;status&quot;: &quot;captured&quot;
          }
        ]
      },
      &quot;refund_policy&quot;: &quot;Duplicate charges are eligible for a refund.&quot;
    },
    &quot;questions&quot;: {
      &quot;refund_requested&quot;: {
        &quot;type&quot;: &quot;noul&quot;,
        &quot;instructions&quot;: &quot;Does `ticket.message` request a refund?&quot;
      },
      &quot;policy_supports_refund&quot;: {
        &quot;type&quot;: &quot;noul&quot;,
        &quot;instructions&quot;: &quot;Does `refund_policy` support the refund requested in `ticket.message`, given `order.charges`?&quot;
      }
    }
  },
  &quot;output&quot;: {
    &quot;model&quot;: &quot;jev-1.13.0&quot;,
    &quot;answers&quot;: {
      &quot;refund_requested&quot;: {
        &quot;type&quot;: &quot;noul&quot;,
        &quot;noul&quot;: 0.99
      },
      &quot;policy_supports_refund&quot;: {
        &quot;type&quot;: &quot;noul&quot;,
        &quot;noul&quot;: 0.98
      }
    },
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 422,
      &quot;output_tokens&quot;: 41
    }
  },
  &quot;raw_response&quot;: {
    &quot;model&quot;: &quot;jev-1.13.0&quot;,
    &quot;answers&quot;: {
      &quot;refund_requested&quot;: {
        &quot;type&quot;: &quot;noul&quot;,
        &quot;noul&quot;: 0.99
      },
      &quot;policy_supports_refund&quot;: {
        &quot;type&quot;: &quot;noul&quot;,
        &quot;noul&quot;: 0.98
      }
    },
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 422,
      &quot;output_tokens&quot;: 41
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;typesafe/jev&#x27;,
  {
    state: {
      ticket: {
        subject: &#x27;Duplicate charge&#x27;,
        message: &#x27;I was charged twice for order A-104. Please refund the duplicate.&#x27;,
      },
      order: {
        id: &#x27;A-104&#x27;,
        charges: [
          { amount_usd: 49, status: &#x27;captured&#x27; },
          { amount_usd: 49, status: &#x27;captured&#x27; },
        ],
      },
      refund_policy: &#x27;Duplicate charges are eligible for a refund.&#x27;,
    },
    questions: {
      refund_requested: { type: &#x27;noul&#x27;, instructions: &#x27;Does `ticket.message` request a refund?&#x27; },
      policy_supports_refund: {
        type: &#x27;noul&#x27;,
        instructions:
          &#x27;Does `refund_policy` support the refund requested in `ticket.message`, given `order.charges`?&#x27;,
      },
    },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;typesafe/jev&quot;,
  &quot;input&quot;: {
    &quot;state&quot;: {
      &quot;ticket&quot;: {
        &quot;subject&quot;: &quot;Duplicate charge&quot;,
        &quot;message&quot;: &quot;I was charged twice for order A-104. Please refund the duplicate.&quot;
      },
      &quot;order&quot;: {
        &quot;id&quot;: &quot;A-104&quot;,
        &quot;charges&quot;: [
          {
            &quot;amount_usd&quot;: 49,
            &quot;status&quot;: &quot;captured&quot;
          },
          {
            &quot;amount_usd&quot;: 49,
            &quot;status&quot;: &quot;captured&quot;
          }
        ]
      },
      &quot;refund_policy&quot;: &quot;Duplicate charges are eligible for a refund.&quot;
    },
    &quot;questions&quot;: {
      &quot;refund_requested&quot;: {
        &quot;type&quot;: &quot;noul&quot;,
        &quot;instructions&quot;: &quot;Does `ticket.message` request a refund?&quot;
      },
      &quot;policy_supports_refund&quot;: {
        &quot;type&quot;: &quot;noul&quot;,
        &quot;instructions&quot;: &quot;Does `refund_policy` support the refund requested in `ticket.message`, given `order.charges`?&quot;
      }
    }
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Support department routing</strong>
<p>Route a support request to the right department</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;state&quot;: &quot;I cannot log in after changing my password, and the reset email never arrives.&quot;,
    &quot;questions&quot;: {
      &quot;department&quot;: {
        &quot;type&quot;: &quot;choice&quot;,
        &quot;instructions&quot;: &quot;Which team should handle this support request?&quot;,
        &quot;criteria&quot;: {
          &quot;account&quot;: &quot;Login, password, profile, or security issues&quot;,
          &quot;billing&quot;: &quot;Charges, invoices, refunds, or subscriptions&quot;,
          &quot;technical&quot;: &quot;Product bugs, outages, or integrations&quot;,
          &quot;other&quot;: &quot;Requests that do not fit the other departments&quot;
        }
      }
    }
  },
  &quot;output&quot;: {
    &quot;model&quot;: &quot;jev-1.13.0&quot;,
    &quot;answers&quot;: {
      &quot;department&quot;: {
        &quot;type&quot;: &quot;choice&quot;,
        &quot;choice&quot;: &quot;account&quot;,
        &quot;confidence&quot;: 1,
        &quot;probabilities&quot;: {
          &quot;technical&quot;: 0,
          &quot;billing&quot;: 0,
          &quot;account&quot;: 1,
          &quot;other&quot;: 0
        }
      }
    },
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 380,
      &quot;output_tokens&quot;: 45
    }
  },
  &quot;raw_response&quot;: {
    &quot;model&quot;: &quot;jev-1.13.0&quot;,
    &quot;answers&quot;: {
      &quot;department&quot;: {
        &quot;type&quot;: &quot;choice&quot;,
        &quot;choice&quot;: &quot;account&quot;,
        &quot;confidence&quot;: 1,
        &quot;probabilities&quot;: {
          &quot;technical&quot;: 0,
          &quot;billing&quot;: 0,
          &quot;account&quot;: 1,
          &quot;other&quot;: 0
        }
      }
    },
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 380,
      &quot;output_tokens&quot;: 45
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;typesafe/jev&#x27;,
  {
    state: &#x27;I cannot log in after changing my password, and the reset email never arrives.&#x27;,
    questions: {
      department: {
        type: &#x27;choice&#x27;,
        instructions: &#x27;Which team should handle this support request?&#x27;,
        criteria: {
          account: &#x27;Login, password, profile, or security issues&#x27;,
          billing: &#x27;Charges, invoices, refunds, or subscriptions&#x27;,
          technical: &#x27;Product bugs, outages, or integrations&#x27;,
          other: &#x27;Requests that do not fit the other departments&#x27;,
        },
      },
    },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;typesafe/jev&quot;,
  &quot;input&quot;: {
    &quot;state&quot;: &quot;I cannot log in after changing my password, and the reset email never arrives.&quot;,
    &quot;questions&quot;: {
      &quot;department&quot;: {
        &quot;type&quot;: &quot;choice&quot;,
        &quot;instructions&quot;: &quot;Which team should handle this support request?&quot;,
        &quot;criteria&quot;: {
          &quot;account&quot;: &quot;Login, password, profile, or security issues&quot;,
          &quot;billing&quot;: &quot;Charges, invoices, refunds, or subscriptions&quot;,
          &quot;technical&quot;: &quot;Product bugs, outages, or integrations&quot;,
          &quot;other&quot;: &quot;Requests that do not fit the other departments&quot;
        }
      }
    }
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Account risk assessment</strong>
<p>Score account risk and determine whether escalation is needed</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;state&quot;: {
      &quot;account_age_days&quot;: 12,
      &quot;recent_events&quot;: [
        &quot;Five failed login attempts&quot;,
        &quot;Password reset requested from a new country&quot;,
        &quot;Successful login from the usual device&quot;
      ],
      &quot;account_verified&quot;: true
    },
    &quot;questions&quot;: {
      &quot;risk_level&quot;: {
        &quot;type&quot;: &quot;score&quot;,
        &quot;instructions&quot;: &quot;How risky does this account activity appear?&quot;,
        &quot;criteria&quot;: [
          &quot;Low risk: activity is consistent with the account history&quot;,
          &quot;Moderate risk: some unusual activity needs monitoring&quot;,
          &quot;High risk: multiple strong indicators of account compromise&quot;
        ]
      },
      &quot;escalate&quot;: {
        &quot;type&quot;: &quot;noul&quot;,
        &quot;instructions&quot;: &quot;Should this account be escalated for manual security review?&quot;,
        &quot;criteria&quot;: {
          &quot;true&quot;: &quot;The activity warrants immediate human review&quot;,
          &quot;false&quot;: &quot;The activity can be handled with normal automated controls&quot;
        }
      }
    }
  },
  &quot;output&quot;: {
    &quot;model&quot;: &quot;jev-1.13.0&quot;,
    &quot;answers&quot;: {
      &quot;risk_level&quot;: {
        &quot;type&quot;: &quot;score&quot;,
        &quot;score&quot;: 1.84,
        &quot;confidence&quot;: 0.77,
        &quot;legend&quot;: {
          &quot;0&quot;: &quot;Low risk: activity is consistent with the account history&quot;,
          &quot;1&quot;: &quot;Moderate risk: some unusual activity needs monitoring&quot;,
          &quot;2&quot;: &quot;High risk: multiple strong indicators of account compromise&quot;
        },
        &quot;probabilities&quot;: {
          &quot;0&quot;: 0,
          &quot;1&quot;: 0.16,
          &quot;2&quot;: 0.84
        }
      },
      &quot;escalate&quot;: {
        &quot;type&quot;: &quot;noul&quot;,
        &quot;noul&quot;: 0.81
      }
    },
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 421,
      &quot;output_tokens&quot;: 36
    }
  },
  &quot;raw_response&quot;: {
    &quot;model&quot;: &quot;jev-1.13.0&quot;,
    &quot;answers&quot;: {
      &quot;risk_level&quot;: {
        &quot;type&quot;: &quot;score&quot;,
        &quot;score&quot;: 1.84,
        &quot;confidence&quot;: 0.77,
        &quot;legend&quot;: {
          &quot;0&quot;: &quot;Low risk: activity is consistent with the account history&quot;,
          &quot;1&quot;: &quot;Moderate risk: some unusual activity needs monitoring&quot;,
          &quot;2&quot;: &quot;High risk: multiple strong indicators of account compromise&quot;
        },
        &quot;probabilities&quot;: {
          &quot;0&quot;: 0,
          &quot;1&quot;: 0.16,
          &quot;2&quot;: 0.84
        }
      },
      &quot;escalate&quot;: {
        &quot;type&quot;: &quot;noul&quot;,
        &quot;noul&quot;: 0.81
      }
    },
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 421,
      &quot;output_tokens&quot;: 36
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;typesafe/jev&#x27;,
  {
    state: {
      account_age_days: 12,
      recent_events: [
        &#x27;Five failed login attempts&#x27;,
        &#x27;Password reset requested from a new country&#x27;,
        &#x27;Successful login from the usual device&#x27;,
      ],
      account_verified: true,
    },
    questions: {
      risk_level: {
        type: &#x27;score&#x27;,
        instructions: &#x27;How risky does this account activity appear?&#x27;,
        criteria: [
          &#x27;Low risk: activity is consistent with the account history&#x27;,
          &#x27;Moderate risk: some unusual activity needs monitoring&#x27;,
          &#x27;High risk: multiple strong indicators of account compromise&#x27;,
        ],
      },
      escalate: {
        type: &#x27;noul&#x27;,
        instructions: &#x27;Should this account be escalated for manual security review?&#x27;,
        criteria: {
          true: &#x27;The activity warrants immediate human review&#x27;,
          false: &#x27;The activity can be handled with normal automated controls&#x27;,
        },
      },
    },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;typesafe/jev&quot;,
  &quot;input&quot;: {
    &quot;state&quot;: {
      &quot;account_age_days&quot;: 12,
      &quot;recent_events&quot;: [
        &quot;Five failed login attempts&quot;,
        &quot;Password reset requested from a new country&quot;,
        &quot;Successful login from the usual device&quot;
      ],
      &quot;account_verified&quot;: true
    },
    &quot;questions&quot;: {
      &quot;risk_level&quot;: {
        &quot;type&quot;: &quot;score&quot;,
        &quot;instructions&quot;: &quot;How risky does this account activity appear?&quot;,
        &quot;criteria&quot;: [
          &quot;Low risk: activity is consistent with the account history&quot;,
          &quot;Moderate risk: some unusual activity needs monitoring&quot;,
          &quot;High risk: multiple strong indicators of account compromise&quot;
        ]
      },
      &quot;escalate&quot;: {
        &quot;type&quot;: &quot;noul&quot;,
        &quot;instructions&quot;: &quot;Should this account be escalated for manual security review?&quot;,
        &quot;criteria&quot;: {
          &quot;true&quot;: &quot;The activity warrants immediate human review&quot;,
          &quot;false&quot;: &quot;The activity can be handled with normal automated controls&quot;
        }
      }
    }
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>state</code></td><td>string or object or array or null</td><td>Required.</td></tr><tr><td><code>questions</code></td><td>object</td><td>Required.</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>model</code></td><td>string</td><td>Required. Minimum length: 1</td></tr><tr><td><code>answers</code></td><td>object</td><td>Required.</td></tr><tr><td><code>usage</code></td><td>object</td><td>Required.</td></tr><tr><td><code>usage.input_tokens</code></td><td>integer</td><td>Required. Minimum: 0; Maximum: 9007199254740991</td></tr><tr><td><code>usage.output_tokens</code></td><td>integer</td><td>Required. Minimum: 0; Maximum: 9007199254740991</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/typesafe/jev/schema-input.json)
- [Output schema](/ai/models/typesafe/jev/schema-output.json)


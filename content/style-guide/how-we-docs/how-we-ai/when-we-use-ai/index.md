---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/how-we-docs/how-we-ai/when-we-use-ai/
  description: Determine when AI aids documentation tasks.
  full_title: When we use AI · Cloudflare Style Guide
  head_html: <title>When we use AI · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Determine when AI aids documentation tasks."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/how-we-docs/how-we-ai/when-we-use-ai/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/how-we-docs/how-we-ai/when-we-use-ai/index.md"><meta property="og:title" content="When we use AI · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Determine when AI aids documentation tasks."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/how-we-docs/how-we-ai/when-we-use-ai/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/how-we-docs/how-we-ai/when-we-use-ai/#page","headline":"When we use AI \u00b7 Cloudflare Style Guide","description":"Determine when AI aids documentation tasks.","url":"https://developers.cloudflare.com/style-guide/how-we-docs/how-we-ai/when-we-use-ai/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/how-we-docs/how-we-ai/when-we-use-ai/
  schema: 1
---
<h2 id="our-core-principles-for-using-ai">Our core principles for using AI</h2>
<p>AI is a powerful tool, but it is not a cure-all. Its success depends heavily on the use case. Knowing its strengths and weaknesses is key to using AI appropriately.</p>
<p>When deciding whether to use AI for a task, use these principles as your guide:</p>
<ol>
<li><strong>The feedback loop is critical:</strong> The single most important factor for success is the feedback loop. How quickly and easily can you test the output and correct for hallucinations? Code and scripts are far easier to test for correctness than subjective content.</li>
<li><strong>Prioritize additive tasks:</strong> AI is generally better for additive tasks, like new things you could not or would not do before, as opposed to operational tasks that are required to keep the business running.</li>
</ol>
<h3 id="how-to-decide-when-to-use-ai">How to decide when to use AI</h3>
<p>We ask ourselves a few questions before we look to AI to solve a problem or streamline a process:</p>
<ul>
<li>Is this a manual, repetitive chore?</li>
<li>Will this task take hours, days, or weeks to complete manually?</li>
<li>Will we need to complete the <em>exact</em> same action over and over again?</li>
<li>Is there a clear logic we can apply to successfully identify or perform the action?</li>
<li>Will this be scalable or useful for others to also use?</li>
</ul>
<p>If we can say <code>yes</code> to these questions, it is a strong candidate for an AI-based solution. If we say <code>no</code> or <code>I do not know</code> to any of them, we first pursue the current process and look for smaller, specific areas where AI could still be helpful.</p>
<h3 id="recommended-use-cases-what-has-worked-for-us">Recommended use cases: What has worked for us</h3>
<p>These are areas where we have found AI to be unequivocally positive and effective.</p>
<h4 id="local-scripts-and-tooling">Local scripts and tooling</h4>
<p>This is the most positive and recommended use case for AI.</p>
<ul>
<li><strong>Why it works:</strong> AI is at its best when you can easily &quot;test&quot; for hallucinations, and code is highly testable.</li>
<li><strong>What to use it for:</strong>
<ul>
<li>Writing local scripts (like Vibecoding scripts) to automate updates in our docs.</li>
<li>Generating simple docs components.</li>
<li>Creating GitHub Actions.</li>
<li>Assisting with competitive doc analyses.</li>
</ul>
</li>
<li><strong>Key benefit:</strong> You own the resulting code. It is stable and will not change, regardless of future changes to AI models or pricing.</li>
</ul>
<h4 id="ai-powered-ides">AI-powered IDEs</h4>
<p>For teams using a docs-as-code approach, AI chat integrated into an IDE, like Windsurf, Cursor, etc., is highly effective for making multiple, streamlined changes.</p>
<ul>
<li><strong>Why it works:</strong>
<ul>
<li>The AI can understand a large amount of context from your codebase, or docs in this case.</li>
<li>The feedback loop for spotting and fixing hallucinations is very short.</li>
<li>Git integration makes it easy to find, review, and remove hallucinations.</li>
</ul>
</li>
<li><strong>Key benefit:</strong> This can save days, if not weeks, of work. For massive documentation updates that require completing the same task repeatedly, AI-enabled IDEs can significantly streamline the process.</li>
<li><strong>Caveat:</strong> Always consider simpler solutions (like regex) first, as they are often better, faster, and cheaper. Use AI when you need to brute-force a large task or navigate high complexity.</li>
</ul>
<h3 id="still-figuring-it-out-what-we-are-optimistic-about-but-getting-mixed-results">Still figuring it out: What we are optimistic about but getting mixed results</h3>
<p>These are areas that show promise but require careful implementation.</p>
<h4 id="ai-for-initial-drafts">AI for initial drafts</h4>
<p>We are optimistic about asking stakeholders to use AI to create <em>initial drafts</em> of documentation before handing them off to the technical writing team.</p>
<ul>
<li><strong>Key value:</strong> The quality of the AI-generated draft itself is often mixed. The primary value is that it acts as a forcing function for the stakeholder to think about documentation as part of their product – not separate from their product – while also sharing key information to the technical writing team as quickly as possible for our busy stakeholders.</li>
<li><strong>Why?</strong> To create a draft, the requester must gather all the necessary background information first. Receiving this information upfront is a significant win for the technical writing team.</li>
<li><strong>Action:</strong> See our <a href="/style-guide/how-we-docs/how-we-ai/prompt-templates/">prompt templates</a> for more information on structuring these requests.</li>
</ul>
<h4 id="customer-facing-chatbots">Customer-facing chatbots</h4>
<p>Our experience with customer-facing chatbots has been mixed.</p>
<ul>
<li><strong>Pros:</strong> Occasionally, it provides a great answer.</li>
<li><strong>Cons:</strong> To prevent hallucinations, bots are often made more &quot;confident.&quot; This leads them to refuse to answer (for example, &quot;I don't know&quot;), which users dislike. On the flipside, users also dislike hallucinations. So, be mindful of the actual user experience and come up with a method for tracking user engagement and success with your documentation chatbot. Depending on the results, you may be able to identify worthwhile documentation gaps to fill, which prevent hallucinations in the future.</li>
<li><strong>Alternative:</strong> At the moment, we are much more optimistic about the potential of AI-powered search and similarity scores. These feel more in our control. However, we are still testing and tracking how our docs can positively influence chatbot experiences at Cloudflare and via third-party apps.</li>
</ul>
<h3 id="not-recommended-what-has-not-worked-for-us-yet">Not recommended: What has not worked for us yet</h3>
<p>Based on our experience, we do not recommend the following use case at this time.</p>
<h4 id="automated-content-editors-bots">Automated content editors (bots)</h4>
<p>We have not found success with bots that automatically suggest content changes (for example, grammar, formatting) via pull requests.</p>
<ul>
<li><strong>Why it failed:</strong>
<ul>
<li><strong>Slow feedback loop:</strong> The GitHub PR context makes the feedback loop for correcting hallucinations very slow and difficult.</li>
<li><strong>Low engagement:</strong> We found that even our own team often closed or ignored the PRs because they were too much effort to verify.</li>
<li><strong>Contributor confusion:</strong> A similar bot used to flag issues on <em>incoming</em> PRs frustrated and confused contributors, and its suggestions were often hallucinations.</li>
</ul>
</li>
</ul>

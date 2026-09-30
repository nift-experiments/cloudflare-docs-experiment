<p>At Cloudflare, we believe that high-quality, customer-facing content is a critical part of the user experience. But as teams scale, maintaining a consistent voice, tone, and terminology across thousands of UI strings, error messages, and API descriptions becomes a monumental challenge. Traditional style guides and glossaries are essential, but they are static. They cannot provide real-time feedback or help us <em>measure</em> content quality.</p>
<p>To solve this, we built CLUE: Content Legibility for User Ease. CLUE is an internal tool that functions as a personal writing assistant for everyone at Cloudflare. It empowers anyone, from engineers to product managers, to feel confident in their content creation.</p>
<p>When a stakeholder shares content with CLUE, it provides a score and actionable recommendations. This simple feedback loop is a powerful mechanism for measuring and improving our content over time.</p>
<h2 id="the-goal-quantifying-good-content">The goal: Quantifying &quot;good content&quot;</h2>
<p>The core challenge CLUE addresses is that &quot;good&quot; content is easy to recognize but hard to measure. We know that effective copy uses an active voice, has an action-led structure, and removes unnecessary words, but how do you quantify that improvement at scale?</p>
<p>Our answer was <strong>content scorecards</strong>. Scorecards are a scalable evaluation tool that creates consistency. They allow us to assign measurable value to the elements that define &quot;good content,&quot; focusing on the criteria most critical for user success, satisfaction, and understanding.</p>
<p>The user flow is designed to be straightforward: you select your content type, enter your content, and CLUE provides instant feedback. It supports a wide range of critical content, including:</p>
<ul>
<li>General UI content and page descriptions</li>
<li>Error messages</li>
<li>API endpoint and parameter descriptions</li>
<li>Customer-facing emails</li>
</ul>
<h2 id="how-it-is-built-a-hybrid-model-driven-approach">How it is built: A hybrid, model-driven approach</h2>
<p>CLUE was truly built by Cloudflare, for Cloudflare, on Cloudflare. The application itself is built on Cloudflare Pages and protected by Cloudflare Access.</p>
<p>We adopted a model-driven approach for content evaluation, which provides a systematic, data-driven, and consistent assessment, removing the subjectivity of manual reviews. This model allows us to assess content in seconds, handle complex criteria like readability, and weight criteria based on what we find to be most critical for users.</p>
<p>Critically, CLUE is not just one thing, it is a hybrid solution of AI and traditional checks. This combination allows us to evaluate context while still having the granular control needed for some elements of our style guide.</p>
<h2 id="the-workflow-using-clue-as-an-llm-copy-editor">The workflow: Using CLUE as an LLM copy editor</h2>
<p>The rise of Generative AI and LLMs, like Gemini, has been a boon for generating text quickly. However, an LLM does not inherently understand or apply Cloudflare's specific content guidelines, voice, and tone.</p>
<p>This is where CLUE's role becomes essential. CLUE is not designed to <em>write</em> content for you; it is designed to make sure the content you <em>do</em> write meets our standards.</p>
<p>Think of CLUE as a specialized copy editor. It ensures that any piece of content — whether human-generated or created with an LLM's help — is ready for our users. This pairing is incredibly powerful:</p>
<ul>
<li><strong>Generate:</strong> A stakeholder uses an LLM to quickly draft initial versions of API descriptions or an error message.</li>
<li><strong>Refine:</strong> They paste that LLM-generated content into CLUE.</li>
<li><strong>Iterate:</strong> CLUE provides targeted tips on how to better meet Cloudflare's glossary, style guide, voice, tone, and UX best practices, turning a generic draft into a polished, effective piece of content.</li>
</ul>
<p>This democratizes UX writing, improves our efficiency by reducing manual reviews, and ultimately builds user trust through a consistent, high-quality experience. It helps users learn our products faster and resolve issues more efficiently, which is our ultimate goal.</p>

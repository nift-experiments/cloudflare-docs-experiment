---
cp9:
  canonical: https://developers.cloudflare.com/analytics/sampling/
  description: Understand how Cloudflare uses sampling for analytics.
  full_title: Understanding sampling in Cloudflare Analytics · Cloudflare Analytics docs
  head_html: <title>Understanding sampling in Cloudflare Analytics · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand how Cloudflare uses sampling for analytics."><link rel="canonical" href="https://developers.cloudflare.com/analytics/sampling/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/sampling/index.md"><meta property="og:title" content="Understanding sampling in Cloudflare Analytics · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand how Cloudflare uses sampling for analytics."><meta property="og:url" content="https://developers.cloudflare.com/analytics/sampling/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Analytics"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/sampling/#page","headline":"Understanding sampling in Cloudflare Analytics \u00b7 Cloudflare Analytics docs","description":"Understand how Cloudflare uses sampling for analytics.","url":"https://developers.cloudflare.com/analytics/sampling/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/sampling/
  schema: 1
---
<p><a href="https://en.wikipedia.org/wiki/Sampling_(statistics)">Sampling</a> is a technique used in analytics to analyze a subset of data rather than processing every individual data point. In Cloudflare Analytics, sampling ensures efficient performance and scalability while maintaining high accuracy and reliability. This document provides a comprehensive overview of how sampling works, why it is used, and its impact on analytics across different Cloudflare tools.</p>
<h2 id="how-sampling-works">How sampling works</h2>
<p>We use a sampling method called <a href="https://blog.cloudflare.com/explaining-cloudflares-abr-analytics/">Adaptive Bit Rate (ABR)</a> to ensure that queries complete quickly, even when working with large datasets. ABR dynamically adjusts the level of detail in the data retrieved based on query complexity and duration. This approach ensures fairness by preventing large or complex queries from consuming a disproportionate amount of computing resources, which could otherwise slow down or block smaller queries. By distributing resources more equitably, ABR allows the system to maintain consistent performance for all users, regardless of the dataset size.</p>
<p>To make this possible, data is stored at multiple resolutions (100%, 10%, 1%), each representing different sampling percentages. When a query is run, ABR selects the best resolution based on the query's complexity and number of rows to retrieve. By dynamically adjusting the data resolution, ABR optimizes performance and prevents delays. This sets it apart from systems that struggle with timeouts, errors, or high costs when dealing with large datasets.</p>
<h2 id="why-sampling-is-applied">Why sampling is applied</h2>
<p>Cloudflare's data pipeline handles <a href="https://blog.cloudflare.com/how-we-make-sense-of-too-much-data">over 700 million events per second</a> (and growing) across its global network. Processing and storing all this data in real-time would be prohibitively expensive and time-consuming. By leveraging carefully designed sampling methods, Cloudflare Analytics delivers accurate and actionable data, balancing precision with performance.</p>
<p>Sampling enables:</p>
<ul>
<li><strong>Scalability</strong>: Reduces the volume of data processed without compromising insights.</li>
<li><strong>Performance</strong>: Speeds up query execution for analytics.</li>
<li><strong>Cost-Efficiency</strong>: Minimizes resource usage and storage needs.</li>
</ul>
<h2 id="can-i-trust-sampled-data">Can I trust sampled data?</h2>
<p>Sampled data is highly reliable, and can provide insights that are as dependable as those derived from full datasets. Cloudflare designs sampling techniques to ensure we capture the essential characteristics of the entire dataset, delivering results you can trust.</p>
<p>Sampling is an approach similarly used in other domains, for instance:</p>
<ul>
<li>
<p>Google Maps: Just as online maps display lower-resolution images when zoomed out and higher-resolution images when zoomed in — keeping the total number of pixels relatively constant — Cloudflare Analytics dynamically adjusts sampling rates to efficiently provide insights, ensuring queries return consistent and accurate results regardless of dataset size.</p>
</li>
<li>
<p>Opinion Polls: Similar to how pollsters sample a subset of the population to predict election outcomes, Cloudflare samples a portion of your data to provide accurate, system-wide insights.</p>
</li>
<li>
<p>Movie Frames: Watching a movie at 30 frames per second (fps) instead of 60 fps does not change the overall experience, much like how analyzing fewer data points still reveals the same patterns and trends in your analytics dataset.</p>
</li>
</ul>
<p>We acknowledge it can be challenging to verify the exact resolution of ABR query results at this time. However, as a general rule, you can check the number of rows read. A higher number of rows read will result in higher resolution results. For example, results based on thousands of rows are highly likely to be representative, while those based on just a few rows may not be as reliable.</p>
<p>In the near future, we plan to expose confidence intervals along with query results, so you can see precisely how accurate your results are.</p>
<h2 id="additional-considerations">Additional considerations</h2>
<p><strong>When sampling occurs</strong></p>
<ul>
<li>Sampling is typically applied to very high-traffic datasets where full data analysis would be impractical.</li>
<li>For smaller datasets, full data analysis is often performed without sampling.</li>
</ul>
<p><strong>Sampling rates</strong></p>
<ul>
<li>Sampling rates vary depending on the dataset and product.</li>
<li>Cloudflare ensures that sampling rates are consistent within a single dataset to maintain accuracy across queries.</li>
</ul>
<p><strong>Impact on metrics</strong></p>
<ul>
<li>While sampling reduces the volume of processed data, aggregated metrics like totals, averages, and percentiles are extrapolated based on the sample size. This ensures the reported metrics represent the entire dataset accurately.</li>
</ul>
<p><strong>Limitations</strong></p>
<ul>
<li>Sampling may not capture extremely rare events with very low occurrence rates.</li>
</ul>
<p><strong>Sampling in analytics interfaces</strong></p>
<ul>
<li>GraphQL API: Sampling metadata is included in the query response. For more information, refer to the sampling <a href="/analytics/graphql-api/sampling/">GraphQL Analytics API</a> documentation.</li>
<li>Workers Analytics Engine: For more information, refer to the <a href="/analytics/analytics-engine/sampling/">Workers Analytics Engine</a> documentation.</li>
<li>Dashboard Analytics: Displays an icon with the sampled percentage of data, if sampled data was used for the visualization.</li>
</ul>

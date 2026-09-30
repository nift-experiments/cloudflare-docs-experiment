---
cp9:
  canonical: https://developers.cloudflare.com/china-network/concepts/icp/
  description: Obtain and display an ICP license number required for websites operating in China.
  full_title: Internet Content Provider (ICP) · Cloudflare China Network docs
  head_html: <title>Internet Content Provider (ICP) · Cloudflare China Network docs</title><meta name="generator" content="Nift"><meta name="description" content="Obtain and display an ICP license number required for websites operating in China."><link rel="canonical" href="https://developers.cloudflare.com/china-network/concepts/icp/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/china-network/concepts/icp/index.md"><meta property="og:title" content="Internet Content Provider (ICP) · Cloudflare China Network docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Obtain and display an ICP license number required for websites operating in China."><meta property="og:url" content="https://developers.cloudflare.com/china-network/concepts/icp/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="China Network"><meta name="algolia_product_filter" content="China Network"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="China Network"><meta name="pcx_tags" content="Compliance"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/china-network/concepts/icp/#page","headline":"Internet Content Provider (ICP) \u00b7 Cloudflare China Network docs","description":"Obtain and display an ICP license number required for websites operating in China.","url":"https://developers.cloudflare.com/china-network/concepts/icp/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Compliance"]}</script>
  markdown: true
  noindex: false
  route: /china-network/concepts/icp/
  schema: 1
---
<p>To operate a website in China, you need government permission called an Internet Content Provider (ICP) number. Think of it as a permit — without one, your site can be shut down.</p>
<p>The ICP system is a licensing regime established by the Telecommunications Regulations of the People's Republic of China (中华人民共和国电信条例), introduced in September 2000.</p>
<p>Under the ICP regime, all websites with their own domain name that operate inside China must obtain a license. This applies whether the site is hosted on a server in Mainland China or delivered to visitors in China through a CDN. Licenses are issued at the provincial level. You can use the Ministry of Industry and Information Technology (MIIT) website to <a href="https://beian.miit.gov.cn/#/Integrated/recordQuery">check if a domain already has an ICP number</a> (only available in Chinese).</p>
<p>All public websites in Mainland China must have an ICP number <a href="#display-your-icp-number">displayed on the website's home page</a>. Websites with the same apex domain can share the same ICP number. China-based hosting providers are instructed to shut down any website (often without notice) without an ICP number.</p>
<h2 id="types-of-icp">Types of ICP</h2>
<p>To host web services in Mainland China, you are legally required to acquire an <strong>ICP filing</strong> or an <strong>ICP license</strong> in China. An ICP filing covers non-commercial (informational) sites, while an ICP license is required for sites that sell goods or services.</p>
<p>The type of ICP you must obtain depends on the type of website you are providing to customers in China:</p>
<table>
<thead>
<tr>
<th></th>
<th>ICP filing</th>
<th>ICP license</th>
</tr>
</thead>
<tbody>
<tr>
<td>Definition</td>
<td>An ICP filing, known in Chinese as “Bei’An,” is the first level of ICP registration. An ICP filing enables the holder to host a website on a server or CDN in Mainland China for informational purposes only.</td>
<td>An ICP license, known as “ICP Zheng” in Chinese, allows online platforms or third-party sellers selling goods and services to deploy their website on a hosting server or CDN within Mainland China.</td>
</tr>
<tr>
<td>Website Purpose</td>
<td>Non-commercial and non-transactional purposes.</td>
<td>Commercial and transactional purposes.</td>
</tr>
<tr>
<td>Eligibility</td>
<td>Representative office<br/>Wholly foreign-owned enterprise<br/>Joint venture<br/>Local company<br/>Individuals (personal website)</td>
<td>Joint venture (foreign company with less than 50% ownership)<br/>Local company</td>
</tr>
<tr>
<td>Example format</td>
<td>Beijing ICP preparation XXXXXXXX number</td>
<td>Beijing ICP license XXXXXXXX number</td>
</tr>
<tr>
<td>Other requirements</td>
<td>N/A</td>
<td>Companies acquiring an ICP license must already have obtained an ICP filing.</td>
</tr>
<tr>
<td>Timeline</td>
<td>1-2 months</td>
<td>2-3 months</td>
</tr>
</tbody>
</table>
<p>If you wish to host a marketing-related website, you only need an ICP filing.</p>
<hr />
<h2 id="obtain-an-icp-number">Obtain an ICP number</h2>
<p>Cloudflare recommends that you apply for an ICP license through your hosting or cloud services provider, who will register the ICP number on your behalf. You will need to provide the following documents to your provider:</p>
<table>
<thead>
<tr>
<th>For Individuals</th>
<th>For Commercial Companies</th>
</tr>
</thead>
<tbody>
<tr>
<td>– ICP application form<br/>– Copy of your personal ID<br/>– Forms to authenticate website information<br/>– Copy of your domain certificate</td>
<td>– Copy of your business license<br/>– Your organization code certificate</td>
</tr>
</tbody>
</table>
<p>After all required documents are submitted, it can take four to eight weeks to obtain an ICP number, depending on the type of website and the province where the company is registered. Registration with the MIIT is free, but your provider may charge a processing fee.</p>
<p>After receiving the ICP number and the certificate, add it to your website's home page.</p>
<h2 id="display-your-icp-number">Display your ICP number</h2>
<p>After you obtain an ICP number, you must display it in the footer of your website, like in the following example:</p>
<p><img src="/assets/upstream/images/china-network/icp-number-in-footer.png" alt="An ICP number displayed in the footer of a website." /></p>

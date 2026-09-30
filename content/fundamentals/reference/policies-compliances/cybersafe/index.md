---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cybersafe/
  description: Project Cybersafe Schools provides eligible schools with free Cloudflare Email Security and Gateway products to meet CIPA requirements.
  full_title: Project Cybersafe Schools · Cloudflare Fundamentals docs
  head_html: <title>Project Cybersafe Schools · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Project Cybersafe Schools provides eligible schools with free Cloudflare Email Security and Gateway products to meet CIPA requirements."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cybersafe/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cybersafe/index.md"><meta property="og:title" content="Project Cybersafe Schools · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Project Cybersafe Schools provides eligible schools with free Cloudflare Email Security and Gateway products to meet CIPA requirements."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cybersafe/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cybersafe/#page","headline":"Project Cybersafe Schools \u00b7 Cloudflare Fundamentals docs","description":"Project Cybersafe Schools provides eligible schools with free Cloudflare Email Security and Gateway products to meet CIPA requirements.","url":"https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cybersafe/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/reference/policies-compliances/cybersafe/
  schema: 1
---
<p>Project Cybersafe Schools grants eligible schools with free access to Cloudflare's <a href="/email-security/">Email security</a> and <a href="/cloudflare-one/traffic-policies/">Gateway</a> products.</p>
<h2 id="school-eligibility">School Eligibility</h2>
<p>This program is only available to eligible school districts. To be eligible, Project Cybersafe School participants must be:</p>
<ul>
<li>K-12 public school districts located in the United States.</li>
<li>Up to 2,500 students in the district.</li>
</ul>
<h2 id="children-s-internet-protection-act-cipa">Children’s Internet Protection Act (CIPA)</h2>
<p>The <a href="https://www.fcc.gov/sites/default/files/childrens_internet_protection_act_cipa.pdf">Children's Internet Protection Act (CIPA)</a> is a federal law enacted by the United States Congress to address concerns about children's access to inappropriate or harmful content over the Internet. CIPA requires K-12 schools and libraries that receive certain federal funding to implement Internet safety measures to protect minors from harmful online content.</p>
<p>The law aims to prevent students from accessing explicit, obscene, or otherwise harmful material. It also emphasizes the use of technology protection measures, including DNS filtering, to safeguard against Internet threats such as ransomware, phishing sites, and other potentially harmful content.</p>
<h3 id="cipa-requirements">CIPA Requirements</h3>
<p>CIPA mandates that K-12 schools and libraries adopt Internet safety policies that include measures to block or filter access to specific categories of content. These categories encompass a wide range of topics that could be harmful or inappropriate for minors. Compliance with these requirements helps ensure that students' online experiences are safer and more secure.</p>
<h3 id="configuration">Configuration</h3>
<p>To facilitate compliance with CIPA requirements, administrators can <a href="/cloudflare-one/traffic-policies/dns-policies/common-policies/#turn-on-cipa-filter">enable a single filtering policy option</a>. This includes applying the required filter categories to block access to unwanted or harmful online content.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9007.md")
</aside>
<p>Cloudflare’s recommended CIPA rule blocks the following content subcategories:</p>
<ul>
<li>Adult Themes</li>
<li>Alcohol</li>
<li>Anonymizer</li>
<li>Brand Embedding</li>
<li>Child Abuse</li>
<li>Command and Control &amp; Botnet</li>
<li>Cryptomining</li>
<li>DGA Domains</li>
<li>DNS Tunneling</li>
<li>Drugs</li>
<li>Gambling</li>
<li>Hacking</li>
<li>Malware</li>
<li>Militancy, Hate &amp; Extremism</li>
<li>Nudity</li>
<li>P2P</li>
<li>Phishing</li>
<li>Pornography</li>
<li>Private IP Address</li>
<li>Profanity</li>
<li>Questionable Activities</li>
<li>School Cheating</li>
<li>Spam</li>
<li>Spyware</li>
<li>Tobacco</li>
<li>Violence</li>
<li>Weapons</li>
</ul>
<p>Review the <a href="/cloudflare-one/traffic-policies/domain-categories/">domain categories</a> for more information.</p>
<h3 id="onboarding-guide">Onboarding Guide</h3>
<p>For a comprehensive guide, refer to the <a href="/learning-paths/cybersafe/concepts/">Project Cybersafe Schools Learning Path</a>, which takes you step by step through the technical concepts, creating an account, onboarding your traffic, and enabling the CIPA filters.</p>

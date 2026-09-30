---
cp9:
  canonical: https://developers.cloudflare.com/data-localization/region-support/
  description: Supported regions for Geo Key Manager, Regional Services, and Customer Metadata Boundary.
  full_title: Region support · Cloudflare Data Localization Suite docs
  head_html: <title>Region support · Cloudflare Data Localization Suite docs</title><meta name="generator" content="Nift"><meta name="description" content="Supported regions for Geo Key Manager, Regional Services, and Customer Metadata Boundary."><link rel="canonical" href="https://developers.cloudflare.com/data-localization/region-support/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/data-localization/region-support/index.md"><meta property="og:title" content="Region support · Cloudflare Data Localization Suite docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Supported regions for Geo Key Manager, Regional Services, and Customer Metadata Boundary."><meta property="og:url" content="https://developers.cloudflare.com/data-localization/region-support/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Data Localization Suite"><meta name="algolia_product_filter" content="Data Localization Suite"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Data Localization Suite"><meta name="pcx_tags" content="Compliance"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/data-localization/region-support/#page","headline":"Region support \u00b7 Cloudflare Data Localization Suite docs","description":"Supported regions for Geo Key Manager, Regional Services, and Customer Metadata Boundary.","url":"https://developers.cloudflare.com/data-localization/region-support/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Compliance"]}</script>
  markdown: true
  noindex: false
  route: /data-localization/region-support/
  schema: 1
---
<p>The Data Localization Suite allows you to restrict where your data is processed and stored. The table below shows which regions are available for each DLS feature:</p>
<ul>
<li><strong>Geo Key Manager</strong> — restricts where your TLS private keys are stored.</li>
<li><strong>Regional Services</strong> — restricts which Cloudflare data centers can decrypt and inspect your HTTPS traffic.</li>
<li><strong>Customer Metadata Boundary (CMB)</strong> — restricts where your logs and analytics data are stored.</li>
</ul>
<h2 id="region-types">Region types</h2>
<p>Regional Services regions come in two types:</p>
<ul>
<li><strong>Managed regions</strong> — predefined regions that Cloudflare maintains, identified by a region key (for example, <code>eu</code> or <code>us</code>). These are the regions listed in the tables below. They are available to all accounts, though some may require specific entitlements. Most customers use a managed region.</li>
<li><strong>Custom regions</strong> — regions tailored to your account that restrict processing to a specific set of data centers, for when the managed regions do not meet your compliance requirements. Custom regions are set up through your account team. They are available for <a href="/data-localization/regional-services/spectrum-applications/">Regionalized Spectrum Applications</a> and <a href="/data-localization/regional-services/ip-bindings/">Regionalized IP Bindings</a>, but not for <a href="/data-localization/regional-services/regional-hostnames/">Regional Hostnames</a>.</li>
</ul>
<p>Managed and custom regions apply to <strong>Regional Services</strong>. The other Data Localization Suite features use their own region settings:</p>
<ul>
<li><strong>Customer Metadata Boundary</strong> can be set to the <strong>United States</strong> or the <strong>European Union</strong>. By default no boundary is applied. FedRAMP customers set it to the United States.</li>
<li><strong>Geo Key Manager</strong> controls where TLS private keys are stored using its own set of locations.</li>
</ul>
<p>The tables below show which managed regions each product supports.</p>
<h2 id="available-regions">Available regions</h2>
<p>Some regions are defined by geography (for example, &quot;Germany&quot;), while others are defined by compliance frameworks:</p>
<ul>
<li><strong>FedRAMP Moderate</strong> — the US Federal Risk and Authorization Management Program, a government security certification standard. &quot;Domestic&quot; means only US-based certified data centers. &quot;International&quot; includes certified data centers outside the US.</li>
<li><strong>IRAP Protected</strong> — the Australian government's Information Security Registered Assessors Program. This region includes IRAP-assessed data centers, which may be located outside Australia.</li>
<li><strong>ISO 27001 Certified European Union</strong> — restricts traffic to EU data centers that hold ISO 27001 certification, an international standard for information security management.</li>
<li><strong>Cloudflare Green Energy</strong> — restricts traffic to data centers powered by renewable energy sources. This is an energy-sourcing constraint, not a geographic one.</li>
</ul>
<p>&quot;Exclusive of&quot; regions work in reverse — they exclude specific countries rather than restricting to them. For example, &quot;Exclusive of Russia and Belarus&quot; means Cloudflare will use any data center worldwide except those in Russia and Belarus.</p>
<p>Support by product and region is summarized in the following table. In the <strong>Customer Metadata Boundary</strong> column:</p>
<ul>
<li>✅ — the region corresponds to a metadata boundary you can select. CMB supports the <strong>United States</strong> and the <strong>European Union</strong> only; FedRAMP regions use the United States boundary.</li>
<li>&quot;Can use EU metadata boundary.&quot; — the country is within the European Union, so the EU boundary applies.</li>
<li>✘ — Customer Metadata Boundary is not available for this region.</li>
</ul>
<table>
<thead>
<tr>
<th>Region</th>
<th>Geo Key Manager</th>
<th>Regional Services</th>
<th>Customer Metadata Boundary</th>
</tr>
</thead>
<tbody>
<tr>
<td>Australia</td>
<td>✅ <sup><a href="#footnote-1">1</a></sup></td>
<td>✅</td>
<td>✘</td>
</tr>
<tr>
<td>Austria</td>
<td>✘</td>
<td>✅</td>
<td>Can use EU metadata boundary.</td>
</tr>
<tr>
<td>Brazil</td>
<td>✘</td>
<td>✅</td>
<td>✘</td>
</tr>
<tr>
<td>Canada</td>
<td>✅ <sup><a href="#footnote-1">1</a></sup></td>
<td>✅</td>
<td>✘</td>
</tr>
<tr>
<td>Cloudflare Green Energy</td>
<td>✘</td>
<td>✅</td>
<td>✘</td>
</tr>
<tr>
<td>European Union</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Exclusive of Hong Kong and Macau</td>
<td>✘</td>
<td>✅</td>
<td>✘</td>
</tr>
<tr>
<td>Exclusive of Russia and Belarus</td>
<td>✘</td>
<td>✅</td>
<td>✘</td>
</tr>
<tr>
<td>FedRAMP Moderate Compliant (Domestic)</td>
<td>✅ <sup><a href="#footnote-1">1</a></sup></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>FedRAMP Moderate Compliant (International)</td>
<td>✘</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>France</td>
<td>✘</td>
<td>✅</td>
<td>Can use EU metadata boundary.</td>
</tr>
<tr>
<td>Germany</td>
<td>✅ <sup><a href="#footnote-1">1</a></sup></td>
<td>✅</td>
<td>Can use EU metadata boundary.</td>
</tr>
<tr>
<td>Hong Kong</td>
<td>✘</td>
<td>✅</td>
<td>✘</td>
</tr>
<tr>
<td>India</td>
<td>✅ <sup><a href="#footnote-1">1</a></sup></td>
<td>✅</td>
<td>✘</td>
</tr>
<tr>
<td><a href="https://www.cloudflare.com/cloudflare-for-government/australia/irap/">IRAP</a> Protected</td>
<td>✘</td>
<td>✅</td>
<td>✘</td>
</tr>
<tr>
<td>ISO 27001 Certified European Union</td>
<td>✘</td>
<td>✅</td>
<td>Can use EU metadata boundary.</td>
</tr>
<tr>
<td>Italy</td>
<td>✘</td>
<td>✅</td>
<td>Can use EU metadata boundary.</td>
</tr>
<tr>
<td>Japan</td>
<td>✅ <sup><a href="#footnote-1">1</a></sup></td>
<td>✅</td>
<td>✘</td>
</tr>
<tr>
<td>NATO</td>
<td>✘</td>
<td>✅</td>
<td>✘</td>
</tr>
<tr>
<td>Netherlands</td>
<td>✘</td>
<td>✅</td>
<td>Can use EU metadata boundary.</td>
</tr>
<tr>
<td>Russia</td>
<td>✘</td>
<td>✅</td>
<td>✘</td>
</tr>
<tr>
<td>Saudi Arabia</td>
<td>✘</td>
<td>✅</td>
<td>✘</td>
</tr>
<tr>
<td>Singapore</td>
<td>✅ <sup><a href="#footnote-1">1</a></sup></td>
<td>✅</td>
<td>✘</td>
</tr>
<tr>
<td>South Africa</td>
<td>✘</td>
<td>✅</td>
<td>✘</td>
</tr>
<tr>
<td>South Korea</td>
<td>✅ <sup><a href="#footnote-1">1</a></sup></td>
<td>✅</td>
<td>✘</td>
</tr>
<tr>
<td>Spain</td>
<td>✘</td>
<td>✅</td>
<td>Can use EU metadata boundary.</td>
</tr>
<tr>
<td>Switzerland</td>
<td>✘</td>
<td>✅</td>
<td>✘</td>
</tr>
<tr>
<td>Taiwan</td>
<td>✘</td>
<td>✅</td>
<td>✘</td>
</tr>
<tr>
<td>Turkey</td>
<td>✘</td>
<td>✅</td>
<td>✘</td>
</tr>
<tr>
<td>United Arab Emirates</td>
<td>✘</td>
<td>✅</td>
<td>✘</td>
</tr>
<tr>
<td>United Kingdom</td>
<td>✅ <sup><a href="#footnote-1">1</a></sup></td>
<td>✅</td>
<td>Can use EU metadata boundary.</td>
</tr>
<tr>
<td>United States of America</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>US State of California</td>
<td>✘</td>
<td>✅</td>
<td>✘</td>
</tr>
<tr>
<td>US State of Florida</td>
<td>✘</td>
<td>✅</td>
<td>✘</td>
</tr>
<tr>
<td>US State of Texas</td>
<td>✘</td>
<td>✅</td>
<td>✘</td>
</tr>
</tbody>
</table>
<p>Refer to the table below for the complete list of available regions and their definitions.</p>
<table>
<thead>
<tr>
<th>Region</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr>
<td>Australia</td>
<td>Cloudflare will only use data centers that are physically located within Australia to decrypt and service HTTPS traffic.</td>
</tr>
<tr>
<td>Austria</td>
<td>Cloudflare will only use data centers that are physically located within Austria to decrypt and service HTTPS traffic.</td>
</tr>
<tr>
<td>Brazil</td>
<td>Cloudflare will only use data centers that are physically located within Brazil to decrypt and service HTTPS traffic.</td>
</tr>
<tr>
<td>Canada</td>
<td>Cloudflare will only use data centers that are physically located within Canada to decrypt and service HTTPS traffic.</td>
</tr>
<tr>
<td>Cloudflare Green Energy</td>
<td>Cloudflare will only use data centers that are committed to powering their operations with <a href="https://www.cloudflare.com/impact/">renewable energy</a>.</td>
</tr>
<tr>
<td>European Union</td>
<td>Cloudflare will only use data centers that are physically located within the European Union. For more details, refer to the <a href="https://european-union.europa.eu/principles-countries-history/country-profiles_en">list of European Union countries</a>.</td>
</tr>
<tr>
<td>Exclusive of Hong Kong and Macau</td>
<td>Cloudflare will only use data centers that are NOT physically located within Hong Kong and Macau to decrypt and service HTTPS traffic.</td>
</tr>
<tr>
<td>Exclusive of Russia and Belarus</td>
<td>Cloudflare will only use data centers that are NOT physically located within Russia and Belarus to decrypt and service HTTPS traffic.</td>
</tr>
<tr>
<td>FedRAMP Moderate Compliant (Domestic)</td>
<td>Cloudflare will only use data centers that are FedRAMP Moderate certified and located within the United States.</td>
</tr>
<tr>
<td>FedRAMP Moderate Compliant (International)</td>
<td>Cloudflare will only use data centers that are FedRAMP Moderate certified, including certified locations outside the United States.</td>
</tr>
<tr>
<td>France</td>
<td>Cloudflare will only use data centers that are physically located within Metropolitan France (the European territory of France) to decrypt and service HTTPS traffic.</td>
</tr>
<tr>
<td>Germany</td>
<td>Cloudflare will only use data centers that are physically located within Germany to decrypt and service HTTPS traffic.</td>
</tr>
<tr>
<td>Hong Kong</td>
<td>Cloudflare will only use data centers that are physically located within Hong Kong to decrypt and service HTTPS traffic.</td>
</tr>
<tr>
<td>India</td>
<td>Cloudflare will only use data centers that are physically located within India to decrypt and service HTTPS traffic.</td>
</tr>
<tr>
<td>ISO 27001 Certified European Union</td>
<td>Cloudflare will only use data centers that are physically located within the <a href="https://european-union.europa.eu/principles-countries-history/country-profiles_en">European Union</a> and that adhere to the ISO 27001 certification.</td>
</tr>
<tr>
<td>IRAP Protected</td>
<td>Cloudflare will only use data centers that are IRAP protected, including certified locations outside Australia.</td>
</tr>
<tr>
<td>Italy</td>
<td>Cloudflare will only use data centers that are physically located within Italy to decrypt and service HTTPS traffic.</td>
</tr>
<tr>
<td>Japan</td>
<td>Cloudflare will only use data centers that are physically located within Japan to decrypt and service HTTPS traffic.</td>
</tr>
<tr>
<td>NATO</td>
<td>Cloudflare will only use data centers that are physically located within North Atlantic Treaty Organization (NATO) countries. For more details, refer to the <a href="https://www.nato.int/nato-welcome/">list of NATO countries</a>.</td>
</tr>
<tr>
<td>Netherlands</td>
<td>Cloudflare will only use data centers that are physically located within the Netherlands to decrypt and service HTTPS traffic.</td>
</tr>
<tr>
<td>Russia</td>
<td>Cloudflare will only use data centers that are physically located within Russia to decrypt and service HTTPS traffic.</td>
</tr>
<tr>
<td>Saudi Arabia</td>
<td>Cloudflare will only use data centers that are physically located within Saudi Arabia to decrypt and service HTTPS traffic.</td>
</tr>
<tr>
<td>Singapore</td>
<td>Cloudflare will only use data centers that are physically located within Singapore to decrypt and service HTTPS traffic.</td>
</tr>
<tr>
<td>South Africa</td>
<td>Cloudflare will only use data centers that are physically located within South Africa to decrypt and service HTTPS traffic.</td>
</tr>
<tr>
<td>South Korea</td>
<td>Cloudflare will only use data centers that are physically located within South Korea to decrypt and service HTTPS traffic.</td>
</tr>
<tr>
<td>Spain</td>
<td>Cloudflare will only use data centers that are physically located within Spain to decrypt and service HTTPS traffic.</td>
</tr>
<tr>
<td>Switzerland</td>
<td>Cloudflare will only use data centers that are physically located within Switzerland to decrypt and service HTTPS traffic.</td>
</tr>
<tr>
<td>Taiwan</td>
<td>Cloudflare will only use data centers that are physically located within Taiwan to decrypt and service HTTPS traffic.</td>
</tr>
<tr>
<td>Turkey</td>
<td>Cloudflare will only use data centers that are physically located within Turkey to decrypt and service HTTPS traffic.</td>
</tr>
<tr>
<td>United Arab Emirates</td>
<td>Cloudflare will only use data centers that are physically located within United Arab Emirates to decrypt and service HTTPS traffic.</td>
</tr>
<tr>
<td>United Kingdom</td>
<td>Cloudflare will only use data centers that are physically located within the United Kingdom to decrypt and service HTTPS traffic.</td>
</tr>
<tr>
<td>United States of America</td>
<td>Cloudflare will only use data centers that are physically located within the United States of America to decrypt and service HTTPS traffic.</td>
</tr>
<tr>
<td>US State of California</td>
<td>Cloudflare will only use data centers that are physically located within the US State of California to decrypt and service HTTPS traffic.</td>
</tr>
<tr>
<td>US State of Florida</td>
<td>Cloudflare will only use data centers that are physically located within the US State of Florida to decrypt and service HTTPS traffic.</td>
</tr>
<tr>
<td>US State of Texas</td>
<td>Cloudflare will only use data centers that are physically located within the US State of Texas to decrypt and service HTTPS traffic.</td>
</tr>
</tbody>
</table>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Only supported in [Geo Key Manager v2](/ssl/edge-certificates/geokey-manager/), the current version with expanded region support.</li></ol></section>

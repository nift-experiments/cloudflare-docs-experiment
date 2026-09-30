---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.accepted_languages/
  description: List of language tags provided in the Accept-Language HTTP request header.
  full_title: http.request.accepted_languages · Cloudflare Ruleset Engine docs
  head_html: <title>http.request.accepted_languages · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="List of language tags provided in the Accept-Language HTTP request header."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.accepted_languages/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="http.request.accepted_languages · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="List of language tags provided in the Accept-Language HTTP request header."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.accepted_languages/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.accepted_languages/#page","headline":"http.request.accepted_languages \u00b7 Cloudflare Ruleset Engine docs","description":"List of language tags provided in the Accept-Language HTTP request header.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.accepted_languages/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ruleset-engine/rules-language/fields/reference/http.request.accepted_languages/
  schema: 1
---
<h1 id="http-request-accepted-languages">http.request.accepted_languages</h1>

**Data type:** Array<String>

<p>List of language tags provided in the <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Accept-Language"><code>Accept-Language</code></a> HTTP request header.</p>

<p>Language tags are sorted by weight (<code>;q=&lt;weight&gt;</code>, with a default weight of <code>1</code>) in descending order.</p>
<p>If the HTTP header is not present in the request or is empty, <code>http.request.accepted_languages[0]</code> will return a &quot;<a href="/ruleset-engine/rules-language/values/#notes">missing value</a>&quot;, which the <a href="/ruleset-engine/rules-language/functions/#concat"><code>concat()</code></a> function will handle as an empty string.</p>
<p>If the HTTP header includes the language tag <code>*</code> it will not be stored in the array.</p>
<p><strong>Note</strong>: This field is only available in <a href="/rules/transform/">Transform Rules</a>.</p>

**Example usage:**

```txt
# Example 1: Request with header "Accept-Language: fr-CH, fr;q=0.8, en;q=0.9, de;q=0.7, *;q=0.5".
# In this case:
http.request.accepted_languages[0] ==> "fr-CH"
http.request.accepted_languages    ==> ["fr-CH", "en", "fr", "de"]

# Example 2: Request without an `Accept-Language` HTTP header and a URI of "https://www.example.com/my-path".
# In this case:
concat("/", http.request.accepted_languages[0], http.request.uri.path) ==> "//my-path"
```

<h2 id="categories">Categories</h2>

- Request
- Headers

**Keywords:** request, client, visitor


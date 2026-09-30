---
cp9:
  canonical: https://developers.cloudflare.com/email-security/account-setup/sso/
  description: Configure SAML-based single sign-on for Email Security with identity providers like Okta or Azure AD.
  full_title: SSO integration · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>SSO integration · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure SAML-based single sign-on for Email Security with identity providers like Okta or Azure AD."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/account-setup/sso/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/account-setup/sso/index.md"><meta property="og:title" content="SSO integration · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure SAML-based single sign-on for Email Security with identity providers like Okta or Azure AD."><meta property="og:url" content="https://developers.cloudflare.com/email-security/account-setup/sso/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/account-setup/sso/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="area-1-has-been-renamed">Area 1 has been renamed</h3>
@markup("md", "content/.markup/bodies/8496.md")
</aside>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="access-to-area-1">Access to Area 1</h3>
@markup("md", "content/.markup/bodies/8495.md")
</aside>
<p>For added security and convenience, Email security (formerly Area 1) offers support for <span class="nb-glossary-tooltip" title="SAML">Security Assertion Markup Language based (SAML-based)</span> single sign-on (SSO) logins. Organizations are able to choose between having users access Email security (formerly Area 1) with a username and password plus a <span class="nb-glossary-tooltip" title="two-factor authentication (2FA)">two-factor authentication (2FA)</span> code, or using an SSO provider, such as OneLogin or Okta.</p>
<h2 id="saml-configuration-options">SAML configuration options</h2>
<ul>
<li><strong>Identity Provider initiated (IDP-initiated) SAML</strong>: IDP-initiated configurations (like Okta or OneLogin) require the IDP to be accessible to the Email security infrastructure in order to successfully authenticate users. At the most basic level, the user selects an application from their IDP. Then, the IDP communicates with Email security using a SAML assertion to provide identity information for the user requesting to login to the Email security dashboard.</li>
<li><strong>Service Provider Initiated (SP-initiated) SAML</strong>: SP-initiated configurations are the most common SAML authentication mechanisms. The main difference compared to IDP is that the service provider (like Email security) does not require any direct connection to the IDP in order to authenticate a user. The user's browser provides the ability for the SAML exchange to occur but the service provider and the IDP do not directly communicate with each other.</li>
</ul>
<p>Email security (formerly Area 1) only supports IDP-initiated SAML setup at this point.</p>
<h2 id="setup">Setup</h2>
<p>For more details on setup, refer to the following resources:</p>
<ul class="directory-listing"><li><a href="/email-security/account-setup/sso/generic-sso/">Generic SSO guide</a></li><li><a href="/email-security/account-setup/sso/okta/">Okta guide</a></li><li><a href="/email-security/account-setup/sso/azure/">Azure guide</a></li><li><a href="/cloudflare-one/access-controls/applications/http-apps/saas-apps/area-1/">Cloudflare Access for SaaS</a></li></ul>

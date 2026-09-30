<p>Predefined detection entries are Cloudflare-managed detections for specific types of sensitive content. You can review these entries from the <strong>Predefined</strong> view in <strong>Detection entries</strong>.</p>
<p>You can add any predefined detection entry directly to a custom <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/#build-a-custom-profile">DLP profile</a> or <a href="/cloudflare-one/data-loss-prevention/data-classification/build-a-data-class/">data class</a>. Use the following reference to review all predefined detection entries currently supported by Cloudflare DLP.</p>
<table>
<thead>
<tr>
<th>Detection entry</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>AI Prompt Content: Credentials and Secrets</td>
<td>Prompt contains API keys, passwords, or other sensitive credentials</td>
</tr>
<tr>
<td>AI Prompt Content: Customer data</td>
<td>Prompt contains customer names, projects, business activities, or confidential customer contexts</td>
</tr>
<tr>
<td>AI Prompt Content: Financial Information</td>
<td>Prompt contains actual financial numbers or confidential business data</td>
</tr>
<tr>
<td>AI Prompt Content: PII</td>
<td>Prompt contains personal information (names, SSNs, emails, etc.)</td>
</tr>
<tr>
<td>AI Prompt Content: Source code</td>
<td>Prompt contains source code, code snippets, or proprietary algorithms</td>
</tr>
<tr>
<td>AI Prompt Intent: Code Abuse and Malicious Code</td>
<td>Malicious code or attempts to exploit vulnerabilities</td>
</tr>
<tr>
<td>AI Prompt Intent: Jailbreak</td>
<td>Prompt attempts to circumvent security policies</td>
</tr>
<tr>
<td>AI Prompt Intent: PII</td>
<td>Prompt requests specific personal information about individuals</td>
</tr>
<tr>
<td>Amazon AWS Access Key ID</td>
<td>Detects Amazon AWS access key IDs such as <code>AKIA&lt;ACCESS_KEY_ID&gt;</code>.</td>
</tr>
<tr>
<td>Amazon AWS Secret Access Key</td>
<td>Detects potential Amazon AWS secret access keys such as <code>&lt;AWS_SECRET_ACCESS_KEY&gt;</code>.</td>
</tr>
<tr>
<td>American Express Card Number</td>
<td>Detects American Express credit card numbers such as &quot;378282246310005&quot;.</td>
</tr>
<tr>
<td>American Express Text</td>
<td>Detects mentions of the American Express brand name such as &quot;American Express&quot;.</td>
</tr>
<tr>
<td>Australia Address</td>
<td>Detects Australian street addresses with state and postcode such as &quot;100 George St, Sydney NSW 2000&quot;.</td>
</tr>
<tr>
<td>Australia Business (ABN)</td>
<td>Detects Australian Business Numbers (ABN) such as &quot;51 824 753 556&quot;.</td>
</tr>
<tr>
<td>Australia Company (ACN)</td>
<td>Detects Australian Company Numbers (ACN) such as &quot;001 000 004&quot;.</td>
</tr>
<tr>
<td>Australia Medicare</td>
<td>Detects Australian Medicare card numbers such as &quot;2000000006&quot;.</td>
</tr>
<tr>
<td>Australia Passport Number</td>
<td>Detects Australian passport numbers such as &quot;L1234567&quot;.</td>
</tr>
<tr>
<td>Australia Tax File Number</td>
<td>Detects Australian Tax File Numbers (TFN) such as &quot;85 655 734&quot;.</td>
</tr>
<tr>
<td>Austria SSN (SV-Nummer)</td>
<td>Detects Austrian social security numbers (SV-Nummer) such as &quot;1018 010180&quot;.</td>
</tr>
<tr>
<td>Austria Tax ID</td>
<td>Detects Austrian tax identification numbers (Steuernummer) such as &quot;12 345/6789&quot;.</td>
</tr>
<tr>
<td>Austria VAT (UID)</td>
<td>Detects Austrian VAT numbers (UID-Nummer) such as &quot;ATU12345678&quot;.</td>
</tr>
<tr>
<td>Belgium Tax ID (NN)</td>
<td>Detects Belgian national numbers (Numéro National / Rijksregisternummer) such as &quot;85.07.30-000.61&quot;.</td>
</tr>
<tr>
<td>Belgium VAT</td>
<td>Detects Belgian VAT numbers such as &quot;BE0000000097&quot;.</td>
</tr>
<tr>
<td>Bitcoin Wallet</td>
<td>Detects Bitcoin wallet addresses such as &quot;1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2&quot;.</td>
</tr>
<tr>
<td>Brazil CNPJ</td>
<td>Detects Brazilian corporate taxpayer registry numbers (CNPJ) such as &quot;11.222.333/0001-81&quot;.</td>
</tr>
<tr>
<td>Brazil CPF (Tax ID)</td>
<td>Detects Brazilian individual taxpayer registry numbers (CPF) such as &quot;529.982.247-25&quot;.</td>
</tr>
<tr>
<td>Bulgaria Uniform Civil (EGN)</td>
<td>Detects Bulgarian Uniform Civil Numbers (EGN) such as &quot;2405500007&quot;.</td>
</tr>
<tr>
<td>C</td>
<td>Detects C source code.</td>
</tr>
<tr>
<td>C#</td>
<td>Detects C# source code.</td>
</tr>
<tr>
<td>C++</td>
<td>Detects C++ source code.</td>
</tr>
<tr>
<td>Canada Bank Account Number</td>
<td>Detects Canadian bank account numbers (institution + transit + account) such as &quot;12345-678 1234567&quot;.</td>
</tr>
<tr>
<td>Canada Health Number</td>
<td>Detects Canadian provincial health card numbers such as &quot;1234-567-897&quot;.</td>
</tr>
<tr>
<td>Canada Passport</td>
<td>Detects Canadian passport numbers such as &quot;AB123456&quot;.</td>
</tr>
<tr>
<td>Canada PHIN (Manitoba)</td>
<td>Detects Manitoba Personal Health Identification Numbers (PHIN) such as &quot;100000009&quot;.</td>
</tr>
<tr>
<td>Canada Physical Address</td>
<td>Detects Canadian street addresses with postal code such as &quot;100 Main St, Ottawa, ON K1A 0B1&quot;.</td>
</tr>
<tr>
<td>Canada Social Insurance Number</td>
<td>Detects Canadian Social Insurance Numbers (SIN) such as &quot;114 905 474&quot;.</td>
</tr>
<tr>
<td>Chile National ID (RUT)</td>
<td>Detects Chilean national identification numbers (RUT / Rol Único Tributario) such as &quot;12.345.678-5&quot;.</td>
</tr>
<tr>
<td>China ID Card</td>
<td>Detects Chinese resident identity card numbers such as &quot;11010519491231002X&quot;.</td>
</tr>
<tr>
<td>Cloudflare Account Owned API Token</td>
<td>Detects Cloudflare account-owned API tokens such as <code>cfat_&lt;ACCOUNT_OWNED_API_TOKEN&gt;</code>.</td>
</tr>
<tr>
<td>Cloudflare User API Key</td>
<td>Detects Cloudflare user API keys such as <code>cfk_&lt;USER_API_KEY&gt;</code>.</td>
</tr>
<tr>
<td>Cloudflare User API Token</td>
<td>Detects Cloudflare user API tokens such as <code>cfut_&lt;USER_API_TOKEN&gt;</code>.</td>
</tr>
<tr>
<td>Croatia Personal ID (OIB)</td>
<td>Detects Croatian personal identification numbers (OIB) such as &quot;10000000005&quot;.</td>
</tr>
<tr>
<td>CVV Card Number (labeled)</td>
<td>Detects credit card CVV/CVC verification codes in context of the &quot;cvv&quot; keyword, such as &quot;cvv: 033&quot;.</td>
</tr>
<tr>
<td>Denmark Tax (CPR)</td>
<td>Detects Danish personal identification numbers (CPR-nummer) such as &quot;010180-0008&quot;.</td>
</tr>
<tr>
<td>Diners Club Card Number</td>
<td>Detects Diners Club credit card numbers such as &quot;30121690374838&quot;.</td>
</tr>
<tr>
<td>Discord Webhook</td>
<td>Detects Discord webhook URLs such as a webhook URL under <code>discord.com/api/webhooks/</code>.</td>
</tr>
<tr>
<td>Email Address</td>
<td>Detects email addresses such as &quot;<a href="mailto:test@example.com">test@example.com</a>&quot;.</td>
</tr>
<tr>
<td>Ethereum Wallet</td>
<td>Detects Ethereum wallet addresses such as &quot;0x71C7656EC7ab88b098defB751B7401B5f6d8976F&quot;.</td>
</tr>
<tr>
<td>EU Passport</td>
<td>Detects EU member state passport numbers such as &quot;AB1234567&quot;.</td>
</tr>
<tr>
<td>FDA Active Ingredients</td>
<td>Detects FDA-registered drug active ingredient names such as &quot;ABEMACICLIB&quot;.</td>
</tr>
<tr>
<td>FDA Drug Names</td>
<td>Detects FDA-registered drug names such as &quot;ABACAVIR&quot;.</td>
</tr>
<tr>
<td>Finland Tax ID</td>
<td>Detects Finnish personal identity codes (Henkilötunnus / HETU) such as &quot;311280-888Y&quot;.</td>
</tr>
<tr>
<td>France CNI (National ID)</td>
<td>Detects French national identity card numbers (Carte nationale d'identité) such as &quot;12345678901&quot;.</td>
</tr>
<tr>
<td>France Passport</td>
<td>Detects French passport numbers such as &quot;12AB34567&quot;.</td>
</tr>
<tr>
<td>France Social Security Number</td>
<td>Detects French social security (INSEE) numbers such as &quot;145081849670637&quot;.</td>
</tr>
<tr>
<td>France Tax ID (SPI)</td>
<td>Detects French tax identification numbers (Numéro fiscal SPI) such as &quot;1234567890123&quot;.</td>
</tr>
<tr>
<td>France VAT</td>
<td>Detects French VAT numbers such as &quot;FR12000000000&quot;.</td>
</tr>
<tr>
<td>Full Name</td>
<td>Detects personal full names.</td>
</tr>
<tr>
<td>Germany Tax ID</td>
<td>Detects German tax identification numbers (Steueridentifikationsnummer) such as &quot;10000000005&quot;.</td>
</tr>
<tr>
<td>Germany VAT</td>
<td>Detects German VAT numbers (USt-IdNr) such as &quot;DE100000003&quot;.</td>
</tr>
<tr>
<td>GitHub PAT</td>
<td>Detects GitHub personal access tokens such as a token beginning with <code>ghp_</code>.</td>
</tr>
<tr>
<td>Go</td>
<td>Detects Go source code.</td>
</tr>
<tr>
<td>Google GCP API Key</td>
<td>Detects Google Cloud Platform API keys such as <code>AIza&lt;API_KEY&gt;</code>.</td>
</tr>
<tr>
<td>Greece Tax (AFM)</td>
<td>Detects Greek tax identification numbers (AFM) such as &quot;100000003&quot;.</td>
</tr>
<tr>
<td>Haskell</td>
<td>Detects Haskell source code.</td>
</tr>
<tr>
<td>Hong Kong Identity Card Number</td>
<td>Detects Hong Kong identity card (HKID) numbers such as &quot;F543210(A)&quot;.</td>
</tr>
<tr>
<td>Hungary Tax</td>
<td>Detects Hungarian tax identification numbers (Adóazonosító jel) such as &quot;8000000008&quot;.</td>
</tr>
<tr>
<td>IBAN</td>
<td>Detects International Bank Account Numbers (IBAN) such as &quot;GB94 BARC 1020 1530 0934 59&quot;.</td>
</tr>
<tr>
<td>ICD-10 FY2023 Short Description</td>
<td>Detects ICD-10 FY2023 medical diagnosis terms such as &quot;Typhoid fever, unspecified&quot;.</td>
</tr>
<tr>
<td>ICD-11 Short Description</td>
<td>Detects ICD-11 medical diagnosis terms such as &quot;ABDOMINAL ACTINOMYCOSIS&quot;.</td>
</tr>
<tr>
<td>India Aadhaar</td>
<td>Detects Indian Aadhaar national identification numbers such as &quot;2345 6789 0124&quot;.</td>
</tr>
<tr>
<td>India GST (GSTIN)</td>
<td>Detects Indian Goods and Services Tax identification numbers (GSTIN) such as &quot;22AAAAA0000A1Z5&quot;.</td>
</tr>
<tr>
<td>India PAN Card</td>
<td>Detects Indian Permanent Account Number (PAN) card identifiers such as &quot;ABCDE1234F&quot;.</td>
</tr>
<tr>
<td>India Voter ID</td>
<td>Detects Indian Voter ID (EPIC) numbers such as &quot;ABC1234567&quot;.</td>
</tr>
<tr>
<td>Indonesia Identity Card Number</td>
<td>Detects Indonesian identity card (KTP/NIK) numbers such as &quot;3203012503770011&quot;.</td>
</tr>
<tr>
<td>Indonesia Tax (NPWP)</td>
<td>Detects Indonesian taxpayer identification numbers (NPWP) such as &quot;12.345.678.9-012.345&quot;.</td>
</tr>
<tr>
<td>Ireland Tax (PPS)</td>
<td>Detects Irish Personal Public Service numbers (PPS) such as &quot;1234567FA&quot;.</td>
</tr>
<tr>
<td>Ireland VAT</td>
<td>Detects Ireland VAT numbers such as &quot;IE1234567T&quot;.</td>
</tr>
<tr>
<td>Italy Fiscal Code</td>
<td>Detects Italian fiscal codes (Codice Fiscale) such as &quot;BNZVCN32S10E573Z&quot;.</td>
</tr>
<tr>
<td>Japan Postal Code</td>
<td>Detects a Japanese postal code preceded by the 〒 marker, such as &quot;〒100-0001&quot;. Free-form addresses without a 〒 postal-code marker are not matched.</td>
</tr>
<tr>
<td>Japan My Number (Corp)</td>
<td>Detects Japanese corporate My Number identifiers (Hojin Bango) such as &quot;7000012050002&quot;.</td>
</tr>
<tr>
<td>Japan My Number (Person)</td>
<td>Detects Japanese individual My Number identifiers (Kojin Bango) such as &quot;100000000005&quot;.</td>
</tr>
<tr>
<td>Japan Names (Kanji, labeled)</td>
<td>Detects a kanji personal name only when it immediately follows an inline label such as 氏名, 名前, or Name — for example &quot;氏名: 田中太郎&quot;. Bare kanji names with no preceding label (for example a standalone name or one in a spreadsheet column) are not matched.</td>
</tr>
<tr>
<td>Japan Passport</td>
<td>Detects Japanese passport numbers such as &quot;TZ1234567&quot;.</td>
</tr>
<tr>
<td>Java</td>
<td>Detects Java source code.</td>
</tr>
<tr>
<td>JavaScript</td>
<td>Detects JavaScript source code.</td>
</tr>
<tr>
<td>Korea Resident Number (RRN)</td>
<td>Detects South Korean Resident Registration Numbers (RRN) such as &quot;850515-1234567&quot;.</td>
</tr>
<tr>
<td>Lua</td>
<td>Detects Lua source code.</td>
</tr>
<tr>
<td>Luxembourg Tax</td>
<td>Detects Luxembourg national identification numbers (Matricule) such as &quot;1985010112345&quot;.</td>
</tr>
<tr>
<td>Luxembourg VAT</td>
<td>Detects Luxembourg VAT numbers such as &quot;LU10000053&quot;.</td>
</tr>
<tr>
<td>Malaysian National Identity Card Number</td>
<td>Detects Malaysian national identity card (MyKad) numbers such as &quot;560224-10-8354&quot;.</td>
</tr>
<tr>
<td>Mastercard Card Number</td>
<td>Detects Mastercard credit card numbers such as &quot;5252 5971 4219 4116&quot;.</td>
</tr>
<tr>
<td>Mastercard Text</td>
<td>Detects mentions of the Mastercard brand name such as &quot;Mastercard&quot;.</td>
</tr>
<tr>
<td>Microsoft Azure Client Secret</td>
<td>Detects Microsoft Azure client secrets such as <code>&lt;AZURE_CLIENT_SECRET&gt;</code>.</td>
</tr>
<tr>
<td>MX CLABE (Bank)</td>
<td>Detects Mexican CLABE bank account numbers such as &quot;032180000118359719&quot;.</td>
</tr>
<tr>
<td>MX CURP</td>
<td>Detects Mexican CURP codes such as &quot;GOMC850515HJCRRR05&quot;.</td>
</tr>
<tr>
<td>Netherlands BSN</td>
<td>Detects Dutch citizen service numbers (Burgerservicenummer / BSN) such as &quot;123456782&quot;.</td>
</tr>
<tr>
<td>Netherlands VAT</td>
<td>Detects Dutch VAT numbers (Btw-nummer) such as &quot;NL123456782B01&quot;.</td>
</tr>
<tr>
<td>NPM Token</td>
<td>Detects npm registry access tokens such as a token beginning with <code>npm_</code>.</td>
</tr>
<tr>
<td>NZ NHI Number</td>
<td>Detects New Zealand National Health Index (NHI) numbers such as &quot;ZZZ0016&quot;.</td>
</tr>
<tr>
<td>NZ Tax (IRD)</td>
<td>Detects New Zealand Inland Revenue Department (IRD) tax numbers such as &quot;49-091-850&quot;.</td>
</tr>
<tr>
<td>OpenAI API Key</td>
<td>Detects OpenAI API keys such as a key beginning with <code>sk-proj-</code>.</td>
</tr>
<tr>
<td>Peru Tax (RUC)</td>
<td>Detects Peruvian taxpayer identification numbers (RUC) such as &quot;20000000001&quot;.</td>
</tr>
<tr>
<td>Peru Unique ID (DNI)</td>
<td>Detects Peruvian national identity numbers (DNI) such as &quot;12345678&quot;.</td>
</tr>
<tr>
<td>Philippines Unified Multi-Purpose ID Identity Number</td>
<td>Detects Philippines Unified Multi-Purpose ID (UMID) numbers such as &quot;2460-1501400-1&quot;.</td>
</tr>
<tr>
<td>Poland National ID (PESEL)</td>
<td>Detects Polish national identification numbers (PESEL) such as &quot;85051500006&quot;.</td>
</tr>
<tr>
<td>Poland REGON</td>
<td>Detects Polish National Business Registry numbers (REGON) such as &quot;100000008&quot;.</td>
</tr>
<tr>
<td>Poland Tax (NIP)</td>
<td>Detects Polish tax identification numbers (NIP) such as &quot;123-456-32-18&quot;.</td>
</tr>
<tr>
<td>Portugal Tax (NIF)</td>
<td>Detects Portuguese tax identification numbers (NIF / Número de Contribuinte) such as &quot;100000002&quot;.</td>
</tr>
<tr>
<td>PyPI Token</td>
<td>Detects PyPI package upload tokens such as a token beginning with <code>pypi-</code>.</td>
</tr>
<tr>
<td>Python</td>
<td>Detects Python source code.</td>
</tr>
<tr>
<td>R</td>
<td>Detects R source code.</td>
</tr>
<tr>
<td>Rust</td>
<td>Detects Rust source code.</td>
</tr>
<tr>
<td>Singapore National Registration Identity Card Number</td>
<td>Detects Singapore NRIC/FIN identity card numbers such as &quot;S6792120H&quot;.</td>
</tr>
<tr>
<td>Slack API Token</td>
<td>Detects Slack API tokens such as a token beginning with <code>xoxb-</code>.</td>
</tr>
<tr>
<td>Slack Webhook</td>
<td>Detects Slack incoming webhook URLs such as a webhook URL under <code>hooks.slack.com/services/</code>.</td>
</tr>
<tr>
<td>Spain DNI/NIF</td>
<td>Detects Spanish national identity numbers (DNI/NIF) such as &quot;12345678Z&quot;.</td>
</tr>
<tr>
<td>Spain SSN</td>
<td>Detects Spanish Social Security affiliation numbers (NAF) such as &quot;28 1234567890&quot;.</td>
</tr>
<tr>
<td>Spain Tax (CIF)</td>
<td>Detects Spanish corporate tax identification codes (CIF) such as &quot;A58818501&quot;.</td>
</tr>
<tr>
<td>SSH Private Key</td>
<td>Detects SSH private key material such as &quot;-----BEGIN OPENSSH PRIVATE KEY-----&quot;.</td>
</tr>
<tr>
<td>Stripe Granular Restricted Key</td>
<td>Detects Stripe live-mode restricted API keys such as a key beginning with <code>rk_live_</code>.</td>
</tr>
<tr>
<td>Stripe Standard Secret Key</td>
<td>Detects Stripe live-mode secret API keys such as a key beginning with <code>sk_live_</code>.</td>
</tr>
<tr>
<td>Sweden Tax</td>
<td>Detects Swedish personal identity numbers (Personnummer) such as &quot;811228-9874&quot;.</td>
</tr>
<tr>
<td>SWIFT</td>
<td>Detects SWIFT/BIC business identifier codes such as &quot;PMFAUS66&quot;.</td>
</tr>
<tr>
<td>Swift</td>
<td>Detects Swift source code.</td>
</tr>
<tr>
<td>Taiwan National Identification Number</td>
<td>Detects Taiwan national identification numbers such as &quot;W171845961&quot;.</td>
</tr>
<tr>
<td>Thai Identity Card Number</td>
<td>Detects Thai national identity card numbers such as &quot;4-8547-01245-28-9&quot;.</td>
</tr>
<tr>
<td>UAE Passport</td>
<td>Detects United Arab Emirates passport numbers such as &quot;A1234567&quot;.</td>
</tr>
<tr>
<td>Union Pay Card Number</td>
<td>Detects UnionPay credit card numbers such as &quot;6250941006528599&quot;.</td>
</tr>
<tr>
<td>Union Pay Text</td>
<td>Detects mentions of the UnionPay brand name such as &quot;Union Pay&quot;.</td>
</tr>
<tr>
<td>United Kingdom National Insurance Number</td>
<td>Detects UK National Insurance Numbers (NINO) such as &quot;OC 66 31 85 C&quot;.</td>
</tr>
<tr>
<td>United Kingdom NHS Number</td>
<td>Detects UK NHS patient identification numbers such as &quot;485-585-0454&quot;.</td>
</tr>
<tr>
<td>United States ABA Routing Number</td>
<td>Detects US ABA bank routing numbers such as &quot;021000021&quot;.</td>
</tr>
<tr>
<td>United States SSN Numeric Detection</td>
<td>Detects US Social Security Numbers such as &quot;123-45-6789&quot;.</td>
</tr>
<tr>
<td>United States SSN Text</td>
<td>Detects mentions of &quot;SSN&quot; or &quot;social security&quot; as a keyword, such as &quot;social security&quot;.</td>
</tr>
<tr>
<td>Unsanitized HAR File</td>
<td>Detects HAR (HTTP Archive) files that may contain unsanitized authentication tokens or session data, such as a HAR file containing <code>Authorization: Bearer &lt;USER_API_TOKEN&gt;</code>.</td>
</tr>
<tr>
<td>Uruguay ID (CI)</td>
<td>Detects Uruguayan national identity numbers (Cédula de Identidad) such as &quot;1.234.500-8&quot;.</td>
</tr>
<tr>
<td>US Driver's License Number</td>
<td>Detects US driver's license numbers such as &quot;CA License: A1234567&quot;.</td>
</tr>
<tr>
<td>US Individual Tax Identification Number (ITIN)</td>
<td>Detects US Individual Taxpayer Identification Numbers (ITIN) such as &quot;934-78-5678&quot;.</td>
</tr>
<tr>
<td>US Mailing Address</td>
<td>Detects US mailing addresses such as &quot;100 First St, Chicago, IL 60601&quot;.</td>
</tr>
<tr>
<td>US Passport Number</td>
<td>Detects US passport numbers such as &quot;A12345678&quot;.</td>
</tr>
<tr>
<td>US Phone Number</td>
<td>Detects US phone numbers such as &quot;555-555-5555&quot;.</td>
</tr>
<tr>
<td>Visa Card Number</td>
<td>Detects Visa credit card numbers such as &quot;4111 1111 1111 1111&quot;.</td>
</tr>
<tr>
<td>Visa Text</td>
<td>Detects mentions of the Visa brand name such as &quot;Visa&quot;.</td>
</tr>
</tbody>
</table>

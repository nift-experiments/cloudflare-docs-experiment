---
cp9:
  canonical: https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/array/
  description: Scalar functions for manipulating arrays
  full_title: Array functions · Cloudflare Pipelines Docs
  head_html: <title>Array functions · Cloudflare Pipelines Docs</title><meta name="generator" content="Nift"><meta name="description" content="Scalar functions for manipulating arrays"><link rel="canonical" href="https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/array/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/array/index.md"><meta property="og:title" content="Array functions · Cloudflare Pipelines Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Scalar functions for manipulating arrays"><meta property="og:url" content="https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/array/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pipelines"><meta name="algolia_product_filter" content="Pipelines"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_additional_products" content="Pipelines"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/array/#page","headline":"Array functions \u00b7 Cloudflare Pipelines Docs","description":"Scalar functions for manipulating arrays","url":"https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/array/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pipelines/sql-reference/scalar-functions/array/
  schema: 1
---
<p><em>Cloudflare Pipelines scalar function implementations are based on
<a href="https://arrow.apache.org/datafusion/">Apache DataFusion</a> (via <a href="https://www.arroyo.dev/">Arroyo</a>) and these docs are derived from
the DataFusion function reference.</em></p>
<h2 id="array-append"><code>array_append</code></h2>
<p>Appends an element to the end of an array.</p>
<pre tabindex="0"><code>array_append(array, element)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
<li><strong>element</strong>: Element to append to the array.</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select array_append([1, 2, 3], 4);&#10;&#43;--------------------------------------+&#10;| array_append(List([1,2,3]),Int64(4)) |&#10;&#43;--------------------------------------+&#10;| [1, 2, 3, 4]                         |&#10;&#43;--------------------------------------+&#10;</code></pre>
<p><strong>Aliases</strong></p>
<ul>
<li>array_push_back</li>
<li>list_append</li>
<li>list_push_back</li>
</ul>
<h2 id="array-sort"><code>array_sort</code></h2>
<p>Sort array.</p>
<pre tabindex="0"><code>array_sort(array, desc, nulls_first)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
<li><strong>desc</strong>: Whether to sort in descending order(<code>ASC</code> or <code>DESC</code>).</li>
<li><strong>nulls_first</strong>: Whether to sort nulls first(<code>NULLS FIRST</code> or <code>NULLS LAST</code>).</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select array_sort([3, 1, 2]);&#10;&#43;-----------------------------+&#10;| array_sort(List([3,1,2]))   |&#10;&#43;-----------------------------+&#10;| [1, 2, 3]                   |&#10;&#43;-----------------------------+&#10;</code></pre>
<p><strong>Aliases</strong></p>
<ul>
<li>list_sort</li>
</ul>
<h2 id="array-resize"><code>array_resize</code></h2>
<p>Resizes the list to contain size elements. Initializes new elements with value or empty if value is not set.</p>
<pre tabindex="0"><code>array_resize(array, size, value)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
<li><strong>size</strong>: New size of given array.</li>
<li><strong>value</strong>: Defines new elements' value or empty if value is not set.</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select array_resize([1, 2, 3], 5, 0);&#10;&#43;-------------------------------------+&#10;| array_resize(List([1,2,3],5,0))     |&#10;&#43;-------------------------------------+&#10;| [1, 2, 3, 0, 0]                     |&#10;&#43;-------------------------------------+&#10;</code></pre>
<p><strong>Aliases</strong></p>
<ul>
<li>list_resize</li>
</ul>
<h2 id="array-cat"><code>array_cat</code></h2>
<p><em>Alias of <a href="#array_concat">array_concat</a>.</em></p>
<h2 id="array-concat"><code>array_concat</code></h2>
<p>Concatenates arrays.</p>
<pre tabindex="0"><code>array_concat(array[, ..., array_n])&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array</strong>: Array expression to concatenate.
Can be a constant, column, or function, and any combination of array operators.</li>
<li><strong>array_n</strong>: Subsequent array column or literal array to concatenate.</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select array_concat([1, 2], [3, 4], [5, 6]);&#10;&#43;---------------------------------------------------+&#10;| array_concat(List([1,2]),List([3,4]),List([5,6])) |&#10;&#43;---------------------------------------------------+&#10;| [1, 2, 3, 4, 5, 6]                                |&#10;&#43;---------------------------------------------------+&#10;</code></pre>
<p><strong>Aliases</strong></p>
<ul>
<li>array_cat</li>
<li>list_cat</li>
<li>list_concat</li>
</ul>
<h2 id="array-contains"><code>array_contains</code></h2>
<p><em>Alias of <a href="#array_has">array_has</a>.</em></p>
<h2 id="array-has"><code>array_has</code></h2>
<p>Returns true if the array contains the element</p>
<pre tabindex="0"><code>array_has(array, element)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
<li><strong>element</strong>: Scalar or Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
</ul>
<p><strong>Aliases</strong></p>
<ul>
<li>list_has</li>
</ul>
<h2 id="array-has-all"><code>array_has_all</code></h2>
<p>Returns true if all elements of sub-array exist in array</p>
<pre tabindex="0"><code>array_has_all(array, sub-array)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
<li><strong>sub-array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
</ul>
<p><strong>Aliases</strong></p>
<ul>
<li>list_has_all</li>
</ul>
<h2 id="array-has-any"><code>array_has_any</code></h2>
<p>Returns true if any elements exist in both arrays</p>
<pre tabindex="0"><code>array_has_any(array, sub-array)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
<li><strong>sub-array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
</ul>
<p><strong>Aliases</strong></p>
<ul>
<li>list_has_any</li>
</ul>
<h2 id="array-dims"><code>array_dims</code></h2>
<p>Returns an array of the array's dimensions.</p>
<pre tabindex="0"><code>array_dims(array)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select array_dims([[1, 2, 3], [4, 5, 6]]);&#10;&#43;---------------------------------+&#10;| array_dims(List([1,2,3,4,5,6])) |&#10;&#43;---------------------------------+&#10;| [2, 3]                          |&#10;&#43;---------------------------------+&#10;</code></pre>
<p><strong>Aliases</strong></p>
<ul>
<li>list_dims</li>
</ul>
<h2 id="array-distinct"><code>array_distinct</code></h2>
<p>Returns distinct values from the array after removing duplicates.</p>
<pre tabindex="0"><code>array_distinct(array)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select array_distinct([1, 3, 2, 3, 1, 2, 4]);&#10;&#43;---------------------------------+&#10;| array_distinct(List([1,2,3,4])) |&#10;&#43;---------------------------------+&#10;| [1, 2, 3, 4]                    |&#10;&#43;---------------------------------+&#10;</code></pre>
<p><strong>Aliases</strong></p>
<ul>
<li>list_distinct</li>
</ul>
<h2 id="array-element"><code>array_element</code></h2>
<p>Extracts the element with the index n from the array.</p>
<pre tabindex="0"><code>array_element(array, index)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
<li><strong>index</strong>: Index to extract the element from the array.</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select array_element([1, 2, 3, 4], 3);&#10;&#43;-----------------------------------------+&#10;| array_element(List([1,2,3,4]),Int64(3)) |&#10;&#43;-----------------------------------------+&#10;| 3                                       |&#10;&#43;-----------------------------------------+&#10;</code></pre>
<p><strong>Aliases</strong></p>
<ul>
<li>array_extract</li>
<li>list_element</li>
<li>list_extract</li>
</ul>
<h2 id="array-extract"><code>array_extract</code></h2>
<p><em>Alias of <a href="#array_element">array_element</a>.</em></p>
<h2 id="array-fill"><code>array_fill</code></h2>
<p>Returns an array filled with copies of the given value.</p>
<p>DEPRECATED: use <code>array_repeat</code> instead!</p>
<pre tabindex="0"><code>array_fill(element, array)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
<li><strong>element</strong>: Element to copy to the array.</li>
</ul>
<h2 id="flatten"><code>flatten</code></h2>
<p>Converts an array of arrays to a flat array</p>
<ul>
<li>Applies to any depth of nested arrays</li>
<li>Does not change arrays that are already flat</li>
</ul>
<p>The flattened array contains all the elements from all source arrays.</p>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array</strong>: Array expression
Can be a constant, column, or function, and any combination of array operators.</li>
</ul>
<pre tabindex="0"><code>flatten(array)&#10;</code></pre>
<h2 id="array-indexof"><code>array_indexof</code></h2>
<p><em>Alias of <a href="#array_position">array_position</a>.</em></p>
<h2 id="array-intersect"><code>array_intersect</code></h2>
<p>Returns an array of elements in the intersection of array1 and array2.</p>
<pre tabindex="0"><code>array_intersect(array1, array2)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array1</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
<li><strong>array2</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select array_intersect([1, 2, 3, 4], [5, 6, 3, 4]);&#10;&#43;----------------------------------------------------+&#10;| array_intersect([1, 2, 3, 4], [5, 6, 3, 4]);       |&#10;&#43;----------------------------------------------------+&#10;| [3, 4]                                             |&#10;&#43;----------------------------------------------------+&#10;&gt; select array_intersect([1, 2, 3, 4], [5, 6, 7, 8]);&#10;&#43;----------------------------------------------------+&#10;| array_intersect([1, 2, 3, 4], [5, 6, 7, 8]);       |&#10;&#43;----------------------------------------------------+&#10;| []                                                 |&#10;&#43;----------------------------------------------------+&#10;</code></pre>
<hr />
<p><strong>Aliases</strong></p>
<ul>
<li>list_intersect</li>
</ul>
<h2 id="array-join"><code>array_join</code></h2>
<p><em>Alias of <a href="#array_to_string">array_to_string</a>.</em></p>
<h2 id="array-length"><code>array_length</code></h2>
<p>Returns the length of the array dimension.</p>
<pre tabindex="0"><code>array_length(array, dimension)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
<li><strong>dimension</strong>: Array dimension.</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select array_length([1, 2, 3, 4, 5]);&#10;&#43;---------------------------------+&#10;| array_length(List([1,2,3,4,5])) |&#10;&#43;---------------------------------+&#10;| 5                               |&#10;&#43;---------------------------------+&#10;</code></pre>
<p><strong>Aliases</strong></p>
<ul>
<li>list_length</li>
</ul>
<h2 id="array-ndims"><code>array_ndims</code></h2>
<p>Returns the number of dimensions of the array.</p>
<pre tabindex="0"><code>array_ndims(array, element)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select array_ndims([[1, 2, 3], [4, 5, 6]]);&#10;&#43;----------------------------------+&#10;| array_ndims(List([1,2,3,4,5,6])) |&#10;&#43;----------------------------------+&#10;| 2                                |&#10;&#43;----------------------------------+&#10;</code></pre>
<p><strong>Aliases</strong></p>
<ul>
<li>list_ndims</li>
</ul>
<h2 id="array-prepend"><code>array_prepend</code></h2>
<p>Prepends an element to the beginning of an array.</p>
<pre tabindex="0"><code>array_prepend(element, array)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>element</strong>: Element to prepend to the array.</li>
<li><strong>array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select array_prepend(1, [2, 3, 4]);&#10;&#43;---------------------------------------+&#10;| array_prepend(Int64(1),List([2,3,4])) |&#10;&#43;---------------------------------------+&#10;| [1, 2, 3, 4]                          |&#10;&#43;---------------------------------------+&#10;</code></pre>
<p><strong>Aliases</strong></p>
<ul>
<li>array_push_front</li>
<li>list_prepend</li>
<li>list_push_front</li>
</ul>
<h2 id="array-pop-front"><code>array_pop_front</code></h2>
<p>Returns the array without the first element.</p>
<pre tabindex="0"><code>array_pop_front(array)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select array_pop_front([1, 2, 3]);&#10;&#43;-------------------------------+&#10;| array_pop_front(List([1,2,3])) |&#10;&#43;-------------------------------+&#10;| [2, 3]                        |&#10;&#43;-------------------------------+&#10;</code></pre>
<p><strong>Aliases</strong></p>
<ul>
<li>list_pop_front</li>
</ul>
<h2 id="array-pop-back"><code>array_pop_back</code></h2>
<p>Returns the array without the last element.</p>
<pre tabindex="0"><code>array_pop_back(array)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select array_pop_back([1, 2, 3]);&#10;&#43;-------------------------------+&#10;| array_pop_back(List([1,2,3])) |&#10;&#43;-------------------------------+&#10;| [1, 2]                        |&#10;&#43;-------------------------------+&#10;</code></pre>
<p><strong>Aliases</strong></p>
<ul>
<li>list_pop_back</li>
</ul>
<h2 id="array-position"><code>array_position</code></h2>
<p>Returns the position of the first occurrence of the specified element in the array.</p>
<pre tabindex="0"><code>array_position(array, element)&#10;array_position(array, element, index)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
<li><strong>element</strong>: Element to search for position in the array.</li>
<li><strong>index</strong>: Index at which to start searching.</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select array_position([1, 2, 2, 3, 1, 4], 2);&#10;&#43;----------------------------------------------+&#10;| array_position(List([1,2,2,3,1,4]),Int64(2)) |&#10;&#43;----------------------------------------------+&#10;| 2                                            |&#10;&#43;----------------------------------------------+&#10;</code></pre>
<p><strong>Aliases</strong></p>
<ul>
<li>array_indexof</li>
<li>list_indexof</li>
<li>list_position</li>
</ul>
<h2 id="array-positions"><code>array_positions</code></h2>
<p>Searches for an element in the array, returns all occurrences.</p>
<pre tabindex="0"><code>array_positions(array, element)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
<li><strong>element</strong>: Element to search for positions in the array.</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select array_positions([1, 2, 2, 3, 1, 4], 2);&#10;&#43;-----------------------------------------------+&#10;| array_positions(List([1,2,2,3,1,4]),Int64(2)) |&#10;&#43;-----------------------------------------------+&#10;| [2, 3]                                        |&#10;&#43;-----------------------------------------------+&#10;</code></pre>
<p><strong>Aliases</strong></p>
<ul>
<li>list_positions</li>
</ul>
<h2 id="array-push-back"><code>array_push_back</code></h2>
<p><em>Alias of <a href="#array_append">array_append</a>.</em></p>
<h2 id="array-push-front"><code>array_push_front</code></h2>
<p><em>Alias of <a href="#array_prepend">array_prepend</a>.</em></p>
<h2 id="array-repeat"><code>array_repeat</code></h2>
<p>Returns an array containing element <code>count</code> times.</p>
<pre tabindex="0"><code>array_repeat(element, count)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>element</strong>: Element expression.
Can be a constant, column, or function, and any combination of array operators.</li>
<li><strong>count</strong>: Value of how many times to repeat the element.</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select array_repeat(1, 3);&#10;&#43;---------------------------------+&#10;| array_repeat(Int64(1),Int64(3)) |&#10;&#43;---------------------------------+&#10;| [1, 1, 1]                       |&#10;&#43;---------------------------------+&#10;</code></pre>
<pre tabindex="0"><code>&gt; select array_repeat([1, 2], 2);&#10;&#43;------------------------------------+&#10;| array_repeat(List([1,2]),Int64(2)) |&#10;&#43;------------------------------------+&#10;| [[1, 2], [1, 2]]                   |&#10;&#43;------------------------------------+&#10;</code></pre>
<p><strong>Aliases</strong></p>
<ul>
<li>list_repeat</li>
</ul>
<h2 id="array-remove"><code>array_remove</code></h2>
<p>Removes the first element from the array equal to the given value.</p>
<pre tabindex="0"><code>array_remove(array, element)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
<li><strong>element</strong>: Element to be removed from the array.</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select array_remove([1, 2, 2, 3, 2, 1, 4], 2);&#10;&#43;----------------------------------------------+&#10;| array_remove(List([1,2,2,3,2,1,4]),Int64(2)) |&#10;&#43;----------------------------------------------+&#10;| [1, 2, 3, 2, 1, 4]                           |&#10;&#43;----------------------------------------------+&#10;</code></pre>
<p><strong>Aliases</strong></p>
<ul>
<li>list_remove</li>
</ul>
<h2 id="array-remove-n"><code>array_remove_n</code></h2>
<p>Removes the first <code>max</code> elements from the array equal to the given value.</p>
<pre tabindex="0"><code>array_remove_n(array, element, max)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
<li><strong>element</strong>: Element to be removed from the array.</li>
<li><strong>max</strong>: Number of first occurrences to remove.</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select array_remove_n([1, 2, 2, 3, 2, 1, 4], 2, 2);&#10;&#43;---------------------------------------------------------+&#10;| array_remove_n(List([1,2,2,3,2,1,4]),Int64(2),Int64(2)) |&#10;&#43;---------------------------------------------------------+&#10;| [1, 3, 2, 1, 4]                                         |&#10;&#43;---------------------------------------------------------+&#10;</code></pre>
<p><strong>Aliases</strong></p>
<ul>
<li>list_remove_n</li>
</ul>
<h2 id="array-remove-all"><code>array_remove_all</code></h2>
<p>Removes all elements from the array equal to the given value.</p>
<pre tabindex="0"><code>array_remove_all(array, element)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
<li><strong>element</strong>: Element to be removed from the array.</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select array_remove_all([1, 2, 2, 3, 2, 1, 4], 2);&#10;&#43;--------------------------------------------------+&#10;| array_remove_all(List([1,2,2,3,2,1,4]),Int64(2)) |&#10;&#43;--------------------------------------------------+&#10;| [1, 3, 1, 4]                                     |&#10;&#43;--------------------------------------------------+&#10;</code></pre>
<p><strong>Aliases</strong></p>
<ul>
<li>list_remove_all</li>
</ul>
<h2 id="array-replace"><code>array_replace</code></h2>
<p>Replaces the first occurrence of the specified element with another specified element.</p>
<pre tabindex="0"><code>array_replace(array, from, to)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
<li><strong>from</strong>: Initial element.</li>
<li><strong>to</strong>: Final element.</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select array_replace([1, 2, 2, 3, 2, 1, 4], 2, 5);&#10;&#43;--------------------------------------------------------+&#10;| array_replace(List([1,2,2,3,2,1,4]),Int64(2),Int64(5)) |&#10;&#43;--------------------------------------------------------+&#10;| [1, 5, 2, 3, 2, 1, 4]                                  |&#10;&#43;--------------------------------------------------------+&#10;</code></pre>
<p><strong>Aliases</strong></p>
<ul>
<li>list_replace</li>
</ul>
<h2 id="array-replace-n"><code>array_replace_n</code></h2>
<p>Replaces the first <code>max</code> occurrences of the specified element with another specified element.</p>
<pre tabindex="0"><code>array_replace_n(array, from, to, max)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
<li><strong>from</strong>: Initial element.</li>
<li><strong>to</strong>: Final element.</li>
<li><strong>max</strong>: Number of first occurrences to replace.</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select array_replace_n([1, 2, 2, 3, 2, 1, 4], 2, 5, 2);&#10;&#43;-------------------------------------------------------------------+&#10;| array_replace_n(List([1,2,2,3,2,1,4]),Int64(2),Int64(5),Int64(2)) |&#10;&#43;-------------------------------------------------------------------+&#10;| [1, 5, 5, 3, 2, 1, 4]                                             |&#10;&#43;-------------------------------------------------------------------+&#10;</code></pre>
<p><strong>Aliases</strong></p>
<ul>
<li>list_replace_n</li>
</ul>
<h2 id="array-replace-all"><code>array_replace_all</code></h2>
<p>Replaces all occurrences of the specified element with another specified element.</p>
<pre tabindex="0"><code>array_replace_all(array, from, to)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
<li><strong>from</strong>: Initial element.</li>
<li><strong>to</strong>: Final element.</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select array_replace_all([1, 2, 2, 3, 2, 1, 4], 2, 5);&#10;&#43;------------------------------------------------------------+&#10;| array_replace_all(List([1,2,2,3,2,1,4]),Int64(2),Int64(5)) |&#10;&#43;------------------------------------------------------------+&#10;| [1, 5, 5, 3, 5, 1, 4]                                      |&#10;&#43;------------------------------------------------------------+&#10;</code></pre>
<p><strong>Aliases</strong></p>
<ul>
<li>list_replace_all</li>
</ul>
<h2 id="array-reverse"><code>array_reverse</code></h2>
<p>Returns the array with the order of the elements reversed.</p>
<pre tabindex="0"><code>array_reverse(array)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select array_reverse([1, 2, 3, 4]);&#10;&#43;------------------------------------------------------------+&#10;| array_reverse(List([1, 2, 3, 4]))                          |&#10;&#43;------------------------------------------------------------+&#10;| [4, 3, 2, 1]                                               |&#10;&#43;------------------------------------------------------------+&#10;</code></pre>
<p><strong>Aliases</strong></p>
<ul>
<li>list_reverse</li>
</ul>
<h2 id="array-slice"><code>array_slice</code></h2>
<p>Returns a slice of the array based on 1-indexed start and end positions.</p>
<pre tabindex="0"><code>array_slice(array, begin, end)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
<li><strong>begin</strong>: Index of the first element.
If negative, it counts backward from the end of the array.</li>
<li><strong>end</strong>: Index of the last element.
If negative, it counts backward from the end of the array.</li>
<li><strong>stride</strong>: Stride of the array slice. The default is 1.</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select array_slice([1, 2, 3, 4, 5, 6, 7, 8], 3, 6);&#10;&#43;--------------------------------------------------------+&#10;| array_slice(List([1,2,3,4,5,6,7,8]),Int64(3),Int64(6)) |&#10;&#43;--------------------------------------------------------+&#10;| [3, 4, 5, 6]                                           |&#10;&#43;--------------------------------------------------------+&#10;</code></pre>
<p><strong>Aliases</strong></p>
<ul>
<li>list_slice</li>
</ul>
<h2 id="array-to-string"><code>array_to_string</code></h2>
<p>Converts each element to its text representation.</p>
<pre tabindex="0"><code>array_to_string(array, delimiter)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
<li><strong>delimiter</strong>: Array element separator.</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select array_to_string([[1, 2, 3, 4], [5, 6, 7, 8]], &#x27;,&#x27;);&#10;&#43;----------------------------------------------------+&#10;| array_to_string(List([1,2,3,4,5,6,7,8]),Utf8(&quot;,&quot;)) |&#10;&#43;----------------------------------------------------+&#10;| 1,2,3,4,5,6,7,8                                    |&#10;&#43;----------------------------------------------------+&#10;</code></pre>
<p><strong>Aliases</strong></p>
<ul>
<li>array_join</li>
<li>list_join</li>
<li>list_to_string</li>
</ul>
<h2 id="array-union"><code>array_union</code></h2>
<p>Returns an array of elements that are present in both arrays (all elements from both arrays) with out duplicates.</p>
<pre tabindex="0"><code>array_union(array1, array2)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array1</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
<li><strong>array2</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select array_union([1, 2, 3, 4], [5, 6, 3, 4]);&#10;&#43;----------------------------------------------------+&#10;| array_union([1, 2, 3, 4], [5, 6, 3, 4]);           |&#10;&#43;----------------------------------------------------+&#10;| [1, 2, 3, 4, 5, 6]                                 |&#10;&#43;----------------------------------------------------+&#10;&gt; select array_union([1, 2, 3, 4], [5, 6, 7, 8]);&#10;&#43;----------------------------------------------------+&#10;| array_union([1, 2, 3, 4], [5, 6, 7, 8]);           |&#10;&#43;----------------------------------------------------+&#10;| [1, 2, 3, 4, 5, 6, 7, 8]                           |&#10;&#43;----------------------------------------------------+&#10;</code></pre>
<hr />
<p><strong>Aliases</strong></p>
<ul>
<li>list_union</li>
</ul>
<h2 id="array-except"><code>array_except</code></h2>
<p>Returns an array of the elements that appear in the first array but not in the second.</p>
<pre tabindex="0"><code>array_except(array1, array2)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array1</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
<li><strong>array2</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select array_except([1, 2, 3, 4], [5, 6, 3, 4]);&#10;&#43;----------------------------------------------------+&#10;| array_except([1, 2, 3, 4], [5, 6, 3, 4]);           |&#10;&#43;----------------------------------------------------+&#10;| [1, 2]                                 |&#10;&#43;----------------------------------------------------+&#10;&gt; select array_except([1, 2, 3, 4], [3, 4, 5, 6]);&#10;&#43;----------------------------------------------------+&#10;| array_except([1, 2, 3, 4], [3, 4, 5, 6]);           |&#10;&#43;----------------------------------------------------+&#10;| [1, 2]                                 |&#10;&#43;----------------------------------------------------+&#10;</code></pre>
<hr />
<p><strong>Aliases</strong></p>
<ul>
<li>list_except</li>
</ul>
<h2 id="cardinality"><code>cardinality</code></h2>
<p>Returns the total number of elements in the array.</p>
<pre tabindex="0"><code>cardinality(array)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select cardinality([[1, 2, 3, 4], [5, 6, 7, 8]]);&#10;&#43;--------------------------------------+&#10;| cardinality(List([1,2,3,4,5,6,7,8])) |&#10;&#43;--------------------------------------+&#10;| 8                                    |&#10;&#43;--------------------------------------+&#10;</code></pre>
<h2 id="empty"><code>empty</code></h2>
<p>Returns 1 for an empty array or 0 for a non-empty array.</p>
<pre tabindex="0"><code>empty(array)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select empty([1]);&#10;&#43;------------------+&#10;| empty(List([1])) |&#10;&#43;------------------+&#10;| 0                |&#10;&#43;------------------+&#10;</code></pre>
<p><strong>Aliases</strong></p>
<ul>
<li>array_empty,</li>
<li>list_empty</li>
</ul>
<h2 id="generate-series"><code>generate_series</code></h2>
<p>Similar to the range function, but it includes the upper bound.</p>
<pre tabindex="0"><code>generate_series(start, stop, step)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>start</strong>: start of the range</li>
<li><strong>end</strong>: end of the range (included)</li>
<li><strong>step</strong>: increase by step (can not be 0)</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select generate_series(1,3);&#10;&#43;------------------------------------+&#10;| generate_series(Int64(1),Int64(3)) |&#10;&#43;------------------------------------+&#10;| [1, 2, 3]                          |&#10;&#43;------------------------------------+&#10;</code></pre>
<h2 id="list-append"><code>list_append</code></h2>
<p><em>Alias of <a href="#array_append">array_append</a>.</em></p>
<h2 id="list-cat"><code>list_cat</code></h2>
<p><em>Alias of <a href="#array_concat">array_concat</a>.</em></p>
<h2 id="list-concat"><code>list_concat</code></h2>
<p><em>Alias of <a href="#array_concat">array_concat</a>.</em></p>
<h2 id="list-dims"><code>list_dims</code></h2>
<p><em>Alias of <a href="#array_dims">array_dims</a>.</em></p>
<h2 id="list-distinct"><code>list_distinct</code></h2>
<p><em>Alias of <a href="#array_distinct">array_dims</a>.</em></p>
<h2 id="list-element"><code>list_element</code></h2>
<p><em>Alias of <a href="#array_element">array_element</a>.</em></p>
<h2 id="list-empty"><code>list_empty</code></h2>
<p><em>Alias of <a href="#empty">empty</a>.</em></p>
<h2 id="list-except"><code>list_except</code></h2>
<p><em>Alias of <a href="#array_except">array_element</a>.</em></p>
<h2 id="list-extract"><code>list_extract</code></h2>
<p><em>Alias of <a href="#array_element">array_element</a>.</em></p>
<h2 id="list-has"><code>list_has</code></h2>
<p><em>Alias of <a href="#array_has">array_has</a>.</em></p>
<h2 id="list-has-all"><code>list_has_all</code></h2>
<p><em>Alias of <a href="#array_has_all">array_has_all</a>.</em></p>
<h2 id="list-has-any"><code>list_has_any</code></h2>
<p><em>Alias of <a href="#array_has_any">array_has_any</a>.</em></p>
<h2 id="list-indexof"><code>list_indexof</code></h2>
<p><em>Alias of <a href="#array_position">array_position</a>.</em></p>
<h2 id="list-intersect"><code>list_intersect</code></h2>
<p><em>Alias of <a href="#array_intersect">array_position</a>.</em></p>
<h2 id="list-join"><code>list_join</code></h2>
<p><em>Alias of <a href="#array_to_string">array_to_string</a>.</em></p>
<h2 id="list-length"><code>list_length</code></h2>
<p><em>Alias of <a href="#array_length">array_length</a>.</em></p>
<h2 id="list-ndims"><code>list_ndims</code></h2>
<p><em>Alias of <a href="#array_ndims">array_ndims</a>.</em></p>
<h2 id="list-prepend"><code>list_prepend</code></h2>
<p><em>Alias of <a href="#array_prepend">array_prepend</a>.</em></p>
<h2 id="list-pop-back"><code>list_pop_back</code></h2>
<p><em>Alias of <a href="#array_pop_back">array_pop_back</a>.</em></p>
<h2 id="list-pop-front"><code>list_pop_front</code></h2>
<p><em>Alias of <a href="#array_pop_front">array_pop_front</a>.</em></p>
<h2 id="list-position"><code>list_position</code></h2>
<p><em>Alias of <a href="#array_position">array_position</a>.</em></p>
<h2 id="list-positions"><code>list_positions</code></h2>
<p><em>Alias of <a href="#array_positions">array_positions</a>.</em></p>
<h2 id="list-push-back"><code>list_push_back</code></h2>
<p><em>Alias of <a href="#array_append">array_append</a>.</em></p>
<h2 id="list-push-front"><code>list_push_front</code></h2>
<p><em>Alias of <a href="#array_prepend">array_prepend</a>.</em></p>
<h2 id="list-repeat"><code>list_repeat</code></h2>
<p><em>Alias of <a href="#array_repeat">array_repeat</a>.</em></p>
<h2 id="list-resize"><code>list_resize</code></h2>
<p><em>Alias of <a href="#array_resize">array_resize</a>.</em></p>
<h2 id="list-remove"><code>list_remove</code></h2>
<p><em>Alias of <a href="#array_remove">array_remove</a>.</em></p>
<h2 id="list-remove-n"><code>list_remove_n</code></h2>
<p><em>Alias of <a href="#array_remove_n">array_remove_n</a>.</em></p>
<h2 id="list-remove-all"><code>list_remove_all</code></h2>
<p><em>Alias of <a href="#array_remove_all">array_remove_all</a>.</em></p>
<h2 id="list-replace"><code>list_replace</code></h2>
<p><em>Alias of <a href="#array_replace">array_replace</a>.</em></p>
<h2 id="list-replace-n"><code>list_replace_n</code></h2>
<p><em>Alias of <a href="#array_replace_n">array_replace_n</a>.</em></p>
<h2 id="list-replace-all"><code>list_replace_all</code></h2>
<p><em>Alias of <a href="#array_replace_all">array_replace_all</a>.</em></p>
<h2 id="list-reverse"><code>list_reverse</code></h2>
<p><em>Alias of <a href="#array_reverse">array_reverse</a>.</em></p>
<h2 id="list-slice"><code>list_slice</code></h2>
<p><em>Alias of <a href="#array_slice">array_slice</a>.</em></p>
<h2 id="list-sort"><code>list_sort</code></h2>
<p><em>Alias of <a href="#array_sort">array_sort</a>.</em></p>
<h2 id="list-to-string"><code>list_to_string</code></h2>
<p><em>Alias of <a href="#array_to_string">array_to_string</a>.</em></p>
<h2 id="list-union"><code>list_union</code></h2>
<p><em>Alias of <a href="#array_union">array_union</a>.</em></p>
<h2 id="make-array"><code>make_array</code></h2>
<p>Returns an Arrow array using the specified input expressions.</p>
<pre tabindex="0"><code>make_array(expression1[, ..., expression_n])&#10;</code></pre>
<h2 id="array-empty"><code>array_empty</code></h2>
<p><em>Alias of <a href="#empty">empty</a>.</em></p>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression_n</strong>: Expression to include in the output array.
Can be a constant, column, or function, and any combination of arithmetic or
string operators.</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select make_array(1, 2, 3, 4, 5);&#10;&#43;----------------------------------------------------------+&#10;| make_array(Int64(1),Int64(2),Int64(3),Int64(4),Int64(5)) |&#10;&#43;----------------------------------------------------------+&#10;| [1, 2, 3, 4, 5]                                          |&#10;&#43;----------------------------------------------------------+&#10;</code></pre>
<p><strong>Aliases</strong></p>
<ul>
<li>make_list</li>
</ul>
<h2 id="make-list"><code>make_list</code></h2>
<p><em>Alias of <a href="#make_array">make_array</a>.</em></p>
<h2 id="string-to-array"><code>string_to_array</code></h2>
<p>Splits a string in to an array of substrings based on a delimiter. Any substrings matching the optional <code>null_str</code> argument are replaced with NULL.
<code>SELECT string_to_array('abc##def', '##')</code> or <code>SELECT string_to_array('abc def', ' ', 'def')</code></p>
<pre tabindex="0"><code>starts_with(str, delimiter[, null_str])&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to split.</li>
<li><strong>delimiter</strong>: Delimiter string to split on.</li>
<li><strong>null_str</strong>: Substring values to be replaced with <code>NULL</code></li>
</ul>
<p><strong>Aliases</strong></p>
<ul>
<li>string_to_list</li>
</ul>
<h2 id="string-to-list"><code>string_to_list</code></h2>
<p><em>Alias of <a href="#string_to_array">string_to_array</a>.</em></p>
<h2 id="trim-array"><code>trim_array</code></h2>
<p>Removes the last n elements from the array.</p>
<p>DEPRECATED: use <code>array_slice</code> instead!</p>
<pre tabindex="0"><code>trim_array(array, n)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>array</strong>: Array expression.
Can be a constant, column, or function, and any combination of array operators.</li>
<li><strong>n</strong>: Element to trim the array.</li>
</ul>
<h2 id="range"><code>range</code></h2>
<p>Returns an Arrow array between start and stop with step. <code>SELECT range(2, 10, 3) -&gt; [2, 5, 8]</code> or <code>SELECT range(DATE '1992-09-01', DATE '1993-03-01', INTERVAL '1' MONTH);</code></p>
<p>The range start..end contains all values with start &lt;= x &lt; end. It is empty if start &gt;= end.</p>
<p>Step can not be 0 (then the range will be nonsense.).</p>
<p>Note that when the required range is a number, it accepts (stop), (start, stop), and (start, stop, step) as parameters, but when the required range is a date, it must be 3 non-NULL parameters.
For example,</p>
<pre tabindex="0"><code class="language-sql">SELECT range(3);&#10;SELECT range(1,5);&#10;SELECT range(1,5,1);&#10;</code></pre>
<p>are allowed in number ranges</p>
<p>but in date ranges, only</p>
<pre tabindex="0"><code class="language-sql">SELECT range(DATE &#x27;1992-09-01&#x27;, DATE &#x27;1993-03-01&#x27;, INTERVAL &#x27;1&#x27; MONTH);&#10;</code></pre>
<p>is allowed, and</p>
<pre tabindex="0"><code class="language-sql">SELECT range(DATE &#x27;1992-09-01&#x27;, DATE &#x27;1993-03-01&#x27;, NULL);&#10;SELECT range(NULL, DATE &#x27;1993-03-01&#x27;, INTERVAL &#x27;1&#x27; MONTH);&#10;SELECT range(DATE &#x27;1992-09-01&#x27;, NULL, INTERVAL &#x27;1&#x27; MONTH);&#10;</code></pre>
<p>are not allowed</p>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>start</strong>: start of the range</li>
<li><strong>end</strong>: end of the range (not included)</li>
<li><strong>step</strong>: increase by step (can not be 0)</li>
</ul>
<p><strong>Aliases</strong></p>
<ul>
<li>generate_series</li>
</ul>

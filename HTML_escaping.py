# Implementing HTML Escaping
def escape_html(s):
    for (i, o) in (("&", "&amp;"),
                   (">", "&gt;"),
                   ("<", "&lt;"),
                   ('"', "&quot;")):
        s = s.replace(i, o)
    return s
   
   
# Refactored with cgi script
# import cgi
# def escape_html(s):
#     return cgi.escape(s, quote = True)


print escape_html('>')
# &gt;
print escape_html('<')
# &lt;
print escape_html('"')
# &quot;
print escape_html("&")
# &amp;
print escape_html("<b>html!</b>")
# &lt;b&gt;html!&lt;/b&gt;
print escape_html('"hello, & = &amp;"')
# &quot;hello, &amp; = &amp;amp;&quot;

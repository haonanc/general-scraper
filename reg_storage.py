
# Extract data from courseForum
# url_main = 'https://rabi.phys.virginia.edu/mySIS/CC2/'
# web_regexp_config2 = """href=.(.*\.html)"""
# web_regexp_config = """<a href=['"](.*)amp;(.*)amp;(.*)["']"""
# url_prefix = ['https://rabi.phys.virginia.edu/mySIS/CC2/']
# regexp_class = """\('([A-Z]{2,4})','(\d{2,4})'\);">(.+)<\/td><\/tr>"""
# regexp_pro = """([a-zA-Z]{2,}[- ]?[0-9]{4}).*<strong>([A-Za-z ]+).*Name=([A-Z][a-z]+ [A-Z][a-z]+)"""
# regexp_des = """<td class="CourseNum">(.*)<\/td><td class="CourseName">.*\n.*class="CourseDescription">(.*?)<"""

# Extract data from lous list
#\('([A-Z]{2,4})','(\d{2,4})'\);">(.+)<\/td><\/tr>
#([a-zA-Z]{2,}[- ]?[0-9]{4}).*<strong>([A-Za-z ]+).*Name=([A-Z][a-z]+ [A-Z][a-z]+)
#([a-zA-Z]{2,}[- ]?[0-9]{4}).*<strong>([A-Z][a-z]+ [A-Z][a-z]+).*Name=([A-Z][a-z]+ [A-Z][a-z]+)
#\('([A-Z]{2,4})','(\d{2,4})'\);">([a-zA-Z \-,]+)<
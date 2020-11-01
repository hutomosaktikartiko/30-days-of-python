msg_template = """Hello {name},
Thank you for joining {website}. We are verry
happy to have you with us.
"""

def format_msg(my_name = "Hutomo",website = "manusia.com"):
    my_msg = msg_template.format(name=my_name, website=website)
    return my_msg
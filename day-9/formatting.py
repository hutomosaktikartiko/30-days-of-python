msg_template = """Hello {my_name},
Thank you for joining {website}. We are verry
happy to have you with us.
"""

def format_msg(my_name = "Hutomo",website = "manusia.com"):
    my_msg = msg_template.format(my_name=my_name, website=website)
    return my_msg
"""Example of using the colorlogging library."""

import colorlogging

colorlogging.show_info("This is a status message", important=True)
colorlogging.show_warning("This is a warning message")
colorlogging.show_error("This is an error message")

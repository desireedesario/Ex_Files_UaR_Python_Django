#runs commands associated with our project
#basically runs commands
#COMMONLY LEFT ALONE AFTER BEING CREATED THROUGH DJANGO
#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "firstdjango.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

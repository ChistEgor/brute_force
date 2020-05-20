"""
This is the main file where you can select the method
(but in general any way you want :)) to search for a password or logins.
Of course you can add a new password/logins search method
"""

from components import logics, generators, some_requests


logics.hack_n_password_for_all_logins(  # here you change the name of the search method
    generators.generate_logins,
    generators.generate_passwords_brute_force,  # here you change to generate_popular_passwords or ...
    some_requests.request_local_server,
)

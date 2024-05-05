"""
This script runs the application using a development server.
"""
import io
import pstats

import bottle
import os
import sys
import cProfile

# routes contains the HTTP handlers for our server and must be imported.
# import routes

# def profile(func):
#     """Decorator for run function profile"""
#     def wrapper(*args, **kwargs):
#         profile_filename = func.__name__ + '.prof'
#         profiler = cProfile.Profile()
#         result = profiler.runcall(func, *args, **kwargs)
#         profiler.dump_stats(profile_filename)
#         return result
#     return wrapper

def wsgi_app():
    """Returns the application to make available through wfastcgi. This is used
    when the site is published to Microsoft Azure."""
    return bottle.default_app()

# @profile
def main():
    if '--debug' in sys.argv[1:] or 'SERVER_DEBUG' in os.environ:
        # Debug mode will enable more verbose output in the console window.
        # It must be set at the beginning of the script.
        bottle.debug(True)

    if __name__ == '__main__':
        PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
        STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static').replace('\\', '/')
        HOST = os.environ.get('SERVER_HOST', 'localhost')
        try:
            PORT = int(os.environ.get('SERVER_PORT', '5555'))
        except ValueError:
            PORT = 5555

        @bottle.route('/static/<filepath:path>')
        def server_static(filepath):
            """Handler for static files, used with the development server.
            When running under a production server such as IIS or Apache,
            the server should be configured to serve the static files."""
            return bottle.static_file(filepath, root=STATIC_ROOT)

        # Starts a local test server.
        bottle.run(server='wsgiref', host=HOST, port=PORT)

# main = profile(main())

pr = cProfile.Profile()
pr.enable()

my_result = main()

pr.disable()
s = io.StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
ps.print_stats()

with open('test.txt', 'w+') as f:
    f.write(s.getvalue())

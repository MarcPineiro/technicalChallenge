from django.shortcuts import render

def handle_error(request, error_message):
    """
    Handle errors and render the error page.

    :param request: Request object
    :param error_message: Error message to display
    :return: Rendered error page
    """
    return render(request, 'error.html', {'error_message': error_message})

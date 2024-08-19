from colorama import Fore, Style


def error_answer(answer: str) -> str:
    return Fore.RED + answer + Style.RESET_ALL


# print valid bot answer
def print_valid(answer: str) -> None:
    print(Fore.GREEN + answer + Style.RESET_ALL)


# print valid bot answer
def print_error(answer: str) -> None:
    print(error_answer(answer))


# wrapper for input
def colored_input(request: str) -> str:
    # add color for request
    print(colored_request + request, end='')

    # add color for input
    user_input = input(colored_user_input)

    # reset colors after user input response
    print(Style.RESET_ALL, end='')

    return user_input


colored_request = Style.RESET_ALL + Fore.CYAN + "Enter a command: "
colored_user_input = Style.RESET_ALL + Fore.YELLOW

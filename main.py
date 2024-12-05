
from colorama import Fore, Style
def mostrar_menu():
    print(Fore.CYAN + "======= MENÚ PRINCIPAL =======" + Style.RESET_ALL)
    print(Fore.CYAN + "SELECCIONA UNA OPCION MEDIANTE UN NUMERO:" + Style.RESET_ALL)
    print(Fore.GREEN + "1. Añadir tarea" + Style.RESET_ALL)
    print(Fore.WHITE + "2. Ver tareas" + Style.RESET_ALL)
    print(Fore.YELLOW + "3. Actualizar tarea" + Style.RESET_ALL)
    print(Fore.BLUE + "4. Eliminar tarea" + Style.RESET_ALL)
    print(Fore.RED + "5. Salir" + Style.RESET_ALL)

mostrar_menu()

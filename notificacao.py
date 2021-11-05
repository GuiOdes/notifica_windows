from win10toast import ToastNotifier

# inicialização
toaster = ToastNotifier()

titulo = input("Título da notificação: ")
mensagem = input("Mensagem da notificação: ")

toaster.show_toast(titulo, mensagem, threaded=True, icon_path=None, duration=3)
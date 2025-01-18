import flet as ft


def principal(janela: ft.Page):
    janela.title = "Aula 2 Flet"
    janela.bgcolor = ft.colors.CYAN

    #____________________________________________________________________________________________________Mensagem do botão
    mensagem = ft.Text(
        value="",
        color=ft.colors.WHITE
    )
    
    def exibir_mensagem(e):
        mensagem.value = "Olá senhor estudante"
        janela.update()
    #____________________________________________________________________________________________________Mensagem do botão

    #___________________________________________________________________________________________________Container do Titulo 
    titulo = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    value="Aula 2 Flet",
                    color=ft.colors.WHITE,
                    size=30,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.ElevatedButton(
                    text="Clique em Mim",
                    bgcolor=ft.colors.GREEN,
                    color=ft.colors.WHITE,
                    on_click=exibir_mensagem
                )
            ]
        ),
        alignment=ft.alignment.center,
        margin=10,
        padding=10,
        bgcolor=ft.Colors.AMBER,
        width=250,
        height=250,
        border_radius=10
    )
    
    janela.add(
        titulo,
        mensagem
    )
#______________________________________________________________________________________________________Container do Titulo

ft.app(target=principal)


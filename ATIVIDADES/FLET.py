import flet as ft

def main(page: ft.Page):
    # Função que será chamada quando o botão for clicado
    def button_clicked(e):
        # Exibir o texto digitado no campo de texto
        page.add(ft.Text(f"Você digitou: {txt_field.value}"))

    # Criar um campo de texto
    txt_field = ft.TextField(label="Digite algo")

    # Criar um botão
    btn = ft.ElevatedButton(text="Exibir", on_click=button_clicked)

    # Adicionar os componentes à página
    page.add(txt_field, btn)

# Rodar a aplicação Flet
ft.app(target=main)
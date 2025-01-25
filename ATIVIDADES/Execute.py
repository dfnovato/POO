import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import threading
from rembg import remove
import io


def process_text_image(image_path):
    """Remove o fundo de uma imagem usando o rembg."""
    try:
        with open(image_path, "rb") as f:
            input_image = f.read()

        # Usar rembg para remover o fundo
        output_image = remove(input_image)

        # Carregar o resultado em PIL para exibição
        result_image = Image.open(io.BytesIO(output_image))
        return result_image

    except Exception as e:
        raise RuntimeError(f"Erro ao processar a imagem: {e}")


def update_result_label(image, label):
    """Atualiza a interface gráfica com a imagem processada."""
    try:
        result_tk = ImageTk.PhotoImage(image)

        label.config(image=result_tk, text="")
        label.image = result_tk
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao atualizar a interface: {e}")


def remove_background(image_path, result_label):
    """Função principal de remoção de fundo executada em thread."""
    try:
        result_label.config(text="Processando a imagem...")
        result_image = process_text_image(image_path)
        update_result_label(result_image, result_label)
        result_label.config(text="Imagem processada com sucesso!")
    except FileNotFoundError:
        messagebox.showerror("Erro", "O arquivo selecionado não foi encontrado.")
    except Exception as e:
        messagebox.showerror("Erro", str(e))
        result_label.config(text="Erro ao processar a imagem.")


def open_image(result_label):
    """Abre um diálogo para seleção de imagem."""
    file_path = filedialog.askopenfilename(
        title="Selecionar Imagem",
        filetypes=[("Imagens", "*.jpg *.jpeg *.png *.bmp *.tiff")]
    )
    if not file_path:
        return

    # Processar a imagem em uma thread separada
    thread = threading.Thread(target=remove_background, args=(file_path, result_label))
    thread.start()


def create_gui():
    """Configura e inicia a interface gráfica."""
    root = tk.Tk()
    root.title("Remoção de Fundo de Imagem")

    # Botão para carregar a imagem
    open_button = tk.Button(root, text="Selecionar Imagem", command=lambda: open_image(result_label))
    open_button.pack(pady=10)

    # Área para exibir a imagem processada
    result_label = tk.Label(root, text="Nenhuma imagem carregada", font=("Arial", 12), wraplength=400)
    result_label.pack(pady=10)

    # Iniciar o loop da interface
    root.mainloop()


if __name__ == "__main__":
    create_gui()

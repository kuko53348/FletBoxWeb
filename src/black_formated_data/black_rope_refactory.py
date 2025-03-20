import autopep8
import isort
import os
import sys
import ast

# pip install autopep8


class CodeFormatter:
    """
    ```python
    ## Ejemplo de uso

    >>> from black_rope_refactory import CodeFormatter
    >>> # CREATE CODE
    >>> code_to_refactor = "code as string '
    >>> formatter = CodeFormatter(code=code_to_refactor)
    >>> codigo_corregido = formatter.fix_code()

        ```
    """

    def __init__(self, code=None, file_path=None, indent_level: int = 0):
        self.code = code
        self.file_path = file_path
        self.indent_level = indent_level
        if file_path:
            self.code = self._read_file()

    def _read_file(self):
        """Lee el contenido de un archivo."""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"El archivo {self.file_path} no existe.")
        with open(self.file_path, "r") as file:
            return file.read()

    def _write_file(self, code):
        """Escribe el contenido corregido en un archivo."""
        with open(self.file_path, "w") as file:
            file.write(code)

    def _validate_syntax(self):
        """Valida la sintaxis del código."""
        try:
            ast.parse(self.code)
            return True
        except SyntaxError:
            return False

    def _fix_indentation(self):
        """Corrige manualmente la indentación del código."""
        lines = self.code.splitlines()
        corrected_lines = []

        indent_level = self.indent_level
        for line in lines:
            stripped_line = line.lstrip()
            if stripped_line.startswith(
                ("def ", "class ", "if ", "for ", "while ", "else:", "elif ")
            ):
                corrected_lines.append(" " * indent_level * 4 + stripped_line)
                if stripped_line.endswith(":"):
                    indent_level += 1
            elif stripped_line.startswith(("return ", "print ", "pass ")):
                corrected_lines.append(" " * indent_level * 4 + stripped_line)
            else:
                corrected_lines.append(" " * indent_level * 4 + stripped_line)
                if stripped_line.endswith(":"):
                    indent_level += 1
        self.code = "\n".join(corrected_lines)

    def format_code(self):
        """Formatea el código usando autopep8."""
        if not self.code:
            raise ValueError("No se ha proporcionado código para formatear.")
        return autopep8.fix_code(self.code, options={"aggressive": 1})

    def sort_imports(self):
        """Ordena las importaciones usando isort."""
        if not self.code:
            raise ValueError(
                "No se ha proporcionado código para ordenar importaciones."
            )
        return isort.code(self.code)

    def remove_trailing_whitespace(self):
        """Elimina espacios en blanco al final de las líneas."""
        if not self.code:
            raise ValueError(
                "No se ha proporcionado código para eliminar espacios en blanco."
            )
        lines = self.code.splitlines()
        cleaned_lines = [line.rstrip() for line in lines]
        return "\n".join(cleaned_lines)

    def fix_code(self):
        """Aplica todas las correcciones al código."""
        if not self.code:
            raise ValueError("No se ha proporcionado código para corregir.")

        # Corregir indentación manualmente si la sintaxis no es válida
        if not self._validate_syntax():
            print(
                "El código tiene errores de sintaxis. Corrigiendo indentación manualmente..."
            )
            self._fix_indentation()

        # Aplicar correcciones
        self.code = self.sort_imports()
        self.code = self.format_code()
        self.code = self.remove_trailing_whitespace()

        return self.code

    def fix_file(self):
        """Corrige y guarda el código en el archivo."""
        if not self.file_path:
            raise ValueError("No se ha proporcionado una ruta de archivo.")

        self.code = self._read_file()
        self.fix_code()
        self._write_file(self.code)
        print(f"El archivo {self.file_path} ha sido corregido y guardado.")


if __name__ == "__main__":
    # Ejemplo de uso
    codigo_desordenado = """

import flet as ft

class data(ft.Container()):
    def __init__():
        self.data=""

    def build(self):
    self.content=ft.Container(
        content=ft.Text(
value="hello",
        ))
"""

    # Corrección de código en memoria
    formatter = CodeFormatter(code=codigo_desordenado)
    codigo_corregido = formatter.fix_code()
    print("Código corregido:")
    print(codigo_corregido)

    # Corrección de un archivo
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        formatter = CodeFormatter(file_path=file_path)
        formatter.fix_file()
    else:
        print("No se proporcionó un archivo para corregir.")

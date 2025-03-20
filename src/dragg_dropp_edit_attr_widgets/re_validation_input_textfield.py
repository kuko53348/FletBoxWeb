import re


def input_filter_by(filter_type: str = "str", payload: str = ""):
    """
    ### filter_type
    - str int float float_int

    ### Input filter by str
    - Get only str
    ```python
    >>> exemple_text =  "Hola 123, este es un, texto con números 45.6 y símbolos @#!"
    >>> data_generated = input_filter_by(filter_type='str', payload=exemple_text)
    ```
    - Get only int
    ```python
    >>> exemple_text = "Los números son 123666, 45.6, 7890, y 100."
    >>> data_generated = input_filter_by(filter_type='int', payload=exemple_text)
    ```
    - Get only float
    ```python
    >>> exemple_text = "Los precios son 1255.54, 45.50, y 100.0, pero no 123 o 45."
    >>> data_generated = input_filter_by(filter_type='float', payload=exemple_text)
    ```
    - Get only float_int
    ```python
    >>> exemple_text = "Los valores son 123 , 45.6, 7890, y 100.0, pero no abc o 12.34.56."
    >>> data_generated = input_filter_by(filter_type='float_int', payload=exemple_text)
    ```
    #### get filter data
    -get all filter data by input with module re

    """
    # 'str' ,'int' ,'float' ,'float_int'

    if filter_type == "str":
        # only strings
        current_filter = r"[A-Za-záéíóúÁÉÍÓÚñÑ]+"
        strings = re.findall(current_filter, payload)
        return " ".join(strings)

    elif filter_type == "int":
        # only int
        current_filter = r"\d+"
        strings = re.findall(current_filter, payload)
        return strings[0] if len(strings) else 0.01

    elif filter_type == "float":
        # only float
        current_filter = r"\d+\.\d+"
        strings = re.findall(current_filter, payload)
        return strings[0] if len(strings) else 0.01

    elif filter_type == "float_int":
        # only float and int
        current_filter = r"\b\d+\.\d+\b|\b\d+\b"
        strings = re.findall(current_filter, payload)
        return strings[0] if len(strings) else 0.01

    else:
        return False

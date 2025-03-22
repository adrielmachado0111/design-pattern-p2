from abc import ABC, abstractmethod
from typing import Any

# Interfaces y clases base

# Interfaz para los lectores de documentos
class DocumentReader(ABC):
    @abstractmethod
    def read(self, file_path: str) -> None:
        pass
    
    @abstractmethod
    def get_content(self) -> Any:
        pass

# Implementaciones de DocumentReader para diferentes formatos
class XLSXReader(DocumentReader):
    def read(self, file_path: str) -> None:
        print(f"Leyendo archivo XLSX: {file_path}")
        # Implementación específica para leer archivos XLSX
        # En una implementación real, usaríamos una biblioteca como pandas o openpyxl
    
    def get_content(self) -> Any:
        # Retorna el contenido del documento en un formato genérico
        return {}

class DOCXReader(DocumentReader):
    def read(self, file_path: str) -> None:
        print(f"Leyendo archivo DOCX: {file_path}")
        # Implementación específica para leer archivos DOCX
        # En una implementación real, usaríamos una biblioteca como python-docx
    
    def get_content(self) -> Any:
        # Retorna el contenido del documento en un formato genérico
        return {}

class XMLReader(DocumentReader):
    def read(self, file_path: str) -> None:
        print(f"Leyendo archivo XML: {file_path}")
        # Implementación específica para leer archivos XML
        # En una implementación real, usaríamos una biblioteca como xml.etree.ElementTree
    
    def get_content(self) -> Any:
        # Retorna el contenido del documento en un formato genérico
        return {}

# Factory para crear los lectores de documentos
class DocumentReaderFactory:
    @staticmethod
    def create_reader(format_type: str) -> DocumentReader:
        if format_type.lower() == "xlsx":
            return XLSXReader()
        elif format_type.lower() == "docx":
            return DOCXReader()
        elif format_type.lower() == "xml":
            return XMLReader()
        else:
            raise ValueError(f"Formato no soportado: {format_type}")

# Interfaz para el Builder de documentos
class DocumentBuilder(ABC):
    @abstractmethod
    def build_document(self) -> None:
        pass
    
    @abstractmethod
    def add_table(self, data: Any) -> None:
        pass
    
    @abstractmethod
    def add_text(self, text: str, style: str) -> None:
        pass
    
    @abstractmethod
    def add_header(self, text: str, level: int) -> None:
        pass
    
    @abstractmethod
    def add_image(self, image_path: str, width: int, height: int) -> None:
        pass
    
    @abstractmethod
    def get_result(self) -> Any:
        pass

# Implementación del Builder para PDF
class PDFBuilder(DocumentBuilder):
    def __init__(self):
        self.document = {}  # Representaría el documento PDF en construcción
    
    def build_document(self) -> None:
        print("Iniciando la construcción del documento PDF")
        # Inicialización del documento
        # En una implementación real, usaríamos una biblioteca como reportlab o PyPDF2
    
    def add_table(self, data: Any) -> None:
        print("Agregando tabla al documento PDF")
        # Lógica para agregar una tabla al PDF
    
    def add_text(self, text: str, style: str) -> None:
        print(f"Agregando texto con estilo {style}: {text}")
        # Lógica para agregar texto al PDF
    
    def add_header(self, text: str, level: int) -> None:
        print(f"Agregando encabezado nivel {level}: {text}")
        # Lógica para agregar encabezados al PDF
    
    def add_image(self, image_path: str, width: int, height: int) -> None:
        print(f"Agregando imagen: {image_path}")
        # Lógica para agregar imágenes al PDF
    
    def get_result(self) -> Any:
        print("Retornando documento PDF finalizado")
        return self.document

# Interfaz para los procesadores de documentos
class DocumentProcessor(ABC):
    @abstractmethod
    def process(self, data: Any, builder: DocumentBuilder) -> None:
        pass
    
    @abstractmethod
    def get_result(self) -> Any:
        pass

# Implementaciones de procesadores específicos
class TableProcessor(DocumentProcessor):
    def process(self, data: Any, builder: DocumentBuilder) -> None:
        print("Procesando datos para crear tabla")
        builder.add_table(data)
    
    def get_result(self) -> Any:
        return {}  # Retorna el resultado del procesamiento

class TextProcessor(DocumentProcessor):
    def process(self, data: Any, builder: DocumentBuilder) -> None:
        print("Procesando datos para crear texto")
        # Suponiendo que data contiene información sobre el texto y su estilo
        builder.add_text("Texto de ejemplo", "normal")
    
    def get_result(self) -> Any:
        return {}  # Retorna el resultado del procesamiento

# Director para coordinar la construcción del documento
class DocumentDirector:
    def construct(self, builder: DocumentBuilder, content: Any) -> None:
        builder.build_document()
        
        # Ejemplo de lógica para construir el documento
        # Dependiendo del contenido, se llamaría a diferentes métodos del builder
        builder.add_header("Documento de Ejemplo", 1)
        builder.add_text("Este es un documento generado automáticamente", "normal")
        
        # Aquí procesaríamos el contenido real extraído del documento de origen
        # Por ejemplo, podríamos iterar sobre las secciones del contenido y
        # llamar a los métodos apropiados del builder

# Clase para manejar plantillas de documentos
class DocumentTemplate:
    def __init__(self):
        self.template = None
        self.data = None
    
    def load(self, template_path: str) -> None:
        print(f"Cargando plantilla desde: {template_path}")
        # Lógica para cargar la plantilla
        self.template = {}
    
    def fill_template(self, data: Any) -> None:
        print("Llenando plantilla con datos")
        self.data = data
        # Lógica para llenar la plantilla con los datos
    
    def export(self) -> Any:
        print("Exportando documento desde plantilla")
        # Lógica para exportar el documento final
        return {}

# Clase principal de la aplicación que demuestra el uso de los patrones
class PDFGenerationSystem:
    @staticmethod
    def run():
        # Ejemplo de uso del sistema
        
        # 1. El cliente selecciona el formato de origen
        selected_format = "xlsx"
        file_path = f"ruta/al/documento.{selected_format}"
        
        # 2. Crear el lector apropiado usando el Factory
        reader_factory = DocumentReaderFactory()
        reader = reader_factory.create_reader(selected_format)
        
        # 3. Leer el documento
        reader.read(file_path)
        content = reader.get_content()
        
        # 4. Crear el builder para el documento PDF
        pdf_builder = PDFBuilder()
        
        # 5. Procesar el contenido
        table_processor = TableProcessor()
        table_processor.process(content, pdf_builder)
        
        # 6. Usar el director para coordinar la construcción
        director = DocumentDirector()
        director.construct(pdf_builder, content)
        
        # 7. Obtener el resultado final
        final_document = pdf_builder.get_result()
        
        # 8. Alternativamente, usar una plantilla
        template = DocumentTemplate()
        template.load("ruta/a/plantilla.pdf")
        template.fill_template(content)
        document_from_template = template.export()
        
        print("Documento PDF generado exitosamente")

# Ejemplo de ejecución
if __name__ == "__main__":
    PDFGenerationSystem.run()
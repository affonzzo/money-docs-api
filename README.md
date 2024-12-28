# Money Docs Backend

Este é o backend do Money Docs, responsável por processar documentos usando a biblioteca Docling.

## Configuração

1. Crie um ambiente virtual Python:
```bash
python -m venv venv
```

2. Ative o ambiente virtual:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Executando o Backend

Para iniciar o servidor:

```bash
python main.py
```

O servidor estará disponível em `http://localhost:8000`

## Endpoints

### POST /convert
Converte um documento para o formato especificado.

Parâmetros:
- `file`: Arquivo a ser convertido
- `output_format`: Formato de saída ("markdown", "json", "html")
- `use_ocr`: (opcional) Usar OCR para PDFs escaneados
- `extract_tables`: (opcional) Extrair estrutura de tabelas
- `max_pages`: (opcional) Número máximo de páginas a processar